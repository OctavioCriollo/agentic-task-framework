# Correcciones Pendientes - Framework v2.2

**Fecha:** 2026-01-15
**Estado:** DOCUMENTACIÓN DE PENDIENTES
**Correcciones Aplicadas:** 8/28 (Fase 1 + Fase 2 completadas)
**Correcciones Pendientes:** 20 (Fase 3 + Fase 4 no implementadas)

---

## RESUMEN EJECUTIVO

Este documento lista todas las correcciones que **NO han sido aplicadas** pero fueron identificadas en el análisis exhaustivo del framework.

**Estado del Framework:**
- ✅ Fase 1 (CRÍTICAS): 3/3 completadas
- ✅ Fase 2 (ALTAS): 5/5 completadas
- ⏸️ Fase 3 (MEDIAS): 0/4 pendientes
- ⏸️ Fase 4 (BAJAS): 0/4 pendientes

**Framework actualmente:** ROBUSTO y operacional para uso en producción

---

## FASE 3: CORRECCIONES MEDIAS (Pendientes)

**Estimado total:** 24-30 horas
**Prioridad:** Media
**Estado:** NO IMPLEMENTADAS

### M1: Implementar Test Suite Básico ⏸️

**Estado:** PENDIENTE
**Prioridad:** ALTA (aunque categorizada como Media)
**Estimado:** 8-12 horas
**Riesgo:** BAJO

**Descripción:**
Crear tests automatizados para componentes core del framework.

**Tests prioritarios:**

1. **test_project_manager.py**
 - `test_create_project()` - Verifica creación de estructura
 - `test_create_task()` - Verifica creación de tareas con v2.2 ORGANIZED
 - `test_register_task_report_validates()` - Verifica validaciones (OutputNotFoundError, etc.)
 - `test_update_task_status()` - Verifica cambios de estado
 - `test_get_task_report_path()` - Verifica que retorna reports/ subdirectory

2. **test_framework_validator.py**
 - `test_validate_task_naming()` - Verifica naming conventions (kebab-case)
 - `test_validate_prompt_architecture()` - Verifica 2-layer prompt structure
 - `test_validate_project_structure()` - Verifica conformidad v2.2

3. **test_integration.py**
 - `test_full_workflow()` - Workflow completo: crear proyecto → tarea → registrar reporte → synthesis
 - `test_error_handling()` - Verifica custom exceptions funcionan

**Framework de testing:** pytest

**Coverage objetivo:** 60% de `core/`

**Impacto:**
- ✅ Previene regresiones futuras
- ✅ Refactoring seguro
- ✅ Documentación ejecutable (tests como ejemplos)
- ✅ Confianza para cambios

**Pre-requisitos:**
```bash
pip install pytest pytest-cov
```

**Comandos:**
```bash
# Ejecutar tests
pytest tests/ -v

# Con coverage
pytest tests/ --cov=core --cov-report=html
```

**Estructura propuesta:**
```
tests/
├── __init__.py
├── test_project_manager.py
├── test_framework_validator.py
├── test_integration.py
└── fixtures/
 ├── sample_project.json
 └── sample_prompt.md
```

---

### M2: Remover Backward Compatibility ⏸️

**Estado:** PENDIENTE
**Prioridad:** MEDIA
**Estimado:** 4-6 horas
**Riesgo:** ALTO (rompe proyectos legacy si no se migran antes)

**Descripción:**
Eliminar soporte para reportes en ubicación legacy (root de tarea).

**IMPORTANTE:** NO confundir con `reports/` de raíz del framework.

**Qué es "backward compatibility":**

Actualmente `register_task_report()` acepta reportes en DOS ubicaciones:
1. ✅ `projects/[id]/tasks/[task]/reports/reporte.md` (v2.2 ORGANIZED)
2. ❌ `projects/[id]/tasks/[task]/reporte.md` (legacy v1.0)

**Código actual (con backward compatibility):**
```python
# project_manager.py líneas 345-367
report_path_v22 = task_dir / "reports" / report_filename
report_path_legacy = task_dir / report_filename

if report_path_v22.exists():
 report_path = report_path_v22
elif report_path_legacy.exists(): # ← Backward compatibility
 report_path = report_path_legacy
 print("WARNING: legacy structure")
else:
 raise OutputNotFoundError(...)
```

**Código propuesto (solo v2.2):**
```python
# Simplificado - solo v2.2
report_path = task_dir / "reports" / report_filename
if not report_path.exists():
 raise OutputNotFoundError(f"Report not found: {report_path}")
```

**PRE-REQUISITO CRÍTICO:**

**ANTES de M2, ejecutar A4 (migrate_v10_to_v22.py)** para mover todos los reportes legacy a `reports/`.

**Proyectos afectados actualmente:**
- `investigaci-n-clo-covid-19-20251222-195407` - Tiene reportes MIXED (root + reports/)

**Pasos para implementar M2:**

1. **PRIMERO:** Ejecutar migration script en TODOS los proyectos existentes
 ```bash
 python core/migrate_v10_to_v22.py projects/investigaci-n-clo-covid-19-20251222-195407
 ```

2. **SEGUNDO:** Verificar que NO quedan reportes en root de tareas
 ```bash
 python core/check_empty_reports.py [project-id]
 ```

3. **TERCERO:** Aplicar M2 (eliminar código backward compatible)

**Impacto:**
- ✅ Código más simple y mantenible
- ✅ Elimina warnings de "legacy structure"
- ✅ Fuerza conformidad v2.2 ORGANIZED
- WARNING: Proyectos legacy no migrados dejarán de funcionar

**Archivos a modificar:**
- `core/project_manager.py` - `register_task_report()` líneas 345-367

---

### M3: Sincronizar Documentación ⏸️

**Estado:** PENDIENTE
**Prioridad:** MEDIA
**Estimado:** 8-10 horas
**Riesgo:** BAJO

**Descripción:**
Eliminar inconsistencias entre documentos y establecer fuente de verdad única.

**Archivos afectados:**
- `CLAUDE.md` (266 líneas)
- `README.md` (502 líneas)
- `docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md` (274 líneas)
- `docs/CHECKLIST.md` (243 líneas)

**Inconsistencias identificadas:**

1. **Comandos Python inconsistentes**
 - README.md usa: `py -3 core/project_manager.py`
 - CLAUDE.md usa: `python core/framework_validator.py`
 - **Solución:** Estandarizar a `python` (funciona con venv activado)

2. **API signatures difieren**
 - CLAUDE.md L111 muestra `register_task_report(project_id, task_name, report_filename)`
 - Código real en project_manager.py L320 tiene parámetros adicionales de validación
 - **Solución:** Actualizar ejemplos en docs

3. **Estructura de proyecto en CLAUDE.md no muestra README.md**
 - CLAUDE.md L34-44 no menciona README.md auto-generado
 - **Solución:** Agregar README.md a la estructura visual

4. **Naming conventions no explicadas**
 - README.md L282-286 menciona kebab-case y snake_case pero no explica cuándo usar cada uno
 - **Solución:** Tabla de decisión clara

5. **Templates difieren**
 - ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md tiene template de README.md
 - project_manager.py `_generate_task_readme()` genera diferente formato
 - **Solución:** Sincronizar templates

**Propuesta: Establecer Source of Truth**

**README.md** = Fuente de verdad principal
- Documentación de usuario
- Ejemplos validados contra código real
- Changelog actualizado

**CLAUDE.md** = Subconjunto de README.md
- Instrucciones específicas para Claude Code
- Referencias a README.md para detalles

**docs/** = Documentación técnica detallada
- Especificaciones (ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md)
- Protocolos (PROTOCOLO_PROMPTS_AGENTES.md)
- Arquitectura (ARQUITECTURA_JERARQUICA_PROYECTO.md)

**Tareas específicas:**

1. ✅ Actualizar ejemplos de código en README.md y CLAUDE.md
2. ✅ Unificar comandos Python a `python`
3. ✅ Sincronizar estructuras de proyecto visuales
4. ✅ Crear tabla de naming conventions
5. ✅ Validar que ejemplos funcionan (copiar/pegar y ejecutar)
6. ✅ Actualizar fecha de changelog (actualmente dice fecha incorrecta)

**Impacto:**
- ✅ Documentación confiable
- ✅ Menos confusión para usuarios
- ✅ Ejemplos que realmente funcionan
- ✅ Onboarding más fácil

---

### M4: Agregar Logging Estructurado ⏸️

**Estado:** PENDIENTE
**Prioridad:** MEDIA
**Estimado:** 4-6 horas
**Riesgo:** BAJO

**Descripción:**
Reemplazar `print()` statements con logging module de Python para mejor debugging y producción.

**Problema actual:**

Código usa `print()` para todo:
```python
print("✓ Project created")
print(f"WARNING: Report in legacy location: {path}")
print(f"ERROR: Validation failed")
```

**Problemas:**
- No hay niveles de severidad
- No hay timestamps
- No hay filtering (todo o nada)
- No hay configuración por módulo
- No hay logs en archivo

**Solución propuesta:**

Usar logging estándar de Python:

```python
import logging

logger = logging.getLogger(__name__)

# En vez de print()
logger.info("Project created: %s", project_id)
logger.warning("Report in legacy location: %s", report_path)
logger.error("Validation failed: %s", error_message)
logger.debug("Task info loaded: %s", task_info)
```

**Configuración en project_manager.py:**

```python
# Al inicio del módulo
import logging

# Configurar logger
logging.basicConfig(
 level=logging.INFO,
 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 handlers=[
 logging.FileHandler('framework.log'),
 logging.StreamHandler()
 ]
)

logger = logging.getLogger(__name__)
```

**Beneficios:**

- ✅ Logs con timestamps automáticos
- ✅ Filtrado por nivel (DEBUG, INFO, WARNING, ERROR)
- ✅ Logs a archivo para debugging
- ✅ Configuración externa (sin cambiar código)
- ✅ Logs por módulo (core.project_manager vs core.validator)

**Niveles recomendados:**

- `DEBUG`: Detalles internos (valores de variables, flujo)
- `INFO`: Operaciones normales (proyecto creado, tarea registrada)
- `WARNING`: Anomalías no críticas (legacy structure, missing optional fields)
- `ERROR`: Errores que impiden operación (validation failed, file not found)

**Archivos a modificar:**
- `core/project_manager.py` - Reemplazar ~30 print() statements
- `core/framework_validator.py` - Reemplazar ~15 print() statements
- Utility scripts - Reemplazar print() con logging

**Configuración de usuario:**

```python
# Para debugging detallado
logging.getLogger('core').setLevel(logging.DEBUG)

# Para silencioso (solo errores)
logging.getLogger('core').setLevel(logging.ERROR)
```

**Impacto:**
- ✅ Debugging mucho más fácil
- ✅ Producción-ready
- ✅ Análisis de problemas post-mortem (logs en archivo)
- ✅ Configuración flexible sin cambiar código

---

## FASE 4: CORRECCIONES BAJAS (Pendientes)

**Estimado total:** 40+ horas
**Prioridad:** Baja (nice to have)
**Estado:** NO IMPLEMENTADAS

### L1: Refactorizar ProjectManager ⏸️

**Estado:** PENDIENTE
**Prioridad:** BAJA
**Estimado:** 12-16 horas
**Riesgo:** MEDIO (refactoring grande)

**Descripción:**
Separar ProjectManager monolítico en módulos con responsabilidades únicas.

**Problema actual:**

`core/project_manager.py` tiene 625 líneas con múltiples responsabilidades:
- Gestión de proyectos
- Gestión de tareas
- Validación
- Serialización JSON
- Custom exceptions
- CLI (implícito)

**Propuesta de estructura:**

```
core/
├── project_manager.py # Solo ProjectManager class
│ - create_project()
│ - create_task()
│ - get_project_info()
│
├── validators.py # Validaciones y exceptions
│ - OutputNotFoundError
│ - InvalidOutputError
│ - DuplicateReportError
│ - ValidationError
│
├── serializers.py # JSON read/write
│ - load_project_info()
│ - save_project_info()
│ - load_task_info()
│ - save_task_info()
│
└── cli.py # CLI commands
 - main()
 - create_project_cli()
 - list_projects_cli()
```

**Beneficios:**
- ✅ Separation of concerns
- ✅ Módulos más pequeños y testeables
- ✅ Reutilización de componentes
- ✅ Imports más claros

**Impacto:**
- WARNING: Cambios en imports en otros archivos
- WARNING: Tests deben actualizarse
- ✅ Código más mantenible a largo plazo

**Riesgo:** MEDIO - Refactoring grande puede introducir bugs

---

### L2: Implementar Repository Pattern ⏸️

**Estado:** PENDIENTE
**Prioridad:** BAJA
**Estimado:** 16-20 horas
**Riesgo:** ALTO (cambio arquitectónico)

**Descripción:**
Abstraer acceso a filesystem usando Repository pattern para mejor testabilidad.

**Problema actual:**

ProjectManager accede directamente a filesystem:
```python
project_dir = self.base_dir / project_id
project_info_path = project_dir / "project_info.json"
with open(project_info_path, 'r') as f:
 project_info = json.load(f)
```

**Dificulta testing:**
- Requiere filesystem real
- Necesita setup/cleanup de directorios
- Tests lentos (I/O real)

**Solución: Repository Pattern**

```python
class ProjectRepository:
 """Abstract data access layer."""

 def save_project(self, project: Project) -> None:
 """Save project to storage."""
 raise NotImplementedError

 def load_project(self, project_id: str) -> Project:
 """Load project from storage."""
 raise NotImplementedError

 def delete_project(self, project_id: str) -> None:
 """Delete project from storage."""
 raise NotImplementedError

 def list_projects(self, filters: dict = None) -> List[Project]:
 """List projects with optional filters."""
 raise NotImplementedError


class FileSystemRepository(ProjectRepository):
 """Implementation using filesystem."""

 def __init__(self, base_dir: Path):
 self.base_dir = base_dir

 def save_project(self, project: Project) -> None:
 # Implementation with actual file I/O
 pass


class InMemoryRepository(ProjectRepository):
 """Implementation for testing (no filesystem)."""

 def __init__(self):
 self.projects = {}

 def save_project(self, project: Project) -> None:
 self.projects[project.id] = project
```

**Uso en ProjectManager:**

```python
class ProjectManager:
 def __init__(self, repository: ProjectRepository):
 self.repo = repository

 def create_project(self, name, user_request):
 project = Project(...)
 self.repo.save_project(project)
 return project
```

**Beneficios:**
- ✅ Testing sin filesystem (InMemoryRepository)
- ✅ Tests 10x más rápidos
- ✅ Posibilidad de backends alternativos (database, cloud)
- ✅ Abstraction limpia

**Impacto:**
- WARNING: Cambio arquitectónico significativo
- WARNING: Todos los tests deben reescribirse
- WARNING: API de ProjectManager cambia (constructor diferente)

**Riesgo:** ALTO - Cambio arquitectónico complejo

---

### L3: GitHub Actions CI/CD ⏸️

**Estado:** PENDIENTE
**Prioridad:** BAJA
**Estimado:** 6-8 horas
**Riesgo:** BAJO

**Descripción:**
Configurar GitHub Actions para tests automáticos, linting y type checking en cada commit.

**Pre-requisito:** M1 (tests) debe estar implementado

**Workflow propuesto:**

`.github/workflows/ci.yml`:
```yaml
name: CI

on: [push, pull_request]

jobs:
 test:
 runs-on: ubuntu-latest

 steps:
 - uses: actions/checkout@v3

 - name: Set up Python
 uses: actions/setup-python@v4
 with:
 python-version: '3.11'

 - name: Install dependencies
 run: |
 pip install -r requirements.txt
 pip install pytest pytest-cov ruff mypy

 - name: Run tests
 run: pytest tests/ -v --cov=core --cov-report=xml

 - name: Lint with ruff
 run: ruff check core/ tests/

 - name: Type check with mypy
 run: mypy core/

 - name: Upload coverage
 uses: codecov/codecov-action@v3
 with:
 file: ./coverage.xml
```

**Quality gates configurados:**

1. **Tests**: Deben pasar todos los tests
2. **Linting**: Código debe cumplir estándares (ruff)
3. **Type checking**: Type hints deben ser correctos (mypy)
4. **Coverage**: Coverage no debe bajar de umbral (ej: 60%)

**Beneficios:**
- ✅ Validación automática en cada commit
- ✅ No merge si tests fallan
- ✅ Código limpio forzado
- ✅ Coverage tracking

**Impacto:**
- ✅ Calidad de código asegurada
- ✅ Menos bugs en producción
- ✅ Refactoring seguro

**Riesgo:** BAJO - No afecta código existente

---

### L4: Project Templates System ⏸️

**Estado:** PENDIENTE
**Prioridad:** BAJA
**Estimado:** 8-12 horas
**Riesgo:** BAJO

**Descripción:**
Sistema de templates para crear proyectos predefinidos con tareas estándar.

**Problema actual:**

Crear proyectos multi-agente requiere:
1. Crear proyecto
2. Crear múltiples tareas manualmente
3. Configurar cada tarea individualmente
4. Repetitivo para proyectos similares

**Solución: Templates**

```python
# core/templates.py

TEMPLATES = {
 "research_multi_agent": {
 "description": "Research project with multiple specialized agents",
 "tasks": [
 {
 "name": "technical-analysis",
 "description": "Technical analysis component",
 "prompt_template": "..."
 },
 {
 "name": "market-research",
 "description": "Market research component",
 "prompt_template": "..."
 },
 {
 "name": "competitive-analysis",
 "description": "Competitive analysis component",
 "prompt_template": "..."
 }
 ]
 },

 "single_deep_dive": {
 "description": "Single agent deep investigation",
 "tasks": [
 {
 "name": "deep-investigation",
 "description": "Comprehensive deep dive",
 "prompt_template": "..."
 }
 ]
 }
}
```

**API propuesta:**

```python
# Crear proyecto desde template
pm = ProjectManager()
project = pm.create_from_template(
 template_name="research_multi_agent",
 project_name="AI Market Analysis",
 user_request="Analyze AI market landscape",
 context="Competitive analysis for startup"
)

# Template crea automáticamente:
# - Proyecto con metadata
# - 3 tareas pre-configuradas
# - Prompts con placeholders rellenados
```

**Templates incluidos:**

1. **research_multi_agent**: 3-5 agentes especializados
2. **single_deep_dive**: 1 agente investigación profunda
3. **code_analysis**: Análisis de codebase
4. **market_research**: Investigación de mercado
5. **technical_spec**: Especificación técnica

**Beneficios:**
- ✅ Setup instantáneo
- ✅ Best practices incorporadas
- ✅ Prompts pre-validados
- ✅ Menos errores de configuración

**Impacto:**
- ✅ Productividad aumentada
- ✅ Consistencia en proyectos
- ✅ Onboarding más fácil

**Riesgo:** BAJO - Funcionalidad adicional, no rompe existente

---

## RESUMEN DE PENDIENTES

### Por Fase

| Fase | Items | Estimado | Riesgo | Prioridad Real |
|------|-------|----------|--------|----------------|
| Fase 3 | 4 | 24-30h | BAJO-ALTO | **M1 es ALTA** |
| Fase 4 | 4 | 40+h | BAJO-ALTO | Nice to have |

### Por Prioridad Real (Re-evaluado)

**ALTA (hacer pronto):**
- M1: Tests básicos - CRÍTICO para refactoring seguro
- M3: Sincronizar docs - IMPORTANTE para evitar confusión

**MEDIA (hacer eventualmente):**
- M4: Logging - Mejora debugging
- M2: Remover backward compatibility - Simplifica código

**BAJA (nice to have):**
- L1, L2, L3, L4 - Mejoras arquitectónicas

### Recomendación de Implementación

**Opción A: Solo M1 (Mínimo recomendado)**
- Implementar tests básicos
- Estimado: 8-12 horas
- Protege contra regresiones futuras

**Opción B: M1 + M3 (Recomendado)**
- Tests + Documentación sincronizada
- Estimado: 16-22 horas
- Framework production-ready con docs confiables

**Opción C: Fase 3 completa**
- M1 + M2 + M3 + M4
- Estimado: 24-30 horas
- Framework completamente robusto

**Opción D: Usar framework como está**
- No implementar pendientes ahora
- Framework es FUNCIONAL y ROBUSTO
- Implementar pendientes cuando sea necesario

---

## NOTAS IMPORTANTES

### WARNING: Orden de Implementación Crítico

Si decides implementar M2 (remover backward compatibility):

**ORDEN OBLIGATORIO:**
1. A4: Migrar proyectos legacy (ya implementado ✅)
2. Ejecutar migration en proyectos existentes
3. Verificar que no quedan reportes en ubicación legacy
4. ENTONCES implementar M2

**NO implementar M2 antes de migrar proyectos** o se romperán.

### Proyectos Afectados por M2

Proyectos con reportes en ubicación legacy (root de tarea):
- `investigaci-n-clo-covid-19-20251222-195407`

Antes de M2, ejecutar:
```bash
python core/migrate_v10_to_v22.py projects/investigaci-n-clo-covid-19-20251222-195407
```

### Estado Actual

**Framework es OPERATIVO sin implementar pendientes.**

Fase 3 y 4 son **mejoras incrementales**, no correcciones críticas.

Puedes:
- ✅ Usar framework ahora
- ✅ Crear proyectos multi-agente
- ✅ Ejecutar investigaciones complejas
- ✅ Implementar pendientes gradualmente

---

## DOCUMENTOS RELACIONADOS

- `reports/ANALISIS_EXHAUSTIVO_FRAMEWORK_v22_20260115.md` - Análisis completo con 28 problemas identificados
- `reports/CORRECCIONES_APLICADAS_20260115.md` - 8 correcciones implementadas (Fase 1 + 2)
- `reports/SESION_ANALISIS_Y_ROADMAP_20260115.md` - Roadmap completo y decisiones
- `docs/PROTOCOLO_PROMPTS_AGENTES.md` - Protocolo para agentes (prevenir archivos mal ubicados)
- `docs/ARQUITECTURA_JERARQUICA_PROYECTO.md` - Estructura del proyecto (fuente de verdad)

---

**Documento creado:** 2026-01-15
**Mantenido por:** Coordinador Claude
**Estado:** ACTIVO - REFERENCIA DE PENDIENTES
