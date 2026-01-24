#!/bin/bash
# Guardar como core/fix_c6_remove_task_manager.sh

echo "Removiendo task_manager.py deprecated..."

# Verificar que no hay imports
echo "Verificando imports de task_manager..."
grep_result=$(grep -r "import task_manager\|from task_manager" core/ --include="*.py" | grep -v "task_manager.py" || true)

if [ -n "$grep_result" ]; then
    echo "ERROR: Se encontraron imports de task_manager:"
    echo "$grep_result"
    exit 1
fi

echo "OK: No hay imports de task_manager en otros modulos"

# Crear directorio legacy
mkdir -p legacy

# Mover task_manager.py
mv core/task_manager.py legacy/

echo "COMPLETADO: task_manager.py movido a legacy/"

# Agregar README en legacy/
cat > legacy/README.md << 'EOF'
# Legacy Code

Este directorio contiene codigo deprecated del framework.

## task_manager.py

**Estado:** DEPRECATED desde Framework v2.0

**Razon de deprecacion:**
Sistema de multiples ventanas reemplazado por arquitectura Task tool en background

**Reemplazo:**
- Usar ProjectManager (core/project_manager.py)
- Usar Task tool de Claude Code

**Fecha de deprecacion:** 2025-12-21

**Preservado para:**
- Referencia historica
- Compatibilidad con proyectos antiguos (pre-v2.0)

**NO USAR en proyectos nuevos**

---

Para sistema actual ver:
- ../README.md
- ../CLAUDE.md
- ../core/project_manager.py
EOF

echo "COMPLETADO: README creado en legacy/"

# Agregar nota en CHANGELOG
changelog_note='
### Remocion de Codigo Deprecated

**task_manager.py removido de core/**

- Movido a: legacy/task_manager.py
- Estado: DEPRECATED desde v2.0
- Reemplazo: ProjectManager + Task tool
- Razon: Sistema de multiples ventanas obsoleto
- Fecha de remocion: 2025-12-31

Si necesitas task_manager.py para proyectos antiguos (pre-v2.0), ver legacy/
'

# Agregar a README.md en seccion Changelog
echo "$changelog_note" >> CHANGELOG_REMOVAL.md

echo "COMPLETADO: Nota agregada a CHANGELOG_REMOVAL.md"

# Listar contenido de legacy/
echo ""
echo "Contenido de legacy/:"
ls -la legacy/

echo ""
echo "CORRECCION C6 COMPLETADA"
