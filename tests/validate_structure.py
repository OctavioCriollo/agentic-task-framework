#!/usr/bin/env python3
"""
Validador de Estructura de Proyectos
Framework v2.2 Baseline Validation Suite

Valida que proyectos cumplan con ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md (ORGANIZED)

Estructura esperada:
projects/[project-id]/tasks/[task-name]/
  ├── task_info.json          (REQUERIDO)
  ├── prompt.md               (REQUERIDO)
  ├── README.md               (REQUERIDO)
  └── reports/                (REQUERIDO - todos los reportes aqui)
      ├── [tema]_[aspecto]_[detalles].md
      └── ...
"""
import json
import re
from pathlib import Path
from typing import Tuple, List, Dict


def validate_structure(project_id: str) -> Tuple[bool, List[str]]:
    """
    Valida que proyecto cumple v2.2 ORGANIZED

    Args:
        project_id: ID del proyecto a validar

    Returns:
        tuple: (passed, errors)
            - passed (bool): True si todas las validaciones pasan
            - errors (list): Lista de errores encontrados
    """
    errors = []
    warnings = []

    print("="*60)
    print(f"VALIDACION DE ESTRUCTURA - PROYECTO: {project_id}")
    print("="*60)
    print()

    project_dir = Path("projects") / project_id
    tasks_dir = project_dir / "tasks"

    if not project_dir.exists():
        errors.append(f"Proyecto {project_id} no existe en projects/")
        return False, errors

    if not tasks_dir.exists():
        errors.append(f"Directorio tasks/ no existe en proyecto {project_id}")
        return False, errors

    # Obtener todas las tareas
    task_dirs = [d for d in tasks_dir.iterdir() if d.is_dir()]

    if not task_dirs:
        warnings.append(f"Proyecto {project_id} no tiene tareas")

    print(f"Total de tareas: {len(task_dirs)}")
    print()

    # Contadores
    compliant_tasks = 0
    non_compliant_tasks = 0

    # Validar cada tarea
    for task_dir in task_dirs:
        task_name = task_dir.name
        task_errors = []

        print(f"Validando: {task_name}")

        # Test 1: Archivos obligatorios existen
        required_files = ["task_info.json", "prompt.md", "README.md"]
        reports_dir = task_dir / "reports"

        for req_file in required_files:
            if not (task_dir / req_file).exists():
                task_errors.append(f"  - Falta archivo obligatorio: {req_file}")

        if not reports_dir.exists():
            task_errors.append(f"  - Falta directorio obligatorio: reports/")

        # Test 2: No hay archivos .md en root (excepto README.md y prompt.md)
        allowed_md_in_root = {"README.md", "prompt.md"}

        for md_file in task_dir.glob("*.md"):
            if md_file.name not in allowed_md_in_root:
                task_errors.append(
                    f"  - Archivo .md en root (debe estar en reports/): {md_file.name}"
                )

        # Test 3: task_info.json es valido y tiene campos requeridos
        task_info_path = task_dir / "task_info.json"
        if task_info_path.exists():
            try:
                with open(task_info_path, 'r', encoding='utf-8') as f:
                    task_info = json.load(f)

                # Campos requeridos
                required_fields = ["task_name", "description", "status", "reports"]
                for field in required_fields:
                    if field not in task_info:
                        task_errors.append(
                            f"  - task_info.json falta campo requerido: {field}"
                        )

                # Verificar que reportes listados existen
                if "reports" in task_info and reports_dir.exists():
                    listed_reports = task_info["reports"]

                    for report in listed_reports:
                        # Limpiar prefijo "reports/" si existe (inconsistencia)
                        clean_report = report.replace("reports/", "")

                        # No debe listar README.md (ese esta en root)
                        if clean_report == "README.md":
                            task_errors.append(
                                f"  - task_info.json lista 'README.md' como reporte "
                                f"(README.md debe estar solo en root)"
                            )
                            continue

                        # Verificar que archivo existe
                        report_path = reports_dir / clean_report
                        if not report_path.exists():
                            task_errors.append(
                                f"  - task_info.json lista '{report}' pero no existe"
                            )

                # Verificar que reportes reales estan listados
                if reports_dir.exists():
                    real_reports = [r.name for r in reports_dir.glob("*.md")]
                    listed = [r.replace("reports/", "") for r in task_info.get("reports", [])]

                    for real_report in real_reports:
                        if real_report not in listed:
                            # Solo warning si status es completed
                            if task_info.get("status") == "completed":
                                task_errors.append(
                                    f"  - Reporte '{real_report}' existe pero NO esta "
                                    f"listado en task_info.json"
                                )

            except json.JSONDecodeError as e:
                task_errors.append(f"  - task_info.json no es JSON valido: {e}")
            except Exception as e:
                task_errors.append(f"  - Error leyendo task_info.json: {e}")

        # Test 4: Naming de reportes (snake_case minusculas, no SCREAMING)
        if reports_dir.exists():
            for report in reports_dir.glob("*.md"):
                filename = report.name

                # Verificar que no sea SCREAMING_SNAKE_CASE
                if filename.isupper() or re.match(r'^[A-Z_]+\.md$', filename):
                    task_errors.append(
                        f"  - Reporte con naming incorrecto (debe ser snake_case): "
                        f"{filename}"
                    )

                # Verificar que sea snake_case (minusculas + underscores)
                # Excepto README.md si existiera (no deberia estar aqui)
                if filename != "README.md":
                    if not re.match(r'^[a-z0-9_]+\.md$', filename):
                        task_errors.append(
                            f"  - Reporte no sigue snake_case: {filename}"
                        )

        # Test 5: Nombre de tarea sigue convencion kebab-case
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)+$', task_name):
            task_errors.append(
                f"  - Nombre de tarea no sigue kebab-case: {task_name}"
            )

        # Test 6: Si status es completed, debe tener al menos 1 reporte
        if task_info_path.exists():
            try:
                with open(task_info_path, 'r', encoding='utf-8') as f:
                    task_info = json.load(f)

                if task_info.get("status") == "completed":
                    if reports_dir.exists():
                        reports_count = len(list(reports_dir.glob("*.md")))
                        if reports_count == 0:
                            task_errors.append(
                                f"  - Tarea marcada 'completed' pero reports/ esta vacio"
                            )
                    else:
                        task_errors.append(
                            f"  - Tarea marcada 'completed' pero no tiene reports/"
                        )
            except:
                pass

        # Resumen de tarea
        if task_errors:
            print("  STATUS: NON-COMPLIANT")
            errors.extend([f"{task_name}{err}" for err in task_errors])
            non_compliant_tasks += 1
        else:
            print("  STATUS: COMPLIANT")
            compliant_tasks += 1

        print()

    # Resumen global
    print("="*60)
    print("RESUMEN")
    print("="*60)
    print(f"Tareas COMPLIANT: {compliant_tasks}")
    print(f"Tareas NON-COMPLIANT: {non_compliant_tasks}")
    print(f"Compliance rate: {compliant_tasks/(compliant_tasks+non_compliant_tasks)*100:.1f}%"
          if (compliant_tasks+non_compliant_tasks) > 0 else "N/A")
    print()

    passed = len(errors) == 0
    return passed, errors


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python validate_structure.py [project-id]")
        print()
        print("Ejemplo:")
        print("  python validate_structure.py investigaci-n-clo-covid-19-20251222-195407")
        exit(1)

    project_id = sys.argv[1]
    passed, errors = validate_structure(project_id)

    if passed:
        print("RESULTADO: PASS")
        print("Estructura cumple v2.2 ORGANIZED")
    else:
        print(f"RESULTADO: FAIL ({len(errors)} errores)")
        print()
        print("ERRORES ENCONTRADOS:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")

    print("="*60)
    exit(0 if passed else 1)
