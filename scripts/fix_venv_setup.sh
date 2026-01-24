#!/bin/bash
# fix_venv_setup.sh - Corrige la configuración del virtual environment
# Migra pytest/pytest-cov de global Python a venv local

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRAMEWORK_DIR="$(dirname "$SCRIPT_DIR")"
VENV_DIR="$FRAMEWORK_DIR/.venv"

echo "============================================"
echo "Fix Virtual Environment Setup"
echo "============================================"
echo ""

# Función para detectar Python
detect_python() {
    if command -v python3 &> /dev/null; then
        echo "python3"
    elif command -v python &> /dev/null; then
        echo "python"
    elif command -v py &> /dev/null; then
        echo "py -3"
    else
        echo "ERROR: No Python installation found" >&2
        exit 1
    fi
}

PYTHON_CMD=$(detect_python)
echo "✓ Python command: $PYTHON_CMD"
echo ""

# 1. Verificar estado actual
echo "PASO 1: Verificando estado actual..."
echo "-------------------------------------------"

# Verificar si estamos en venv
if [ -n "$VIRTUAL_ENV" ]; then
    echo "⚠️  WARNING: Ya estás en un virtual environment"
    echo "   Desactivando primero..."
    deactivate 2>/dev/null || true
fi

# Verificar paquetes en global Python
echo ""
echo "Paquetes en Python global:"
$PYTHON_CMD -m pip list --format=columns 2>/dev/null | grep -E "pytest|pytest-cov" || echo "  (ninguno)"

# Verificar paquetes en venv (si existe)
if [ -d "$VENV_DIR" ]; then
    echo ""
    echo "Paquetes en venv actual:"
    "$VENV_DIR/Scripts/python.exe" -m pip list --format=columns 2>/dev/null | grep -E "pytest|pytest-cov" || echo "  (ninguno)"
fi

echo ""
read -p "¿Continuar con la corrección? (y/N) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Operación cancelada."
    exit 0
fi

# 2. Backup del venv actual
echo ""
echo "PASO 2: Backup del venv actual (si existe)..."
echo "-------------------------------------------"
if [ -d "$VENV_DIR" ]; then
    BACKUP_DIR="$VENV_DIR.backup_$(date +%Y%m%d_%H%M%S)"
    echo "Creando backup en: $BACKUP_DIR"
    mv "$VENV_DIR" "$BACKUP_DIR"
    echo "✓ Backup creado"
else
    echo "No hay venv existente, omitiendo backup"
fi

# 3. Crear venv limpio
echo ""
echo "PASO 3: Creando virtual environment limpio..."
echo "-------------------------------------------"
$PYTHON_CMD -m venv "$VENV_DIR"
echo "✓ Virtual environment creado"

# 4. Activar venv
echo ""
echo "PASO 4: Activando virtual environment..."
echo "-------------------------------------------"
source "$VENV_DIR/Scripts/activate"
echo "✓ Virtual environment activado"

# Verificar que estamos en venv
CURRENT_PYTHON=$(which python)
echo "  Python actual: $CURRENT_PYTHON"

# 5. Actualizar pip en venv
echo ""
echo "PASO 5: Actualizando pip en venv..."
echo "-------------------------------------------"
python -m pip install --upgrade pip --quiet
echo "✓ Pip actualizado a $(pip --version)"

# 6. Instalar dependencias de testing
echo ""
echo "PASO 6: Instalando dependencias de testing en venv..."
echo "-------------------------------------------"
echo "Instalando pytest y pytest-cov..."
pip install pytest pytest-cov --quiet
echo "✓ pytest $(pip show pytest | grep Version | cut -d ' ' -f 2) instalado"
echo "✓ pytest-cov $(pip show pytest-cov | grep Version | cut -d ' ' -f 2) instalado"

# 7. Instalar dependencias opcionales (si se descomenta requirements.txt)
echo ""
echo "PASO 7: Instalando requirements.txt (si hay)..."
echo "-------------------------------------------"
if [ -f "$FRAMEWORK_DIR/requirements.txt" ]; then
    pip install -r "$FRAMEWORK_DIR/requirements.txt" --quiet 2>/dev/null || echo "  (no hay paquetes en requirements.txt)"
    echo "✓ requirements.txt procesado"
else
    echo "  (no existe requirements.txt)"
fi

# 8. Verificación final
echo ""
echo "PASO 8: Verificación final..."
echo "-------------------------------------------"
echo ""
echo "Paquetes instalados en venv:"
pip list --format=columns

echo ""
echo "Verificando imports del framework..."
python -c "from core.project_manager import ProjectManager; print('✓ ProjectManager importado correctamente')"
python -c "from core.framework_validator import FrameworkValidator; print('✓ FrameworkValidator importado correctamente')"

echo ""
echo "Ejecutando tests..."
python -m pytest tests/ -v --tb=short -q

echo ""
echo "============================================"
echo "✓ CORRECCIÓN COMPLETADA"
echo "============================================"
echo ""
echo "Virtual environment configurado correctamente en:"
echo "  $VENV_DIR"
echo ""
echo "Para activarlo en futuras sesiones:"
echo "  source venv/Scripts/activate"
echo ""
echo "O simplemente ejecuta:"
echo "  ./start_coordinator.sh"
echo ""
echo "NOTA: Los paquetes pytest y pytest-cov siguen en Python global."
echo "      Para limpiarlos manualmente (OPCIONAL):"
echo "      pip uninstall pytest pytest-cov"
echo ""
