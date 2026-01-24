# Criterios de Clasificación de Proyectos

**Fecha:** 2026-01-17
**Propósito:** Definir EXACTAMENTE cuándo un proyecto va a `projects/` vs `archive/audits/`
**Criticidad:** MÁXIMA - Afecta toda la organización del framework

---

## PREGUNTA FUNDAMENTAL

**¿El framework es la HERRAMIENTA o el OBJETO de la investigación?**

- **HERRAMIENTA** → El framework se usa para investigar algo externo → `projects/`
- **OBJETO** → El framework mismo es lo que se investiga/mejora → `archive/audits/`

---

## CRITERIOS DE DECISIÓN

### ✅ Criterio 1: ¿QUÉ SE ESTÁ ANALIZANDO?

| Se analiza...                                                   | Ubicación         |
| --------------------------------------------------------------- | ----------------- |
| Código del framework (`core/`, `scripts/`, `tests/`)            | `archive/audits/` |
| Documentación del framework (`docs/`, `CLAUDE.md`, `README.md`) | `archive/audits/` |
| Estructura de proyectos (metadata, conformidad v2.2)            | `archive/audits/` |
| Funcionamiento del framework (bugs, performance)                | `archive/audits/` |
| Tema científico (COVID, ClO₂, virología)                        | `projects/`       |
| Tema tecnológico externo (extensiones YouTube, APIs)            | `projects/`       |
| Tema de investigación general                                   | `projects/`       |

### ✅ Criterio 2: ¿CUÁL ES EL OUTPUT ESPERADO?

| Output esperado...                    | Ubicación         |
| ------------------------------------- | ----------------- |
| Bugs identificados en el framework    | `archive/audits/` |
| Correcciones al código del framework  | `archive/audits/` |
| Mejoras a la documentación            | `archive/audits/` |
| Validación de conformidad estructural | `archive/audits/` |
| Plan de correcciones del framework    | `archive/audits/` |
| Prompts reconstruidos de auditorías   | `archive/audits/` |
| Conocimiento sobre tema científico    | `projects/`       |
| Análisis de competencia/mercado       | `projects/`       |
| Reporte de investigación temática     | `projects/`       |
| Síntesis de información externa       | `projects/`       |

### ✅ Criterio 3: ¿QUIÉN ES EL BENEFICIARIO?

| Beneficiario...                   | Ubicación         |
| --------------------------------- | ----------------- |
| El framework (mejora el sistema)  | `archive/audits/` |
| Los desarrolladores del framework | `archive/audits/` |
| El usuario (obtiene conocimiento) | `projects/`       |
| Cliente final con información     | `projects/`       |

### ✅ Criterio 4: ¿QUÉ ARCHIVOS SE LEEN?

| Archivos leídos principalmente...                        | Ubicación         |
| -------------------------------------------------------- | ----------------- |
| `core/*.py`, `scripts/*.py`, `tests/*.py`                | `archive/audits/` |
| `docs/*.md`, `CLAUDE.md`, `README.md`                    | `archive/audits/` |
| `projects/*/project_info.json` (para validar estructura) | `archive/audits/` |
| Papers científicos, artículos, web externos              | `projects/`       |
| APIs externas, bases de datos públicas                   | `projects/`       |
| Código de terceros (GitHub, etc.)                        | `projects/`       |

---

## EJEMPLOS CLASIFICADOS

### `archive/audits/` - Auditorías y Mejoras del Framework

**Solicitudes del usuario:**

1. ✅ "Audita el framework v2.2 completo"
   
   - **Razón:** Analiza código/docs del framework
   - **Output:** Bugs, inconsistencias, plan de corrección

2. ✅ "Encuentra todas las inconsistencias en ProjectManager"
   
   - **Razón:** Analiza `core/project_manager.py`
   - **Output:** Bugs en el código del framework

3. ✅ "Valida que todos los proyectos cumplen v2.2 ORGANIZED"
   
   - **Razón:** Analiza estructura de `projects/`
   - **Output:** Conformidad estructural del framework

4. ✅ "Mejora el sistema de logging del framework"
   
   - **Razón:** Mejora código del framework
   - **Output:** Correcciones a `core/*.py`

5. ✅ "Reconstruye los prompts de las auditorías de enero"
   
   - **Razón:** Meta-trabajo sobre auditorías del framework
   - **Output:** Documentación de auditorías pasadas

6. ✅ "Analiza por qué los agentes instalan paquetes en global Python"
   
   - **Razón:** Problema sistémico del framework
   - **Output:** Root cause analysis + corrección al framework

7. ✅ "Crea tests automatizados para ProjectManager"
   
   - **Razón:** Mejora el framework (testing)
   - **Output:** `tests/test_project_manager.py`

8. ✅ "Migra todos los proyectos de venv/ a .venv/"
   
   - **Razón:** Actualización del framework
   - **Output:** Scripts de migración + correcciones

### `projects/` - Investigaciones de Usuario

**Solicitudes del usuario:**

1. ✅ "Investiga tratamientos con ClO₂ para COVID-19"
   
   - **Razón:** Tema científico externo
   - **Output:** Conocimiento sobre ClO₂/COVID

2. ✅ "Analiza la competencia de extensiones de YouTube"
   
   - **Razón:** Análisis de mercado externo
   - **Output:** Reporte de competencia

3. ✅ "Estudia la virología molecular de SARS-CoV-2"
   
   - **Razón:** Tema científico externo
   - **Output:** Conocimiento virológico

4. ✅ "Compara protocolos CDS de Kalcker vs COMUSAV"
   
   - **Razón:** Comparación de información externa
   - **Output:** Análisis comparativo

5. ✅ "Investiga APIs de YouTube para detección de ads"
   
   - **Razón:** Investigación técnica externa
   - **Output:** Documentación de APIs externas

6. ✅ "Analiza papers sobre inactivación viral con oxidantes"
   
   - **Razón:** Revisión bibliográfica
   - **Output:** Síntesis de papers

---

## CASOS AMBIGUOS - CÓMO DECIDIR

### QUESTION: Caso 1: "Analiza los proyectos de COVID existentes"

**Análisis:**

- ¿Qué se analiza? → Proyectos en `projects/investigaci-n-clo-covid-19-*/`
- ¿Para qué?
  - Si es para **validar estructura v2.2** → `archive/audits/` (mejora framework)
  - Si es para **sintetizar hallazgos de COVID** → `projects/` (tema externo)

**Decisión:** Depende del PROPÓSITO

- "Valida conformidad v2.2 del proyecto COVID" → `archive/audits/`
- "Resume hallazgos de virología del proyecto COVID" → `projects/` (nuevo proyecto de síntesis)

### QUESTION: Caso 2: "Documenta cómo usar ProjectManager"

**Análisis:**

- ¿Qué se documenta? → Uso de `ProjectManager`
- ¿Cuál es el output? → Documentación técnica

**Decisión:** `docs/` (NO es proyecto)

- No va a `archive/audits/` (no es auditoría)
- No va a `projects/` (no es investigación)
- Va a `docs/GUIA_USO_PROJECT_MANAGER.md`

### QUESTION: Caso 3: "Investiga por qué falla el proyecto YouTube"

**Análisis:**

- ¿Qué se investiga? → Fallo en ejecución
- ¿Es el framework o el contenido?
  - Si falla por **bug en ProjectManager** → `archive/audits/`
  - Si falla por **rate limit de agente** → `archive/audits/` (problema sistémico)
  - Si falla por **contenido incorrecto de YouTube** → `projects/` (rehacer investigación)

**Decisión:** Probablemente `archive/audits/` (fallos operacionales = problemas del framework)

---

## ÁRBOL DE DECISIÓN

```
Usuario solicita tarea
 ->
┌─────────────────────────────────────────────┐
│ ¿El framework es el OBJETO de análisis? │
│ (¿Se analiza código/docs/estructura del │
│ framework mismo?) │
└─────────────────────────────────────────────┘
 -> ->
 SÍ NO
 -> ->
 │ │
 │ ┌──────────────────┐
 │ │ ¿Se genera │
 │ │ conocimiento │
 │ │ sobre tema │
 │ │ externo? │
 │ └──────────────────┘
 │ ->
 │ SÍ
 │ ->
 -> ->
┌─────────────────┐ ┌─────────────────┐
│ archive/audits/ │ │ projects/ │
│ │ │ │
│ - Auditorías │ │ - COVID-19 │
│ - Mejoras │ │ - YouTube │
│ - Validaciones │ │ - ClO₂ │
│ - Correcciones │ │ - Virología │
└─────────────────┘ └─────────────────┘
```

---

## PROTOCOLO OPERATIVO

### Cuando el usuario hace una solicitud:

**PASO 1: Identificar el objeto de análisis**

```
"¿Qué voy a analizar principalmente?"
- Código del framework → archive/audits/
- Docs del framework → archive/audits/
- Tema externo → projects/
```

**PASO 2: Identificar el output esperado**

```
"¿Qué se va a generar?"
- Mejoras al framework → archive/audits/
- Conocimiento externo → projects/
```

**PASO 3: Si hay duda, preguntar al usuario**

```
"Para clarificar: ¿quieres que analice el framework mismo
o que use el framework para investigar [tema externo]?"
```

**PASO 4: Crear proyecto en ubicación correcta**

```python
from pathlib import Path
from core.project_manager import ProjectManager

# Para auditorías del framework
pm = ProjectManager(base_dir="archive/audits")

# Para investigaciones de usuario
pm = ProjectManager(base_dir="projects") # default
```

---

## CONVENCIÓN DE NOMBRES

### `archive/audits/` - Nombre del proyecto

**Patrón:**

```
auditor-[tema]-[fecha]
```

**Ejemplos:**

```
auditor-a-framework-v2-2-20251227-222837
auditoria-venv-contaminacion-20260116-103022
validacion-conformidad-v22-20260120-145533
reconstruccion-prompts-enero-20260117-125539
```

### `projects/` - Nombre del proyecto

**Patrón:**

```
[tema-investigacion]-[fecha]
```

**Ejemplos:**

```
investigaci-n-clo-covid-19-20251222-195407
youtube-skip-ads-extension-20260113-200039
sintesis-protocolos-cds-20260118-093022
```

---

## EXCEPCIONES Y CASOS ESPECIALES

### WARNING: Excepción 1: Reportes de Sesión

**¿Dónde van los reportes de auditoría?**

- El PROYECTO va a: `archive/audits/[proyecto-id]/`
- Los REPORTES DE SESIÓN van a: `reports/AUDITORIA_*.md`

**Ejemplo:**

- Proyecto: `archive/audits/auditor-a-framework-v2-2-20251227-222837/`
- Reporte de sesión: `reports/SESION_REPORT_20260102.md`

**Razón:**

- Proyecto = estructura formal con ProjectManager
- Reporte = síntesis del coordinador para el usuario

### WARNING: Excepción 2: Mejoras Menores

**"Arregla este typo en README.md"**

- **NO crear proyecto** en `archive/audits/`
- Hacer corrección directa
- Documentar en commit message

**Razón:** Cambios triviales no requieren proyecto formal

### WARNING: Excepción 3: Documentación Nueva

**"Documenta la arquitectura del framework"**

- **NO crear proyecto**
- Crear directamente en `docs/ARQUITECTURA_*.md`
- Si requiere investigación profunda → `archive/audits/` + output a `docs/`

---

## VALIDACIÓN DE LA DECISIÓN

### ✅ Checklist antes de crear proyecto

Antes de ejecutar `pm.create_project()`:

- [ ] Identifiqué el OBJETO de análisis (framework vs externo)
- [ ] Identifiqué el OUTPUT esperado (mejora framework vs conocimiento)
- [ ] Identifiqué el BENEFICIARIO (framework vs usuario)
- [ ] Decidí ubicación: `archive/audits/` o `projects/`
- [ ] Si hay duda, consulté con el usuario
- [ ] Nombre del proyecto sigue convención correcta

---

## RESUMEN VISUAL

```
┌─────────────────────────────────────────────────────────┐
│ SOLICITUD DEL USUARIO                                   │
└─────────────────────────────────────────────────────────┘
 ->
 ┌────────────────────────────────┐
 │ ¿Qué se va a analizar?         │
 └────────────────────────────────┘
 -> ->
 ┌─────────────┐ ┌──────────────┐
 │ FRAMEWORK   │ │ EXTERNO      │
 │ (código,    │ │ (COVID,      │
 │ docs,       │ │ YouTube,     │
 │ metadata) │ │ papers)        │
 └─────────────┘ └──────────────┘
 -> ->
 ┌─────────────┐ ┌──────────────┐
 │ archive/    │ │ projects/    │
 │ audits/     │ │              │
 └─────────────┘ └──────────────┘
```

---

## EJEMPLOS REALES DEL FRAMEWORK

### ✅ Correctamente ubicados

**`archive/audits/auditor-a-framework-v2-2-20251227-222837/`**

- Solicitud: "Audita el framework v2.2"
- Objeto: Framework
- Output: 42 problemas identificados + plan de corrección
- ✅ CORRECTO

**`projects/investigaci-n-clo-covid-19-20251222-195407/`**

- Solicitud: "Investiga ClO₂ para COVID-19"
- Objeto: ClO₂/COVID (externo)
- Output: Conocimiento sobre tratamiento
- ✅ CORRECTO

### ❌ Incorrectamente ubicados

**`projects/auditor-as-enero-2026-retroactivo-20260117-125539/`**

- Solicitud: "Reconstruye prompts de auditorías"
- Objeto: Auditorías del framework (meta-trabajo)
- Output: Prompts de auditorías pasadas
- ❌ INCORRECTO: Debería estar en `archive/audits/`

---

## CONCLUSIÓN

**Regla de Oro:**

> "Si analizas EL FRAMEWORK → `archive/audits/`
> Si analizas CON EL FRAMEWORK → `projects/`"

**En caso de duda:**

1. Lee este documento
2. Usa el árbol de decisión
3. Aplica los 4 criterios
4. Si aún hay duda, pregunta al usuario

---

**Documento creado:** 2026-01-17
**Mantenido por:** Coordinador Claude
**Estado:** ACTIVO - FUENTE DE VERDAD
**Versión:** 1.0
