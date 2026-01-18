#!/usr/bin/env python
"""
Reorganize task structure to comply with v2.2 ORGANIZED standard

Migrates tasks from FLAT or MIXED patterns to ORGANIZED:
- Creates reports/ subdirectory
- Moves all report .md files to reports/
- Creates README.md in root if missing
- Validates final structure
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple


def create_readme_from_reports(task_dir: Path, task_name: str, reports: List[str]) -> str:
    """Generate README.md content based on existing reports."""

    # Load task_info for description
    task_info_path = task_dir / "task_info.json"
    description = "Análisis especializado"

    if task_info_path.exists():
        try:
            with open(task_info_path, 'r', encoding='utf-8') as f:
                task_info = json.load(f)
                description = task_info.get("description", description)
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            # If task_info is missing/corrupt, use default description
            pass

    # Generate title from task name
    title = task_name.replace('-', ' ').title()

    readme_content = f"""# {title.upper()}

## INTRODUCCIÓN

{description}

## CONTENIDO DEL ANÁLISIS

### Documentos principales

"""

    # Add each report
    for i, report in enumerate(sorted(reports), 1):
        # Try to make a nice description from filename
        report_name = report.replace('_', ' ').replace('.md', '').title()
        readme_content += f"""{i}. **[{report}](reports/{report})**
   - {report_name}

"""

    readme_content += """
## NAVEGACIÓN RÁPIDA

Revisa los documentos en el directorio reports/ según tu interés.

## HALLAZGOS CLAVE

Consultar reportes individuales para hallazgos específicos.

## METODOLOGÍA

Análisis basado en revisión de literatura científica y evidencia experimental.

---

**Nota:** Esta tarea sigue el estándar v2.2 ORGANIZED del framework.
"""

    return readme_content


def reorganize_task(task_dir: Path, dry_run: bool = False) -> Tuple[bool, List[str]]:
    """
    Reorganize a single task to ORGANIZED standard.

    Returns:
        Tuple of (success, messages)
    """

    task_name = task_dir.name
    messages = []

    messages.append(f"Processing task: {task_name}")
    messages.append(f"  Location: {task_dir}")

    # Check current state
    reports_dir = task_dir / "reports"
    readme_path = task_dir / "README.md"

    # Find all .md files in root (excluding prompt.md and README.md)
    md_files_in_root = []
    for item in task_dir.iterdir():
        if item.is_file() and item.suffix == '.md':
            if item.name not in ['prompt.md', 'README.md', 'task_info.json']:
                md_files_in_root.append(item.name)

    # Determine actions needed
    needs_reports_dir = not reports_dir.exists()
    needs_move = len(md_files_in_root) > 0
    needs_readme = not readme_path.exists()

    if not needs_reports_dir and not needs_move and not needs_readme:
        messages.append("  SKIP: Already compliant with ORGANIZED standard")
        return True, messages

    messages.append(f"  Actions needed:")
    if needs_reports_dir:
        messages.append(f"    - Create reports/ subdirectory")
    if needs_move:
        messages.append(f"    - Move {len(md_files_in_root)} files to reports/")
    if needs_readme:
        messages.append(f"    - Create README.md")

    if dry_run:
        messages.append("  DRY RUN: No changes made")
        return True, messages

    # Execute reorganization
    try:
        # Step 1: Create reports/ directory
        if needs_reports_dir:
            reports_dir.mkdir(exist_ok=True)
            messages.append(f"  CREATED: reports/")

        # Step 2: Move .md files to reports/
        if needs_move:
            for md_file in md_files_in_root:
                src = task_dir / md_file
                dst = reports_dir / md_file

                # Check if destination already exists
                if dst.exists():
                    messages.append(f"    SKIP: {md_file} (already exists in reports/)")
                    continue

                shutil.move(str(src), str(dst))
                messages.append(f"    MOVED: {md_file} -> reports/")

        # Step 3: Create README.md if needed
        if needs_readme:
            # Get list of all reports (including those already in reports/)
            all_reports = [f.name for f in reports_dir.iterdir() if f.is_file() and f.suffix == '.md']

            readme_content = create_readme_from_reports(task_dir, task_name, all_reports)

            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)

            messages.append(f"  CREATED: README.md")

        messages.append(f"  SUCCESS: Task reorganized")
        return True, messages

    except Exception as e:
        messages.append(f"  ERROR: {str(e)}")
        return False, messages


def main():
    """Main reorganization function."""

    import sys

    # Get framework root
    script_dir = Path(__file__).parent
    framework_root = script_dir.parent

    # Parse arguments
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

    # Get project and optionally specific task
    if len(sys.argv) < 2:
        print("Usage: python core/reorganize_task_structure.py [project-id] [task-name] [--dry-run]")
        print()
        print("Examples:")
        print("  # Reorganize all tasks in project")
        print("  python core/reorganize_task_structure.py investigaci-n-clo-covid-19-20251222-195407")
        print()
        print("  # Reorganize specific task")
        print("  python core/reorganize_task_structure.py investigaci-n-clo-covid-19-20251222-195407 selectividad-molecular-celular-clo2")
        print()
        print("  # Dry run (preview changes)")
        print("  python core/reorganize_task_structure.py investigaci-n-clo-covid-19-20251222-195407 --dry-run")
        return 1

    project_id = sys.argv[1]
    specific_task = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None

    project_root = framework_root / "projects" / project_id
    tasks_dir = project_root / "tasks"

    if not tasks_dir.exists():
        print(f"ERROR: Tasks directory not found: {tasks_dir}")
        return 1

    print("="*80)
    print("TASK STRUCTURE REORGANIZATION - v2.2 ORGANIZED")
    print("="*80)
    print(f"Project: {project_id}")
    if dry_run:
        print("Mode: DRY RUN (no changes will be made)")
    else:
        print("Mode: EXECUTE (changes will be applied)")
    print()

    # Get tasks to process
    if specific_task:
        task_dir = tasks_dir / specific_task
        if not task_dir.exists():
            print(f"ERROR: Task not found: {specific_task}")
            return 1
        task_dirs = [task_dir]
    else:
        task_dirs = sorted([d for d in tasks_dir.iterdir() if d.is_dir()])

    print(f"Tasks to process: {len(task_dirs)}")
    print()

    # Process each task
    results = []
    for task_dir in task_dirs:
        success, messages = reorganize_task(task_dir, dry_run=dry_run)
        results.append((task_dir.name, success, messages))

        for msg in messages:
            print(msg)
        print()

    # Summary
    print("="*80)
    print("SUMMARY")
    print("="*80)

    successful = sum(1 for _, success, _ in results if success)
    failed = len(results) - successful

    print(f"Total tasks: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

    if failed > 0:
        print()
        print("Failed tasks:")
        for name, success, _ in results:
            if not success:
                print(f"  - {name}")

    if not dry_run and successful > 0:
        print()
        print("Reorganization complete. Validating...")
        print()

        # Run validator
        from framework_validator import FrameworkValidator

        validator = FrameworkValidator(framework_root)
        valid, messages = validator.validate_project_structure(project_id)

        if valid:
            print("VALIDATION: Project structure is now compliant")
        else:
            print("VALIDATION WARNINGS:")
            for msg in messages:
                print(f"  {msg}")

    print("="*80)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    exit(main())
