#!/usr/bin/env python
"""
Audit script to verify all tasks comply with framework v2.2 standards
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple


def audit_task(task_dir: Path) -> Dict:
    """Audit a single task directory."""

    task_name = task_dir.name
    issues = []
    warnings = []
    files_found = []

    # Check required files
    task_info_path = task_dir / "task_info.json"
    prompt_path = task_dir / "prompt.md"

    if not task_info_path.exists():
        issues.append("MISSING: task_info.json")
    else:
        files_found.append("task_info.json")
        # Verify it's valid JSON
        try:
            with open(task_info_path, 'r', encoding='utf-8') as f:
                task_info = json.load(f)

            # Check required fields
            required_fields = ["task_name", "description", "created", "status", "prompt_file", "reports"]
            for field in required_fields:
                if field not in task_info:
                    issues.append(f"task_info.json missing field: {field}")

        except json.JSONDecodeError as e:
            issues.append(f"task_info.json is invalid JSON: {e}")
        except Exception as e:
            issues.append(f"Error reading task_info.json: {e}")

    if not prompt_path.exists():
        issues.append("MISSING: prompt.md")
    else:
        files_found.append("prompt.md")

    # List all markdown files
    md_files = [f.name for f in task_dir.iterdir() if f.is_file() and f.suffix == '.md']

    # List subdirectories
    subdirs = [d.name for d in task_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]

    # Check for reports subdirectory (optional but common)
    reports_dir = task_dir / "reports"
    if reports_dir.exists():
        subdirs_note = f"Has reports/ subdirectory with {len(list(reports_dir.iterdir()))} files"
    else:
        subdirs_note = "No reports/ subdirectory"

    return {
        "task_name": task_name,
        "issues": issues,
        "warnings": warnings,
        "files_found": files_found,
        "md_files": md_files,
        "subdirs": subdirs,
        "subdirs_note": subdirs_note,
        "compliant": len(issues) == 0
    }


def main():
    """Main audit function."""
    parser = argparse.ArgumentParser(
        description="Audit project compliance with Framework v2.2 standards"
    )
    parser.add_argument(
        "project_id",
        help="Project ID to audit"
    )
    args = parser.parse_args()

    # Get framework root
    script_dir = Path(__file__).parent
    framework_root = script_dir.parent

    # Project to audit
    project_id = args.project_id
    project_root = framework_root / "projects" / project_id
    tasks_dir = project_root / "tasks"

    if not project_root.exists():
        print(f"ERROR: Project not found: {project_id}")
        print(f"Looked in: {project_root}")
        return 1

    if not tasks_dir.exists():
        print(f"ERROR: Tasks directory not found: {tasks_dir}")
        return 1

    print("="*80)
    print(f"FRAMEWORK v2.2 COMPLIANCE AUDIT")
    print(f"Project: {project_id}")
    print("="*80)
    print()

    # Get all task directories
    task_dirs = sorted([d for d in tasks_dir.iterdir() if d.is_dir()])

    print(f"Total tasks found: {len(task_dirs)}")
    print()

    # Audit each task
    results = []
    compliant_count = 0
    non_compliant_count = 0

    for task_dir in task_dirs:
        result = audit_task(task_dir)
        results.append(result)

        if result["compliant"]:
            compliant_count += 1
        else:
            non_compliant_count += 1

    # Print detailed results
    print("-"*80)
    print("DETAILED TASK AUDIT")
    print("-"*80)
    print()

    for i, result in enumerate(results, 1):
        task_name = result["task_name"]
        compliant = result["compliant"]

        status = "COMPLIANT" if compliant else "NON-COMPLIANT"
        status_symbol = "OK" if compliant else "FAIL"

        print(f"{i}. {task_name}")
        print(f"   Status: {status_symbol} - {status}")

        if result["files_found"]:
            print(f"   Required files: {', '.join(result['files_found'])}")

        if result["issues"]:
            print(f"   ISSUES:")
            for issue in result["issues"]:
                print(f"      - {issue}")

        if result["warnings"]:
            print(f"   WARNINGS:")
            for warning in result["warnings"]:
                print(f"      - {warning}")

        print(f"   Markdown files: {len(result['md_files'])} total")
        if len(result['md_files']) <= 5:
            for md_file in result['md_files']:
                print(f"      - {md_file}")
        else:
            for md_file in result['md_files'][:3]:
                print(f"      - {md_file}")
            print(f"      ... and {len(result['md_files']) - 3} more")

        if result["subdirs"]:
            print(f"   Subdirectories: {', '.join(result['subdirs'])}")

        print(f"   {result['subdirs_note']}")
        print()

    # Summary
    print("="*80)
    print("AUDIT SUMMARY")
    print("="*80)
    print(f"Total tasks: {len(results)}")
    print(f"Compliant: {compliant_count}")
    print(f"Non-compliant: {non_compliant_count}")
    print()

    if non_compliant_count > 0:
        print("NON-COMPLIANT TASKS:")
        for result in results:
            if not result["compliant"]:
                print(f"  - {result['task_name']}")
                for issue in result["issues"]:
                    print(f"      {issue}")
        print()

    # Check project-level structure
    print("-"*80)
    print("PROJECT-LEVEL STRUCTURE")
    print("-"*80)

    project_info = project_root / "project_info.json"
    context_md = project_root / "context.md"
    synthesis_dir = project_root / "synthesis"

    print(f"project_info.json: {'EXISTS' if project_info.exists() else 'MISSING'}")
    print(f"context.md: {'EXISTS' if context_md.exists() else 'MISSING'}")
    print(f"tasks/: {'EXISTS' if tasks_dir.exists() else 'MISSING'}")
    print(f"synthesis/: {'EXISTS' if synthesis_dir.exists() else 'MISSING'}")
    print()

    # Overall verdict
    project_compliant = (
        project_info.exists() and
        context_md.exists() and
        tasks_dir.exists() and
        synthesis_dir.exists() and
        non_compliant_count == 0
    )

    print("="*80)
    if project_compliant:
        print("VERDICT: PROJECT FULLY COMPLIANT with Framework v2.2")
    else:
        print("VERDICT: PROJECT HAS COMPLIANCE ISSUES")
        print()
        print("ACTION REQUIRED: Fix non-compliant tasks")
    print("="*80)

    return 0 if project_compliant else 1


if __name__ == "__main__":
    exit(main())
