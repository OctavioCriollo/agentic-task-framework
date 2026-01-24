#!/usr/bin/env python3
"""
Verifica que NO haya símbolos no permitidos en los documentos.
Solo busca símbolos que NO están en la whitelist.
"""

import re
from pathlib import Path
from collections import defaultdict

# WHITELIST completa de símbolos permitidos
ALLOWED_SYMBOLS = {
    # Status indicators
    '✓', '✅', '✗', '❌',
    # Status circles
    '🟡', '🟢', '🔴', '🟠',
    # Radio buttons
    '⚪', '⚫', '🔘',
    # Geometric
    '●',
    # Arrows
    '←', '→', '↑', '↓', '↔', '↕',
    # Emphasis
    '☆', '★', '⚠', '⚡', '❓',
    # Box drawing
    '─', '│', '┌', '┐', '└', '┘', '├', '┤', '╱', '╲',
    '┬', '┴', '┼', '━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋',
}

# Patrones para encontrar símbolos Unicode especiales
emoji_pattern = re.compile(r'[\U0001F000-\U0001FFFF]')  # Emojis
geometric_pattern = re.compile(r'[\u25A0-\u25FF]')  # Geometric shapes
arrows_pattern = re.compile(r'[\u2190-\u21FF]')  # Arrows
misc_symbols = re.compile(r'[\u2600-\u27BF]')  # Misc symbols
box_drawing = re.compile(r'[\u2500-\u257F]')  # Box drawing

def find_non_allowed_symbols():
    """Encuentra símbolos que NO están en la whitelist"""

    violations = []

    # Buscar TODOS los archivos .md y .py en TODO el proyecto
    base_path = Path('.')

    # Excluir directorios que no deben revisarse
    exclude_dirs = {'.git', '.venv', '.venv.backup_20260117_120935', '.pytest_cache', '__pycache__', 'node_modules', '.memory_backups', 'archive', 'scripts', 'reports', 'legacy'}

    # Buscar recursivamente
    all_files = []
    for path in base_path.rglob('*'):
        # Saltar directorios excluidos
        if any(excluded in path.parts for excluded in exclude_dirs):
            continue

        # Solo archivos .md y .py
        if path.suffix in ['.md', '.py'] and path.is_file():
            all_files.append(path)

    for md_file in all_files:

        try:
            content = md_file.read_text(encoding='utf-8')
            lines = content.split('\n')

            for line_num, line in enumerate(lines, 1):
                # Buscar todos los símbolos especiales
                found_symbols = set()
                found_symbols.update(emoji_pattern.findall(line))
                found_symbols.update(geometric_pattern.findall(line))
                found_symbols.update(arrows_pattern.findall(line))
                found_symbols.update(misc_symbols.findall(line))
                found_symbols.update(box_drawing.findall(line))

                # Filtrar solo los que NO están permitidos
                non_allowed = found_symbols - ALLOWED_SYMBOLS

                if non_allowed:
                    violations.append({
                        'file': str(md_file),
                        'line': line_num,
                        'symbols': non_allowed,
                        'content': line.strip()[:100]
                    })

        except Exception as e:
            # Silenciar errores de encoding en archivos binarios
            pass

    return violations

def main():
    print("Verificando símbolos no permitidos...")
    print()

    violations = find_non_allowed_symbols()

    if not violations:
        print("PERFECTO: No se encontraron simbolos no permitidos")
        print()
        print("Todos los documentos cumplen con el protocolo de whitelist.")
        return

    print(f"VIOLACIONES ENCONTRADAS: {len(violations)}")
    print()

    # Agrupar por archivo
    by_file = defaultdict(list)
    for v in violations:
        by_file[v['file']].append(v)

    # Guardar a archivo
    with open('reports/VIOLACIONES_SIMBOLOS.md', 'w', encoding='utf-8') as f:
        f.write("# VIOLACIONES DE PROTOCOLO - SÍMBOLOS NO PERMITIDOS\n\n")

        for filename, file_violations in sorted(by_file.items()):
            f.write(f"\n## {filename}\n\n")
            for v in file_violations:
                symbols_str = ' '.join(v['symbols'])
                f.write(f"- **Línea {v['line']}**: {symbols_str}\n")
                f.write(f"  - Contenido: `{v['content']}`\n")

                # Mostrar códigos Unicode
                codes = [f"U+{ord(s):04X}" for s in v['symbols']]
                f.write(f"  - Unicode: {', '.join(codes)}\n")
            f.write("\n")

        f.write("\n---\n\n")
        f.write(f"**Total de violaciones:** {len(violations)} en {len(by_file)} archivo(s)\n\n")
        f.write("Estos símbolos deben ser removidos o reemplazados con texto.\n")

    print(f"Encontradas {len(violations)} violaciones en {len(by_file)} archivo(s)")
    print("Detalles guardados en: reports/VIOLACIONES_SIMBOLOS.md")

if __name__ == '__main__':
    main()
