# TAREA: AUDITORIA DE ESTRUCTURA DE PROYECTOS

## TU ROL

Eres un Structure Validator y QA Engineer especializado en validación de compliance. Tu trabajo es verificar que proyectos existentes cumplan con estándares definidos.

## OBJETIVO

Auditar el proyecto COVID-19 existente contra el estándar v2.2 ORGANIZED y generar reporte detallado de cumplimiento por tarea.

## PROYECTO A AUDITAR

projects/investigaci-n-clo-covid-19-20251222-195407/

Este proyecto tiene múltiples tareas. Debes verificar cada una contra v2.2 ORGANIZED.

## ESTANDAR v2.2 ORGANIZED

Cada tarea DEBE tener:

```
tasks/[nombre-tarea]/
  ├── task_info.json          (REQUERIDO - metadata)
  ├── prompt.md               (REQUERIDO - prompt usado)
  ├── README.md               (REQUERIDO - índice/overview)
  └── reports/                (REQUERIDO - subdirectorio)
      ├── [tema]_[aspecto]_[detalles].md
      └── ...
```

Convenciones:
- Nombres de tareas: kebab-case (ej: analisis-quimica-molecular)
- Nombres de reportes: snake_case (ej: quimica_molecular_clo2.md)
- NO archivos .md en root (excepto README.md y prompt.md)
- TODOS los reportes en reports/

## VERIFICACIONES REQUERIDAS

Para cada tarea del proyecto:

### 1. Archivos Obligatorios
- ¿Existe task_info.json?
- ¿Existe prompt.md?
- ¿Existe README.md?
- ¿Existe directorio reports/?

### 2. Estructura de Archivos
- ¿Hay archivos .md en root (excepto permitidos)?
- ¿Todos los reportes están en reports/?
- ¿Hay archivos huérfanos fuera de estructura?

### 3. Naming Conventions
- ¿Nombre de tarea es kebab-case?
- ¿Nombres de reportes son snake_case?
- ¿Nombres son descriptivos del contenido?

### 4. Contenido de task_info.json
- ¿Formato JSON válido?
- ¿Tiene campos requeridos (task_name, description, status, reports)?
- ¿Lista de reports coincide con archivos reales?
- ¿Status es válido (in_progress, completed, failed)?

### 5. Contenido de README.md
- ¿Existe y tiene contenido?
- ¿Sirve como índice de la tarea?
- ¿Lista los reportes en reports/?
- ¿Tiene estructura básica (título, introducción, contenido)?

### 6. Contenido de reports/
- ¿Cuántos archivos hay?
- ¿Son todos .md?
- ¿Tienen contenido o están vacíos?
- ¿Nombres siguen convención snake_case?

## METODOLOGIA

1. Lista todas las tareas en tasks/
2. Para cada tarea, verifica estructura completa
3. Lee task_info.json y valida contenido
4. Verifica que lista de reports coincida con realidad
5. Revisa README.md
6. Cuenta archivos en reports/
7. Identifica archivos fuera de lugar
8. Compara contra estándar v2.2

## ESTRUCTURA DE OUTPUT

Reporte en: reports/validacion_proyecto_covid.md

```markdown
# AUDITORIA DE ESTRUCTURA - PROYECTO COVID-19

## RESUMEN EJECUTIVO

- Total de tareas: X
- Tareas COMPLIANT: X
- Tareas NON-COMPLIANT: X
- Archivos fuera de estructura: X
- Tareas con reports/ vacío: X

## VALIDACION POR TAREA

### [nombre-tarea-1]

**Ubicación**: tasks/[nombre-tarea-1]/

**Archivos Obligatorios**:
- task_info.json: PRESENTE / AUSENTE
- prompt.md: PRESENTE / AUSENTE
- README.md: PRESENTE / AUSENTE
- reports/: PRESENTE / AUSENTE

**Estructura**:
- Archivos .md en root (no permitidos): X encontrados
  - [lista de archivos]
- Reportes en reports/: X archivos
  - [lista de reportes]

**Naming**:
- Nombre de tarea: VALIDO (kebab-case) / INVALIDO
- Nombres de reportes: X válidos, X inválidos
  - Inválidos: [lista]

**task_info.json**:
- JSON válido: SI / NO
- Campos requeridos: COMPLETOS / FALTANTES
- Status: [valor]
- Reports listados: [lista]
- Reports reales: [lista]
- Coinciden: SI / NO

**README.md**:
- Tiene contenido: SI / NO (X palabras)
- Lista reportes: SI / NO
- Estructura básica: SI / NO

**Compliance**: COMPLIANT / NON-COMPLIANT
**Problemas**: [lista de problemas específicos]
**Correcciones necesarias**: [lista]

---

[Repetir para cada tarea]

## TAREAS COMPLIANT (v2.2 ORGANIZED)

### Lista
1. [nombre-tarea-1] - Sin problemas
2. [nombre-tarea-2] - Sin problemas
...

Total: X tareas

## TAREAS NON-COMPLIANT

### Por Tipo de Problema

**Falta task_info.json**:
- [tarea-1]
- [tarea-2]

**Falta README.md**:
- [tarea-3]

**Reportes en root (no en reports/)**:
- [tarea-4]: 3 archivos
- [tarea-5]: 1 archivo

**reports/ vacío**:
- [tarea-6]
- [tarea-7]

**Naming incorrecto**:
- [tarea-8]: nombre usa snake_case en vez de kebab-case
- [tarea-9]: reportes usan camelCase

## ARCHIVOS FUERA DE ESTRUCTURA

### Archivos huérfanos
[Lista de archivos que no están donde deberían]

### Directorios no estándar
[Directorios que no siguen estructura v2.2]

## ESTADISTICAS

### Por Compliance
- COMPLIANT: X (X%)
- NON-COMPLIANT: X (X%)

### Por Tipo de Problema
- Sin task_info.json: X tareas
- Sin README.md: X tareas
- Sin reports/: X tareas
- Reportes en root: X tareas
- reports/ vacío: X tareas
- Naming incorrecto: X tareas

### Archivos
- Total archivos .md: X
- En reports/: X
- En root (no permitidos): X
- Reportes vacíos (0 bytes): X

## PLAN DE CORRECCION

### Acción 1: Crear archivos faltantes
```bash
# Para tareas sin task_info.json
python core/fix_project_structure.py [project-id] [task-name]
```

### Acción 2: Reorganizar estructura
```bash
# Para tareas con reportes en root
python core/reorganize_task_structure.py [project-id] [task-name]
```

### Acción 3: Correcciones manuales
- [Lista de correcciones que requieren intervención manual]

## RECOMENDACIONES

### Prioritarias
1. Corregir X tareas con reports/ vacío
2. Mover X reportes de root a reports/
3. Crear X archivos task_info.json faltantes

### Importantes
1. Renombrar X tareas con naming incorrecto
2. Crear X README.md faltantes
3. Validar contenido de task_info.json

### Mejoras
1. Mejorar README.md de tareas COMPLIANT
2. Estandarizar formato de reportes
3. Agregar más metadata a task_info.json

## CONCLUSION

[Resumen del estado del proyecto COVID vs estándar v2.2]
[Viabilidad de migración a Forge v1.0]
[Esfuerzo estimado para correcciones]
```

## CRITERIOS DE CALIDAD

- Verifica TODAS las tareas sin omitir ninguna
- Sé específico con nombres de archivos
- Cuantifica problemas (X tareas, X archivos)
- Proporciona comandos ejecutables para correcciones
- Clasifica por severidad

## HERRAMIENTAS

- Read: leer archivos JSON y MD
- Glob: encontrar archivos por patrón
- Bash: listar directorios, contar archivos

## FORMATO

Profesional, sin emojis, markdown estándar.

## ENTREGABLE

1. Reporte en reports/validacion_proyecto_covid.md
2. Validación completa de todas las tareas
3. Plan de corrección ejecutable
4. Métricas cuantificables
