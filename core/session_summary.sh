#!/bin/bash
#
# Session Summary Generator
# Updates CLAUDE.md with session history before backup
#

TARGET_DIR="$1"
SESSION_TYPE="${2:-coordinator}"  # coordinator or task

if [ -z "$TARGET_DIR" ]; then
    echo "Error: TARGET_DIR requerido"
    exit 1
fi

CLAUDE_MD="$TARGET_DIR/CLAUDE.md"
TASK_REGISTRY="$TARGET_DIR/.task_registry.json"

if [ ! -f "$CLAUDE_MD" ]; then
    echo "Advertencia: CLAUDE.md no encontrado"
    exit 0
fi

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Generate session metadata
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
TIMESTAMP_SHORT=$(date +"%Y-%m-%d")
SESSION_DURATION="N/A"

# Count tasks created (if coordinator)
TASKS_COUNT=0
if [ -f "$TASK_REGISTRY" ]; then
    TASKS_COUNT=$(python -c "import json; print(len(json.load(open('$TASK_REGISTRY'))['tasks']))" 2>/dev/null || echo "0")
fi

# Create session summary
SESSION_SUMMARY="
---

## Historial de Sesión

### Última Sesión: $TIMESTAMP_SHORT

**Fecha y hora de cierre:** $TIMESTAMP
**Tipo de sesión:** $SESSION_TYPE
**Tareas activas:** $TASKS_COUNT

**Metadata:**
- Framework version: 1.0.0
- Sesión cerrada correctamente
- Backup automático creado

---

Última actualización: $TIMESTAMP
"

# Update CLAUDE.md with session history
# Replace the placeholder sections
if grep -q "## Historial de Sesión" "$CLAUDE_MD"; then
    # Remove old history section and add new one
    sed -i '/## Historial de Sesión/,/---/d' "$CLAUDE_MD"
fi

# Remove old "Última actualización" line if exists
sed -i '/^Última actualización:/d' "$CLAUDE_MD"

# Append new session summary
echo "$SESSION_SUMMARY" >> "$CLAUDE_MD"

echo -e "${GREEN}✓ Historial de sesión actualizado${NC}"

exit 0
