#!/bin/bash
# Guardar como core/fix_a2_rename_screaming_snake_case.sh

PROJECT_ID="investigaci-n-clo-covid-19-20251222-195407"
PROJECT_DIR="projects/$PROJECT_ID/tasks"

echo "Renombrando archivos SCREAMING_SNAKE_CASE..."

# Tarea 1: selectividad-molecular-celular-clo2
TASK1="$PROJECT_DIR/selectividad-molecular-celular-clo2/reports"

if [ -d "$TASK1" ]; then
    echo "Procesando selectividad-molecular-celular-clo2..."

    cd "$TASK1"

    # Renombrar archivos
    [ -f "DIAGRAMAS_Y_MODELOS.md" ] && mv "DIAGRAMAS_Y_MODELOS.md" "diagramas_y_modelos.md" && echo "  Renombrado: DIAGRAMAS_Y_MODELOS.md -> diagramas_y_modelos.md"
    [ -f "INDICE_GENERAL.md" ] && mv "INDICE_GENERAL.md" "indice_general.md" && echo "  Renombrado: INDICE_GENERAL.md -> indice_general.md"

    cd - > /dev/null
fi

# Tarea 2: ventana-terapeutica-toxicologia-clo2
TASK2="$PROJECT_DIR/ventana-terapeutica-toxicologia-clo2/reports"

if [ -d "$TASK2" ]; then
    echo "Procesando ventana-terapeutica-toxicologia-clo2..."

    cd "$TASK2"

    [ -f "RESUMEN_EJECUTIVO.md" ] && mv "RESUMEN_EJECUTIVO.md" "resumen_ejecutivo.md" && echo "  Renombrado: RESUMEN_EJECUTIVO.md -> resumen_ejecutivo.md"

    cd - > /dev/null
fi

echo ""
echo "Actualizando task_info.json..."

# Actualizar task_info.json con script Python
python - << 'EOF'
import json
from pathlib import Path

project_dir = Path("projects/investigaci-n-clo-covid-19-20251222-195407/tasks")

# Tarea 1
task1_info = project_dir / "selectividad-molecular-celular-clo2/task_info.json"
if task1_info.exists():
    with open(task1_info, 'r', encoding='utf-8') as f:
        info = json.load(f)

    # Actualizar nombres
    if "reports" in info:
        info["reports"] = [
            r.replace("DIAGRAMAS_Y_MODELOS.md", "diagramas_y_modelos.md")
             .replace("INDICE_GENERAL.md", "indice_general.md")
            for r in info["reports"]
        ]

    with open(task1_info, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    print("  Actualizado: selectividad-molecular-celular-clo2/task_info.json")

# Tarea 2
task2_info = project_dir / "ventana-terapeutica-toxicologia-clo2/task_info.json"
if task2_info.exists():
    with open(task2_info, 'r', encoding='utf-8') as f:
        info = json.load(f)

    if "reports" in info:
        info["reports"] = [
            r.replace("RESUMEN_EJECUTIVO.md", "resumen_ejecutivo.md")
            for r in info["reports"]
        ]

    with open(task2_info, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    print("  Actualizado: ventana-terapeutica-toxicologia-clo2/task_info.json")

print("\nActualizacion de metadata completada")
EOF

echo ""
echo "CORRECCION A2 COMPLETADA"
echo ""
echo "Archivos renombrados:"
echo "  diagramas_y_modelos.md (antes DIAGRAMAS_Y_MODELOS.md)"
echo "  indice_general.md (antes INDICE_GENERAL.md)"
echo "  resumen_ejecutivo.md (antes RESUMEN_EJECUTIVO.md)"
