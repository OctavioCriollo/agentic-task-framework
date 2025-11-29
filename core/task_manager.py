#!/usr/bin/env python3
"""
Agentic Task Framework - Task Manager
Professional task orchestration system
"""

import os
import sys
import json
import uuid
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import argparse


class TaskManager:
    """
    Professional task management system
    Handles dynamic task creation, prompt design, and agent launching
    """

    def __init__(self, framework_dir: Optional[str] = None):
        self.framework_dir = framework_dir or os.getcwd()
        self.tasks_dir = os.path.join(self.framework_dir, "tasks")
        self.core_dir = os.path.join(self.framework_dir, "core")
        self.registry_file = os.path.join(self.framework_dir, ".task_registry.json")

        self._ensure_structure()

    def _ensure_structure(self):
        """Ensure framework structure exists"""
        os.makedirs(self.tasks_dir, exist_ok=True)
        os.makedirs(self.core_dir, exist_ok=True)

        if not os.path.exists(self.registry_file):
            self._init_registry()

    def _init_registry(self):
        """Initialize task registry"""
        registry = {
            "framework_version": "1.0.0",
            "created": datetime.now().isoformat(),
            "tasks": []
        }
        self._save_registry(registry)

    def create_task(
        self,
        name: str,
        task_type: str,
        prompt_content: str,
        description: str = "",
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Create a new specialized task

        Args:
            name: Task identifier (kebab-case)
            task_type: Type of task (analysis, research, development, etc.)
            prompt_content: Dynamically designed prompt for this specific task
            description: Human-readable description
            context: Additional context from main conversation

        Returns:
            Task metadata
        """
        # Generate task ID
        task_id = self._generate_task_id(name)

        # Create task directory structure
        task_dir = os.path.join(self.tasks_dir, task_id)
        os.makedirs(task_dir, exist_ok=True)
        os.makedirs(os.path.join(task_dir, "context"), exist_ok=True)
        os.makedirs(os.path.join(task_dir, "output"), exist_ok=True)
        os.makedirs(os.path.join(task_dir, ".memory_backups"), exist_ok=True)

        # Create CLAUDE.md with dynamically designed prompt
        claude_md_path = os.path.join(task_dir, "CLAUDE.md")
        with open(claude_md_path, 'w', encoding='utf-8') as f:
            f.write(prompt_content)

        # Save context if provided
        if context:
            context_path = os.path.join(task_dir, "context", "initial_context.json")
            with open(context_path, 'w', encoding='utf-8') as f:
                json.dump(context, f, indent=2, ensure_ascii=False)

        # Register task
        task_metadata = {
            "id": task_id,
            "name": name,
            "type": task_type,
            "description": description,
            "created": datetime.now().isoformat(),
            "status": "active",
            "directory": task_dir,
            "prompt_file": claude_md_path
        }

        self._register_task(task_metadata)

        # Launch specialized agent
        self._launch_agent(task_dir, task_id)

        return task_metadata

    def _generate_task_id(self, name: str) -> str:
        """Generate unique task ID"""
        # Sanitize name
        safe_name = name.lower().replace(" ", "-").replace("_", "-")
        # Remove special characters
        safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '-')
        # Add short UUID for uniqueness
        unique_id = str(uuid.uuid4())[:8]
        return f"{safe_name}-{unique_id}"

    def _launch_agent(self, task_dir: str, task_id: str):
        """Launch specialized agent in new terminal"""
        launcher_script = os.path.join(self.core_dir, "task_launcher.sh")

        if not os.path.exists(launcher_script):
            print(f"✗ Error: task_launcher.sh no encontrado en {self.core_dir}", file=sys.stderr)
            return

        try:
            # Launch with mintty for Windows Git Bash
            subprocess.Popen(
                ['mintty', '-t', f'Task: {task_id}',
                 '-e', 'bash', launcher_script, task_dir],
                cwd=task_dir
            )
            print(f"✓ Agente especializado lanzado")
        except FileNotFoundError:
            # Fallback: try direct bash
            try:
                subprocess.Popen(
                    ['bash', launcher_script, task_dir],
                    cwd=task_dir
                )
                print(f"✓ Agente lanzado (modo compatibilidad)")
            except Exception as e:
                print(f"✗ Error al lanzar agente: {e}", file=sys.stderr)

    def _register_task(self, task_metadata: Dict):
        """Register task in registry"""
        registry = self._load_registry()
        registry["tasks"].append(task_metadata)
        self._save_registry(registry)

    def list_tasks(self, status_filter: Optional[str] = None) -> List[Dict]:
        """List all tasks, optionally filtered by status"""
        registry = self._load_registry()
        tasks = registry["tasks"]

        if status_filter:
            tasks = [t for t in tasks if t["status"] == status_filter]

        return tasks

    def get_task(self, task_id: str) -> Optional[Dict]:
        """Get task metadata by ID"""
        registry = self._load_registry()
        for task in registry["tasks"]:
            if task["id"] == task_id or task["id"].startswith(task_id):
                return task
        return None

    def update_task_status(self, task_id: str, new_status: str):
        """Update task status"""
        registry = self._load_registry()
        for task in registry["tasks"]:
            if task["id"] == task_id or task["id"].startswith(task_id):
                task["status"] = new_status
                task["updated"] = datetime.now().isoformat()
                break
        self._save_registry(registry)

    def _load_registry(self) -> Dict:
        """Load task registry"""
        if not os.path.exists(self.registry_file):
            self._init_registry()
        with open(self.registry_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_registry(self, registry: Dict):
        """Save task registry"""
        with open(self.registry_file, 'w', encoding='utf-8') as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Agentic Task Framework - Task Manager"
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Create task
    create_parser = subparsers.add_parser('create', help='Create new task')
    create_parser.add_argument('--name', required=True, help='Task name')
    create_parser.add_argument('--type', required=True, help='Task type')
    create_parser.add_argument('--prompt', required=True, help='Prompt content or file')
    create_parser.add_argument('--description', default="", help='Description')
    create_parser.add_argument('--context', help='Context JSON file')

    # List tasks
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--status', help='Filter by status')

    # Get task
    get_parser = subparsers.add_parser('get', help='Get task info')
    get_parser.add_argument('task_id', help='Task ID')

    # Update status
    update_parser = subparsers.add_parser('update-status', help='Update task status')
    update_parser.add_argument('task_id', help='Task ID')
    update_parser.add_argument('status', help='New status')

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == 'create':
        # Load prompt content
        if os.path.exists(args.prompt):
            with open(args.prompt, 'r', encoding='utf-8') as f:
                prompt_content = f.read()
        else:
            prompt_content = args.prompt

        # Load context if provided
        context = None
        if args.context and os.path.exists(args.context):
            with open(args.context, 'r', encoding='utf-8') as f:
                context = json.load(f)

        # Create task
        task = manager.create_task(
            name=args.name,
            task_type=args.type,
            prompt_content=prompt_content,
            description=args.description,
            context=context
        )

        print(f"\n✓ Tarea creada exitosamente")
        print(f"  ID: {task['id']}")
        print(f"  Nombre: {task['name']}")
        print(f"  Tipo: {task['type']}")
        print(f"  Directorio: {task['directory']}")
        print(f"  Agente lanzado en nueva terminal\n")

    elif args.command == 'list':
        tasks = manager.list_tasks(status_filter=args.status)
        print(f"\n{'='*60}")
        print(f"Tareas Activas: {len(tasks)}")
        print(f"{'='*60}\n")

        if not tasks:
            print("No hay tareas registradas.\n")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['name']} ({task['id']})")
                print(f"   Tipo: {task['type']}")
                print(f"   Estado: {task['status']}")
                print(f"   Creada: {task['created']}")
                print(f"   Directorio: {task['directory']}")
                if task.get('description'):
                    print(f"   Descripción: {task['description']}")
                print()

    elif args.command == 'get':
        task = manager.get_task(args.task_id)
        if task:
            print(f"\n{'='*60}")
            print(f"Tarea: {task['name']}")
            print(f"{'='*60}\n")
            print(json.dumps(task, indent=2, ensure_ascii=False))
            print()
        else:
            print(f"\n✗ Tarea no encontrada: {args.task_id}\n", file=sys.stderr)
            sys.exit(1)

    elif args.command == 'update-status':
        task = manager.get_task(args.task_id)
        if task:
            manager.update_task_status(task['id'], args.status)
            print(f"\n✓ Estado actualizado: {task['name']} -> {args.status}\n")
        else:
            print(f"\n✗ Tarea no encontrada: {args.task_id}\n", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
