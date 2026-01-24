# Arquitectura Jerárquica del Proyecto - Framework Agéntico v2.2

**Fecha de Creación:** 2026-01-15
**Propósito:** Definir EXACTAMENTE qué archivos/documentos van en cada directorio
**Criticidad:** MÁXIMA - Este documento es la FUENTE DE VERDAD para organización de archivos

---

## PRINCIPIO FUNDAMENTAL

**NUNCA crear archivos en ubicaciones arbitrarias.**

Antes de crear CUALQUIER archivo, consultar este documento para determinar su ubicación correcta según su tipo y propósito.

---

## MAPA COMPLETO DE DIRECTORIOS

```
agentic-task-framework/
├── .claude/ # Configuración de Claude Code (NO TOCAR)
├── .git/ # Git repository (NO TOCAR)
├── .memory_backups/ # Backups automáticos de CLAUDE.md
├── core/ # CÓDIGO DEL FRAMEWORK (Python, Bash)
├── docs/ # DOCUMENTACIÓN TÉCNICA (especificaciones, guías)
├── reports/ # REPORTES DE SESIÓN (análisis, auditorías)
├── archive/ # HISTÓRICOS Y LEGACY
├── projects/ # PROYECTOS DE INVESTIGACIÓN (output de agentes)
├── examples/ # EJEMPLOS DE USO
├── legacy/ # WARNING: CÓDIGO OBSOLETO (v1.0)
├── schemas/ # SCHEMAS JSON
├── tests/ # ✅ TESTS AUTOMATIZADOS
├── venv/ # Python virtual environment (NO TOCAR)
│
├── CLAUDE.md # Instrucciones para Claude Code (documentación operativa)
├── README.md # Documentación de usuario (público)
├── requirements.txt # Dependencias Python
├── setup.sh # Script de configuración inicial
└── start_coordinator.sh # Entry point del coordinador
```

---

## 1. RAÍZ DEL PROYECTO `/`

### ✅ QUÉ VA AQUÍ:

**Archivos de configuración y entrada:**
- `CLAUDE.md` - Instrucciones operativas para Claude Code (cómo usar el framework)
- `README.md` - Documentación principal user-facing
- `requirements.txt` - Dependencias Python
- `.gitignore` - Configuración Git
- `setup.sh` - Script de instalación/configuración
- `start_coordinator.sh` - Entry point principal del coordinador

### ❌ QUÉ NO VA AQUÍ:

**NUNCA en raíz:**
- ❌ Scripts Python específicos de proyectos (`create_youtube_skip_project.py`)
- ❌ Scripts temporales de tareas (`setup_youtube_tasks.py`)
- ❌ Prompts temporales (`temp_prompt.md`)
- ❌ Archivos temporales de Claude (`tmpclaude-*-cwd`)
- ❌ Reportes de sesión (van en `reports/`)
- ❌ Código de utilidades (van en `core/`)

### LIMPIEZA NECESARIA:

**Archivos que deben moverse/eliminarse:**
```bash
# Eliminar archivos temporales:
rm -f create_youtube_skip_project.py
rm -f setup_youtube_tasks.py
rm -f temp_prompt.md
rm -f tmpclaude-*-cwd

# Motivo: Scripts temporales específicos de proyectos no van en raíz
```

---

## 2. DIRECTORIO `core/` - CÓDIGO DEL FRAMEWORK

### PROPÓSITO:
Contiene el **código fuente del framework** - la maquinaria que hace funcionar el sistema.

### ✅ QUÉ VA AQUÍ:

**A. Código Python Core (Módulos Principales):**
```python
project_manager.py # Gestor de proyectos y estructura
framework_validator.py # Validador de conformidad
```

**B. Scripts de Utilidad (Python):**
```python
analyze_inconsistencies.py # Análisis de patrones organizacionales
audit_project.py # Auditoría de conformidad v2.2
check_empty_reports.py # Verificación de reportes vacíos
fix_project_structure.py # Corrección de estructura de proyectos legacy
reorganize_task_structure.py # Migración a v2.2 ORGANIZED
migrate_v10_to_v22.py # Migración de metadata v1.0 → v2.2
```

**C. Scripts Bash (Automatización):**
```bash
init_memory.sh # Inicialización de memoria de sesión
update_memory.sh # Actualización de CLAUDE.md
session_summary.sh # Generación de resumen de sesión
task_launcher.sh # Lanzador de tareas
fix_*.sh # Scripts de corrección específicos
```

**D. Templates y Configuración:**
```
context_template.md # Template para context.md de proyectos
workflow_templates.json # Templates de workflows predefinidos
```

### ❌ QUÉ NO VA AQUÍ:

**NUNCA en core/:**
- ❌ Documentación de usuario (va en `docs/`)
- ❌ Reportes de análisis (van en `reports/`)
- ❌ Ejemplos de uso (van en `examples/`)
- ❌ Código de proyectos específicos
- ❌ Outputs de agentes (van en `projects/`)

### REGLA:
Si es **código ejecutable del framework** → `core/`
Si es **documentación sobre el framework** → `docs/`

### CRITICAL: PROBLEMA ENCONTRADO:

**Archivo mal ubicado:**
```
core/INTEGRATION_INSTRUCTIONS_C5.md
```

**Ubicación correcta:** `docs/INTEGRATION_INSTRUCTIONS_C5.md`

**Razón:** Es documentación técnica, no código ejecutable.

---

## 3. DIRECTORIO `docs/` - DOCUMENTACIÓN TÉCNICA

### PROPÓSITO:
Contiene **documentación técnica permanente** sobre el framework - especificaciones, guías, estándares.

### ✅ QUÉ VA AQUÍ:

**A. Especificaciones Técnicas:**
```markdown
ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md # Especificación del estándar v2.2 ORGANIZED
CHECKLIST.md # Checklist manual de validación
ARQUITECTURA_JERARQUICA_PROYECTO.md # Este documento (arquitectura del proyecto)
```

**B. Guías y Mejores Prácticas:**
```markdown
best_practices.md # Mejores prácticas de uso
INTEGRATION_INSTRUCTIONS_*.md # Instrucciones de integración
```

**C. Propuestas (Subdirectorio):**
```
docs/proposals/
└── forge/ # Propuestas del sistema FORGE
```

### ❌ QUÉ NO VA AQUÍ:

**NUNCA en docs/:**
- ❌ Reportes de sesiones específicas (van en `reports/`)
- ❌ Auditorías de sesión (van en `reports/`)
- ❌ Análisis puntuales (van en `reports/`)
- ❌ Código ejecutable (va en `core/`)

### REGLA:
- **Documentación PERMANENTE y TÉCNICA** → `docs/`
- **Documentación TEMPORAL de sesión** → `reports/`

### DIFERENCIA CLAVE: `docs/` vs `reports/`

| Aspecto | `docs/` | `reports/` |
|---------|---------|------------|
| **Naturaleza** | Permanente, versionada | Temporal, histórica |
| **Contenido** | Especificaciones, estándares | Análisis de sesión, auditorías |
| **Audiencia** | Desarrolladores, usuarios | Coordinador, auditoría |
| **Actualización** | Evoluciona con el framework | Se crea y archiva |
| **Ejemplos** | ESTANDAR_v2.2.md, CHECKLIST.md | AUDITORIA_20260114.md |

---

## 4. DIRECTORIO `reports/` - REPORTES DE SESIÓN

### PROPÓSITO DUAL:

**USO PRIMARIO (Post 2026-01-17):**
Síntesis del coordinador sobre trabajo realizado en sesiones.

**USO SECUNDARIO (Legacy - Pre 2026-01-17):**
Auditorías que NO usaron ProjectManager (antes del protocolo).

### ✅ QUÉ VA AQUÍ:

**A. Síntesis de Sesión (Post 2026-01-17):**
```markdown
SESION_REPORT_20260102.md # Reporte general de sesión de trabajo
CORRECCIONES_APLICADAS_20260115.md # Correcciones implementadas en sesión
FASE3_COMPLETADA_20260116.md # Completado de fase de desarrollo
REVIEW_COMPLETO_AUDITORIAS_20260117.md # Síntesis histórica de auditorías
CORRECCION_ESTRUCTURA_AUDITORIAS_20260117.md # Correcciones aplicadas
```

**B. Auditorías Legacy (Pre 2026-01-17) - WARNING: MÉTODO OBSOLETO:**
```markdown
AUDITORIA_FRAMEWORK_COMPLETA_20260114.md # Legacy - Sin ProjectManager
AUDIT_SISTEMICO_20260114.md # Legacy - Sin ProjectManager
ANALISIS_EXHAUSTIVO_FRAMEWORK_v22_20260115.md # Legacy - Agente ae7984d
AUDITORIA_VENV_COMPLETA_20260116.md # Legacy - Análisis manual
```

**Nota:** Todas las auditorías legacy tienen header que indica:
- Método obsoleto
- Prompts reconstruidos en `archive/audits/auditor-as-enero-2026-retroactivo-*/`
- Protocolo correcto a seguir

**C. Metadata:**
```markdown
README.md # Índice de reportes y convenciones
```

### CONVENCIÓN DE NOMBRES:

```
TIPO_DESCRIPCION_FECHA.md

Ejemplos:
SESION_REPORT_20260102.md
AUDITORIA_FRAMEWORK_COMPLETA_20260114.md
ANALISIS_EXHAUSTIVO_FRAMEWORK_v22_20260115.md
CORRECCIONES_APLICADAS_20260115.md
```

**Tipos reconocidos:**
- `SESION_*` - Reportes de sesión
- `AUDITORIA_*` / `AUDIT_*` - Auditorías
- `ANALISIS_*` - Análisis generados por agentes
- `CORRECCIONES_*` - Reportes de correcciones

**Formato de fecha:** `YYYYMMDD` (ISO 8601 compacto)

### ❌ QUÉ NO VA AQUÍ:

**NUNCA en reports/:**
- ❌ Especificaciones técnicas permanentes (van en `docs/`)
- ❌ Código fuente (va en `core/`)
- ❌ Outputs de agentes de investigación (van en `projects/`)
- ❌ **Nuevas auditorías del framework** (van en `archive/audits/`)

### REGLA HACIA ADELANTE (Post 2026-01-17):

**Para auditorías del framework:**
1. ✅ Crear proyecto formal en `archive/audits/` usando ProjectManager
2. ✅ Lanzar agentes con prompts guardados en `tasks/*/prompt.md`
3. ✅ OPCIONALMENTE crear síntesis en `reports/` para el usuario
4. ❌ NUNCA crear solo reporte en `reports/` sin proyecto formal

**Para síntesis de sesiones:**
1. ✅ Crear directamente en `reports/`
2. Ejemplo: `SESION_TRABAJO_20260120.md`, `CORRECCIONES_APLICADAS_*.md`

**Regla simple:**
- **Auditoría del framework** → Proyecto en `archive/audits/` (+ síntesis opcional en `reports/`)
- **Síntesis de sesión** → Directamente en `reports/`
- **Documentación permanente** → `docs/`

---

## 5. DIRECTORIO `archive/` - HISTÓRICOS Y AUDITORÍAS

### PROPÓSITO:
Contiene **auditorías del framework** (completadas o en progreso) y **material histórico**.

### ✅ QUÉ VA AQUÍ:

**A. Auditorías del Framework (`archive/audits/`):**
```
archive/audits/
├── auditor-a-framework-v2-2-20251227-222837/ # Auditoría multi-agente (27 Dic)
└── auditor-as-enero-2026-retroactivo-20260117-125539/ # Reconstrucción prompts (17 Ene)
```

**CRÍTICO:** TODAS las auditorías/mejoras del framework van aquí, incluso las en progreso.

**B. Documentos de Cambios Históricos:**
```markdown
CHANGELOG_REMOVAL.md # Registro de cambios removidos
README.md # Índice de archivos archivados
```

### ESTRUCTURA INTERNA:

```
archive/
├── README.md # Índice de archivos archivados
├── CHANGELOG_REMOVAL.md # Registro de cambios
└── audits/ # AUDITORÍAS DEL FRAMEWORK (activas o completadas)
 └── [proyecto-auditoria]/
 ├── project_info.json
 ├── context.md
 └── tasks/
 └── [tarea]/
 ├── prompt.md
 ├── README.md
 └── reports/
```

### REGLA CRÍTICA:

**TODAS las auditorías del framework → `archive/audits/`**

- ✅ Auditorías en progreso
- ✅ Auditorías completadas
- ✅ Validaciones de conformidad
- ✅ Mejoras al framework
- ✅ Reconstrucción de prompts de auditorías

**Investigaciones de usuario → `projects/`**

- ✅ COVID-19, YouTube, ClO₂, etc.
- ❌ NUNCA auditorías del framework

### CÓMO DECIDIR:

**Ver:** `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md` para criterios detallados.

**Regla simple:** ¿Analizo el framework o CON el framework?
- Analizo EL framework → `archive/audits/`
- Analizo CON el framework → `projects/`

### WARNING: NO CONFUNDIR CON:
- `legacy/` - Código obsoleto del framework (no proyectos)
- `projects/` - Investigaciones de usuario (NO auditorías del framework)

---

## 6. DIRECTORIO `projects/` - PROYECTOS DE INVESTIGACIÓN

### PROPÓSITO:
Contiene **todos los proyectos de investigación** creados por el coordinador y ejecutados por agentes.

### ✅ ESTRUCTURA ESTÁNDAR (v2.2 ORGANIZED):

```
projects/
└── [project-id]/ # ID único: nombre-YYYYMMDD-HHMMSS
 ├── project_info.json # Metadata del proyecto
 ├── context.md # Contexto inicial del usuario
 │
 ├── tasks/ # Tareas ejecutadas por agentes
 │ └── [task-name]/ # Nombre kebab-case
 │ ├── task_info.json # Metadata de la tarea
 │ ├── prompt.md # Prompt usado para el agente
 │ ├── README.md # Overview de la tarea
 │ └── reports/ # OUTPUTS DEL AGENTE AQUÍ
 │ ├── [reporte1].md
 │ ├── [reporte2].md
 │ └── ...
 │
 └── synthesis/ # Síntesis del coordinador
 └── [sintesis-final].md
```

### CONVENCIONES DE NOMBRES:

**Project ID:**
```
[nombre-descriptivo]-YYYYMMDD-HHMMSS

Ejemplos:
investigaci-n-clo-covid-19-20251222-195407
youtube-skip-ads-extension-20260113-200039
```

**Task Name:**
```
[accion]-[tema]-[detalles] (kebab-case)

Ejemplos:
analisis-quimica-molecular-clo2
virologia-sars-cov2
revision-critica-research-kalcker
```

**Report Filenames:**
```
[descripcion_snake_case].md

Ejemplos:
virologia_molecular_sars_cov2.md
analisis_comparativo.md
completion_report.md
```

### CRÍTICO: Dónde van los OUTPUTS de agentes

**SIEMPRE en:**
```
projects/[project-id]/tasks/[task-name]/reports/[reporte].md
```

**NUNCA en:**
- ❌ Root de tarea: `tasks/[task-name]/[reporte].md` (legacy, deprecated)
- ❌ reports/ global: `reports/[reporte].md` (confunde con reportes de sesión)

### REGLA ABSOLUTA:

**Outputs de agentes de investigación** → `projects/[project-id]/tasks/[task-name]/reports/`
**Reportes de sesión de trabajo** → `reports/`

---

## 7. DIRECTORIO `examples/` - EJEMPLOS DE USO

### PROPÓSITO:
Contiene **ejemplos de uso del framework** para nuevos usuarios.

### ✅ QUÉ VA AQUÍ:

```
examples/
├── project_creation.py # Ejemplo de creación de proyecto
├── task_management.py # Ejemplo de gestión de tareas
└── validation_usage.py # Ejemplo de uso del validator
```

### REGLA:
**Código de ejemplo educativo** → `examples/`
**Código funcional del framework** → `core/`

---

## 8. DIRECTORIO `legacy/` - WARNING: CÓDIGO OBSOLETO

### PROPÓSITO:
Contiene **código obsoleto de versiones anteriores** del framework que ya no se usa pero se mantiene para referencia histórica.

### ✅ QUÉ VA AQUÍ:

```
legacy/
└── task_manager.py # v1.0 multi-window system (DEPRECATED)
```

### REGLA:
- **Código obsoleto del framework** → `legacy/`
- **Proyectos archivados** → `archive/`

### WARNING: NUNCA IMPORTAR CÓDIGO DE `legacy/`

---

## 9. DIRECTORIO `schemas/` - SCHEMAS JSON

### PROPÓSITO:
Contiene **schemas JSON** para validación de estructuras de datos.

### ✅ QUÉ VA AQUÍ:

```
schemas/
├── project_info_schema.json # Schema para project_info.json
├── task_info_schema.json # Schema para task_info.json
└── workflow_schema.json # Schema para workflows
```

### REGLA:
**Schemas de validación JSON** → `schemas/`

---

## 10. DIRECTORIO `tests/` - ✅ TESTS AUTOMATIZADOS

### PROPÓSITO:
Contiene **tests unitarios e integración** del framework.

### ✅ QUÉ VA AQUÍ:

```
tests/
├── test_project_manager.py # Tests de ProjectManager
├── test_framework_validator.py # Tests de FrameworkValidator
└── test_integration.py # Tests de integración
```

### ESTADO ACTUAL:
 WARNING: **Vacío** - No hay tests implementados (coverage 0%)

### REGLA:
**Tests automatizados** → `tests/`
**Tests manuales documentados** → `docs/CHECKLIST.md`

---

## RESUMEN DE DECISIONES DE UBICACIÓN

### QUESTION: "¿DÓNDE PONGO ESTE ARCHIVO?"

**Pregúntate:**

#### 1. ¿Es código ejecutable del framework?
→ `core/`

#### 2. ¿Es documentación técnica permanente?
→ `docs/`

#### 3. ¿Es un reporte de una sesión de trabajo?
→ `reports/`

#### 4. ¿Es output de un agente de investigación?
→ `projects/[project-id]/tasks/[task-name]/reports/`

#### 5. ¿Es un proyecto archivado?
→ `archive/`

#### 6. ¿Es código de ejemplo?
→ `examples/`

#### 7. ¿Es un test?
→ `tests/`

#### 8. ¿Es un schema JSON?
→ `schemas/`

#### 9. ¿Es código obsoleto?
→ `legacy/`

---

## CORRECCIONES NECESARIAS DETECTADAS

### CRITICAL: ARCHIVOS EN UBICACIÓN INCORRECTA:

#### A. Raíz del Proyecto → Eliminar

```bash
# Archivos temporales que deben eliminarse:
rm -f create_youtube_skip_project.py
rm -f setup_youtube_tasks.py
rm -f temp_prompt.md
rm -f tmpclaude-*-cwd
```

**Razón:** Scripts temporales específicos de proyectos no van en raíz del framework.

#### B. core/ → docs/

```bash
# Documentación mal ubicada:
mv core/INTEGRATION_INSTRUCTIONS_C5.md docs/INTEGRATION_INSTRUCTIONS_C5.md
```

**Razón:** Es documentación técnica, no código ejecutable.

---

## PROTOCOLO DE CREACIÓN DE ARCHIVOS

### ✅ ANTES DE CREAR UN ARCHIVO:

1. **Identificar tipo de archivo:**
 - ¿Código? ¿Documentación? ¿Reporte? ¿Output de agente?

2. **Consultar este documento:**
 - Buscar la sección correspondiente al tipo

3. **Verificar convenciones de nombres:**
 - ¿Kebab-case? ¿Snake_case? ¿SCREAMING_SNAKE?

4. **Crear en ubicación correcta:**
 - Usar path absoluto para evitar errores

5. **Validar después:**
 - ¿El archivo está donde debe estar?

### ❌ NUNCA:

- ❌ Crear archivos en raíz sin justificación
- ❌ Mezclar outputs de agentes con reportes de sesión
- ❌ Poner documentación en `core/`
- ❌ Poner código en `docs/`

---

## CONVENCIONES DE NOMBRES GLOBALES

### Archivos en `docs/` y `reports/`

**Formato:** `SCREAMING_SNAKE_CASE.md`

```
ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md
AUDITORIA_FRAMEWORK_COMPLETA_20260114.md
CORRECCIONES_APLICADAS_20260115.md
```

### Archivos Python

**Formato:** `snake_case.py`

```
project_manager.py
framework_validator.py
analyze_inconsistencies.py
```

### Archivos Bash

**Formato:** `snake_case.sh`

```
start_coordinator.sh
init_memory.sh
fix_project_structure.sh
```

### Project IDs

**Formato:** `kebab-case-YYYYMMDD-HHMMSS`

```
investigaci-n-clo-covid-19-20251222-195407
youtube-skip-ads-extension-20260113-200039
```

### Task Names

**Formato:** `kebab-case`

```
analisis-quimica-molecular-clo2
virologia-sars-cov2
revision-critica-research-kalcker
```

### Report Filenames (dentro de tasks/)

**Formato:** `snake_case.md`

```
virologia_molecular_sars_cov2.md
analisis_comparativo.md
completion_report.md
```

---

## PREGUNTAS Y RESPUESTAS

### ❓ "He creado un análisis exhaustivo del framework. ¿Dónde va?"

✅ **Respuesta:** `reports/ANALISIS_EXHAUSTIVO_FRAMEWORK_v22_YYYYMMDD.md`

**Razón:** Es un reporte de sesión, no documentación permanente.

---

### ❓ "Creé un script para migrar proyectos v1.0 a v2.2. ¿Dónde va?"

✅ **Respuesta:** `core/migrate_v10_to_v22.py`

**Razón:** Es código funcional del framework.

---

### ❓ "Documenté el estándar v2.2 ORGANIZED. ¿Dónde va?"

✅ **Respuesta:** `docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md`

**Razón:** Es documentación técnica permanente.

---

### ❓ "Un agente generó un reporte de investigación sobre virología. ¿Dónde va?"

✅ **Respuesta:** `projects/[project-id]/tasks/virologia-sars-cov2/reports/virologia_molecular.md`

**Razón:** Es output de un agente de investigación.

---

### ❓ "Hice una auditoría del framework. ¿Dónde va?"

✅ **Respuesta:** `reports/AUDITORIA_FRAMEWORK_COMPLETA_YYYYMMDD.md`

**Razón:** Es un reporte de sesión de auditoría.

---

### ❓ "Creé un script temporal para setup de un proyecto. ¿Dónde va?"

❌ **Respuesta:** **NUNCA en raíz.**

**Opciones correctas:**
1. Si es reutilizable → `core/setup_project_template.py`
2. Si es temporal → Ejecutar inline, no guardar
3. Si es específico de proyecto → `.temp/` (gitignored)

---

## VALIDACIÓN DE ESTRUCTURA

### ✅ Script de Validación Automática

```bash
# Validar estructura del proyecto
python core/framework_validator.py validate-structure

# Validar proyecto específico
python core/framework_validator.py validate-project [project-id]
```

### ✅ Checklist Manual

Ver `docs/CHECKLIST.md` para validación manual exhaustiva.

---

## CHANGELOG DE ESTE DOCUMENTO

### 2026-01-15 - Versión 1.0
- ✅ Creación inicial
- ✅ Definición completa de estructura jerárquica
- ✅ Identificación de archivos mal ubicados
- ✅ Convenciones de nombres documentadas
- ✅ Protocolo de creación de archivos

---

## CONCLUSIÓN

**Este documento es la FUENTE DE VERDAD para organización de archivos en el framework.**

**NUNCA crear archivos sin consultar este documento primero.**

**Si tienes dudas sobre ubicación:**
1. Lee la sección correspondiente
2. Usa la guía de decisiones ("¿DÓNDE PONGO ESTE ARCHIVO?")
3. Valida con `framework_validator.py`

---

**Documento mantenido por:** Coordinador Claude
**Última actualización:** 2026-01-15
**Versión:** 1.0
**Estado:** ACTIVO - FUENTE DE VERDAD
