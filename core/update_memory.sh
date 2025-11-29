#!/bin/bash
#
# Update memory on session close
# Creates backup to preserve context
#

TARGET_DIR="$1"

if [ -z "$TARGET_DIR" ]; then
    echo "Error: TARGET_DIR requerido"
    exit 1
fi

CLAUDE_MD="$TARGET_DIR/CLAUDE.md"
MEMORY_BACKUP_DIR="$TARGET_DIR/.memory_backups"

if [ ! -f "$CLAUDE_MD" ]; then
    echo "Advertencia: CLAUDE.md no encontrado"
    exit 0
fi

# Ensure backup directory exists
mkdir -p "$MEMORY_BACKUP_DIR"

# Create timestamped backup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$MEMORY_BACKUP_DIR/CLAUDE_session_$TIMESTAMP.md"

cp "$CLAUDE_MD" "$BACKUP_FILE"

echo "✓ Memoria respaldada: $(basename $BACKUP_FILE)"

# Optional: Keep only last N backups to save space
# Uncomment to keep only last 50 backups
# cd "$MEMORY_BACKUP_DIR"
# ls -t CLAUDE_*.md | tail -n +51 | xargs -r rm --

exit 0
