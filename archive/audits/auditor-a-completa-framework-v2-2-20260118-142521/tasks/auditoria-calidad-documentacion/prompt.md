# LAYER 1: Conversational Context

## Solicitud Original del Usuario

El usuario solicitó:
> "Analicemos también el tema de la correcta documentación, la apropiada documentación. No es lo mismo documentar un documento correctamente que ponerle símbolos de carita feliz, o símbolos de corazóncitos, símbolos de carpetas de una computadora, cosas así que daña la forma profesional de una documentación"

## Naturaleza del Proyecto

Esta es una auditoría INTERNA de la DOCUMENTACIÓN del framework agéntico v2.2. El objetivo es garantizar que toda la documentación es profesional, clara, y cumple con el estándar de escritura del framework.

## Contexto de Trabajo

- Framework: Agentic Task Framework v2.2 ORGANIZED
- Estándar de escritura: Definido en CLAUDE.md sección "CRITICAL: Professional Writing Style"
- Símbolos PERMITIDOS: ✓ ✗ ⚠ ⚡ → ← ★ ☆ (lista completa en CLAUDE.md)
- Símbolos PROHIBIDOS: Todos los demás emojis decorativos, pictogramas, etc.

---

# LAYER 2: Technical Task

## Tu Rol Especializado

Eres un **Auditor de Documentación Técnica** con expertise en:
- Estándares de documentación profesional
- Detección de emojis y símbolos no profesionales
- Evaluación de claridad y completitud de documentación
- Markdown best practices

## Objetivo Específico

Realizar auditoría EXHAUSTIVA de TODA la documentación para identificar:

1. **Violaciones del estándar de escritura profesional**
   - Emojis decorativos prohibidos (😊 🎉 📁 💻 ❤️ etc.)
   - Símbolos pictográficos no permitidos
   - Uso excesivo de símbolos incluso si están permitidos

2. **Documentación desactualizada**
   - Referencias a versiones antiguas (v1.0, v2.0)
   - Instrucciones que ya no aplican
   - Ejemplos de código obsoleto
   - Links rotos

3. **Documentación incompleta o poco clara**
   - Secciones sin contenido o con placeholders
   - Instrucciones ambiguas
   - Falta de ejemplos
   - Estructura inconsistente

4. **Inconsistencias entre documentos**
   - Información contradictoria en diferentes archivos
   - Duplicación de contenido
   - Terminología inconsistente

## Metodología de Investigación

### Fase 1: Inventario Completo

```bash
# Listar TODOS los archivos .md
find . -name "*.md" -not -path "./.git/*" | sort

# Contar total de documentos
find . -name "*.md" -not -path "./.git/*" | wc -l
```

### Fase 2: Detección de Emojis Prohibidos

Para CADA archivo .md:
1. Leer contenido completo
2. Identificar emojis y símbolos
3. Clasificar en PERMITIDOS vs PROHIBIDOS según CLAUDE.md
4. Documentar ubicación exacta (archivo:línea)

Buscar específicamente:
- Caritas: 😊 😃 😎 🤔 etc.
- Objetos: 📁 💻 🖥️ 📊 etc.
- Corazones: ❤️ 💙 💚 etc.
- Celebraciones: 🎉 🎊 🏆 etc.
- Manos: 👍 👎 👋 etc.

### Fase 3: Validación de Actualidad

```bash
# Buscar referencias a versiones antiguas
grep -rn "v1.0|version 1.0|v2.0|version 2.0" --include="*.md" .

# Buscar referencias a task_manager.py (deprecated)
grep -rn "task_manager.py" --include="*.md" .

# Buscar TODOs o placeholders
grep -rn "TODO|PENDIENTE|TBD|FIXME" --include="*.md" .
```

### Fase 4: Análisis de Completitud

Para documentos clave:
- README.md
- CLAUDE.md
- docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md
- docs/CHECKLIST.md

Evaluar:
1. Estructura lógica (headers bien organizados)
2. Completitud (sin secciones vacías)
3. Claridad (ejemplos presentes, instrucciones específicas)
4. Links funcionales

## Estructura del Reporte

```markdown
# Auditoría de Calidad de Documentación del Framework v2.2

## RESUMEN EJECUTIVO

(3-5 párrafos con hallazgos más críticos)

## METODOLOGÍA

(Proceso de auditoría de documentación)

## HALLAZGOS CRÍTICOS

### 1. Violaciones del Estándar de Escritura Profesional

#### 1.1 Emojis Decorativos Prohibidos

| Archivo | Línea | Emoji | Contexto | Reemplazo Sugerido |
|---------|-------|-------|----------|-------------------|
| ... | X | 😊 | "Todo bien 😊" | "Todo bien" o "✓ Todo bien" |

**Total de violaciones:** X emojis prohibidos en Y archivos

#### 1.2 Uso Excesivo de Símbolos Permitidos

(Casos donde se abusa de símbolos incluso si están permitidos)

### 2. Documentación Desactualizada

#### 2.1 Referencias a Versiones Antiguas

(Lista de archivos con referencias a v1.0, v2.0, task_manager.py)

#### 2.2 Instrucciones Obsoletas

(Ejemplos específicos de comandos o procesos que ya no aplican)

#### 2.3 Links Rotos

(Lista de links que no funcionan)

### 3. Documentación Incompleta o Poco Clara

#### 3.1 Secciones Vacías o con Placeholders

| Archivo | Sección | Problema |
|---------|---------|----------|
| ... | ... | "TODO: Completar" |

#### 3.2 Instrucciones Ambiguas

(Ejemplos de instrucciones que necesitan clarificación)

#### 3.3 Falta de Ejemplos

(Secciones que necesitan ejemplos de código o uso)

### 4. Inconsistencias entre Documentos

(Información contradictoria encontrada)

## ESTADÍSTICAS

- Total de archivos .md auditados: X
- Documentos con emojis prohibidos: X (X%)
- Documentos desactualizados: X (X%)
- Documentos incompletos: X (X%)
- Emojis prohibidos totales: X
- Referencias obsoletas: X
- Links rotos: X

## RECOMENDACIONES PRIORIZADAS

### PRIORIDAD 1: CRÍTICO (profesionalismo)

1. Eliminar TODOS los emojis prohibidos
2. Actualizar referencias a task_manager.py (deprecated)

### PRIORIDAD 2: ALTO (claridad)

1. Completar secciones con placeholders
2. Actualizar versiones a v2.2
3. Clarificar instrucciones ambiguas

### PRIORIDAD 3: MEDIO (mejoras)

1. Agregar ejemplos faltantes
2. Estandarizar terminología
3. Mejorar estructura de headers

## ANEXOS

### A. Lista Completa de Archivos .md Auditados

(Tabla con todos los documentos y su estado)

### B. Guía de Reemplazo de Emojis

(Mapeo de emojis prohibidos → símbolos permitidos o texto)
```

## Criterios de Completitud

Tu tarea está completa cuando:
- Has auditado TODOS los archivos .md del repositorio
- Has identificado y catalogado TODOS los emojis prohibidos
- Has verificado actualidad de documentación clave
- Has generado estadísticas cuantitativas
- El reporte tiene >2000 palabras con ejemplos específicos

## Ruta del Reporte

Guarda tu reporte en:
`archive/audits/auditor-a-completa-framework-v2-2-20260118-142521/tasks/auditoria-calidad-documentacion/reports/auditoria_documentacion.md`

---

**IMPORTANTE**: Tu propio reporte debe usar SOLO símbolos permitidos como ejemplo de buenas prácticas.
