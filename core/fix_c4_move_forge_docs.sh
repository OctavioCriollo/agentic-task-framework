#!/bin/bash
# Guardar como core/fix_c4_move_forge_docs.sh

echo "Moviendo documentos FORGE a proposals/..."

# Crear directorio
mkdir -p docs/proposals/forge

# Mover documentos FORGE
mv FORGE_ARCHITECTURE_v1.0.md docs/proposals/forge/
mv FORGE_INTERFACES_v1.0.md docs/proposals/forge/
mv FORGE_SPECIFICATION_SUMMARY.md docs/proposals/forge/

# Crear README de advertencia
cat > docs/proposals/forge/README.md << 'EOF'
# Propuesta: FORGE Framework v1.0

**Estado:** PROPUESTA NO IMPLEMENTADA

**Fecha de Especificacion:** 2025-12-26

**Version Actual del Framework:** v2.2 (ver ../../../README.md)

---

## Que es FORGE

FORGE (Framework for Orchestrated Research with Governed Execution) es una propuesta de rediseño completo del Agentic Task Framework basada en principios declarativos inspirados en A2WG (Agent-to-Workflow Graph).

## Estado de Implementacion

**NO IMPLEMENTADO**

Los documentos en este directorio son especificaciones tecnicas, NO codigo funcional.

- FORGE_ARCHITECTURE_v1.0.md: Arquitectura propuesta
- FORGE_INTERFACES_v1.0.md: Interfaces de API propuestas
- FORGE_SPECIFICATION_SUMMARY.md: Resumen y comparacion con v2.2

## Componentes Propuestos (NO EXISTEN)

- ForgeKernel, PolicyKernel, EvidenceLedger
- WorkGraph, ExecutionPlan, RecoveryService

## Schemas Propuestos (NO EXISTEN)

- schemas/workgraph_v1.0.schema.json
- schemas/policy_config_v1.0.schema.json
- schemas/execution_plan_v1.0.schema.json
- schemas/evidence_record_v1.0.schema.json

## Timeline

**Pendiente decision y aprobacion**

No hay fecha de implementacion confirmada.

## Para Usar el Framework HOY

Ver documentacion de v2.2:
- ../../../README.md
- ../../../CLAUDE.md
- ../../../ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md

---

**Advertencia:** Estos documentos son propuestas arquitectonicas para discusion. NO representan el estado actual del framework ni deben usarse como referencia de implementacion.
EOF

# Agregar advertencia al inicio de cada documento FORGE
for file in docs/proposals/forge/FORGE_*.md; do
    echo "Agregando advertencia a $(basename $file)..."

    warning='> **ADVERTENCIA:** Este es un documento de PROPUESTA. NO representa el estado actual del framework.
> Framework actual: v2.2 - Ver ../../../README.md
> Estado: ESPECIFICACION NO IMPLEMENTADA

---

'

    # Agregar al inicio
    echo "$warning" | cat - "$file" > "$file.tmp"
    mv "$file.tmp" "$file"
done

echo "COMPLETADO: Documentos FORGE movidos a docs/proposals/forge/"
echo "Archivos afectados:"
ls -la docs/proposals/forge/
