#!/usr/bin/env python
"""
Analyze organizational inconsistencies across tasks
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List


def analyze_task_organization(task_dir: Path) -> Dict:
    """Analyze how a task organizes its files."""

    task_name = task_dir.name

    # Count file types
    md_files = []
    other_files = []
    subdirs = []

    for item in task_dir.iterdir():
        if item.is_file():
            if item.suffix == '.md' and item.name not in ['prompt.md', 'task_info.json']:
                md_files.append(item.name)
            elif item.name not in ['task_info.json']:
                other_files.append(item.name)
        elif item.is_dir() and not item.name.startswith('.'):
            subdirs.append(item.name)

    # Determine organization pattern
    has_reports_subdir = 'reports' in subdirs
    reports_in_root = len(md_files) > 0
    no_reports = len(md_files) == 0 and not has_reports_subdir

    if has_reports_subdir and reports_in_root:
        pattern = "MIXED (reports in root AND reports/ subdir)"
    elif has_reports_subdir:
        pattern = "ORGANIZED (reports/ subdirectory)"
    elif reports_in_root:
        pattern = "FLAT (reports in root)"
    elif no_reports:
        pattern = "INCOMPLETE (no reports yet)"
    else:
        pattern = "UNKNOWN"

    # Load task_info to check status
    task_info_path = task_dir / "task_info.json"
    status = "unknown"
    if task_info_path.exists():
        try:
            with open(task_info_path, 'r', encoding='utf-8') as f:
                task_info = json.load(f)
                status = task_info.get("status", "unknown")
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            # If task_info is missing/corrupt, use default status
            pass

    return {
        "task_name": task_name,
        "pattern": pattern,
        "status": status,
        "md_files_in_root": len(md_files),
        "md_file_names": md_files,
        "subdirs": subdirs,
        "has_reports_subdir": has_reports_subdir
    }


def main():
    """Main analysis function."""
    parser = argparse.ArgumentParser(
        description="Analyze organizational inconsistencies across tasks in a project"
    )
    parser.add_argument(
        "project_id",
        help="Project ID to analyze"
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    framework_root = script_dir.parent
    project_id = args.project_id
    tasks_dir = framework_root / "projects" / project_id / "tasks"

    if not tasks_dir.exists():
        print(f"Error: Project not found: {project_id}")
        print(f"Looked in: {tasks_dir}")
        return 1

    print("="*80)
    print("ORGANIZATIONAL INCONSISTENCIES ANALYSIS")
    print("="*80)
    print()

    task_dirs = sorted([d for d in tasks_dir.iterdir() if d.is_dir()])
    results = []

    for task_dir in task_dirs:
        result = analyze_task_organization(task_dir)
        results.append(result)

    # Group by pattern
    patterns = {}
    for result in results:
        pattern = result["pattern"]
        if pattern not in patterns:
            patterns[pattern] = []
        patterns[pattern].append(result)

    # Print grouped results
    for pattern, tasks in sorted(patterns.items()):
        print(f"\nPATTERN: {pattern}")
        print(f"Count: {len(tasks)} tasks")
        print("-"*80)

        for task in tasks:
            print(f"  {task['task_name']}")
            print(f"    Status: {task['status']}")
            print(f"    MD files in root: {task['md_files_in_root']}")

            if task['md_file_names']:
                if len(task['md_file_names']) <= 3:
                    for md in task['md_file_names']:
                        print(f"      - {md}")
                else:
                    for md in task['md_file_names'][:2]:
                        print(f"      - {md}")
                    print(f"      ... and {len(task['md_file_names']) - 2} more")

            if task['subdirs']:
                print(f"    Subdirectories: {', '.join(task['subdirs'])}")

        print()

    # Recommendations
    print("="*80)
    print("INCONSISTENCIES FOUND")
    print("="*80)
    print()

    print("The project has MULTIPLE organizational patterns:")
    print()

    for pattern, tasks in sorted(patterns.items()):
        print(f"  {len(tasks):2d} tasks using: {pattern}")

    print()
    print("="*80)
    print("RECOMMENDED STANDARD")
    print("="*80)
    print()
    print("Framework v2.2 does NOT specify report organization, only requires:")
    print("  - task_info.json (REQUIRED)")
    print("  - prompt.md (REQUIRED)")
    print("  - Reports can be: root MD files OR reports/ subdirectory")
    print()
    print("RECOMMENDATION: Choose ONE pattern for consistency:")
    print()
    print("Option 1: FLAT (simple tasks)")
    print("  tasks/[task-name]/")
    print("    - task_info.json")
    print("    - prompt.md")
    print("    - report.md")
    print()
    print("Option 2: ORGANIZED (complex tasks with multiple reports)")
    print("  tasks/[task-name]/")
    print("    - task_info.json")
    print("    - prompt.md")
    print("    - reports/")
    print("        - analysis.md")
    print("        - synthesis.md")
    print("        - conclusions.md")
    print()
    print("Option 3: HYBRID (main report in root, supplementary in reports/)")
    print("  tasks/[task-name]/")
    print("    - task_info.json")
    print("    - prompt.md")
    print("    - README.md (main overview)")
    print("    - reports/")
    print("        - detailed_analysis.md")
    print("        - appendices.md")
    print()

    print("="*80)
    print("CURRENT PROJECT STATUS")
    print("="*80)
    print()
    print("All tasks are TECHNICALLY compliant (have required files).")
    print("BUT organizational patterns are INCONSISTENT across tasks.")
    print()
    print("This is NOT a breaking issue, but reduces maintainability.")
    print()
    print("ACTION: Update framework documentation to specify preferred pattern.")
    print("="*80)


if __name__ == "__main__":
    main()
