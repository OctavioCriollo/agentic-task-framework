#!/bin/bash
#
# Agentic Task Framework - Setup Script
# Configures virtual environment and dependencies
#

set -e

FRAMEWORK_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$FRAMEWORK_DIR/venv"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}  Agentic Task Framework${NC}"
echo -e "${BLUE}  Setup & Installation${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""

# Check if Python is available
echo -e "${BLUE}Verificando Python...${NC}"

if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version)
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python --version)
elif command -v py &> /dev/null; then
    PYTHON_CMD="py"
    PYTHON_VERSION=$(py --version)
else
    echo -e "${YELLOW}Error: Python no encontrado${NC}"
    echo "Por favor instala Python 3.8 o superior desde:"
    echo "  https://www.python.org/downloads/"
    exit 1
fi

echo -e "${GREEN}✓ $PYTHON_VERSION encontrado${NC}"
echo ""

# Check if venv already exists
if [ -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Entorno virtual ya existe en: $VENV_DIR${NC}"
    echo "¿Deseas recrearlo? (esto eliminará el actual)"
    read -p "Recrear venv? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}Eliminando venv existente...${NC}"
        rm -rf "$VENV_DIR"
    else
        echo -e "${GREEN}Usando venv existente${NC}"
        echo ""
        echo -e "${GREEN}Setup completo.${NC}"
        echo "Para activar el entorno virtual:"
        echo "  source venv/Scripts/activate  (Git Bash)"
        echo "  venv\\Scripts\\activate.bat    (CMD)"
        exit 0
    fi
fi

# Create virtual environment
echo -e "${BLUE}Creando entorno virtual...${NC}"
$PYTHON_CMD -m venv "$VENV_DIR"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Entorno virtual creado${NC}"
else
    echo -e "${YELLOW}Error al crear entorno virtual${NC}"
    exit 1
fi

# Activate virtual environment
echo -e "${BLUE}Activando entorno virtual...${NC}"

if [ -f "$VENV_DIR/Scripts/activate" ]; then
    source "$VENV_DIR/Scripts/activate"
elif [ -f "$VENV_DIR/bin/activate" ]; then
    source "$VENV_DIR/bin/activate"
else
    echo -e "${YELLOW}Error: No se pudo activar venv${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Entorno virtual activado${NC}"
echo ""

# Upgrade pip
echo -e "${BLUE}Actualizando pip...${NC}"
python -m pip install --upgrade pip --quiet

echo -e "${GREEN}✓ pip actualizado${NC}"
echo ""

# Install dependencies (currently none, but prepared for future)
if [ -f "$FRAMEWORK_DIR/requirements.txt" ]; then
    echo -e "${BLUE}Instalando dependencias...${NC}"
    pip install -r "$FRAMEWORK_DIR/requirements.txt" --quiet

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Dependencias instaladas${NC}"
    else
        echo -e "${YELLOW}Advertencia: Algunas dependencias pueden haber fallado${NC}"
    fi
else
    echo -e "${BLUE}No hay archivo requirements.txt${NC}"
    echo -e "${GREEN}✓ No se requieren dependencias externas${NC}"
fi

echo ""
echo -e "${GREEN}=================================${NC}"
echo -e "${GREEN}  Setup Completo${NC}"
echo -e "${GREEN}=================================${NC}"
echo ""
echo "Entorno virtual creado en: $VENV_DIR"
echo ""
echo -e "${BLUE}Próximos pasos:${NC}"
echo ""
echo "1. Para usar el framework, simplemente ejecuta:"
echo "   ${GREEN}./start_coordinator.sh${NC}"
echo "   (El script activará el venv automáticamente)"
echo ""
echo "2. Para activar manualmente el venv:"
echo "   ${GREEN}source venv/Scripts/activate${NC}  (Git Bash/Linux)"
echo "   ${GREEN}venv\\Scripts\\activate.bat${NC}    (Windows CMD)"
echo ""
echo "3. Para desactivar el venv:"
echo "   ${GREEN}deactivate${NC}"
echo ""
