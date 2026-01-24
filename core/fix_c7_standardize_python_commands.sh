#!/bin/bash
# Guardar como core/fix_c7_standardize_python_commands.sh

echo "Estandarizando comandos Python..."

# Forma canonica: python
CANONICAL="python"

echo "Forma canonica seleccionada: $CANONICAL"

# Backup todos los .md
for file in *.md docs/**/*.md; do
    if [ -f "$file" ]; then
        cp "$file" "$file.backup_c7"
    fi
done

echo "Backups creados (.backup_c7)"

# Reemplazar python3 -> python (solo en codigo, no en texto)
find . -name "*.md" -type f -exec sed -i 's/`python3 /`python /g' {} \;
find . -name "*.md" -type f -exec sed -i 's/ python3 / python /g' {} \;

# Reemplazar py -3 -> python
find . -name "*.md" -type f -exec sed -i 's/`py -3 /`python /g' {} \;
find . -name "*.md" -type f -exec sed -i 's/ py -3 / python /g' {} \;

echo "Reemplazos completados"

# Actualizar shebangs en scripts Python
find core -name "*.py" -type f -exec sed -i '1s|#!/usr/bin/env python3|#!/usr/bin/env python|' {} \; 2>/dev/null || true

echo "Shebangs actualizados en scripts Python"

# Generar reporte de cambios
echo ""
echo "Reporte de Cambios:"
echo "==================="

count=0
for file in *.md docs/**/*.md; do
    if [ -f "$file" ] && [ -f "$file.backup_c7" ]; then
        if ! diff -q "$file.backup_c7" "$file" >/dev/null 2>&1; then
            changes=$(diff "$file.backup_c7" "$file" | grep -c "python" || echo "0")
            if [ "$changes" -gt 0 ]; then
                echo "$file: modificado"
                count=$((count + 1))
            fi
        fi
    fi
done

echo "Total archivos modificados: $count"

echo ""
echo "CORRECCION C7 COMPLETADA"
echo ""
echo "Para revertir si es necesario:"
echo "  find . -name '*.md.backup_c7' -exec bash -c 'mv \"\$1\" \"\${1%.backup_c7}\"' _ {} \;"
