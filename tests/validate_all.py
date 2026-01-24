#!/usr/bin/env python3
"""
Suite Master de Validacion - Framework v2.2 Baseline
Ejecuta todas las validaciones del framework

Validaciones:
1. Documentacion: Consistencia, versiones, referencias
2. Codigo: Calidad, docstrings, legacy code
3. Estructura: Compliance con v2.2 ORGANIZED

Este script determina si el baseline v2.2 esta limpio y listo
para migracion a Forge v1.0
"""
import sys
from pathlib import Path
from datetime import datetime

# Importar validadores
sys.path.insert(0, str(Path(__file__).parent))
from validate_docs import validate_docs
from validate_code import validate_code
from validate_structure import validate_structure


def print_header(text: str):
    """Imprime header formateado"""
    print()
    print("="*70)
    print(f"  {text}")
    print("="*70)
    print()


def validate_all(project_id: str) -> bool:
    """
    Ejecuta todos los validadores

    Args:
        project_id: ID del proyecto a validar

    Returns:
        bool: True si todos pasan
    """
    print_header("SUITE DE VALIDACION FRAMEWORK v2.2 BASELINE")

    print(f"Proyecto a validar: {project_id}")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_passed = True
    results = {}

    # Validar documentacion
    print_header("VALIDACION 1/3: DOCUMENTACION")
    docs_passed, docs_errors = validate_docs()
    results['docs'] = (docs_passed, docs_errors)

    # Validar codigo
    print_header("VALIDACION 2/3: CODIGO PYTHON")
    code_passed, code_errors = validate_code()
    results['code'] = (code_passed, code_errors)

    # Validar estructura
    print_header(f"VALIDACION 3/3: ESTRUCTURA DEL PROYECTO")
    struct_passed, struct_errors = validate_structure(project_id)
    results['structure'] = (struct_passed, struct_errors)

    # Reporte consolidado
    print_header("RESULTADOS CONSOLIDADOS")

    total_errors = 0
    for name, (passed, errors) in results.items():
        status = "PASS" if passed else "FAIL"
        symbol = "[✓]" if passed else "[✗]"

        error_count = len(errors)
        total_errors += error_count

        print(f"{symbol} {name.upper():<15} {status:<10} ({error_count} errores)")

        # Mostrar primeros errores
        if not passed and errors:
            for error in errors[:3]:  # Primeros 3
                # Truncar si es muy largo
                error_text = error if len(error) < 80 else error[:77] + "..."
                print(f"      - {error_text}")

            if len(errors) > 3:
                print(f"      ... y {len(errors)-3} errores mas")

        all_passed = all_passed and passed

    print()
    print("-"*70)
    print(f"Total de errores: {total_errors}")
    print("-"*70)
    print()

    # Criterios de aceptacion
    print_header("CRITERIOS DE ACEPTACION")

    criteria = {
        "Documentacion consistente (v2.2)": results['docs'][0],
        "Codigo limpio (sin deprecated activo)": results['code'][0],
        "Estructura compliant (v2.2 ORGANIZED)": results['structure'][0]
    }

    for criterion, met in criteria.items():
        symbol = "[✓]" if met else "[✗]"
        status = "CUMPLE" if met else "NO CUMPLE"
        print(f"{symbol} {criterion:<50} {status}")

    print()

    # Resultado final
    print_header("RESULTADO FINAL")

    if all_passed:
        print("                    *** BASELINE LIMPIO ***")
        print()
        print("  El framework v2.2 esta LISTO para:")
        print("    - Uso en produccion con confianza")
        print("    - Migracion a Forge v1.0")
        print("    - Documentacion como referencia baseline")
        print()
        print("  Proximos pasos recomendados:")
        print("    1. Crear tag git para baseline v2.2")
        print("    2. Documentar lecciones aprendidas")
        print("    3. Proceder con Forge v1.0 si es necesario")
        print()
    else:
        print("            *** CORRECCIONES NECESARIAS ***")
        print()
        print(f"  Se identificaron {total_errors} problemas que requieren atencion")
        print()
        print("  Acciones recomendadas:")
        print("    1. Revisar errores reportados arriba")
        print("    2. Aplicar correcciones segun plan de remediacion")
        print("    3. Re-ejecutar validate_all.py")
        print("    4. Repetir hasta alcanzar PASS")
        print()
        print("  Para ver errores detallados, ejecutar validadores individuales:")
        print("    - python tests/validate_docs.py")
        print("    - python tests/validate_code.py")
        print(f"    - python tests/validate_structure.py {project_id}")
        print()

    print("="*70)
    print()

    return all_passed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("="*70)
        print("  SUITE DE VALIDACION FRAMEWORK v2.2 BASELINE")
        print("="*70)
        print()
        print("Uso: python validate_all.py [project-id]")
        print()
        print("Este script valida:")
        print("  1. Documentacion (consistencia, versiones, referencias)")
        print("  2. Codigo Python (calidad, docstrings, legacy code)")
        print("  3. Estructura de proyecto (compliance v2.2 ORGANIZED)")
        print()
        print("Ejemplo:")
        print("  python tests/validate_all.py investigaci-n-clo-covid-19-20251222-195407")
        print()
        print("="*70)
        exit(1)

    project_id = sys.argv[1]
    passed = validate_all(project_id)

    exit(0 if passed else 1)
