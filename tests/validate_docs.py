#!/usr/bin/env python3
"""
Validador de Consistencia de Documentacion
Framework v2.2 Baseline Validation Suite

Valida:
- Versiones consistentes (v2.2 en todos los docs)
- Referencias a archivos existen
- Comandos Python consistentes
- Sin contradicciones entre documentos
"""
import re
from pathlib import Path
from typing import Tuple, List


def validate_docs() -> Tuple[bool, List[str]]:
    """
    Valida consistencia de documentacion del framework

    Returns:
        tuple: (passed, errors)
            - passed (bool): True si todas las validaciones pasan
            - errors (list): Lista de errores encontrados
    """
    errors = []

    # Documentos core a validar
    docs = [
        "CLAUDE.md",
        "README.md",
        "ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md",
        "CHECKLIST.md"
    ]

    print("="*60)
    print("VALIDACION DE DOCUMENTACION")
    print("="*60)
    print()

    # Test 1: Versiones consistentes (DEBE SER v2.2)
    print("[1/6] Verificando versiones...")
    wrong_versions_found = False

    for doc in docs:
        doc_path = Path(doc)
        if not doc_path.exists():
            errors.append(f"{doc}: archivo no existe")
            continue

        content = doc_path.read_text(encoding='utf-8')

        # Buscar versiones INCORRECTAS (v1.0, v2.0, v2.1)
        # Excepto en contexto de changelog o menciones historicas
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            # Skip changelogs
            if 'changelog' in line.lower() or '###' in line:
                continue

            # Buscar versiones incorrectas
            wrong_versions = re.findall(r'(?:version|versión|framework)\s+v?(1\.0|2\.0|2\.1)\b',
                                       line, re.IGNORECASE)
            if wrong_versions:
                errors.append(f"{doc}:{i}: menciona version incorrecta {wrong_versions[0]} "
                            f"(esperada v2.2)")
                wrong_versions_found = True

    if not wrong_versions_found:
        print("  PASS - Versiones consistentes (v2.2)")

    # Test 2: Referencias a archivos existen
    print("[2/6] Verificando referencias a archivos...")
    broken_refs_found = False

    for doc in docs:
        doc_path = Path(doc)
        if not doc_path.exists():
            continue

        content = doc_path.read_text(encoding='utf-8')

        # Buscar referencias a archivos .py, .md, .json en codigo/paths
        # Patrones: `archivo.py`, core/archivo.py, etc.
        refs = re.findall(r'`?([a-zA-Z_/]+\.(?:py|md|json))`?', content)

        for ref in refs:
            # Skip URLs y paths obvio remotos
            if ref.startswith('http') or ref.startswith('www'):
                continue

            # Limpiar backticks si existen
            ref = ref.strip('`')

            # Verificar existencia
            ref_path = Path(ref)
            if not ref_path.exists():
                # Verificar si es relativo a algun directorio conocido
                alt_paths = [
                    Path(f"core/{ref}"),
                    Path(f"projects/{ref}"),
                    Path(f"docs/{ref}")
                ]

                exists_somewhere = any(p.exists() for p in alt_paths)

                if not exists_somewhere and not any(x in ref for x in ['example', 'placeholder', '[', ']']):
                    errors.append(f"{doc}: referencia rota a {ref}")
                    broken_refs_found = True

    if not broken_refs_found:
        print("  PASS - Referencias validas")

    # Test 3: Comandos Python consistentes
    print("[3/6] Verificando comandos Python...")
    python_commands = {}

    for doc in docs:
        doc_path = Path(doc)
        if not doc_path.exists():
            continue

        content = doc_path.read_text(encoding='utf-8')

        # Buscar comandos python
        cmds = re.findall(r'\b(python3?|py\s+-3|py)\s+', content)

        # Normalizar
        normalized_cmds = []
        for cmd in cmds:
            cmd = cmd.strip()
            if cmd == 'py -3':
                normalized_cmds.append('py -3')
            elif cmd.startswith('python'):
                normalized_cmds.append(cmd)
            elif cmd == 'py':
                normalized_cmds.append('py')

        if normalized_cmds:
            python_commands[doc] = set(normalized_cmds)

    # Verificar consistencia
    all_cmds = set()
    for cmds in python_commands.values():
        all_cmds.update(cmds)

    if len(all_cmds) > 1:
        errors.append(f"Comandos Python inconsistentes: {all_cmds}. "
                     f"Usar uno solo: 'python' recomendado")
        print(f"  FAIL - Comandos inconsistentes: {all_cmds}")
    else:
        print(f"  PASS - Comandos Python consistentes")

    # Test 4: FORGE docs no estan en root
    print("[4/6] Verificando ubicacion de FORGE docs...")
    forge_docs_in_root = []
    forge_docs = [
        "FORGE_ARCHITECTURE_v1.0.md",
        "FORGE_INTERFACES_v1.0.md",
        "FORGE_SPECIFICATION_SUMMARY.md"
    ]

    for forge_doc in forge_docs:
        if Path(forge_doc).exists():
            forge_docs_in_root.append(forge_doc)

    if forge_docs_in_root:
        errors.append(f"FORGE docs en root (deben estar en docs/proposals/forge/): "
                     f"{forge_docs_in_root}")
        print(f"  FAIL - FORGE docs en ubicacion incorrecta")
    else:
        print("  PASS - FORGE docs en ubicacion correcta (o no existen)")

    # Test 5: Estructura de reportes consistente (todos en reports/)
    print("[5/6] Verificando ejemplos de estructura...")
    structure_inconsistencies = False

    claude_path = Path("CLAUDE.md")
    if claude_path.exists():
        content = claude_path.read_text(encoding='utf-8')

        # Buscar ejemplos que muestren reportes en root (incorrecto)
        # Pattern: archivos .md fuera de reports/ en ejemplos de estructura
        if re.search(r'tasks/.*\n.*├── .*\.md\s*$', content, re.MULTILINE):
            # Verificar que NO sea README.md o prompt.md
            matches = re.findall(r'├── ([a-z_]+\.md)', content)
            for match in matches:
                if match not in ['README.md', 'prompt.md', 'task_info.json']:
                    errors.append(f"CLAUDE.md: ejemplo muestra reporte '{match}' en root "
                                f"(debe estar en reports/)")
                    structure_inconsistencies = True

    if not structure_inconsistencies:
        print("  PASS - Ejemplos de estructura correctos")

    # Test 6: Changelog dates consistentes entre README y CLAUDE
    print("[6/6] Verificando changelog dates...")
    readme_dates = {}
    claude_dates = {}

    readme_path = Path("README.md")
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        # Buscar ### vX.Y (YYYY-MM-DD)
        matches = re.findall(r'###\s+v([\d.]+)\s+\((\d{4}-\d{2}-\d{2})\)', content)
        readme_dates = {version: date for version, date in matches}

    claude_path = Path("CLAUDE.md")
    if claude_path.exists():
        content = claude_path.read_text(encoding='utf-8')
        matches = re.findall(r'###\s+v([\d.]+)\s+\((\d{4}-\d{2}-\d{2})\)', content)
        claude_dates = {version: date for version, date in matches}

    # Comparar fechas comunes
    for version in readme_dates:
        if version in claude_dates:
            if readme_dates[version] != claude_dates[version]:
                errors.append(f"Changelog date inconsistente para v{version}: "
                            f"README={readme_dates[version]}, "
                            f"CLAUDE={claude_dates[version]}")

    if readme_dates == claude_dates or not (readme_dates and claude_dates):
        print("  PASS - Changelog dates consistentes")

    # Resumen
    print()
    print("="*60)
    passed = len(errors) == 0
    return passed, errors


if __name__ == "__main__":
    passed, errors = validate_docs()

    if passed:
        print("RESULTADO: PASS")
        print("Documentacion es consistente")
    else:
        print(f"RESULTADO: FAIL ({len(errors)} errores)")
        print()
        print("ERRORES ENCONTRADOS:")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")

    print("="*60)
    exit(0 if passed else 1)
