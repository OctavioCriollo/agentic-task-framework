# Auditoría Sistémica del Framework v2.2

> ** WARNING: NOTA - MÉTODO LEGACY:**
> Este reporte fue creado antes de establecer el protocolo de ProjectManager (17 de enero de 2026).
> A partir de esa fecha, TODAS las auditorías deben usar proyectos formales en `archive/audits/`.
>
> **Prompts reconstruidos:** `archive/audits/auditor-as-enero-2026-retroactivo-20260117-125539/tasks/auditoria-sistemica-youtube-20260114/`
>
> **Ver protocolo correcto:** `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md` y `CLAUDE.md` sección "Always Use ProjectManager for Audits"

## Sesión: YouTube Ad-Skip Extension Project
**Fecha:** 2026-01-14
**Auditor:** Coordinador Claude
**Criticidad:** ALTA

---

## Resumen Ejecutivo

Durante la ejecución del proyecto YouTube Ad-Skip Extension, se identificaron **5 fallos sistémicos críticos** que comprometen la integridad del framework v2.2 ORGANIZED.

**Impacto:** Los agentes background NO están siguiendo el protocolo establecido, creando:
- Proyectos duplicados fuera de estructura
- Reportes no registrados
- Pérdida de trazabilidad
- Violación del estándar v2.2 ORGANIZED

**Acción Requerida:** Corrección inmediata de protocolos y validaciones.

---

## Problemas Identificados

### P1: Agentes Background Crean Proyectos Duplicados [CRÍTICO]

**Evidencia:**
```
projects/
├── youtube-skip-ads-extension-20260113-200039 ← CORRECTO
├── youtube-skip-ads-extension-20260113-200039-20260113-200511 ← DUPLICADO
└── youtube-skip-ads-extension-20260113-200039-20260113-200432 ← DUPLICADO (eliminado)
```

**Causa Raíz:**
- Agentes background tienen acceso a `ProjectManager`
- Algunos agentes intentaron crear su propio proyecto en lugar de usar el existente
- NO hay validación que prevenga esto

**Protocolo Violado:**
- Solo el COORDINADOR debe crear proyectos
- Agentes solo deben ESCRIBIR en proyectos existentes

**Impacto:**
- Fragmentación de datos
- Confusión sobre cuál es el proyecto correcto
- Pérdida de información (proyecto duplicado eliminado)

**Solución Propuesta:**
1. Modificar prompts de agentes para NO incluir código ProjectManager
2. Los agentes deben recibir RUTAS ABSOLUTAS, no crear proyectos
3. Añadir validación en ProjectManager.create_project() que detecte duplicados

---

### P2: Rutas Relativas en Prompts de Agentes [ALTO]

**Evidencia:**
Prompt enviado a agentes contenía:
```
## Ubicación del Output

Guarda tu reporte en:
`projects/youtube-skip-ads-extension-20260113-200039/tasks/analisis-tecnico/reports/analisis_tecnico_completo.md`
```

**Causa Raíz:**
- Ruta es RELATIVA (asume working directory)
- Agentes background pueden ejecutarse desde diferente working directory
- NO hay garantía de que `projects/` esté en su PWD

**Protocolo Violado:**
- Framework NO especifica cómo dar rutas a agentes
- Falta de estándar para paths

**Impacto:**
- Agentes pueden guardar en ubicación incorrecta
- Archivos "perdidos" en directorios inesperados

**Solución Propuesta:**
1. SIEMPRE usar rutas ABSOLUTAS en prompts
2. Usar `pm.get_task_reports_dir()` que retorna ruta absoluta
3. Documentar en CLAUDE.md: "NEVER use relative paths in agent prompts"

---

### P3: NO Hay Validación de que Agentes Guardaron Correctamente [CRÍTICO]

**Evidencia:**
- Coordinador lanzó 5 agentes
- Agentes alcanzaron rate limit y NO guardaron reportes
- Coordinador NO detectó el fallo
- Coordinador asumió que reportes existían

**Causa Raíz:**
- NO hay callback o verificación post-ejecución de agentes
- Coordinador NO valida que archivos existan después de Task tool
- `pm.register_task_report()` NO fue llamado

**Protocolo Violado:**
- Output Validation (CLAUDE.md línea 117-123) NO se ejecutó
- "ProjectManager validates outputs **before** registering" - NO ocurrió

**Impacto:**
- Pérdida de trabajo de agentes
- Coordinador procede con datos incompletos
- Usuario recibe información parcial

**Solución Propuesta:**
1. Después de cada Task tool, coordinador DEBE verificar:
 ```python
 if not Path(report_path).exists():
 raise OutputNotFoundError(f"Agent failed to create {report_path}")
 ```
2. Usar `pm.register_task_report()` obligatoriamente (lanza excepciones si falla)
3. Añadir paso en protocolo: "6. Validate agent outputs before synthesis"

---

### P4: Coordinador NO Usa register_task_report() [ALTO]

**Evidencia:**
- Coordinador creó 4 reportes manualmente (Write tool)
- NO ejecutó `pm.register_task_report()` para ninguno
- `task_info.json` NO se actualizó con reportes

**Verificación:**
```bash
# task_info.json aún dice "reports": []
cat projects/youtube-skip-ads-extension-20260113-200039/tasks/analisis-tecnico/task_info.json
```

**Causa Raíz:**
- Coordinador olvidó el paso de registro
- NO hay reminder automático en flujo
- CLAUDE.md NO es suficientemente explícito sobre CUÁNDO registrar

**Protocolo Violado:**
- CLAUDE.md línea 109-114: "Register report (validates file exists)"
- Paso 5 del protocolo coordinador (línea 133): NO especifica registro

**Impacto:**
- ProjectManager pierde tracking de outputs
- `pm.get_project_summary()` NO muestra reportes
- Reportes "huérfanos" sin metadata

**Solución Propuesta:**
1. Actualizar protocolo coordinador (CLAUDE.md) paso 5:
 ```
 5. **Synthesize results** from all agent reports
 - First, REGISTER all reports: pm.register_task_report()
 - Then, read and synthesize
 ```
2. Crear helper function: `pm.register_all_reports_in_task()`
3. Añadir validation en síntesis que falle si reports no registrados

---

### P5: Coordinador Eliminó Directorio Sin Verificar Contenido [MEDIO]

**Evidencia:**
- Coordinador vio directorio `youtube-skip-ads-extension-20260113-200039-20260113-200432`
- Ejecutó `rm -rf` inmediatamente sin investigar
- Contenido desconocido (potencialmente perdido)

**Causa Raíz:**
- Protocolo de cleanup NO existe
- NO hay checklist antes de `rm -rf`
- Falta de caution sistemática

**Protocolo Violado:**
- NO hay protocolo de limpieza en CLAUDE.md
- Principio de "verificar antes de destruir" NO documentado

**Impacto:**
- Posible pérdida de datos
- NO reversible (rm -rf es permanente)

**Solución Propuesta:**
1. Añadir a CLAUDE.md sección "Cleanup Protocol":
 ```
 Before deleting ANY directory:
 1. `ls -la <dir>` - List contents
 2. `du -sh <dir>` - Check size
 3. Review files with `cat` or `head`
 4. Confirm with user if unsure
 5. ONLY THEN: rm -rf
 ```
2. Considerar `mv` a `archive/deleted-YYYYMMDD/` en lugar de `rm -rf`
3. Implementar "undo" mechanism (mover a papelera vs eliminar)

---

## Problemas Secundarios (No Críticos)

### P6: NO Hay Logging de Acciones de Agentes

**Impacto:** Difícil debugging post-mortem

**Solución:** Cada agente debe escribir log en `projects/<id>/tasks/<task>/agent.log`

### P7: Proyectos Duplicados NO Detectados Automáticamente

**Impacto:** Contaminación de `projects/`

**Solución:** ProjectManager.create_project() debe buscar duplicados (mismo name + día)

### P8: Scripts Temporales Contaminan Directorio Raíz [ALTO]

**Evidencia:**
```bash
# Directorio raíz contaminado:
ls -la | grep youtube
-rwxr-xr-x 1 ... create_youtube_skip_project.py
-rwxr-xr-x 1 ... setup_youtube_tasks.py
```

**Causa Raíz:**
- Coordinador creó scripts Python específicos del proyecto en directorio raíz
- NO hay protocolo sobre DÓNDE crear archivos temporales
- Confusión entre archivos del framework vs archivos de sesión

**Protocolo Violado:**
- Principio de separación: Framework files vs Project files
- Directorio raíz debe contener solo:
 - `core/` - Framework code
 - `projects/` - User projects
 - `docs/` - Documentation
 - `reports/` - Session reports
 - NO scripts temporales de proyectos individuales

**Impacto:**
- Contaminación del repositorio
- Confusión: ¿qué archivos son del framework vs temporales?
- Git tracking innecesario de archivos desechables
- Dificultad para mantener repositorio limpio

**Ubicación Correcta:**
Estos scripts debieron estar en:
1. **Opción A:** `projects/<project-id>/scripts/` (si se necesitan persistir)
2. **Opción B:** NO crearlos - ejecutar Python directamente:
 ```python
 # En vez de crear create_youtube_skip_project.py, ejecutar inline:
 from core.project_manager import ProjectManager
 pm = ProjectManager()
 project = pm.create_project(...)
 ```
3. **Opción C:** `temp/` o `.temp/` directory (gitignored)

**Solución Propuesta:**
1. Añadir a CLAUDE.md "File Creation Protocol":
 ```markdown
 ## Where to Create Files

 **Framework Code:** core/, docs/, tests/
 **Session Reports:** reports/YYYYMMDD-description.md
 **Project Assets:** projects/<project-id>/
 **Temporary Scripts:** Use Python REPL or .temp/ (gitignored)

 **NEVER create in root:**
 - Project-specific .py files
 - Temporary data files
 - Session-specific scripts
 ```

2. Añadir `.temp/` a .gitignore:
 ```
 # Temporary session files
 .temp/
 temp/
 *_temp.py
 ```

3. Cleanup script para detectar archivos huérfanos en raíz:
 ```python
 # scripts/cleanup_root.py
 def find_orphaned_files():
 """Detecta archivos que no pertenecen al framework en raíz"""
 # Lista de archivos/dirs legítimos
 allowed = {
 'core', 'projects', 'docs', 'reports', 'archive',
 'legacy', 'examples', 'tests', 'schemas',
 '.git', '.claude', '.memory_backups',
 'CLAUDE.md', 'README.md', '.gitignore',
 'requirements.txt', 'setup.sh', 'start_coordinator.sh'
 }
 # Detectar todo lo demás
 ```

---

## Matriz de Criticidad

| ID | Problema | Criticidad | Impacto en Integridad | Solución Complejidad |
|----|----------|------------|----------------------|---------------------|
| P1 | Agentes crean proyectos duplicados | CRÍTICO | ALTA | MEDIA |
| P2 | Rutas relativas en prompts | ALTO | MEDIA | BAJA |
| P3 | NO validación de outputs | CRÍTICO | ALTA | BAJA |
| P4 | NO uso de register_task_report | ALTO | MEDIA | BAJA |
| P5 | Eliminación sin verificar | MEDIO | BAJA | BAJA |
| P6 | Sin logging de agentes | BAJO | BAJA | MEDIA |
| P7 | Duplicados no detectados | MEDIO | MEDIA | MEDIA |
| P8 | Scripts temporales en directorio raíz | ALTO | MEDIA | BAJA |

---

## Correcciones Requeridas (Priorizadas)

### Nivel 1: CRÍTICO (Implementar HOY)

**C1.1: Validación Post-Agent Execution**
```python
# Añadir a core/project_manager.py
def validate_task_outputs(self, project_id: str, task_name: str):
 """
 Valida que todos los reportes esperados existan.
 Lanza OutputNotFoundError si faltan.
 """
 task_info_path = self.base_dir / project_id / "tasks" / task_name / "task_info.json"
 with open(task_info_path) as f:
 task_info = json.load(f)

 reports_dir = self.base_dir / project_id / "tasks" / task_name / "reports"

 # Si reports/ está vacío, FALLO
 if not any(reports_dir.iterdir()):
 raise OutputNotFoundError(
 f"Task {task_name} has NO reports in reports/ directory. "
 f"Agent execution may have failed."
 )
```

**C1.2: Uso Obligatorio de Rutas Absolutas**
```python
# Modificar pm.get_task_reports_dir() para retornar Path absoluto
def get_task_reports_dir(self, project_id: str, task_name: str) -> str:
 task_name_clean = self._sanitize_name(task_name)
 reports_dir = (self.base_dir / project_id / "tasks" / task_name_clean / "reports").resolve()
 reports_dir.mkdir(exist_ok=True)
 return str(reports_dir) # Retorna absolute path
```

**C1.3: Prevenir Agentes de Crear Proyectos**
```
Modificar prompts de agentes:
- NO incluir import ProjectManager
- NO incluir código de creación de proyecto
- SOLO incluir path absoluto donde guardar
```

### Nivel 2: ALTO (Implementar Esta Semana)

**C2.1: Actualizar CLAUDE.md Protocolo Coordinador**
```markdown
## Coordinator Role (Updated)

When operating as coordinator:

1. Design investigations with multi-agent strategies
2. Create prompts using 2-layer architecture
3. **Get absolute paths:** Use pm.get_task_reports_dir() for agent output locations
4. Launch agents using Task tool with run_in_background=True
5. **Monitor completion:** Check TaskOutput for completion status
6. **VALIDATE outputs:** Verify reports exist using pm.validate_task_outputs()
7. **REGISTER reports:** Use pm.register_task_report() for each output
8. Synthesize results from all agent reports
9. Present findings to user in integrated format
```

**C2.2: Helper para Registro Masivo**
```python
def register_all_reports_in_task(self, project_id: str, task_name: str):
 """
 Auto-detecta y registra todos los .md en reports/ de una tarea.
 """
 reports_dir = self.base_dir / project_id / "tasks" / task_name / "reports"

 for report_file in reports_dir.glob("*.md"):
 try:
 self.register_task_report(
 project_id=project_id,
 task_name=task_name,
 report_filename=report_file.name
 )
 except DuplicateReportError:
 pass # Ya registrado, OK
```

### Nivel 3: MEDIO (Mejoras Futuras)

**C3.1: Protocolo de Cleanup**
```markdown
## Cleanup Protocol

Before deleting ANY directory:

1. **Inspect:** `ls -la <dir>` - List all contents
2. **Size check:** `du -sh <dir>` - Verify if significant data
3. **Content review:** `cat` or `head` key files
4. **User confirmation:** If unsure, ASK USER before deleting
5. **Safe delete:** Consider `mv` to `archive/deleted-YYYYMMDD/` instead of `rm -rf`

NEVER use `rm -rf` on:
- projects/* directories (use archive instead)
- Any directory you didn't create in current session
- Directories with unknown origin
```

**C3.2: Detección de Duplicados**
```python
def create_project(self, name: str, ...):
 # Antes de crear, buscar proyectos con mismo name hoy
 today = datetime.now().strftime("%Y%m%d")
 pattern = f"{self._sanitize_name(name)}-{today}*"

 existing = list(self.base_dir.glob(pattern))
 if existing:
 raise ValueError(
 f"Project with name '{name}' already created today: {existing[0].name}\n"
 f"Use existing project or choose different name."
 )

 # ... resto del código
```

---

## Plan de Implementación

### Fase 1: Correcciones Críticas (HOY - 2 horas)

1. ✅ Crear este reporte de auditoría
2. PENDING: Implementar C1.1, C1.2, C1.3 en `core/project_manager.py`
3. PENDING: Actualizar CLAUDE.md con protocolo corregido
4. PENDING: Crear script de validación: `validate_session.py`
5. PENDING: Limpiar proyectos duplicados de esta sesión (con protocolo nuevo)

### Fase 2: Correcciones Altas (Mañana - 1 hora)

6. PENDING: Implementar C2.1, C2.2
7. PENDING: Crear tests de integración para validar correcciones
8. PENDING: Documentar en docs/PROTOCOLS.md

### Fase 3: Mejoras Futuras (Esta Semana)

9. PENDING: Implementar C3.1, C3.2
10. PENDING: Añadir logging de agentes (P6)

---

## Testing de Correcciones

```python
# tests/test_systematic_corrections.py

def test_agent_cannot_create_duplicate_projects():
 """P1: Agentes no pueden crear proyectos duplicados"""
 pm = ProjectManager()
 project1 = pm.create_project(name="test", ...)

 # Intentar crear duplicado debería fallar
 with pytest.raises(ValueError, match="already created today"):
 project2 = pm.create_project(name="test", ...)

def test_absolute_paths_returned():
 """P2: get_task_reports_dir() retorna path absoluto"""
 pm = ProjectManager()
 path = pm.get_task_reports_dir("test-project", "test-task")

 assert Path(path).is_absolute()
 assert "projects" in path # Full path incluye base

def test_validation_detects_missing_reports():
 """P3: validate_task_outputs detecta reportes faltantes"""
 pm = ProjectManager()
 # ... crear proyecto y tarea ...

 # NO crear reportes
 with pytest.raises(OutputNotFoundError, match="has NO reports"):
 pm.validate_task_outputs(project_id, task_name)

def test_register_all_reports():
 """P4: register_all_reports_in_task registra todo"""
 pm = ProjectManager()
 # ... crear reportes en reports/ ...

 pm.register_all_reports_in_task(project_id, task_name)

 task_info = pm.get_task_info(project_id, task_name)
 assert len(task_info['reports']) == 3 # Todos registrados
```

---

## Impacto en Proyectos Existentes

**Proyectos Afectados:**
```bash
ls projects/
# investigacion-clo-covid-19-20251222-195407
# interacciones-clo-in-vivo-...
# youtube-skip-ads-extension-... (×3)
```

**Acción Requerida:**
1. Validar cada proyecto con `framework_validator.py`
2. Registrar reportes huérfanos con `register_all_reports_in_task()`
3. Archivar proyectos duplicados
4. Regenerar project_info.json con reportes completos

---

## Recomendaciones Finales

1. **NUNCA asumir que agentes funcionaron correctamente** - Siempre validar
2. **SIEMPRE usar rutas absolutas** con agentes background
3. **SIEMPRE registrar reportes** con ProjectManager antes de síntesis
4. **NUNCA eliminar sin inspeccionar** - Archivar en lugar de destruir
5. **Documentar protocolos** en CLAUDE.md para coherencia futura

---

**Auditor:** Coordinador Claude
**Fecha:** 2026-01-14 17:30
**Próxima Revisión:** Después de implementar Fase 1
