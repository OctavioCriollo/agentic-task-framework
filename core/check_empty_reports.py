#!/usr/bin/env python
"""
Check which tasks have empty reports/ directories
"""

import json
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Check which tasks have empty reports/ directories"
    )
    parser.add_argument(
        "project_id",
        help="Project ID to check"
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    framework_root = script_dir.parent
    project_id = args.project_id
    tasks_dir = framework_root / "projects" / project_id / "tasks"

    if not tasks_dir.exists():
        print(f"ERROR: Project not found: {project_id}")
        print(f"Looked in: {tasks_dir}")
        return 1

    print("="*80)
    print("CHECKING REPORTS DIRECTORIES")
    print("="*80)
    print()

    empty_tasks = []
    populated_tasks = []

    for task_dir in sorted(tasks_dir.iterdir()):
        if not task_dir.is_dir():
            continue

        task_name = task_dir.name
        reports_dir = task_dir / "reports"

        if not reports_dir.exists():
            print(f"ERROR: {task_name} - No reports/ directory")
            continue

        # Count files in reports/
        report_files = [f for f in reports_dir.iterdir() if f.is_file()]
        count = len(report_files)

        # Get task status
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

        if count == 0:
            empty_tasks.append((task_name, status))
            print(f"EMPTY: {task_name}")
            print(f"  Status: {status}")
            print(f"  Reports: 0 files")
            print()
        else:
            populated_tasks.append((task_name, status, count))
            print(f"OK: {task_name}")
            print(f"  Status: {status}")
            print(f"  Reports: {count} files")
            for rf in report_files[:3]:
                print(f"    - {rf.name}")
            if count > 3:
                print(f"    ... and {count - 3} more")
            print()

    # Summary
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total tasks: {len(empty_tasks) + len(populated_tasks)}")
    print(f"With reports: {len(populated_tasks)}")
    print(f"Empty reports/: {len(empty_tasks)}")
    print()

    if empty_tasks:
        print("TASKS WITH EMPTY REPORTS:")
        for task_name, status in empty_tasks:
            print(f"  - {task_name} (status: {status})")
        print()
        print("ANALYSIS:")
        in_progress_count = sum(1 for _, status in empty_tasks if status == "in_progress")
        completed_count = sum(1 for _, status in empty_tasks if status == "completed")

        print(f"  In progress: {in_progress_count} (esperado - agentes no terminaron)")
        print(f"  Completed: {completed_count} (PROBLEMA - reportes perdidos?)")

    print("="*80)


if __name__ == "__main__":
    main()
