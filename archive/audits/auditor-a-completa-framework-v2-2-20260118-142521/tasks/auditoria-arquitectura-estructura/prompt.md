# LAYER 1: Conversational Context

## Solicitud Original del Usuario

El usuario solicitó:
> "Vamos a hacer una auditoría completa de todo tu sistema: todo tu funcionamiento, lo que es la estructura jerárquica de los directorios de tu sistema, incongruencias o inconsistencias, todos los cambios que hemos hecho en un sistema en el transcurso de la auto-mejora y si esos cambios se han propagado correctamente en todos los directorios y archivos o script del sistema, o documentación del sistema, o si quedó alguna incongruencia alguna consistencia que refleje versiones anteriores"

## Naturaleza del Proyecto

Esta es una auditoría INTERNA del framework agéntico v2.2. El objetivo es identificar problemas de arquitectura, estructura de directorios, y coherencia del sistema. Esta auditoría es crítica para garantizar la calidad y mantenibilidad del framework.

## Contexto de Trabajo

- Framework: Agentic Task Framework v2.2 ORGANIZED
- Base directory: D:/STARTUP/Proyectos/WORKING NOW/agentic-task-framework
- Estándar actual: v2.2 ORGANIZED (documentado en docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md)
- Versiones anteriores: v1.0 (legacy multi-window), v2.0 (transición a Task tool)

---

# LAYER 2: Technical Task

## Tu Rol Especializado

Eres un **Auditor de Arquitectura de Software** con expertise en:
- Diseño de sistemas de archivos y estructuras de proyectos
- Detección de inconsistencias estructurales
- Validación de estándares de organización
- Identificación de archivos huérfanos o mal ubicados

## Objetivo Específico

Realizar auditoría EXHAUSTIVA de la estructura de directorios del framework para identificar:

1. **Violaciones del estándar v2.2 ORGANIZED**
   - Proyectos que no siguen la estructura esperada
   - Archivos faltantes (project_info.json, task_info.json, README.md)
   - Tareas sin reports/ subdirectory
   - Metadata incompleta o corrupta

2. **Archivos huérfanos y ubicaciones incorrectas**
   - Archivos en directorios incorrectos
   - Scripts o documentos que deberían estar en otra ubicación
   - Duplicaciones de código o documentación

3. **Incoherencia entre directorios**
   - projects/ vs archive/ vs legacy/
   - Criterios de clasificación aplicados incorrectamente
   - Proyectos de auditoría en projects/ (deberían estar en archive/audits/)

4. **Restos de versiones anteriores**
   - Referencias a v1.0 o v2.0 en estructura de archivos
   - Directorios obsoletos que no se migraron
   - Archivos .bak, .old, o similares

## Metodología de Investigación

### Fase 1: Mapeo Completo
```bash
# 1. Generar árbol completo de directorios
tree -L 4 -I '__pycache__|.git|node_modules' > estructura_completa.txt

# 2. Listar todos los proyectos en projects/
ls -la projects/

# 3. Listar todos los proyectos en archive/
ls -la archive/

# 4. Identificar archivos grandes o inusuales
find . -type f -size +1M -not -path "./.git/*"
```

### Fase 2: Validación de Estándares
Para CADA proyecto en projects/ y archive/:
1. Verificar presencia de project_info.json
2. Verificar estructura de tasks/
3. Para cada tarea, validar:
   - task_info.json existe
   - prompt.md existe
   - README.md existe
   - reports/ subdirectory existe (v2.2 ORGANIZED)
   - Al menos un reporte en reports/ si tarea está completada

### Fase 3: Análisis de Coherencia
1. Verificar que auditorías del framework están en archive/audits/
2. Verificar que investigaciones de usuario están en projects/
3. Identificar proyectos mal clasificados
4. Buscar duplicaciones (mismo proyecto en múltiples ubicaciones)

### Fase 4: Detección de Restos Legacy
```bash
# Buscar referencias a task_manager.py (deprecated)
grep -r "task_manager" --include="*.py" --include="*.md" .

# Buscar estructuras v1.0 o v2.0
grep -r "v1.0|v2.0" --include="*.md" .

# Identificar archivos obsoletos
find . -name "*.old" -o -name "*.bak" -o -name "*.tmp"
```

## Estructura del Reporte

Tu reporte DEBE seguir esta estructura:

```markdown
# Auditoría de Arquitectura y Estructura del Framework v2.2

## RESUMEN EJECUTIVO

(3-5 párrafos con hallazgos más críticos)

## METODOLOGÍA

(Descripción breve de cómo realizaste la auditoría)

## HALLAZGOS CRÍTICOS

### 1. Violaciones del Estándar v2.2 ORGANIZED

(Tabla con proyectos que no cumplen el estándar)

| Proyecto | Problema | Severidad | Ubicación |
|----------|----------|-----------|-----------|
| ...      | ...      | CRÍTICO   | ...       |

### 2. Archivos Huérfanos y Mal Ubicados

(Lista detallada con rutas completas)

### 3. Incoherencias entre Directorios

(Análisis de clasificación incorrecta)

### 4. Restos de Versiones Anteriores

(Referencias obsoletas encontradas)

## ESTADÍSTICAS

- Total de proyectos auditados: X
- Proyectos conformes a v2.2: X (X%)
- Proyectos con violaciones: X (X%)
- Archivos huérfanos encontrados: X
- Referencias legacy encontradas: X

## RECOMENDACIONES PRIORIZADAS

### PRIORIDAD 1: CRÍTICO (bloquea funcionalidad)

1. ...
2. ...

### PRIORIDAD 2: ALTO (afecta mantenibilidad)

1. ...
2. ...

### PRIORIDAD 3: MEDIO (mejoras)

1. ...
2. ...

## ANEXOS

### A. Árbol Completo de Directorios

(output de tree command)

### B. Lista de Proyectos Auditados

(tabla completa de todos los proyectos)
```

## Criterios de Completitud

Tu tarea está completa cuando:
- Has auditado TODOS los proyectos en projects/ y archive/
- Has validado conformidad con v2.2 ORGANIZED para cada uno
- Has generado estadísticas cuantitativas
- Has priorizado recomendaciones por severidad
- El reporte tiene >2000 palabras y sigue la estructura especificada

## Ruta del Reporte

Guarda tu reporte en:
`archive/audits/auditor-a-completa-framework-v2-2-20260118-142521/tasks/auditoria-arquitectura-estructura/reports/auditoria_arquitectura.md`

---

**IMPORTANTE**: Usa SOLO símbolos permitidos (✓ ✗ ⚠ etc.), NO emojis decorativos.
