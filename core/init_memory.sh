#!/bin/bash
#
# Initialize memory (CLAUDE.md) for coordinator or task
#

TARGET_DIR="$1"
MEMORY_TYPE="$2"  # "coordinator" or "task"

if [ -z "$TARGET_DIR" ] || [ -z "$MEMORY_TYPE" ]; then
    echo "Error: TARGET_DIR y MEMORY_TYPE requeridos"
    exit 1
fi

CLAUDE_MD="$TARGET_DIR/CLAUDE.md"

if [ "$MEMORY_TYPE" = "coordinator" ]; then
    echo "Creando memoria del coordinador..."

    # The actual CLAUDE.md content will be created separately
    # This script just ensures the structure is ready

    if [ ! -f "$CLAUDE_MD" ]; then
        echo "Error: CLAUDE.md debe existir en el directorio"
        echo "Por favor, asegúrate de que CLAUDE.md fue creado"
        exit 1
    fi

    echo "✓ Memoria del coordinador lista"

elif [ "$MEMORY_TYPE" = "task" ]; then
    echo "Verificando memoria de tarea..."

    # For tasks, CLAUDE.md is created by task_manager.py
    # with the dynamically designed prompt

    if [ ! -f "$CLAUDE_MD" ]; then
        echo "Advertencia: Memoria de tarea no encontrada"
        echo "Será creada por el task_manager"
    else
        echo "✓ Memoria de tarea verificada"
    fi
else
    echo "Error: MEMORY_TYPE debe ser 'coordinator' o 'task'"
    exit 1
fi
