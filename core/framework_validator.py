#!/usr/bin/env python
"""
Framework Validator - Deterministic validation system for Agentic Task Framework v2.2

Inspired by A2UI (Agent-to-User Interface) principles:
- Declarative validation before execution
- Agent declares WHAT, validator ensures HOW follows standards
- Security through predefined workflow templates
- Session state tracking for consistency

Uses Python standard library only - no external dependencies required.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from core.__version__ import get_version


class FrameworkValidator:
    """
    Validates framework operations against v2.2 standards before execution.

    Prevents common deviations:
    - Creating tasks without ProjectManager
    - Missing metadata files (task_info.json, prompt.md)
    - Incorrect directory structure
    - Non-standard naming conventions
    - Missing 2-layer prompt architecture
    """

    def __init__(self, framework_root: Optional[Path] = None):
        """
        Initialize validator with framework root directory.

        Args:
            framework_root: Path to framework root. If None, auto-detects.
        """
        if framework_root is None:
            # Auto-detect framework root (directory containing core/ and projects/)
            current = Path(__file__).resolve().parent.parent
            self.framework_root = current
        else:
            self.framework_root = Path(framework_root)

        self.session_file = self.framework_root / ".framework_session.json"
        self.templates_file = self.framework_root / "core" / "workflow_templates.json"
        self.session = self._load_or_create_session()
        self.templates = self._load_templates()

    def _load_or_create_session(self) -> Dict[str, Any]:
        """Load existing session or create new one."""
        if self.session_file.exists():
            with open(self.session_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            session = {
                "session_id": datetime.now().strftime("%Y%m%d-%H%M%S"),
                "framework_version": get_version(),  # SECURITY FIX H3: Single source of truth
                "created": datetime.now().isoformat(),
                "active_project": None,
                "state": {
                    "project_manager_imported": False,
                    "tasks_count": 0,
                    "validation_enabled": True
                },
                "validation_log": []
            }
            self._save_session(session)
            return session

    def _save_session(self, session: Optional[Dict] = None) -> None:
        """Save session state to file."""
        if session is None:
            session = self.session

        with open(self.session_file, 'w', encoding='utf-8') as f:
            json.dump(session, f, indent=2, ensure_ascii=False)

    def _load_templates(self) -> Dict[str, Any]:
        """Load workflow templates if available."""
        if self.templates_file.exists():
            with open(self.templates_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Return default templates
            return {
                "research_workflow": {
                    "steps": [
                        "create_project",
                        "create_tasks",
                        "get_report_paths",
                        "launch_agents",
                        "register_completion"
                    ],
                    "validation_requirements": {
                        "project_manager_required": True,
                        "metadata_files_required": True,
                        "prompt_architecture": "2-layer"
                    }
                }
            }

    def _log_validation(self, operation: str, passed: bool, messages: List[str]) -> None:
        """Log validation result to session."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "passed": passed,
            "messages": messages
        }
        self.session["validation_log"].append(entry)
        self._save_session()

    def validate_research_request(self, user_request: str) -> Tuple[bool, List[str]]:
        """
        Validate a research request before processing.

        Checks:
        - ProjectManager should be used
        - Project should exist or be created
        - Workflow template compliance

        Args:
            user_request: The user's research request

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Check if ProjectManager is imported in coordinator context
        project_manager_path = self.framework_root / "core" / "project_manager.py"
        if not project_manager_path.exists():
            errors.append("ProjectManager module not found at core/project_manager.py")

        # Check if workflow template exists
        if "research_workflow" not in self.templates:
            errors.append("Research workflow template not found in templates")

        # Validation passes if no errors
        passed = len(errors) == 0

        if passed:
            messages = [
                "Research request validation passed",
                "ProjectManager module available",
                "Research workflow template loaded"
            ]
        else:
            messages = errors

        self._log_validation("validate_research_request", passed, messages)
        return passed, messages

    def validate_task_creation(self,
                               project_id: str,
                               task_name: str,
                               prompt: str,
                               using_project_manager: bool = False) -> Tuple[bool, List[str]]:
        """
        Validate task creation before execution.

        Checks:
        - ProjectManager.create_task() is being used
        - Task naming follows convention: [action]-[topic]-[details]
        - Prompt follows 2-layer architecture
        - Project exists

        Args:
            project_id: Target project ID
            task_name: Proposed task name
            prompt: Task prompt content
            using_project_manager: Whether ProjectManager.create_task() will be used

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        warnings = []

        # Check ProjectManager usage
        if not using_project_manager:
            errors.append(
                "CRITICAL: Task must be created using ProjectManager.create_task(). "
                "Do NOT create task manually or save prompt to /tmp/"
            )

        # Check task naming convention
        if not self._validate_task_naming(task_name):
            errors.append(
                f"Task name '{task_name}' does not follow convention: "
                "[action]-[topic]-[details] (kebab-case)"
            )

        # Check 2-layer prompt architecture
        prompt_validation = self._validate_prompt_architecture(prompt)
        if not prompt_validation["valid"]:
            errors.append(
                f"Prompt does not follow 2-layer architecture: {prompt_validation['reason']}"
            )

        # Check project exists
        project_path = self.framework_root / "projects" / project_id
        if not project_path.exists():
            warnings.append(
                f"Project '{project_id}' does not exist yet. "
                "Ensure ProjectManager.create_project() is called first."
            )
        else:
            # Verify project structure
            project_info = project_path / "project_info.json"
            if not project_info.exists():
                errors.append(
                    f"Project '{project_id}' exists but missing project_info.json. "
                    "Project may not have been created with ProjectManager."
                )

        passed = len(errors) == 0
        messages = errors + warnings

        if passed and not warnings:
            messages = [
                "Task creation validation passed",
                f"Task name '{task_name}' follows naming convention",
                "Prompt architecture validated (2-layer)",
                "ProjectManager workflow will be used"
            ]

        self._log_validation("validate_task_creation", passed, messages)
        return passed, messages

    def validate_agent_launch(self,
                             project_id: str,
                             task_name: str,
                             check_metadata: bool = True) -> Tuple[bool, List[str]]:
        """
        Validate agent launch before spawning Task tool.

        Checks:
        - Task was created with ProjectManager
        - task_info.json exists
        - prompt.md exists
        - Task directory structure is correct

        Args:
            project_id: Project ID
            task_name: Task name
            check_metadata: Whether to check for metadata files

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        task_path = self.framework_root / "projects" / project_id / "tasks" / task_name

        if not task_path.exists():
            errors.append(
                f"Task directory does not exist: {task_path}. "
                "Task must be created with ProjectManager.create_task() first."
            )
            passed = False
            self._log_validation("validate_agent_launch", passed, errors)
            return passed, errors

        if check_metadata:
            # Check task_info.json
            task_info = task_path / "task_info.json"
            if not task_info.exists():
                errors.append(
                    f"Missing task_info.json in {task_path}. "
                    "This indicates task was NOT created with ProjectManager."
                )

            # Check prompt.md
            prompt_file = task_path / "prompt.md"
            if not prompt_file.exists():
                errors.append(
                    f"Missing prompt.md in {task_path}. "
                    "ProjectManager.create_task() should auto-save this file."
                )

            # Check directory structure
            expected_dirs = []
            for expected_dir in expected_dirs:
                dir_path = task_path / expected_dir
                if not dir_path.exists():
                    # Not critical, just warning
                    pass

        passed = len(errors) == 0

        if passed:
            messages = [
                "Agent launch validation passed",
                f"Task directory exists: {task_path}",
                "Required metadata files present",
                "Ready to launch agent with Task tool"
            ]
        else:
            messages = errors

        self._log_validation("validate_agent_launch", passed, messages)
        return passed, messages

    def validate_task_structure(self,
                                project_id: str,
                                task_name: str) -> Tuple[bool, List[str]]:
        """
        Validate individual task structure against v2.2 ORGANIZED standard.

        Checks:
        - Task directory exists
        - task_info.json present
        - prompt.md present
        - README.md present (ORGANIZED standard)
        - reports/ subdirectory exists (ORGANIZED standard)
        - No orphaned reports in task root

        Args:
            project_id: Project ID
            task_name: Task name

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        warnings = []

        task_path = self.framework_root / "projects" / project_id / "tasks" / task_name

        if not task_path.exists():
            errors.append(f"Task directory does not exist: {task_path}")
            passed = False
            self._log_validation("validate_task_structure", passed, errors)
            return passed, errors

        # Check required files
        task_info = task_path / "task_info.json"
        if not task_info.exists():
            errors.append(f"Missing task_info.json")

        prompt_file = task_path / "prompt.md"
        if not prompt_file.exists():
            errors.append(f"Missing prompt.md")

        # Check ORGANIZED standard (v2.2)
        readme_file = task_path / "README.md"
        if not readme_file.exists():
            warnings.append("Missing README.md (recommended for ORGANIZED standard)")

        reports_dir = task_path / "reports"
        if not reports_dir.exists():
            warnings.append("Missing reports/ subdirectory (ORGANIZED standard)")

        # Check for orphaned reports (should be in reports/)
        md_files_in_root = [
            f.name for f in task_path.iterdir()
            if f.is_file() and f.suffix == '.md' and f.name not in ['prompt.md', 'README.md']
        ]

        if md_files_in_root:
            warnings.append(
                f"{len(md_files_in_root)} report file(s) in task root (should be in reports/): "
                f"{', '.join(md_files_in_root[:3])}"
            )

        passed = len(errors) == 0
        messages = errors + warnings

        if passed and not warnings:
            messages = [
                f"Task structure validation passed for '{task_name}'",
                "All required files present",
                "Task follows ORGANIZED standard (v2.2)"
            ]

        self._log_validation("validate_task_structure", passed, messages)
        return passed, messages

    def validate_project_structure(self, project_id: str) -> Tuple[bool, List[str]]:
        """
        Validate complete project structure against v2.2 standard.

        Expected structure:
        projects/[project-id]/
          - project_info.json
          - context.md
          - tasks/
          - synthesis/

        Args:
            project_id: Project ID to validate

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        warnings = []

        project_path = self.framework_root / "projects" / project_id

        if not project_path.exists():
            errors.append(f"Project directory does not exist: {project_path}")
            passed = False
            self._log_validation("validate_project_structure", passed, errors)
            return passed, errors

        # Check required files
        project_info = project_path / "project_info.json"
        if not project_info.exists():
            errors.append("Missing project_info.json")

        context_md = project_path / "context.md"
        if not context_md.exists():
            warnings.append("Missing context.md (recommended)")

        # Check required directories
        tasks_dir = project_path / "tasks"
        if not tasks_dir.exists():
            errors.append("Missing tasks/ directory")

        synthesis_dir = project_path / "synthesis"
        if not synthesis_dir.exists():
            warnings.append("Missing synthesis/ directory (recommended)")

        # Validate tasks if tasks/ exists
        if tasks_dir.exists():
            task_errors = self._validate_all_tasks(project_id)
            errors.extend(task_errors)

        passed = len(errors) == 0
        messages = errors + warnings

        if passed and not warnings:
            messages = [
                f"Project structure validation passed for '{project_id}'",
                "All required files present",
                "All required directories present"
            ]

        self._log_validation("validate_project_structure", passed, messages)
        return passed, messages

    def _validate_all_tasks(self, project_id: str) -> List[str]:
        """Validate all tasks in a project."""
        errors = []
        warnings = []
        tasks_path = self.framework_root / "projects" / project_id / "tasks"

        if not tasks_path.exists():
            return errors

        for task_dir in tasks_path.iterdir():
            if task_dir.is_dir():
                task_name = task_dir.name

                # Check task_info.json
                task_info = task_dir / "task_info.json"
                if not task_info.exists():
                    errors.append(
                        f"Task '{task_name}': Missing task_info.json"
                    )

                # Check prompt.md
                prompt_file = task_dir / "prompt.md"
                if not prompt_file.exists():
                    errors.append(
                        f"Task '{task_name}': Missing prompt.md"
                    )

                # Check ORGANIZED standard (v2.2)
                readme_file = task_dir / "README.md"
                reports_dir = task_dir / "reports"

                if not readme_file.exists():
                    warnings.append(
                        f"Task '{task_name}': Missing README.md (recommended for ORGANIZED standard)"
                    )

                if not reports_dir.exists():
                    warnings.append(
                        f"Task '{task_name}': Missing reports/ subdirectory (ORGANIZED standard)"
                    )

                # Check for reports in root (should be in reports/)
                md_files_in_root = [
                    f.name for f in task_dir.iterdir()
                    if f.is_file() and f.suffix == '.md' and f.name not in ['prompt.md', 'README.md']
                ]

                if md_files_in_root:
                    warnings.append(
                        f"Task '{task_name}': {len(md_files_in_root)} report files in root (should be in reports/): {', '.join(md_files_in_root[:3])}"
                    )

        # Return errors only (warnings are informational)
        return errors

    def _validate_task_naming(self, task_name: str) -> bool:
        """
        Validate task naming convention.

        Convention: [action]-[topic]-[details]
        Example: analizar-selectividad-clo2

        Args:
            task_name: Task name to validate

        Returns:
            True if valid, False otherwise
        """
        # Check kebab-case
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)+$', task_name):
            return False

        # Check minimum parts (action-topic)
        parts = task_name.split('-')
        if len(parts) < 2:
            return False

        return True

    def _validate_prompt_architecture(self, prompt: str) -> Dict[str, Any]:
        """
        Validate 2-layer prompt architecture (IMPROVED: structural validation).

        Layer 1 (Conversational): User request, disclaimers, supervision
        Layer 2 (Technical): Role, objectives, methodology, deliverables

        Args:
            prompt: Prompt content to validate

        Returns:
            Dict with 'valid' (bool) and 'reason' (str)
        """
        import re

        # Check minimum total length
        if len(prompt) < 500:
            return {
                "valid": False,
                "reason": "Prompt too short (< 500 chars). 2-layer architecture requires substantial context."
            }

        # SECURITY: Check for layer separator (---)
        # The separator should appear between Layer 1 and Layer 2
        separator_pattern = r'^\s*---+\s*$'
        has_separator = bool(re.search(separator_pattern, prompt, re.MULTILINE))

        if not has_separator:
            return {
                "valid": False,
                "reason": "Missing '---' separator between Layer 1 and Layer 2. Format: '## Layer 1\\n...\\n---\\n## Layer 2\\n...'"
            }

        # Detect sections with headers (## or ###)
        section_pattern = r'^#{1,3}\s+(.+)$'
        sections = re.findall(section_pattern, prompt, re.MULTILINE)

        if len(sections) < 2:
            return {
                "valid": False,
                "reason": f"Not enough sections ({len(sections)} found). Need at least 2 headers for Layer 1 + Layer 2."
            }

        # Analyze sections for Layer 1 markers (context)
        layer1_keywords = ['context', 'contexto', 'user request', 'usuario', 'disclaimer', 'supervision', 'oversight']
        has_layer1_section = any(
            any(kw in section.lower() for kw in layer1_keywords)
            for section in sections[:4]  # Check first 4 sections
        )

        # Analyze sections for Layer 2 markers (technical)
        layer2_keywords = ['objective', 'objetivo', 'methodology', 'metodología', 'role', 'rol', 'deliverable', 'task', 'tarea']
        has_layer2_section = any(
            any(kw in section.lower() for kw in layer2_keywords)
            for section in sections
        )

        # Split prompt into rough halves to validate length per layer
        midpoint = len(prompt) // 2
        layer1_content = prompt[:midpoint]
        layer2_content = prompt[midpoint:]

        # Validate Layer 1 presence and length
        if not has_layer1_section:
            return {
                "valid": False,
                "reason": "Missing Layer 1 (Conversational context). No section headers with context/user request/disclaimer."
            }

        if len(layer1_content) < 200:
            return {
                "valid": False,
                "reason": "Layer 1 too short (< 200 chars). Must include substantial conversational context."
            }

        # Validate Layer 2 presence and length
        if not has_layer2_section:
            return {
                "valid": False,
                "reason": "Missing Layer 2 (Technical details). No section headers with objective/methodology/role."
            }

        if len(layer2_content) < 300:
            return {
                "valid": False,
                "reason": "Layer 2 too short (< 300 chars). Must include technical details, methodology, and deliverables."
            }

        return {
            "valid": True,
            "reason": f"Prompt has {len(sections)} sections with proper 2-layer architecture."
        }

    def get_validation_report(self, last_n: int = 10) -> str:
        """
        Generate validation report from session log.

        Args:
            last_n: Number of recent validations to include

        Returns:
            Formatted report string
        """
        log = self.session["validation_log"][-last_n:]

        report_lines = [
            "Framework Validation Report",
            "=" * 50,
            f"Session ID: {self.session['session_id']}",
            f"Framework Version: {self.session['framework_version']}",
            f"Created: {self.session['created']}",
            "",
            f"Recent Validations (last {len(log)}):",
            ""
        ]

        for i, entry in enumerate(log, 1):
            status = "PASSED" if entry["passed"] else "FAILED"
            report_lines.append(f"{i}. {entry['operation']} - {status}")
            report_lines.append(f"   Time: {entry['timestamp']}")
            for msg in entry['messages']:
                report_lines.append(f"   - {msg}")
            report_lines.append("")

        return "\n".join(report_lines)

    def update_session_state(self, key: str, value: Any) -> None:
        """
        Update session state.

        Args:
            key: State key to update
            value: New value
        """
        self.session["state"][key] = value
        self._save_session()

    def set_active_project(self, project_id: str, validated: bool = True) -> None:
        """
        Set active project in session.

        Args:
            project_id: Project ID
            validated: Whether project structure was validated
        """
        self.session["active_project"] = {
            "id": project_id,
            "validated": validated,
            "set_at": datetime.now().isoformat()
        }
        self._save_session()


def validate_workflow(validator: FrameworkValidator,
                      workflow_type: str,
                      **kwargs) -> Tuple[bool, List[str]]:
    """
    Validate complete workflow execution.

    Args:
        validator: FrameworkValidator instance
        workflow_type: Type of workflow (e.g., 'research_workflow')
        **kwargs: Workflow-specific parameters

    Returns:
        Tuple of (is_valid, messages)
    """
    if workflow_type == "research_workflow":
        return validate_research_workflow(validator, **kwargs)
    else:
        return False, [f"Unknown workflow type: {workflow_type}"]


def validate_research_workflow(validator: FrameworkValidator,
                               user_request: str,
                               project_id: Optional[str] = None,
                               task_names: Optional[List[str]] = None,
                               prompts: Optional[List[str]] = None) -> Tuple[bool, List[str]]:
    """
    Validate research workflow end-to-end.

    Steps:
    1. Validate research request
    2. Validate project exists or can be created
    3. Validate task creation parameters
    4. Validate agent launch readiness

    Args:
        validator: FrameworkValidator instance
        user_request: User's research request
        project_id: Target project ID (if exists)
        task_names: List of proposed task names
        prompts: List of task prompts

    Returns:
        Tuple of (is_valid, messages)
    """
    all_messages = []

    # Step 1: Validate research request
    valid, messages = validator.validate_research_request(user_request)
    all_messages.extend(messages)
    if not valid:
        return False, all_messages

    # Step 2: Validate project
    if project_id:
        valid, messages = validator.validate_project_structure(project_id)
        all_messages.extend(messages)
        # Don't fail if project doesn't exist yet (will be created)

    # Step 3: Validate tasks
    if task_names and prompts:
        if len(task_names) != len(prompts):
            all_messages.append("ERROR: Mismatch between task_names and prompts count")
            return False, all_messages

        for task_name, prompt in zip(task_names, prompts):
            valid, messages = validator.validate_task_creation(
                project_id=project_id or "new-project",
                task_name=task_name,
                prompt=prompt,
                using_project_manager=True
            )
            all_messages.extend(messages)
            if not valid:
                return False, all_messages

    all_messages.append("Research workflow validation passed - ready to execute")
    return True, all_messages


if __name__ == "__main__":
    import sys
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        description='Framework Validation CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        Ejemplos:
          python core/framework_validator.py validate-project mi-proyecto-id
          python core/framework_validator.py report
          python core/framework_validator.py check-task mi-proyecto tarea-1
        ''')
    )

    subparsers = parser.add_subparsers(dest='command', help='Comando a ejecutar')

    # Subcommand: validate-project
    validate_parser = subparsers.add_parser(
        'validate-project',
        help='Validar estructura completa de proyecto'
    )
    validate_parser.add_argument('project_id', help='ID del proyecto')

    # Subcommand: report
    report_parser = subparsers.add_parser(
        'report',
        help='Mostrar reporte de validaciones recientes'
    )
    report_parser.add_argument(
        '--last',
        type=int,
        default=10,
        help='Numero de validaciones a mostrar (default: 10)'
    )

    # Subcommand: check-task
    task_parser = subparsers.add_parser(
        'check-task',
        help='Verificar tarea especifica'
    )
    task_parser.add_argument('project_id', help='ID del proyecto')
    task_parser.add_argument('task_name', help='Nombre de la tarea')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    validator = FrameworkValidator()

    # Ejecutar comando
    if args.command == 'validate-project':
        print(f"Validando proyecto: {args.project_id}")
        valid, messages = validator.validate_project_structure(args.project_id)

        for msg in messages:
            print(msg)

        if valid:
            print(f"\nPROYECTO VALIDO: {args.project_id}")
            sys.exit(0)
        else:
            print(f"\nPROYECTO INVALIDO: {args.project_id}")
            sys.exit(1)

    elif args.command == 'report':
        print("Reporte de Validaciones:\n")
        report = validator.get_validation_report(last_n=args.last)
        print(report)

    elif args.command == 'check-task':
        print(f"Verificando tarea: {args.project_id}/{args.task_name}")
        valid, messages = validator.validate_task_structure(
            args.project_id,
            args.task_name
        )

        for msg in messages:
            print(msg)

        if valid:
            print(f"\nTAREA VALIDA")
            sys.exit(0)
        else:
            print(f"\nTAREA INVALIDA")
            sys.exit(1)
