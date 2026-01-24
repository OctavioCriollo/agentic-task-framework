#!/usr/bin/env python
"""
Script to fix project structure for tasks created before v2.2 validation

This script creates missing task_info.json and prompt.md files for tasks
that were created manually without using ProjectManager.
"""

import json
import os
from datetime import datetime
from pathlib import Path


def create_task_info(task_dir: Path, task_name: str, description: str, status: str = "completed"):
    """Create task_info.json for a task."""

    # Get list of markdown files in directory (reports)
    reports = []
    for item in task_dir.iterdir():
        if item.is_file() and item.suffix == '.md':
            reports.append(item.name)

    task_info = {
        "task_name": task_name,
        "description": description,
        "created": datetime.now().isoformat(),
        "status": status,
        "prompt_file": "prompt.md",
        "reports": reports
    }

    if status == "completed":
        task_info["completed_at"] = datetime.now().isoformat()

    info_path = task_dir / "task_info.json"
    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(task_info, f, indent=2, ensure_ascii=False)

    print(f"Created: {info_path}")
    return task_info


def create_prompt_placeholder(task_dir: Path, task_name: str, description: str):
    """Create prompt.md placeholder based on task reports."""

    prompt_content = f"""# Prompt de Tarea: {task_name}

## Nota de Migracion

Este archivo fue generado automaticamente durante la migracion a Framework v2.2.

La tarea original fue creada manualmente sin usar ProjectManager, por lo que
el prompt exacto no fue preservado. Este es un placeholder reconstruido basado
en los reportes generados.

## Descripcion de la Tarea

{description}

## Contexto del Proyecto

Investigacion cientifica sobre efectividad del dioxido de cloro (ClO2) contra COVID-19.

Instrucciones del usuario:
- Se neutral como cientifico
- Solo evidencia cientifica
- Todo excepto historia y controversia
- Interes en mecanismos moleculares

## Objetivo de la Tarea

{description}

## Metodologia

1. Revision de literatura cientifica peer-reviewed
2. Analisis de mecanismos moleculares
3. Evaluacion de evidencia experimental
4. Sintesis de hallazgos

## Estructura de Output

Documentacion tecnica detallada en formato Markdown.

## Criterios de Completitud

- Analisis exhaustivo del tema
- Referencias a literatura cientifica
- Conclusiones basadas en evidencia
- Documentacion completa

## Reportes Generados

"""

    # Add list of reports
    reports = []
    for item in task_dir.iterdir():
        if item.is_file() and item.suffix == '.md' and item.name != 'prompt.md':
            reports.append(item.name)

    for report in sorted(reports):
        prompt_content += f"- {report}\n"

    prompt_path = task_dir / "prompt.md"
    with open(prompt_path, 'w', encoding='utf-8') as f:
        f.write(prompt_content)

    print(f"Created: {prompt_path}")


def fix_task(project_root: Path, task_name: str, description: str, status: str = "completed"):
    """Fix a single task by creating missing metadata files."""

    task_dir = project_root / "tasks" / task_name

    if not task_dir.exists():
        print(f"ERROR: Task directory not found: {task_dir}")
        return False

    print(f"\nFixing task: {task_name}")
    print(f"  Directory: {task_dir}")

    # Create task_info.json
    task_info_path = task_dir / "task_info.json"
    if task_info_path.exists():
        print(f"  SKIP: task_info.json already exists")
    else:
        create_task_info(task_dir, task_name, description, status)

    # Create prompt.md
    prompt_path = task_dir / "prompt.md"
    if prompt_path.exists():
        print(f"  SKIP: prompt.md already exists")
    else:
        create_prompt_placeholder(task_dir, task_name, description)

    print(f"  DONE: Task {task_name} fixed")
    return True


def main():
    """Main function to fix all tasks in the project."""

    # Get framework root
    script_dir = Path(__file__).parent
    framework_root = script_dir.parent

    # Project to fix
    project_id = "investigaci-n-clo-covid-19-20251222-195407"
    project_root = framework_root / "projects" / project_id

    if not project_root.exists():
        print(f"ERROR: Project not found: {project_root}")
        return 1

    print(f"Fixing project: {project_id}")
    print(f"Project root: {project_root}")

    # Tasks to fix (missing metadata)
    tasks_to_fix = [
        {
            "name": "farmacocinetica-llegada-pulmon-clo2",
            "description": "Analisis farmacocinetico: concentraciones de ClO2 que llegan al pulmon",
            "status": "completed"
        },
        {
            "name": "selectividad-molecular-celular-clo2",
            "description": "Analisis de selectividad molecular y celular: ClO2 vs virus vs celulas humanas",
            "status": "completed"
        },
        {
            "name": "ventana-terapeutica-toxicologia-clo2",
            "description": "Evaluacion de ventana terapeutica y balance riesgo-beneficio de ClO2 para COVID-19",
            "status": "completed"
        },
        {
            "name": "revision-critica-research-kalcker",
            "description": "Revision critica de estudios de investigacion sobre ClO2 (referencia: Kalcker)",
            "status": "completed"
        }
    ]

    # Fix each task
    fixed_count = 0
    for task in tasks_to_fix:
        success = fix_task(
            project_root,
            task["name"],
            task["description"],
            task["status"]
        )
        if success:
            fixed_count += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY: Fixed {fixed_count}/{len(tasks_to_fix)} tasks")
    print(f"{'='*60}")

    # Run validator to verify
    print("\nRunning validator to verify fixes...")
    from framework_validator import FrameworkValidator

    validator = FrameworkValidator(framework_root)
    valid, messages = validator.validate_project_structure(project_id)

    if valid:
        print("SUCCESS: Project structure validation passed")
    else:
        print("VALIDATION FAILED:")
        for msg in messages:
            print(f"  - {msg}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
