#!/bin/bash
#
# Agentic Task Framework - Coordinator Launcher
# Initializes memory and launches coordinator with auto-save
#

# Remove set -e to handle errors gracefully
# set -e

FRAMEWORK_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_MD="$FRAMEWORK_DIR/CLAUDE.md"
MEMORY_BACKUP_DIR="$FRAMEWORK_DIR/.memory_backups"
CORE_DIR="$FRAMEWORK_DIR/core"
VENV_DIR="$FRAMEWORK_DIR/venv"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Error handler
error_exit() {
    echo ""
    echo -e "${RED}=================================${NC}"
    echo -e "${RED}  ERROR DETECTADO${NC}"
    echo -e "${RED}=================================${NC}"
    echo -e "${RED}$1${NC}"
    echo ""
    echo -e "${YELLOW}Presiona ENTER para cerrar...${NC}"
    read
    exit 1
}

echo -e "${BLUE}=================================${NC}"
echo -e "${BLUE}  Agentic Task Framework${NC}"
echo -e "${BLUE}  Coordinador Principal${NC}"
echo -e "${BLUE}=================================${NC}"
echo ""

# ============================================
# AUTO-SETUP: Virtual Environment
# ============================================

# Check if virtual environment exists, create if not
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Primera ejecución detectada${NC}"
    echo -e "${BLUE}Configurando entorno virtual...${NC}"
    echo ""

    # Detect Python command (try 'py' first on Windows, it's more reliable)
    PYTHON_CMD=""

    # Try 'py' first (Windows Python Launcher - most reliable on Windows)
    if command -v py &> /dev/null; then
        # Verify it's not a stub by checking if it can show version
        if py --version &> /dev/null; then
            PYTHON_CMD="py -3"
            PYTHON_VERSION=$(py --version 2>&1)
            echo -e "${GREEN}✓ $PYTHON_VERSION detectado (Python Launcher)${NC}"
        fi
    fi

    # If 'py' didn't work, try python3
    if [ -z "$PYTHON_CMD" ] && command -v python3 &> /dev/null; then
        if python3 --version &> /dev/null 2>&1; then
            PYTHON_CMD="python3"
            PYTHON_VERSION=$(python3 --version 2>&1)
            echo -e "${GREEN}✓ $PYTHON_VERSION detectado${NC}"
        fi
    fi

    # If python3 didn't work, try python
    if [ -z "$PYTHON_CMD" ] && command -v python &> /dev/null; then
        if python --version &> /dev/null 2>&1; then
            PYTHON_CMD="python"
            PYTHON_VERSION=$(python --version 2>&1)
            echo -e "${GREEN}✓ $PYTHON_VERSION detectado${NC}"
        fi
    fi

    # If nothing worked, show error
    if [ -z "$PYTHON_CMD" ]; then
        error_exit "Python no encontrado o no funciona correctamente.\n\nPosibles soluciones:\n1. Instala Python desde: https://www.python.org/downloads/\n2. Durante instalación, marca 'Add Python to PATH'\n3. Desactiva los alias de Microsoft Store:\n   Settings > Apps > App execution aliases\n   Desactiva 'python.exe' y 'python3.exe'"
    fi

    # Create virtual environment
    echo -e "${BLUE}Creando entorno virtual...${NC}"
    if ! $PYTHON_CMD -m venv "$VENV_DIR" 2>&1; then
        error_exit "No se pudo crear entorno virtual.\nVerifica que Python esté correctamente instalado."
    fi
    echo -e "${GREEN}✓ Entorno virtual creado${NC}"

    # Activate venv
    if [ -d "$VENV_DIR" ]; then
        if [ -f "$VENV_DIR/Scripts/activate" ]; then
            source "$VENV_DIR/Scripts/activate"
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}✓ Entorno virtual activado${NC}"
            else
                error_exit "No se pudo activar el entorno virtual"
            fi
        elif [ -f "$VENV_DIR/bin/activate" ]; then
            source "$VENV_DIR/bin/activate"
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}✓ Entorno virtual activado${NC}"
            else
                error_exit "No se pudo activar el entorno virtual"
            fi
        else
            error_exit "No se encontró el script de activación del venv"
        fi

        # Upgrade pip silently
        echo -e "${BLUE}Configurando pip...${NC}"
        python -m pip install --upgrade pip --quiet 2>/dev/null
        echo -e "${GREEN}✓ pip actualizado${NC}"

        # Install dependencies if requirements.txt exists
        if [ -f "$FRAMEWORK_DIR/requirements.txt" ]; then
            echo -e "${BLUE}Instalando dependencias...${NC}"
            pip install -r "$FRAMEWORK_DIR/requirements.txt" --quiet 2>/dev/null
            echo -e "${GREEN}✓ Dependencias instaladas${NC}"
        fi
    fi

    echo ""
    echo -e "${GREEN}✓ Configuración inicial completada${NC}"
    echo ""
else
    # Virtual environment exists, just activate it
    echo -e "${BLUE}Activando entorno virtual...${NC}"
    if [ -f "$VENV_DIR/Scripts/activate" ]; then
        source "$VENV_DIR/Scripts/activate"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Entorno virtual activado${NC}"
        else
            error_exit "No se pudo activar el entorno virtual"
        fi
    elif [ -f "$VENV_DIR/bin/activate" ]; then
        source "$VENV_DIR/bin/activate"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Entorno virtual activado${NC}"
        else
            error_exit "No se pudo activar el entorno virtual"
        fi
    else
        error_exit "No se encontró el script de activación del venv.\nEl directorio venv existe pero parece estar corrupto."
    fi
    echo ""
fi

# ============================================
# END AUTO-SETUP
# ============================================

# Ensure backup directory exists
mkdir -p "$MEMORY_BACKUP_DIR"

# Store Claude Code PID for cleanup
CLAUDE_PID=""

# Function to update memory on exit
update_memory_on_exit() {
    echo ""
    echo -e "${YELLOW}Guardando memoria...${NC}"

    # Update session history in CLAUDE.md
    if [ -f "$CORE_DIR/session_summary.sh" ]; then
        bash "$CORE_DIR/session_summary.sh" "$FRAMEWORK_DIR" "coordinator" 2>/dev/null
    fi

    # Create final backup
    if [ -f "$CLAUDE_MD" ]; then
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        cp "$CLAUDE_MD" "$MEMORY_BACKUP_DIR/CLAUDE_exit_$TIMESTAMP.md" 2>/dev/null
        echo -e "${GREEN}✓ Memoria respaldada${NC}"
    fi

    echo -e "${GREEN}✓ Sesión cerrada${NC}"
}

# Register exit handler for multiple signals
# EXIT: normal exit
# SIGINT: Ctrl+C (capture and handle gracefully)
# SIGTERM: kill command
# SIGHUP: terminal closed/disconnected (X button)
trap update_memory_on_exit EXIT SIGINT SIGTERM SIGHUP

# Check if CLAUDE.md exists
if [ ! -f "$CLAUDE_MD" ]; then
    echo -e "${YELLOW}Primera ejecución detectada${NC}"
    echo -e "${YELLOW}Inicializando memoria del coordinador...${NC}"
    echo ""

    # Initialize memory
    if [ -f "$CORE_DIR/init_memory.sh" ]; then
        bash "$CORE_DIR/init_memory.sh" "$FRAMEWORK_DIR" "coordinator"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Memoria del coordinador inicializada${NC}"
        else
            error_exit "No se pudo inicializar la memoria del coordinador"
        fi
    else
        error_exit "init_memory.sh no encontrado en:\n  $CORE_DIR/init_memory.sh"
    fi
    echo ""
else
    echo -e "${GREEN}✓ Memoria del coordinador encontrada${NC}"

    # Create backup of current memory
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    cp "$CLAUDE_MD" "$MEMORY_BACKUP_DIR/CLAUDE_start_$TIMESTAMP.md"
    echo -e "${GREEN}✓ Backup de seguridad creado${NC}"
    echo ""
fi

# Display memory status
echo -e "${BLUE}════════════════════════════════════════${NC}"
echo -e "${BLUE}  Sistema de Memoria${NC}"
echo -e "${BLUE}════════════════════════════════════════${NC}"
MEMORY_SIZE=$(du -sh "$CLAUDE_MD" 2>/dev/null | cut -f1 || echo "N/A")
BACKUP_COUNT=$(ls -1 "$MEMORY_BACKUP_DIR"/CLAUDE_*.md 2>/dev/null | wc -l || echo "0")
echo -e "${GREEN}✓${NC} Memoria principal: ${GREEN}$MEMORY_SIZE${NC}"
echo -e "${GREEN}✓${NC} Backups disponibles: ${GREEN}$BACKUP_COUNT${NC}"
echo -e "${GREEN}✓${NC} Ubicación: ${BLUE}CLAUDE.md${NC}"
echo ""

# Display tasks status
echo -e "${BLUE}════════════════════════════════════════${NC}"
echo -e "${BLUE}  Estado de Tareas${NC}"
echo -e "${BLUE}════════════════════════════════════════${NC}"
TASK_REGISTRY="$FRAMEWORK_DIR/.task_registry.json"
if [ -f "$TASK_REGISTRY" ]; then
    TASK_COUNT=$(python -c "import json; print(len(json.load(open('$TASK_REGISTRY'))['tasks']))" 2>/dev/null || echo "0")
    if [ "$TASK_COUNT" -gt 0 ]; then
        echo -e "${GREEN}✓${NC} Tareas activas: ${GREEN}$TASK_COUNT${NC}"
    else
        echo -e "${YELLOW}•${NC} No hay tareas activas"
    fi
else
    echo -e "${YELLOW}•${NC} No hay tareas registradas"
fi
echo ""

echo -e "${GREEN}🚀 Iniciando Coordinador...${NC}"
echo -e "${BLUE}Tip: Usa Ctrl+D o 'exit' para cerrar correctamente${NC}"
echo ""

# Set terminal title
FRAMEWORK_NAME=$(basename "$FRAMEWORK_DIR")
TERMINAL_TITLE="$FRAMEWORK_NAME - Coordinador Principal"

# Configure terminal title (works in mintty, bash, etc.)
echo -ne "\033]0;${TERMINAL_TITLE}\007"

# Launch Claude Code
# The trap will execute update_memory_on_exit when this terminates
cd "$FRAMEWORK_DIR"

# Check if claude command exists
if ! command -v claude &> /dev/null; then
    error_exit "Claude Code CLI no encontrado.\nPor favor instala Claude Code desde:\n  https://claude.ai/download"
fi

# Change to framework directory
cd "$FRAMEWORK_DIR" || error_exit "No se pudo cambiar al directorio del framework"

# Launch Claude Code - when it exits, trap executes backup
exec claude code
