#!/bin/bash
# safe_pip_install.sh - Wrapper seguro para pip install
# Previene instalaciones accidentales en Python global
# Parte de la Auditoría de Virtual Environment - 2026-01-16

set -e

# Verificar que venv está activo
if [ -z "$VIRTUAL_ENV" ]; then
    echo "❌ ERROR: Virtual environment not activated"
    echo ""
    echo "This project uses a virtual environment to isolate dependencies."
    echo "Please activate it first:"
    echo ""
    echo "    source .venv/Scripts/activate"
    echo ""
    echo "Or run:"
    echo "    ./start_coordinator.sh  # Auto-activates venv"
    echo ""
    echo "Why this matters:"
    echo "  - Prevents contamination of global Python"
    echo "  - Ensures reproducible environment"
    echo "  - Avoids version conflicts between projects"
    echo ""
    exit 1
fi

# Verificar que estamos en el venv correcto del proyecto
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_VENV="$PROJECT_DIR/.venv"

# Normalizar paths para comparación
CURRENT_VENV_NORMALIZED=$(echo "$VIRTUAL_ENV" | sed 's/\\/\//g')
PROJECT_VENV_NORMALIZED=$(echo "$PROJECT_VENV" | sed 's/\\/\//g')

if [[ "$CURRENT_VENV_NORMALIZED" != "$PROJECT_VENV_NORMALIZED" ]]; then
    echo "⚠️  WARNING: You're in a different virtual environment"
    echo ""
    echo "Current venv:  $VIRTUAL_ENV"
    echo "Project venv:  $PROJECT_VENV"
    echo ""
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
fi

# Si llegamos aquí, todo está OK
echo "✓ Virtual environment active: $VIRTUAL_ENV"
echo ""
echo "Installing packages: $@"
echo "-------------------------------------------"

# Instalar paquetes
pip install "$@"

# Sugerir actualizar requirements.txt
echo ""
echo "-------------------------------------------"
echo "✓ Installation complete"
echo ""
echo "📝 Don't forget to update requirements.txt:"
echo ""
echo "    # Option 1: Freeze all packages"
echo "    pip freeze > requirements.txt"
echo ""
echo "    # Option 2: Add only what you installed"
echo "    echo \"$@\" >> requirements.txt"
echo ""
echo "    # Option 3: Edit requirements.txt manually"
echo "    # (Recommended - keeps file clean)"
echo ""
