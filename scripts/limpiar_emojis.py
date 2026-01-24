#!/usr/bin/env python3
"""
Script para limpiar emojis no permitidos de documentos markdown.

PERMITIDOS:
- Checkmarks: ✓ ✅
- X marks: ✗ ❌
- Status: 🟡

NO PERMITIDOS:
- Todos los demás emojis decorativos
"""

import re
from pathlib import Path
import sys

# Mapeo de emojis no permitidos a texto plano
EMOJI_REPLACEMENTS = {
    '📦': '',
    '🔧': '',
    '📚': '',
    '📊': '',
    '🗂️': '',
    '⚠️': 'WARNING:',
    '🎯': '',
    '✨': '',
    '🚀': '',
    '💡': '',
    '📁': '',
    '📋': '',
    '📝': '',
    '⏳': 'PENDING:',
    '👉': '',
    '➡️': '->',
    '⬅️': '<-',
    '↓': '->',
    '↑': '<-',
    '🔄': '',
    '🚨': 'CRITICAL:',
    '🤔': 'QUESTION:',
    '🔍': 'SEARCH:',
    '🔒': 'SECURE:',
    '🏗️': 'BUILD:',
    '💻': 'CODE:',
    '📈': 'ANALYSIS:',
    # Pictográficos específicos NO permitidos (infantiles)
    '🎉': '',
    '🎓': '',
    '📄': '',
    '📅': '',
    '🗑': '',
    '❗': 'IMPORTANTE:',
    # Box drawing decorativo doble (innecesario)
    '╔': '',
    '╗': '',
    '╚': '',
    '╝': '',
    '║': '|',
    '╠': '|',
    '╣': '|',
    '╦': '-',
    '╩': '-',
    '╬': '+',
    '═': '-',
}

# Emojis permitidos (NO reemplazar)
ALLOWED_EMOJIS = [
    # Checkmarks y X marks
    '✓',   # Checkmark plain
    '✅',  # Checkmark green
    '✗',   # X mark plain
    '❌',  # X mark red
    # Círculos de estado
    '🟡',  # Yellow circle (status: in progress)
    '🟢',  # Green circle (status: active/success)
    '🔴',  # Red circle (status: error/blocked)
    '🟠',  # Orange circle (status: warning/attention)
    # Radio buttons
    '⚪',  # White circle (radio button)
    '⚫',  # Black circle (radio button)
    '🔘',  # Radio button
    # Formas geométricas simples
    '●',   # Black circle filled
    # Flechas direccionales
    '←',   # Left arrow
    '→',   # Right arrow
    '↑',   # Up arrow
    '↓',   # Down arrow
    '↔',   # Horizontal bidirectional arrow
    '↕',   # Vertical bidirectional arrow
    # Símbolos misceláneos aceptables
    '☆',   # Star outline
    '★',   # Star filled (para ratings)
    '⚠',   # Warning triangle
    '⚡',   # Lightning
    '❓',   # Question mark
    # Box drawing (para diagramas de árbol)
    '─', '│', '┌', '┐', '└', '┘', '├', '┤', '╱', '╲',
]

def clean_emojis(content: str) -> tuple[str, int]:
    """
    Limpia emojis no permitidos del contenido.

    Returns:
        (contenido_limpio, numero_de_cambios)
    """
    original = content
    changes = 0

    for emoji, replacement in EMOJI_REPLACEMENTS.items():
        if emoji in content:
            # Contar ocurrencias
            count = content.count(emoji)
            changes += count

            # Reemplazar
            if replacement:
                # Si hay texto de reemplazo, agregar espacio si es necesario
                content = content.replace(emoji, f' {replacement} ')
            else:
                # Si no hay reemplazo, solo quitar el emoji
                content = content.replace(emoji, '')

    # Limpiar espacios múltiples
    content = re.sub(r' {2,}', ' ', content)

    # Limpiar líneas con solo espacios
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped or not line:  # Mantener líneas vacías originales
            cleaned_lines.append(line.rstrip())
        else:
            cleaned_lines.append('')

    content = '\n'.join(cleaned_lines)

    return content, changes

def process_file(filepath: Path) -> tuple[bool, int]:
    """
    Procesa un archivo markdown.

    Returns:
        (fue_modificado, numero_de_cambios)
    """
    try:
        # Leer archivo
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Limpiar emojis
        cleaned_content, changes = clean_emojis(original_content)

        # Si hubo cambios, escribir
        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True, changes

        return False, 0

    except Exception as e:
        print(f"ERROR procesando {filepath}: {e}")
        return False, 0

def main():
    """Procesa todos los archivos markdown en TODO el proyecto"""

    base_dir = Path(__file__).parent.parent

    # Directorios a excluir
    exclude_dirs = {'.git', '.venv', '.venv.backup_20260117_120935', '.pytest_cache',
                   '__pycache__', 'node_modules', '.memory_backups'}

    # Buscar todos los archivos .md recursivamente
    all_md_files = []
    for path in base_dir.rglob('*.md'):
        # Saltar directorios excluidos
        if any(excluded in path.parts for excluded in exclude_dirs):
            continue
        all_md_files.append(path)

    total_files = 0
    total_modified = 0
    total_changes = 0

    print("Limpiando emojis no permitidos de TODO el proyecto...")
    print()

    # Agrupar por directorio padre para mejor visualización
    from collections import defaultdict
    by_dir = defaultdict(list)
    for f in all_md_files:
        parent = f.parent.relative_to(base_dir) if f.parent != base_dir else Path('.')
        by_dir[parent].append(f)

    for directory in sorted(by_dir.keys()):
        print(f"Procesando: {directory}/")
        print("-" * 60)

        for filepath in sorted(by_dir[directory]):
            total_files += 1
            modified, changes = process_file(filepath)

            if modified:
                total_modified += 1
                total_changes += changes
                status = f"LIMPIADO ({changes} cambios)"
            else:
                status = "OK (sin cambios)"

            print(f"  {filepath.name:<50} {status}")

        print()

    # Resumen
    print("=" * 60)
    print(f"Archivos procesados: {total_files}")
    print(f"Archivos modificados: {total_modified}")
    print(f"Total de emojis removidos: {total_changes}")
    print()
    print("COMPLETADO: Todos los documentos han sido limpiados")
    print()
    print("Emojis PERMITIDOS (conservados): checkmarks, X marks, status indicators")

if __name__ == '__main__':
    main()
