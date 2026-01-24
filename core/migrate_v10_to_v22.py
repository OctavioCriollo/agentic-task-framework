#!/usr/bin/env python3
"""
Migrate project metadata from v1.0 to v2.2 format.

Removes legacy fields:
- agents (v1.0)
- outputs.synthesis (v1.0)

Keeps only v2.2 fields:
- tasks
- synthesis

Usage:
    python core/migrate_v10_to_v22.py <project-id>          # Migrate specific project
    python core/migrate_v10_to_v22.py                        # Migrate all projects
    python core/migrate_v10_to_v22.py --no-backup <project>  # Skip backup creation
"""

import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime


def migrate_project(project_dir: Path, backup: bool = True, verbose: bool = True) -> bool:
    """
    Migrate a single project from v1.0 to v2.2 metadata format.

    Args:
        project_dir: Path to project directory
        backup: Whether to create backup file
        verbose: Whether to print progress

    Returns:
        True if migration successful, False otherwise
    """
    project_info_path = project_dir / "project_info.json"

    if not project_info_path.exists():
        if verbose:
            print(f"✗ No project_info.json found in {project_dir.name}")
        return False

    # Load current metadata
    try:
        with open(project_info_path, 'r', encoding='utf-8') as f:
            project_info = json.load(f)
    except json.JSONDecodeError as e:
        if verbose:
            print(f"✗ Invalid JSON in {project_dir.name}: {e}")
        return False
    except Exception as e:
        if verbose:
            print(f"✗ Error reading {project_dir.name}: {e}")
        return False

    # Check if migration needed
    has_legacy_agents = 'agents' in project_info
    has_legacy_outputs = 'outputs' in project_info

    if not has_legacy_agents and not has_legacy_outputs:
        if verbose:
            print(f"✓ Project already v2.2 format: {project_dir.name}")
        return True

    # Create backup if requested
    if backup:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = project_dir / f"project_info.json.backup_{timestamp}"
        shutil.copy(project_info_path, backup_path)
        if verbose:
            print(f"✓ Backup created: {backup_path.name}")

    # Remove legacy fields
    removed_fields = []

    if has_legacy_agents:
        del project_info['agents']
        removed_fields.append('agents')

    if has_legacy_outputs:
        del project_info['outputs']
        removed_fields.append('outputs')

    # Save migrated metadata
    try:
        with open(project_info_path, 'w', encoding='utf-8') as f:
            json.dump(project_info, f, indent=2, ensure_ascii=False)
    except Exception as e:
        if verbose:
            print(f"✗ Error saving {project_dir.name}: {e}")
        return False

    if verbose:
        print(f"✓ Migrated {project_dir.name}: removed {', '.join(removed_fields)}")

    return True


def main():
    """Main migration function."""
    parser = argparse.ArgumentParser(
        description="Migrate projects from v1.0 to v2.2 metadata format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python core/migrate_v10_to_v22.py investigaci-n-clo-covid-19-20251222-195407
    Migrate specific project (with backup)

  python core/migrate_v10_to_v22.py
    Migrate all projects

  python core/migrate_v10_to_v22.py --no-backup
    Migrate all projects without creating backups (not recommended)

  python core/migrate_v10_to_v22.py --quiet
    Migrate silently (only show errors)
        """
    )
    parser.add_argument(
        "project_id",
        nargs='?',
        help="Specific project ID to migrate (optional, migrates all if not specified)"
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Don't create backup files (not recommended)"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress output (only show summary)"
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    framework_root = script_dir.parent
    projects_dir = framework_root / "projects"

    if not projects_dir.exists():
        print(f"✗ Projects directory not found: {projects_dir}")
        return 1

    verbose = not args.quiet

    if args.project_id:
        # Migrate specific project
        project_dir = projects_dir / args.project_id

        if not project_dir.exists():
            print(f"✗ Project not found: {args.project_id}")
            print(f"Looked in: {project_dir}")
            return 1

        if not project_dir.is_dir():
            print(f"✗ Not a directory: {args.project_id}")
            return 1

        if verbose:
            print("="*60)
            print("PROJECT MIGRATION: v1.0 → v2.2")
            print("="*60)
            print(f"Project: {args.project_id}")
            print(f"Backup: {'Yes' if not args.no_backup else 'No'}")
            print("="*60)
            print()

        success = migrate_project(project_dir, backup=not args.no_backup, verbose=verbose)

        if success:
            print()
            print("✓ Migration completed successfully")
            return 0
        else:
            print()
            print("✗ Migration failed")
            return 1

    else:
        # Migrate all projects
        if verbose:
            print("="*60)
            print("BATCH MIGRATION: v1.0 → v2.2")
            print("="*60)
            print(f"Projects directory: {projects_dir}")
            print(f"Backup: {'Yes' if not args.no_backup else 'No'}")
            print("="*60)
            print()

        project_dirs = sorted([d for d in projects_dir.iterdir() if d.is_dir()])

        if not project_dirs:
            print("No projects found")
            return 0

        migrated = 0
        already_v22 = 0
        failed = 0

        for project_dir in project_dirs:
            result = migrate_project(project_dir, backup=not args.no_backup, verbose=verbose)

            if result:
                # Check if it was already v2.2 or actually migrated
                # (migrate_project returns True for both cases)
                migrated += 1
            else:
                failed += 1

        print()
        print("="*60)
        print("MIGRATION SUMMARY")
        print("="*60)
        print(f"Total projects scanned: {len(project_dirs)}")
        print(f"Processed: {migrated}")
        print(f"Failed: {failed}")
        print("="*60)

        if failed > 0:
            print()
            print("⚠ Some migrations failed. Check output above for details.")
            return 1
        else:
            print()
            print("✓ All migrations completed successfully")
            return 0


if __name__ == "__main__":
    exit(main())
