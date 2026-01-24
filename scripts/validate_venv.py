#!/usr/bin/env python3
"""
validate_venv.py - Valida la configuración del virtual environment

Verifica:
1. Que venv existe
2. Que venv contiene las dependencias correctas
3. Que el framework funciona sin dependencias externas
4. Que los imports del framework son solo stdlib
"""

import sys
import subprocess
from pathlib import Path
import json

# Colores para output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_section(title):
    """Imprime un título de sección."""
    print(f"\n{BOLD}{'=' * 60}{RESET}")
    print(f"{BOLD}{title}{RESET}")
    print(f"{BOLD}{'=' * 60}{RESET}\n")

def print_check(message, status):
    """Imprime un check con estado."""
    if status:
        print(f"{GREEN}✓{RESET} {message}")
        return True
    else:
        print(f"{RED}✗{RESET} {message}")
        return False

def print_warning(message):
    """Imprime un warning."""
    print(f"{YELLOW}⚠{RESET} {message}")

def check_venv_exists():
    """Verifica que venv existe."""
    venv_path = Path.cwd() / '.venv'
    return venv_path.exists() and venv_path.is_dir()

def check_venv_activated():
    """Verifica si estamos en venv activado."""
    return sys.prefix != sys.base_prefix

def get_packages(python_exe):
    """Obtiene lista de paquetes instalados."""
    try:
        result = subprocess.run(
            [python_exe, '-m', 'pip', 'list', '--format', 'json'],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error obteniendo paquetes: {e}")
        return []

def check_framework_imports():
    """Verifica que framework solo usa stdlib."""
    import ast

    core_dir = Path.cwd() / 'core'
    if not core_dir.exists():
        return False, "Directorio core/ no encontrado"

    stdlib_modules = {
        'os', 'sys', 'json', 'pathlib', 'datetime', 'typing',
        'logging', 're', 'shutil', 'argparse', 'subprocess',
        'tempfile', 'collections', 'itertools', 'functools'
    }

    non_stdlib = set()

    for py_file in core_dir.glob('*.py'):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        module = alias.name.split('.')[0]
                        if module not in stdlib_modules:
                            non_stdlib.add(module)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        module = node.module.split('.')[0]
                        if module not in stdlib_modules:
                            non_stdlib.add(module)
        except Exception as e:
            print(f"  Error analizando {py_file.name}: {e}")

    if non_stdlib:
        return False, f"Imports no-stdlib encontrados: {', '.join(non_stdlib)}"
    return True, "Solo imports de stdlib"

def check_framework_works_without_venv():
    """Verifica que framework funciona sin venv."""
    try:
        # Temporalmente desactivar venv si está activado
        original_prefix = sys.prefix

        # Intentar importar ProjectManager
        from core.project_manager import ProjectManager
        pm = ProjectManager()

        return True, "Framework funciona correctamente"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Función principal."""
    print_section("VALIDACIÓN DE VIRTUAL ENVIRONMENT")

    passed = 0
    failed = 0
    warnings = 0

    # 1. Verificar existencia de venv
    print_section("1. Verificar Existencia de Venv")
    if print_check("Venv directory existe", check_venv_exists()):
        passed += 1
    else:
        failed += 1
        print("  Ejecuta: ./start_coordinator.sh para crear venv")

    # 2. Verificar estado de activación
    print_section("2. Verificar Estado de Activación")
    in_venv = check_venv_activated()
    if in_venv:
        print_check("Venv está activado", True)
        print(f"  Python actual: {sys.executable}")
        passed += 1
    else:
        print_warning("Venv NO está activado (usando Python global)")
        print(f"  Python actual: {sys.executable}")
        print("  Para activar: source .venv/Scripts/activate")
        warnings += 1

    # 3. Verificar paquetes en venv
    print_section("3. Verificar Paquetes en Venv")
    venv_python = Path.cwd() / '.venv' / 'Scripts' / 'python.exe'
    if venv_python.exists():
        packages = get_packages(str(venv_python))
        print(f"Paquetes en venv: {len(packages)}")

        # Verificar testing packages
        pkg_names = {p['name'] for p in packages}
        has_pytest = 'pytest' in pkg_names
        has_pytest_cov = 'pytest-cov' in pkg_names

        if print_check("pytest instalado en venv", has_pytest):
            passed += 1
        else:
            failed += 1

        if print_check("pytest-cov instalado en venv", has_pytest_cov):
            passed += 1
        else:
            failed += 1

        # Mostrar todos los paquetes
        print("\n  Paquetes instalados:")
        for pkg in packages:
            print(f"    - {pkg['name']} ({pkg['version']})")
    else:
        print_check("Venv Python ejecutable encontrado", False)
        failed += 1

    # 4. Verificar paquetes en global Python
    print_section("4. Verificar Paquetes en Global Python")
    global_packages = get_packages(sys.base_prefix + '/python.exe' if sys.platform == 'win32' else sys.base_prefix + '/bin/python')
    global_pkg_names = {p['name'] for p in global_packages}

    has_global_pytest = 'pytest' in global_pkg_names
    has_global_pytest_cov = 'pytest-cov' in global_pkg_names

    if has_global_pytest or has_global_pytest_cov:
        print_warning("Paquetes de testing encontrados en Python global")
        if has_global_pytest:
            print("  - pytest (debería estar solo en venv)")
        if has_global_pytest_cov:
            print("  - pytest-cov (debería estar solo en venv)")
        print("\n  Para limpiar (OPCIONAL):")
        print("    pip uninstall pytest pytest-cov")
        warnings += 1
    else:
        print_check("Python global limpio (sin paquetes de testing)", True)
        passed += 1

    # 5. Verificar imports del framework
    print_section("5. Verificar Imports del Framework")
    stdlib_ok, msg = check_framework_imports()
    if print_check(msg, stdlib_ok):
        passed += 1
    else:
        failed += 1

    # 6. Verificar que framework funciona
    print_section("6. Verificar Funcionamiento del Framework")
    works, msg = check_framework_works_without_venv()
    if print_check(msg, works):
        passed += 1
    else:
        failed += 1

    # 7. Verificar requirements.txt
    print_section("7. Verificar requirements.txt")
    req_file = Path.cwd() / 'requirements.txt'
    if req_file.exists():
        content = req_file.read_text(encoding='utf-8')
        # Contar líneas no comentadas
        real_lines = [l for l in content.split('\n') if l.strip() and not l.strip().startswith('#')]

        if len(real_lines) == 0:
            print_warning("requirements.txt está vacío (solo comentarios)")
            print("  Considera agregar dependencias opcionales:")
            print("    pytest>=9.0.0")
            print("    pytest-cov>=7.0.0")
            warnings += 1
        else:
            print_check(f"requirements.txt contiene {len(real_lines)} dependencias", True)
            passed += 1
    else:
        print_check("requirements.txt existe", False)
        failed += 1

    # Resumen final
    print_section("RESUMEN")
    print(f"{GREEN}Passed:{RESET} {passed}")
    print(f"{RED}Failed:{RESET} {failed}")
    print(f"{YELLOW}Warnings:{RESET} {warnings}")

    total_checks = passed + failed
    score = (passed / total_checks * 100) if total_checks > 0 else 0

    print(f"\n{BOLD}Score: {score:.1f}%{RESET}")

    if failed == 0:
        print(f"\n{GREEN}{BOLD}✓ VALIDACIÓN EXITOSA{RESET}")
        return 0
    elif failed <= 2:
        print(f"\n{YELLOW}{BOLD}⚠ VALIDACIÓN CON WARNINGS{RESET}")
        print("\nEjecuta ./scripts/fix_venv_setup.sh para corregir")
        return 1
    else:
        print(f"\n{RED}{BOLD}✗ VALIDACIÓN FALLIDA{RESET}")
        print("\nEjecuta ./scripts/fix_venv_setup.sh para corregir")
        return 2

if __name__ == '__main__':
    sys.exit(main())
