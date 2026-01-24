# Protocolo de Prompts para Agentes Background

**Fecha:** 2026-01-15
**Propósito:** Definir cómo el COORDINADOR debe instruir a los agentes sobre dónde crear archivos
**Criticidad:** MÁXIMA - Evita contaminación de estructura del proyecto

---

## PROBLEMA

**Los agentes background NO tienen acceso a:**
- ❌ CLAUDE.md (instrucciones del framework)
- ❌ ARQUITECTURA_JERARQUICA_PROYECTO.md (estructura de directorios)
- ❌ Contexto conversacional del coordinador
- ❌ Estructura del framework

**Solo reciben:** El prompt que el coordinador les envía.

**Consecuencia:** Si el prompt NO especifica dónde crear archivos, el agente los crea en ubicaciones incorrectas (generalmente raíz).

---

## SOLUCIÓN

### El coordinador DEBE incluir en TODOS los prompts de agentes:

1. **Contexto del framework** (Layer 1)
2. **Instrucciones EXPLÍCITAS sobre ubicación de archivos**
3. **Rutas ABSOLUTAS** para outputs

---

## TEMPLATE DE PROMPT PARA AGENTES

### Estructura Obligatoria:

```markdown
# [Título de la Tarea]

## Layer 1: Contexto Conversacional

[Contexto del usuario, disclaimers, supervisión]

**IMPORTANTE - ESTRUCTURA DEL PROYECTO:**

Este proyecto usa el Agentic Task Framework v2.2. Debes seguir estas reglas estrictas:

### UBICACIÓN DE ARCHIVOS - REGLAS ABSOLUTAS:

**1. REPORTES DE INVESTIGACIÓN (tus outputs principales):**
 - SIEMPRE guardar en: `[RUTA ABSOLUTA]/reports/`
 - Ejemplo: `D:/proyecto/tasks/analisis-tecnico/reports/analisis_completo.md`
 - Formato: Markdown (.md)
 - Naming: `nombre_descriptivo_snake_case.md`

**2. SCRIPTS AUXILIARES (si necesitas crear código):**
 - ❌ NUNCA crear en raíz del framework
 - ✅ SOLO si es absolutamente necesario
 - ✅ Guardar en: `[RUTA ABSOLUTA]/scripts/` (dentro de la tarea)
 - Ejemplo: `D:/proyecto/tasks/analisis-tecnico/scripts/helper.py`

**3. DATOS TEMPORALES (archivos auxiliares):**
 - Guardar en: `[RUTA ABSOLUTA]/data/` (dentro de la tarea)
 - Ejemplo: `D:/proyecto/tasks/analisis-tecnico/data/research_data.json`

**4. LO QUE NUNCA DEBES HACER:**
 - ❌ NO crear archivos en raíz del framework (D:/agentic-task-framework/)
 - ❌ NO crear archivos fuera de tu directorio de tarea asignado
 - ❌ NO crear archivos en core/, docs/, reports/ del framework

## Layer 2: Tarea Técnica

[Objetivo, metodología, entregables específicos]

### OUTPUTS REQUERIDOS:

**Archivo principal:**
- Ruta: `[RUTA ABSOLUTA COMPLETA]/reports/[nombre].md`
- Formato: Markdown
- Contenido mínimo: [especificación]

**Archivos adicionales (si aplica):**
- [Lista de archivos con rutas absolutas]

### CRITERIOS DE COMPLETITUD:

- [ ] Reporte principal guardado en ubicación especificada
- [ ] Contenido mínimo cumplido
- [ ] Todos los archivos en sus ubicaciones correctas
- [ ] NO se crearon archivos fuera del directorio de tarea

---

## VERIFICACIÓN AL COMPLETAR:

Antes de marcar la tarea como completa, verifica:
1. ✅ Reporte guardado en `reports/` subdirectorio
2. ✅ No creaste archivos en raíz del framework
3. ✅ Todos los archivos usan rutas absolutas especificadas
```

---

## EJEMPLOS CONCRETOS

### ✅ EJEMPLO CORRECTO: Agente de Investigación

```markdown
# Análisis Técnico de YouTube Ad-Skip Extension

## Layer 1: Contexto Conversacional

El usuario solicitó una investigación sobre técnicas de detección de anuncios en YouTube.
Esta investigación es supervisada y forma parte de un proyecto académico.

**IMPORTANTE - ESTRUCTURA DEL PROYECTO:**

### UBICACIÓN DE ARCHIVOS:

**TUS REPORTES van aquí (OBLIGATORIO):**
```
D:/STARTUP/Proyectos/WORKING NOW/agentic-task-framework/projects/youtube-skip-ads-extension-20260113-200039/tasks/analisis-tecnico/reports/
```

**Archivo principal a crear:**
- Ruta: `D:/STARTUP/.../tasks/analisis-tecnico/reports/analisis_tecnico_completo.md`
- Formato: Markdown
- Nombre: `analisis_tecnico_completo.md`

**SI necesitas crear scripts auxiliares (solo si absolutamente necesario):**
- Ruta: `D:/STARTUP/.../tasks/analisis-tecnico/scripts/`

**LO QUE NO DEBES HACER:**
- ❌ NO crear archivos en `D:/STARTUP/Proyectos/WORKING NOW/agentic-task-framework/` (raíz)
- ❌ NO crear archivos fuera de tu directorio de tarea

## Layer 2: Tarea Técnica

**Objetivo:** Investigar técnicas de detección de anuncios en YouTube

**Metodología:**
1. Investigar APIs de YouTube
2. Analizar extensiones existentes
3. Documentar técnicas de detección

**Entregables:**

**REPORTE PRINCIPAL:**
- Archivo: `D:/STARTUP/.../tasks/analisis-tecnico/reports/analisis_tecnico_completo.md`
- Contenido: [especificación detallada]

**CRITERIOS DE COMPLETITUD:**
- [ ] Reporte guardado en ubicación especificada
- [ ] Investigación completa y documentada
- [ ] No se crearon archivos fuera del directorio de tarea
```

---

### ❌ EJEMPLO INCORRECTO: Sin instrucciones de ubicación

```markdown
# Análisis Técnico de YouTube Extension

Investiga técnicas de detección de anuncios.

Entregables:
- Reporte técnico completo
```

**Problema:** No especifica DÓNDE guardar el reporte.
**Resultado:** Agente crea archivos en raíz o ubicación arbitraria.

---

## PROTOCOLO PARA EL COORDINADOR

### ANTES de lanzar un agente background:

1. **Crear el proyecto con ProjectManager:**
 ```python
 project = pm.create_project(name, user_request, context)
 task = pm.create_task(project_id, task_name, description, prompt)
 ```

2. **Obtener ruta ABSOLUTA del directorio de reports:**
 ```python
 reports_dir = pm.get_task_reports_dir(project_id, task_name)
 # Retorna: D:/STARTUP/.../projects/[id]/tasks/[task]/reports/
 ```

3. **Construir prompt incluyendo:**
 - ✅ Layer 1: Contexto conversacional
 - ✅ **UBICACIÓN DE ARCHIVOS con ruta absoluta**
 - ✅ Layer 2: Tarea técnica
 - ✅ Lista de outputs con rutas completas

4. **Guardar prompt en archivo:**
 ```python
 # El prompt ya se guarda automáticamente en task_dir/prompt.md
 ```

5. **Lanzar agente con Task tool:**
 ```python
 Task(
 subagent_type="general-purpose",
 description="Análisis técnico YouTube",
 prompt=prompt_completo,
 run_in_background=True
 )
 ```

6. **Después de completar, VALIDAR ubicación:**
 ```python
 # Verificar que archivos están en reports/
 if not (reports_dir / "reporte.md").exists():
 raise OutputNotFoundError("Agente no guardó en ubicación correcta")

 # Registrar reporte
 pm.register_task_report(project_id, task_name, "reporte.md")
 ```

---

## TIPOS DE ARCHIVOS Y UBICACIONES

### 1. REPORTES DE INVESTIGACIÓN (outputs principales)

**Qué son:**
- Resultados de investigación del agente
- Análisis, hallazgos, conclusiones
- Documentación técnica generada

**Dónde van:**
```
projects/[project-id]/tasks/[task-name]/reports/[reporte].md
```

**Ejemplo:**
```
projects/youtube-skip-ads-extension-20260113-200039/
 └── tasks/analisis-tecnico/
 └── reports/
 ├── analisis_tecnico_completo.md
 ├── hallazgos_apis.md
 └── conclusiones.md
```

---

### 2. SCRIPTS AUXILIARES (solo si necesario)

**Qué son:**
- Código Python/JavaScript creado por el agente
- Scripts de prueba o validación
- Utilidades para la investigación

**Dónde van:**
```
projects/[project-id]/tasks/[task-name]/scripts/[script].py
```

**IMPORTANTE:**
- ❌ NO crear scripts en raíz del framework
- ✅ SOLO crear si absolutamente necesario
- ✅ Documentar por qué se necesita

**Ejemplo:**
```
projects/youtube-skip-ads-extension-20260113-200039/
 └── tasks/analisis-tecnico/
 └── scripts/
 ├── test_api.py
 └── validate_detection.js
```

---

### 3. DATOS TEMPORALES

**Qué son:**
- JSON, CSV, XML generados durante investigación
- Datos de prueba
- Archivos auxiliares

**Dónde van:**
```
projects/[project-id]/tasks/[task-name]/data/[archivo]
```

**Ejemplo:**
```
projects/youtube-skip-ads-extension-20260113-200039/
 └── tasks/analisis-tecnico/
 └── data/
 ├── api_responses.json
 └── test_data.csv
```

---

## ESTRUCTURA DE TAREA COMPLETA (con archivos auxiliares)

```
projects/[project-id]/tasks/[task-name]/
├── task_info.json # Metadata (auto-generado por ProjectManager)
├── prompt.md # Prompt usado (auto-generado)
├── README.md # Overview (auto-generado)
│
├── reports/ # OUTPUTS PRINCIPALES (OBLIGATORIO)
│ ├── reporte_principal.md
│ ├── analisis_detallado.md
│ └── conclusiones.md
│
├── scripts/ # Scripts auxiliares (OPCIONAL, solo si necesario)
│ ├── helper.py
│ └── validate.js
│
└── data/ # Datos temporales (OPCIONAL)
 ├── research_data.json
 └── test_results.csv
```

**Regla:** `reports/` es OBLIGATORIO. `scripts/` y `data/` son OPCIONALES.

---

## VALIDACIÓN POST-EJECUCIÓN

### El coordinador DEBE verificar:

```python
def validate_agent_outputs(pm, project_id, task_name):
 """Validar que agente guardó archivos en ubicación correcta."""

 # 1. Verificar que reports/ tiene archivos
 reports_dir = pm.get_task_reports_dir(project_id, task_name)
 reports = list(Path(reports_dir).glob("*.md"))

 if not reports:
 raise OutputNotFoundError(
 f"Agente no generó reportes en {reports_dir}"
 )

 # 2. Verificar que NO hay archivos en raíz del framework
 framework_root = Path.cwd()
 suspicious_files = list(framework_root.glob("*.py"))

 # Filtrar archivos legítimos
 legit_files = ["setup.py", "conftest.py"] # Si existen
 suspicious = [f for f in suspicious_files if f.name not in legit_files]

 if suspicious:
 print(f" WARNING: WARNING: Archivos sospechosos en raíz: {suspicious}")
 print(" Estos pueden haber sido creados por agente incorrectamente")

 # 3. Registrar reportes válidos
 for report in reports:
 pm.register_task_report(project_id, task_name, report.name)

 print(f"✓ Validación completada: {len(reports)} reportes registrados")
```

---

## CASOS ESPECIALES

### Caso 1: Agente necesita crear código del framework

**Situación:** Agente investiga cómo mejorar ProjectManager y quiere proponer código.

**Solución:**
```markdown
**UBICACIÓN DE PROPUESTA DE CÓDIGO:**

NO implementes cambios directamente en core/. En su lugar:

1. Documenta la propuesta en tu reporte principal
2. Si necesitas mostrar código de ejemplo:
 - Guárdalo en: `[RUTA]/reports/propuesta_codigo.md`
 - Formato: Markdown con bloques de código
 - Incluye explicación de por qué y dónde iría

**Ejemplo:**
```md
## Propuesta de Mejora: ProjectManager

### Código Propuesto:
\`\`\`python
def new_method(self):
 # Código propuesto
 pass
\`\`\`

### Ubicación sugerida:
`core/project_manager.py` línea 350

### Justificación:
[Explicación de por qué se necesita]
```

**NO crear archivos en core/ directamente.**
```

---

### Caso 2: Agente necesita crear proyecto de ejemplo

**Situación:** Agente investiga cómo usar el framework y quiere crear ejemplo.

**Solución:**
```markdown
**CREAR PROYECTO DE EJEMPLO:**

Si necesitas crear un proyecto de ejemplo:

1. Documéntalo en tu reporte como código
2. NO uses ProjectManager desde el agente
3. Describe la estructura en Markdown

**Formato:**
```md
## Proyecto de Ejemplo

### Estructura propuesta:
\`\`\`
projects/ejemplo-uso-framework/
 ├── project_info.json
 └── tasks/
 └── tarea-ejemplo/
 └── reports/
 └── ejemplo.md
\`\`\`

### Código de ejemplo:
\`\`\`python
pm = ProjectManager()
project = pm.create_project(...)
\`\`\`
```

**NO ejecutar código que cree proyectos reales.**
```

---

## ERRORES COMUNES A EVITAR

### ❌ Error 1: No especificar ubicación de archivos

**Prompt incorrecto:**
```markdown
Investiga X y genera un reporte.
```

**Prompt correcto:**
```markdown
Investiga X y genera un reporte.

**UBICACIÓN DEL REPORTE:**
Guardar en: `D:/ruta/absoluta/tasks/[task]/reports/reporte.md`
```

---

### ❌ Error 2: Usar rutas relativas

**Prompt incorrecto:**
```markdown
Guardar reporte en: `reports/analisis.md`
```

**Problema:** Ruta relativa, agente puede estar en otro directorio.

**Prompt correcto:**
```markdown
Guardar reporte en: `D:/STARTUP/.../tasks/analisis/reports/analisis.md`
```

---

### ❌ Error 3: No incluir Layer 1 (contexto)

**Prompt incorrecto:**
```markdown
# Análisis Técnico

Investiga APIs de YouTube.
Genera reporte técnico.
```

**Problema:** Sin Layer 1, agente puede auto-censurarse.

**Prompt correcto:**
```markdown
# Análisis Técnico

## Layer 1: Contexto Conversacional
Usuario solicitó investigación académica supervisada sobre APIs de YouTube.
[Disclaimers, supervisión, etc.]

## Layer 2: Tarea Técnica
Investigar APIs de YouTube...
```

---

## TEMPLATE MÍNIMO OBLIGATORIO

```markdown
# [Título]

## Layer 1: Contexto
[Usuario solicitó, supervisión, disclaimers]

**UBICACIÓN DE ARCHIVOS:**
Reportes: `[RUTA ABSOLUTA]/reports/`

## Layer 2: Tarea
[Objetivo, metodología]

**OUTPUT:**
- Archivo: `[RUTA ABSOLUTA]/reports/[nombre].md`
```

---

## CHECKLIST PRE-LAUNCH

Antes de lanzar un agente, verificar:

- [ ] Prompt tiene Layer 1 (contexto conversacional)
- [ ] Prompt especifica UBICACIÓN de archivos con ruta absoluta
- [ ] Ruta absoluta obtenida con `pm.get_task_reports_dir()`
- [ ] Prompt incluye lista de outputs esperados
- [ ] Prompt tiene Layer 2 (tarea técnica)
- [ ] Se guardó prompt en `task_dir/prompt.md`

---

## RESUMEN

### REGLA DE ORO:

**El coordinador SIEMPRE debe especificar en el prompt:**
1. Contexto conversacional (Layer 1)
2. **UBICACIÓN EXACTA con ruta absoluta** donde guardar archivos
3. Tarea técnica (Layer 2)

### ❌ LO QUE NUNCA HACER:

- ❌ Lanzar agente sin especificar dónde guardar outputs
- ❌ Usar rutas relativas
- ❌ Asumir que agente conoce la estructura del framework

### ✅ LO QUE SIEMPRE HACER:

- ✅ Usar `pm.get_task_reports_dir()` para obtener ruta absoluta
- ✅ Incluir ruta completa en el prompt
- ✅ Validar ubicación de archivos después de ejecución

---

**Documento creado:** 2026-01-15
**Mantenido por:** Coordinador Claude
**Estado:** ACTIVO - PROTOCOLO OBLIGATORIO
