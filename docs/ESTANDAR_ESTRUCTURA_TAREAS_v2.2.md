# ESTANDAR DE ESTRUCTURA DE TAREAS - Framework v2.2

## OPCIÓN B: ORGANIZED (OFICIAL)

Todas las tareas deben seguir esta estructura jerárquica.

## Estructura Obligatoria

```
projects/[project-id]/tasks/[task-name]/
  ├── task_info.json          (REQUERIDO - metadata de la tarea)
  ├── prompt.md               (REQUERIDO - prompt usado para crear la tarea)
  ├── README.md               (REQUERIDO - índice/overview de la tarea)
  └── reports/                (REQUERIDO - todos los reportes aquí)
      ├── [tema]_[aspecto]_[detalles].md
      ├── [tema]_[aspecto]_[detalles].md
      └── ...
```

## Convenciones de Nombres

### Nombres de Tareas

**Formato:** `[accion]-[tema]-[detalles]` (kebab-case)

**Componentes:**
- `[accion]`: Verbo que describe qué hace (analizar, investigar, evaluar, revisar)
- `[tema]`: Tema principal (selectividad, farmacocinetica, toxicologia)
- `[detalles]`: Contexto específico (clo2, covid-19, in-vitro)

**Ejemplos:**
- `analizar-selectividad-molecular-clo2`
- `investigar-farmacocinetica-oral-clo2`
- `evaluar-ventana-terapeutica-covid19`
- `revisar-estudios-clinicos-kalcker`

### Nombres de Reportes

**Formato:** `[tema]_[aspecto]_[detalles].md` (snake_case)

**Componentes:**
- `[tema]`: Tema principal del reporte
- `[aspecto]`: Aspecto específico analizado
- `[detalles]`: Contexto o alcance adicional

**Tipos comunes de reportes:**

1. **Análisis técnico:**
   - `quimica_molecular_clo2.md`
   - `farmacocinetica_concentraciones_pulmonares.md`
   - `toxicologia_sistemica_invivo.md`

2. **Análisis comparativo:**
   - `selectividad_viral_vs_humano.md`
   - `efectividad_clo2_vs_remdesivir.md`

3. **Documentos de síntesis:**
   - `resumen_ejecutivo_selectividad.md`
   - `sintesis_hallazgos_principales.md`

4. **Documentos técnicos:**
   - `metodologia_analisis_experimental.md`
   - `protocolos_cds_evaluacion_toxicologica.md`

5. **Material complementario:**
   - `diagramas_modelos_conceptuales.md`
   - `faq_preguntas_frecuentes.md`
   - `referencias_bibliografia_completa.md`

### README.md

**Propósito:** Índice general y punto de entrada a la tarea

**Contenido obligatorio:**
```markdown
# [TÍTULO DE LA TAREA]

## INTRODUCCIÓN
[Descripción breve de la tarea]

## CONTENIDO DEL ANÁLISIS

### Documentos principales

1. **[nombre_reporte.md]**
   - Descripción del contenido
   - Audiencia objetivo
   - ~X palabras/líneas

2. **[otro_reporte.md]**
   - Descripción
   - etc.

## NAVEGACIÓN RÁPIDA

Por audiencia/propósito:
- Para científicos: Leer [reporte_tecnico.md]
- Para resumen ejecutivo: Leer [resumen_ejecutivo.md]

## HALLAZGOS CLAVE

[Resumen de 3-5 hallazgos principales]

## METODOLOGÍA

[Breve descripción del enfoque usado]

## REFERENCIAS

[Si aplica]
```

## Ejemplos Completos

### Ejemplo 1: Tarea Simple (1 reporte principal)

```
tasks/analizar-quimica-molecular-clo2/
  ├── task_info.json
  ├── prompt.md
  ├── README.md
  └── reports/
      └── quimica_molecular_clo2.md
```

### Ejemplo 2: Tarea Moderada (2-3 reportes)

```
tasks/evaluar-ventana-terapeutica-clo2/
  ├── task_info.json
  ├── prompt.md
  ├── README.md
  └── reports/
      ├── analisis_ventana_terapeutica_completo.md
      ├── resumen_ejecutivo.md
      └── balance_riesgo_beneficio.md
```

### Ejemplo 3: Tarea Compleja (múltiples reportes)

```
tasks/analizar-selectividad-molecular-celular-clo2/
  ├── task_info.json
  ├── prompt.md
  ├── README.md
  └── reports/
      ├── analisis_selectividad_viral_vs_humano.md
      ├── resumen_ejecutivo_selectividad.md
      ├── diagramas_modelos_conceptuales.md
      ├── faq_preguntas_frecuentes.md
      ├── metodologia_analisis_molecular.md
      └── referencias_bibliografia.md
```

### Ejemplo 4: Tarea con Subdivisiones

```
tasks/investigar-farmacocinetica-completa-clo2/
  ├── task_info.json
  ├── prompt.md
  ├── README.md
  └── reports/
      ├── farmacocinetica_absorcion_oral.md
      ├── farmacocinetica_distribucion_sistemica.md
      ├── farmacocinetica_concentraciones_pulmonares.md
      ├── farmacocinetica_metabolismo_eliminacion.md
      ├── resumen_ejecutivo_farmacocinetica.md
      └── sintesis_hallazgos_principales.md
```

## Reglas Estrictas

### SIEMPRE

1. README.md en root de la tarea (índice general)
2. Todos los reportes dentro de reports/ subdirectory
3. Nombres de reportes descriptivos del contenido
4. snake_case para nombres de reportes
5. kebab-case para nombres de tareas

### NUNCA

1. Reportes directamente en root (excepto README.md)
2. Nombres genéricos como "reporte.md", "analisis.md", "final.md"
3. Mezclar reportes en root y reports/
4. Usar espacios o caracteres especiales en nombres
5. Nombres que no describan el contenido

## Validación

El Framework Validator verifica:

```python
from core.framework_validator import FrameworkValidator

validator = FrameworkValidator()
valid, messages = validator.validate_task_structure(
    project_id="proyecto-ejemplo",
    task_name="analizar-datos-ejemplo"
)

# Verificaciones:
# - task_info.json existe
# - prompt.md existe
# - README.md existe en root
# - reports/ subdirectory existe
# - No hay archivos .md en root (excepto README.md y prompt.md)
# - Nombres de reportes siguen convención
```

## Migración de Tareas Antiguas

Para tareas creadas antes de este estándar:

```bash
# Usar script de reorganización
python core/reorganize_task_structure.py [project-id] [task-name]
```

Esto:
1. Crea reports/ si no existe
2. Mueve reportes de root a reports/
3. Crea README.md si no existe
4. Valida estructura final

## Prompts para Agentes

Al crear prompts para agentes, SIEMPRE especificar:

```markdown
## ESTRUCTURA DE OUTPUT

IMPORTANTE: Debes guardar tus reportes en la siguiente estructura:

1. README.md (en root de la tarea)
   - Ruta: {task_path}/README.md
   - Contenido: Índice general de la tarea

2. Reportes técnicos (en reports/)
   - Ruta: {task_path}/reports/[nombre_descriptivo].md
   - Usar naming convention: [tema]_[aspecto]_[detalles].md

Ejemplo:
```
{task_path}/
  ├── README.md
  └── reports/
      ├── analisis_principal.md
      ├── resumen_ejecutivo.md
      └── metodologia_detallada.md
```

NO guardar reportes directamente en root (excepto README.md).
```

## Beneficios del Estándar

1. **Consistencia:** Todas las tareas tienen la misma estructura
2. **Navegabilidad:** README.md siempre es el punto de entrada
3. **Escalabilidad:** reports/ puede contener muchos archivos sin desorganizarse
4. **Claridad:** Nombres descriptivos indican contenido
5. **Mantenibilidad:** Fácil encontrar y actualizar documentos
6. **Validación:** Verificable automáticamente

## Versión

**Estándar:** v2.2 ORGANIZED
**Fecha:** 2025-12-26
**Estado:** OFICIAL - Aplicar a todas las tareas nuevas y migrar antiguas

---

**Última actualización:** 2025-12-26
