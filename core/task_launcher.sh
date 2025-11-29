#!/bin/bash
#
# Agentic Task Framework - Task Launcher with Memory
# Launches specialized agent with automatic memory management
#

# Remove set -e to handle errors gracefully
# set -e

TASK_DIR="$1"

if [ -z "$TASK_DIR" ]; then
    echo "Error: Directorio de tarea requerido"
    exit 1
fi

if [ ! -d "$TASK_DIR" ]; then
    echo "Error: Directorio no existe: $TASK_DIR"
    exit 1
fi

TASK_NAME=$(basename "$TASK_DIR")
CLAUDE_MD="$TASK_DIR/CLAUDE.md"
MEMORY_BACKUP_DIR="$TASK_DIR/.memory_backups"
FRAMEWORK_DIR="$(cd "$TASK_DIR/../.." && pwd)"
CORE_DIR="$FRAMEWORK_DIR/core"
VENV_DIR="$FRAMEWORK_DIR/venv"

# Activate virtual environment if it exists
if [ -d "$VENV_DIR" ]; then
    if [ -f "$VENV_DIR/Scripts/activate" ]; then
        source "$VENV_DIR/Scripts/activate"
    elif [ -f "$VENV_DIR/bin/activate" ]; then
        source "$VENV_DIR/bin/activate"
    fi
fi

# Extract clean task name (remove UUID)
CLEAN_TASK_NAME=$(echo "$TASK_NAME" | sed 's/-[a-f0-9]\{8\}$//' | tr '-' ' ' | sed 's/\b\(.\)/\u\1/g')
TERMINAL_TITLE="$CLEAN_TASK_NAME - Agente Especializado"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

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

# Store Claude Code PID for cleanup
CLAUDE_PID=""

# Function to update task memory on exit
update_task_memory() {
    echo ""
    echo -e "${YELLOW}Guardando memoria...${NC}"

    # Update session history in CLAUDE.md
    if [ -f "$CORE_DIR/session_summary.sh" ]; then
        bash "$CORE_DIR/session_summary.sh" "$TASK_DIR" "task" 2>/dev/null
    fi

    # Create final backup
    if [ -f "$CLAUDE_MD" ]; then
        TIMESTAMP=$(date +%Y%m%d_%H%M%S)
        cp "$CLAUDE_MD" "$MEMORY_BACKUP_DIR/CLAUDE_exit_$TIMESTAMP.md" 2>/dev/null
        echo -e "${GREEN}✓ Memoria respaldada${NC}"
    fi

    echo -e "${GREEN}✓ Tarea cerrada${NC}"
}

# Register exit handler for multiple signals
# EXIT: normal exit
# SIGINT: Ctrl+C (capture and handle gracefully)
# SIGTERM: kill command
# SIGHUP: terminal closed/disconnected (X button)
trap update_task_memory EXIT SIGINT SIGTERM SIGHUP

# Ensure backup directory exists
mkdir -p "$MEMORY_BACKUP_DIR"

# Verify CLAUDE.md exists (should be created by task_manager)
if [ ! -f "$CLAUDE_MD" ]; then
    echo -e "${RED}Error: CLAUDE.md no encontrado${NC}"
    echo "Las instrucciones de la tarea deberían haber sido creadas por el coordinador."
    echo "Creando memoria básica de emergencia..."

    cat > "$CLAUDE_MD" << EOF
# Tarea: $TASK_NAME

Esta es una tarea especializada creada por el Coordinador Principal.

## Instrucciones

Las instrucciones específicas deberían estar aquí.
Si ves este mensaje, hubo un problema en la creación de la tarea.

Por favor, consulta con el coordinador principal.

## Progreso

[Se actualizará automáticamente al cerrar]
EOF
fi

# Create backup of initial memory
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
cp "$CLAUDE_MD" "$MEMORY_BACKUP_DIR/CLAUDE_start_$TIMESTAMP.md"

echo -e "${BLUE}════════════════════════════════════════${NC}"
echo -e "${BLUE}  Agente Especializado${NC}"
echo -e "${BLUE}════════════════════════════════════════${NC}"
echo -e "${YELLOW}  Tarea: ${NC}${CLEAN_TASK_NAME}"
echo -e "${BLUE}════════════════════════════════════════${NC}"
echo ""

# Display task info
MEMORY_SIZE=$(du -sh "$CLAUDE_MD" 2>/dev/null | cut -f1 || echo "N/A")
BACKUP_COUNT=$(ls -1 "$MEMORY_BACKUP_DIR"/CLAUDE_*.md 2>/dev/null | wc -l || echo "0")
echo -e "${BLUE}  Sistema de Memoria${NC}"
echo -e "${BLUE}────────────────────────────────────────${NC}"
echo -e "${GREEN}✓${NC} Memoria de tarea: ${GREEN}$MEMORY_SIZE${NC}"
echo -e "${GREEN}✓${NC} Backups disponibles: ${GREEN}$BACKUP_COUNT${NC}"
echo -e "${GREEN}✓${NC} Auto-guardado: ${GREEN}Activo${NC}"
echo ""

echo -e "${BLUE}  Directorio de Trabajo${NC}"
echo -e "${BLUE}────────────────────────────────────────${NC}"
echo -e "${GREEN}✓${NC} Tarea: ${BLUE}$TASK_NAME${NC}"
echo ""

echo -e "${GREEN}🚀 Iniciando agente especializado...${NC}"
echo -e "${BLUE}Tip: Al cerrar, tu progreso se guardará automáticamente${NC}"
echo ""

# Set terminal title
echo -ne "\033]0;${TERMINAL_TITLE}\007"

# Launch Claude Code for this task
cd "$TASK_DIR"

# Check if claude command exists
if ! command -v claude &> /dev/null; then
    error_exit "Claude Code CLI no encontrado.\nPor favor instala Claude Code."
fi

# Change to task directory
cd "$TASK_DIR" || error_exit "No se pudo cambiar al directorio de la tarea"

# Launch Claude Code - when it exits, trap executes backup
exec claude code
