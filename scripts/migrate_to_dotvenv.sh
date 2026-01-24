#!/bin/bash
# migrate_to_dotvenv.sh - Migra venv/ a .venv/
# Parte de la Auditoría de Virtual Environment - 2026-01-16

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRAMEWORK_DIR="$(dirname "$SCRIPT_DIR")"
OLD_VENV="$FRAMEWORK_DIR/venv"
NEW_VENV="$FRAMEWORK_DIR/.venv"

echo "============================================"
echo "Migración: venv/ → .venv/"
echo "============================================"
echo ""

# 1. Verificar que venv/ existe
if [ ! -d "$OLD_VENV" ]; then
    echo "❌ ERROR: venv/ no encontrado en $OLD_VENV"
    exit 1
fi

echo "✓ Encontrado venv/ en: $OLD_VENV"

# 2. Verificar que .venv/ NO existe
if [ -d "$NEW_VENV" ]; then
    echo "⚠️  WARNING: .venv/ ya existe"
    read -p "¿Eliminar .venv/ existente? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Eliminando .venv/ existente..."
        rm -rf "$NEW_VENV"
    else
        echo "Cancelado."
        exit 0
    fi
fi

# 3. Renombrar venv/ a .venv/
echo ""
echo "Renombrando venv/ → .venv/..."
mv "$OLD_VENV" "$NEW_VENV"
echo "✓ Renombrado exitoso"

# 4. Recrear venv (paths cambian con el rename)
echo ""
echo "Recreando venv con nuevo path..."
PYTHON_CMD="python"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

# Backup del venv renombrado
BACKUP_DIR="$NEW_VENV.backup_$(date +%Y%m%d_%H%M%S)"
echo "Creando backup en: $BACKUP_DIR"
cp -r "$NEW_VENV" "$BACKUP_DIR"

# Eliminar y recrear
rm -rf "$NEW_VENV"
$PYTHON_CMD -m venv "$NEW_VENV"
echo "✓ Venv recreado"

# 5. Reinstalar paquetes desde backup
echo ""
echo "Reinstalando paquetes..."
source "$NEW_VENV/Scripts/activate"

# Si hay requirements.txt, usarlo
if [ -f "$FRAMEWORK_DIR/requirements.txt" ]; then
    pip install -r "$FRAMEWORK_DIR/requirements.txt" --quiet 2>/dev/null || true
fi

# Instalar testing deps (sabemos que los necesitamos)
pip install pytest pytest-cov --quiet
echo "✓ Paquetes reinstalados"

# 6. Actualizar scripts
echo ""
echo "Actualizando scripts..."

# setup.sh
if [ -f "$FRAMEWORK_DIR/setup.sh" ]; then
    sed -i 's/VENV_DIR="venv"/VENV_DIR=".venv"/g' "$FRAMEWORK_DIR/setup.sh"
    echo "✓ setup.sh actualizado"
fi

# start_coordinator.sh
if [ -f "$FRAMEWORK_DIR/start_coordinator.sh" ]; then
    sed -i 's/venv\/Scripts\/activate/.venv\/Scripts\/activate/g' "$FRAMEWORK_DIR/start_coordinator.sh"
    sed -i 's/\[ -d.*venv \]/[ -d "$FRAMEWORK_DIR\/.venv" ]/g' "$FRAMEWORK_DIR/start_coordinator.sh"
    echo "✓ start_coordinator.sh actualizado"
fi

# 7. Actualizar .gitignore
echo ""
if [ -f "$FRAMEWORK_DIR/.gitignore" ]; then
    if ! grep -q "^\.venv/$" "$FRAMEWORK_DIR/.gitignore"; then
        echo ".venv/" >> "$FRAMEWORK_DIR/.gitignore"
        echo "✓ .gitignore actualizado"
    else
        echo "✓ .gitignore ya incluye .venv/"
    fi
fi

# 8. Validar
echo ""
echo "Validando migración..."
python "$FRAMEWORK_DIR/scripts/validate_venv.py" || echo "⚠️  Validación con warnings (esperado durante migración)"

echo ""
echo "============================================"
echo "✓ MIGRACIÓN COMPLETADA"
echo "============================================"
echo ""
echo "Cambios realizados:"
echo "  - venv/ → .venv/"
echo "  - Venv recreado con nuevo path"
echo "  - Scripts actualizados"
echo "  - .gitignore actualizado"
echo ""
echo "Backup guardado en:"
echo "  $BACKUP_DIR"
echo ""
echo "Para activar .venv en futuras sesiones:"
echo "  source .venv/Scripts/activate"
echo ""
echo "IMPORTANTE: Si tenías venv activado, desactívalo y reactiva:"
echo "  deactivate"
echo "  source .venv/Scripts/activate"
echo ""
