#!/usr/bin/env python3
"""
Validador de Calidad de Codigo Python
Framework v2.2 Baseline Validation Suite

Valida:
- Docstrings en funciones publicas
- No hay DEPRECATED sin marcar
- No hay codigo comentado extenso
- No hay codigo legacy activo
"""
import ast
import re
from pathlib import Path
from typing import Tuple, List


def validate_code() -> Tuple[bool, List[str]]:
    """
    Valida modulos Python en core/

    Returns:
        tuple: (passed, errors)
            - passed (bool): True si todas las validaciones pasan
            - errors (list): Lista de errores encontrados
    """
    errors = []
    warnings = []

    print("="*60)
    print("VALIDACION DE CODIGO PYTHON")
    print("="*60)
    print()

    core_path = Path("core")
    if not core_path.exists():
        errors.append("Directorio core/ no existe")
        return False, errors

    # Test 1: Docstrings en funciones publicas
    print("[1/5] Verificando docstrings...")
    missing_docstrings = 0

    for module_path in core_path.glob("*.py"):
        if module_path.name.startswith("__"):
            continue

        content = module_path.read_text(encoding='utf-8')

        # Skip deprecated files
        if "DEPRECATED" in content[:500]:
            continue

        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Solo funciones publicas (no empiezan con _)
                    if not node.name.startswith("_"):
                        if not ast.get_docstring(node):
                            errors.append(
                                f"{module_path.name}: funcion publica '{node.name}' "
                                f"sin docstring"
                            )
                            missing_docstrings += 1
        except SyntaxError as e:
            errors.append(f"{module_path.name}: syntax error - {e}")

    if missing_docstrings == 0:
        print(f"  PASS - Todas las funciones publicas tienen docstrings")
    else:
        print(f"  FAIL - {missing_docstrings} funciones sin docstring")

    # Test 2: task_manager.py debe estar marcado como DEPRECATED o removido
    print("[2/5] Verificando codigo legacy...")
    task_manager_path = core_path / "task_manager.py"

    if task_manager_path.exists():
        content = task_manager_path.read_text(encoding='utf-8')

        # Verificar si tiene header DEPRECATED en primeras 100 lineas
        first_lines = '\n'.join(content.split('\n')[:100])

        if "DEPRECATED" not in first_lines:
            errors.append(
                "task_manager.py existe pero NO esta marcado como DEPRECATED "
                "en el header del archivo"
            )
            print("  FAIL - task_manager.py sin marcar deprecated")
        else:
            warnings.append(
                "task_manager.py esta deprecated pero aun presente en core/ "
                "(deberia moverse a legacy/)"
            )
            print("  WARNING - task_manager.py deprecated pero presente")
    else:
        print("  PASS - task_manager.py no existe (removido correctamente)")

    # Test 3: No hay codigo comentado extenso (>10 lineas consecutivas)
    print("[3/5] Verificando codigo comentado...")
    commented_code_found = False

    for module_path in core_path.glob("*.py"):
        content = module_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        consecutive_comments = 0
        max_consecutive = 0
        in_docstring = False

        for line in lines:
            stripped = line.strip()

            # Detectar docstrings
            if '"""' in stripped or "'''" in stripped:
                in_docstring = not in_docstring

            # Skip si estamos en docstring
            if in_docstring:
                consecutive_comments = 0
                continue

            # Contar comentarios consecutivos
            if stripped.startswith('#') and len(stripped) > 3:
                consecutive_comments += 1
                max_consecutive = max(max_consecutive, consecutive_comments)
            else:
                consecutive_comments = 0

        if max_consecutive > 10:
            errors.append(
                f"{module_path.name}: {max_consecutive} lineas de comentarios "
                f"consecutivos (posible codigo comentado)"
            )
            commented_code_found = True

    if not commented_code_found:
        print("  PASS - Sin codigo comentado extenso")

    # Test 4: No hay imports de task_manager en modulos activos
    print("[4/5] Verificando imports legacy...")
    legacy_imports_found = False

    for module_path in core_path.glob("*.py"):
        if module_path.name == "task_manager.py":
            continue  # Skip el mismo archivo

        content = module_path.read_text(encoding='utf-8')

        # Buscar imports de task_manager
        if re.search(r'from\s+task_manager\s+import|import\s+task_manager', content):
            errors.append(
                f"{module_path.name}: importa task_manager (deprecated)"
            )
            legacy_imports_found = True

    if not legacy_imports_found:
        print("  PASS - Sin imports de task_manager")

    # Test 5: Scripts utilities deben ser parametrizados (no hardcoded project_id)
    print("[5/5] Verificando project_id hardcodeado en scripts...")
    hardcoded_scripts = []

    utility_scripts = [
        "fix_project_structure.py",
        "check_empty_reports.py",
        "audit_project.py",
        "analyze_inconsistencies.py"
    ]

    for script_name in utility_scripts:
        script_path = core_path / script_name
        if not script_path.exists():
            continue

        content = script_path.read_text(encoding='utf-8')

        # Buscar project_id = "investigaci..." (hardcoded)
        if re.search(r'project_id\s*=\s*["\']investigaci', content):
            # Verificar que NO este en argparse o como parametro de funcion
            # Si esta como asignacion directa, es hardcoded
            if 'argparse' not in content or 'parser.add_argument' not in content:
                errors.append(
                    f"{script_name}: project_id hardcodeado (debe ser CLI argument)"
                )
                hardcoded_scripts.append(script_name)

    if not hardcoded_scripts:
        print("  PASS - Scripts parametrizados")
    else:
        print(f"  FAIL - {len(hardcoded_scripts)} scripts con project_id hardcodeado")

    # Resumen de warnings
    if warnings:
        print()
        print("ADVERTENCIAS:")
        for warning in warnings:
            print(f"  - {warning}")

    # Resumen final
    print()
    print("="*60)
    passed = len(errors) == 0
    return passed, errors


if __name__ == "__main__":
    passed, errors = validate_code()

    if passed:
        print("RESULTADO: PASS")
        print("Codigo Python cumple estandares")
    else:
        print(f"RESULTADO: FAIL ({len(errors)} errores)")
        print()
        print("ERRORES ENCONTRADOS:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")

    print("="*60)
    exit(0 if passed else 1)
