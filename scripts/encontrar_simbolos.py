#!/usr/bin/env python3
"""
Script para encontrar todos los símbolos/emojis únicos en documentos markdown.
"""

import re
from pathlib import Path
from collections import defaultdict

# Patrones para diferentes tipos de símbolos
emoji_pattern = re.compile(r'[\U0001F000-\U0001F9FF]')  # Emojis
geometric_pattern = re.compile(r'[\u25A0-\u25FF]')  # Geometric shapes
arrows_pattern = re.compile(r'[\u2190-\u21FF]')  # Arrows
misc_symbols = re.compile(r'[\u2600-\u27BF]')  # Misc symbols
box_drawing = re.compile(r'[\u2500-\u257F]')  # Box drawing

def find_all_symbols():
    """Encuentra todos los símbolos en docs/ y reports/"""

    symbol_files = defaultdict(list)

    for directory in ['docs', 'reports']:
        dir_path = Path(directory)
        if not dir_path.exists():
            continue

        for md_file in dir_path.glob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')

                # Buscar todos los símbolos
                symbols = set()
                symbols.update(emoji_pattern.findall(content))
                symbols.update(geometric_pattern.findall(content))
                symbols.update(arrows_pattern.findall(content))
                symbols.update(misc_symbols.findall(content))
                symbols.update(box_drawing.findall(content))

                # Registrar archivo para cada símbolo
                for symbol in symbols:
                    symbol_files[symbol].append(str(md_file))

            except Exception as e:
                print(f"Error leyendo {md_file}: {e}")

    return symbol_files

def categorize_symbol(symbol):
    """Categoriza un símbolo por su código Unicode"""
    code = ord(symbol)

    # Ya aprobados
    approved = ['✓', '✅', '✗', '❌', '🟡', '🟢', '🔴', '⚪', '⚫', '🔘']
    if symbol in approved:
        return 'APROBADO'

    # Box drawing (diagramas de árbol)
    if 0x2500 <= code <= 0x257F:
        return 'BOX_DRAWING'

    # Flechas
    if 0x2190 <= code <= 0x21FF:
        return 'ARROW'

    # Formas geométricas
    if 0x25A0 <= code <= 0x25FF:
        return 'GEOMETRIC'

    # Símbolos misceláneos
    if 0x2600 <= code <= 0x27BF:
        return 'MISC_SYMBOL'

    # Emojis (probablemente pictográficos - NO aceptables)
    if 0x1F000 <= code <= 0x1F9FF:
        return 'EMOJI_PICTOGRAPHIC'

    return 'OTHER'

def main():
    print("Buscando símbolos en documentos...")
    print()

    symbol_files = find_all_symbols()

    if not symbol_files:
        print("No se encontraron símbolos.")
        return

    # Categorizar y mostrar
    categorized = defaultdict(list)
    for symbol in sorted(symbol_files.keys()):
        category = categorize_symbol(symbol)
        categorized[category].append(symbol)

    # Guardar a archivo
    with open('reports/SIMBOLOS_ENCONTRADOS.md', 'w', encoding='utf-8') as f:
        f.write("# SÍMBOLOS ENCONTRADOS EN DOCUMENTACIÓN\n\n")

        # Ya aprobados
        if 'APROBADO' in categorized:
            f.write("## YA APROBADOS (conservar)\n\n")
            for symbol in categorized['APROBADO']:
                files = symbol_files[symbol]
                f.write(f"- {symbol} (U+{ord(symbol):04X}) - Encontrado en {len(files)} archivo(s)\n")
            f.write("\n")

        # Box drawing (probablemente OK - para diagramas)
        if 'BOX_DRAWING' in categorized:
            f.write("## BOX DRAWING (para diagramas de árbol)\n\n")
            for symbol in categorized['BOX_DRAWING']:
                files = symbol_files[symbol]
                f.write(f"- {symbol} (U+{ord(symbol):04X}) - Encontrado en {len(files)} archivo(s)\n")
            f.write("\n")

        # Formas geométricas (PREGUNTAR)
        if 'GEOMETRIC' in categorized:
            f.write("## FORMAS GEOMÉTRICAS (pendiente aprobación)\n\n")
            for symbol in categorized['GEOMETRIC']:
                files = symbol_files[symbol]
                f.write(f"- {symbol} (U+{ord(symbol):04X}) - Encontrado en {len(files)} archivo(s)\n")
                f.write(f"  - Archivos: {', '.join(files[:3])}\n")
            f.write("\n")

        # Flechas (PREGUNTAR)
        if 'ARROW' in categorized:
            f.write("## FLECHAS (pendiente aprobación)\n\n")
            for symbol in categorized['ARROW']:
                files = symbol_files[symbol]
                f.write(f"- {symbol} (U+{ord(symbol):04X}) - Encontrado en {len(files)} archivo(s)\n")
                f.write(f"  - Archivos: {', '.join(files[:3])}\n")
            f.write("\n")

        # Símbolos misc (PREGUNTAR)
        if 'MISC_SYMBOL' in categorized:
            f.write("## SÍMBOLOS MISCELÁNEOS (pendiente aprobación)\n\n")
            for symbol in categorized['MISC_SYMBOL']:
                files = symbol_files[symbol]
                f.write(f"- {symbol} (U+{ord(symbol):04X}) - Encontrado en {len(files)} archivo(s)\n")
                f.write(f"  - Archivos: {', '.join(files[:3])}\n")
            f.write("\n")

        # Emojis pictográficos (probablemente NO aceptables)
        if 'EMOJI_PICTOGRAPHIC' in categorized:
            f.write("## EMOJIS PICTOGRÁFICOS (probablemente NO aceptables)\n\n")
            for symbol in categorized['EMOJI_PICTOGRAPHIC']:
                files = symbol_files[symbol]
                f.write(f"- {symbol} (U+{ord(symbol):04X}) - Encontrado en {len(files)} archivo(s)\n")
                f.write(f"  - Archivos: {', '.join(files[:3])}\n")
            f.write("\n")

    print("Análisis completado.")
    print("Resultados guardados en: reports/SIMBOLOS_ENCONTRADOS.md")
    print()
    print(f"Total de símbolos únicos encontrados: {len(symbol_files)}")
    print()
    print("Categorías:")
    for category, symbols in sorted(categorized.items()):
        print(f"  {category}: {len(symbols)} símbolos")

if __name__ == '__main__':
    main()
