> **ADVERTENCIA:** Este es un documento de PROPUESTA. NO representa el estado actual del framework.
> Framework actual: v2.2 - Ver ../../../README.md
> Estado: ESPECIFICACION NO IMPLEMENTADA

---


# FORGE: Agent-to-WorkGraph Framework v1.0
## Arquitectura Completa - Rediseño del Agentic Task Framework

**Fecha:** 2025-12-26
**Versión:** 1.0.0 (Redesign completo)
**Principio inspirador:** A2UI (Agent-to-User-Interface) de Google
**Concepto nuevo:** A2WG (Agent-to-WorkGraph)

---

## PARTE I: ANÁLISIS DE ARQUITECTURA ACTUAL

### 1.1 Framework Actual (v2.2) - Estado Analizado

**Componentes existentes:**

```
core/
├── project_manager.py Gestión de proyectos/tareas
├── framework_validator.py Validación de estructura
├── task_manager.py [DEPRECATED] Sistema antiguo
├── audit_project.py Auditoría de estructura
├── fix_project_structure.py Migración de estructura
├── reorganize_task_structure.py Reorganización
└── analyze_inconsistencies.py Análisis de patrones

CLAUDE.md Instrucciones del coordinador
README.md Documentación usuario
CHECKLIST.md Validación manual
ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md Estándar de estructura

projects/[project-id]/
 ├── project_info.json Metadata de proyecto
 ├── context.md Contexto usuario
 ├── tasks/[task-name]/
 │ ├── task_info.json Metadata de tarea
 │ ├── prompt.md Prompt usado
 │ ├── README.md Índice
 │ └── reports/ Reportes generados
 └── synthesis/ Síntesis final
```

**Flujo actual:**
```
1. Usuario solicita investigación
2. Coordinador diseña prompts (2-layer architecture)
3. Coordinador usa ProjectManager.create_task()
4. Coordinador lanza agentes con Task tool
5. Agentes ejecutan y (supuestamente) guardan outputs
6. Coordinador sintetiza resultados
```

**Problemas identificados:**

1. **Ejecución imperativa**: Coordinador ejecuta directamente con Task tool
2. **Sin tracking**: No se registran task IDs de agentes lanzados
3. **Sin garantías**: Outputs se pierden si agente falla
4. **Sin recovery**: No hay checkpoints ni rollback
5. **Sin contratos**: No hay validación formal de inputs/outputs
6. **Sin gobernanza**: No hay políticas de seguridad aplicadas
7. **Sin auditoría**: No hay evidencia completa de ejecución
8. **Acoplamiento**: Lógica dispersa entre múltiples módulos

### 1.2 Principios de A2UI que debemos aplicar

**A2UI resuelve:**
```
Problema: ¿Cómo un agente puede generar UI sin ejecutar código inseguro?

Solución:
 - Agente DECLARA componentes en JSON
 - App VALIDA contra catálogo de componentes confiables
 - App RENDERIZA usando implementaciones nativas

Separación:
 Agente → WHAT (declaración)
 App → HOW (ejecución segura)
```

**Principios aplicables a nuestro contexto:**

1. **Declarativo vs Imperativo**: Separar intención de ejecución
2. **Catálogo confiable**: Validar contra especificación formal
3. **Seguridad por diseño**: No ejecutar código arbitrario
4. **Separación de responsabilidades**: WHAT vs HOW
5. **Extensibilidad controlada**: Nuevos componentes vía catálogo

---

## PARTE II: NUEVA ARQUITECTURA - FORGE FRAMEWORK

### 2.1 Concepto Core: A2WG (Agent-to-WorkGraph)

**Definición:**
```
A2WG es un protocolo declarativo donde el coordinador describe
el trabajo completo como un grafo ejecutable (WorkGraph) con
contratos formales, que un runtime valida, gobierna y ejecuta
con garantías de persistencia, trazabilidad y recuperabilidad.
```

**La unidad de intercambio:**
```
NO: Texto, código, comandos
SÍ: WorkGraph (grafo de trabajo ejecutable)
```

**WorkGraph contiene:**
- Tasks[] con contratos formales (input/output schemas)
- Dependencies (DAG de ejecución)
- Gates (puntos de aprobación/verificación)
- Triggers (eventos que disparan ejecución)
- Artifacts (outputs garantizados)
- Policies (reglas de seguridad y límites)

### 2.2 Arquitectura de 7 Capas

```
┌─────────────────────────────────────────────────────────┐
│ 7. INTEGRATION LAYER (External Tools) │
│ GitHub, CI/CD, MCP Servers, Custom Adapters │
└─────────────────────────────────────────────────────────┘
 ↕
┌─────────────────────────────────────────────────────────┐
│ 6. EVIDENCE LAYER (Auditoría) │
│ Evidence Ledger, Artifact Store, Audit Trail │
└─────────────────────────────────────────────────────────┘
 ↕
┌─────────────────────────────────────────────────────────┐
│ 5. EXECUTION LAYER (Ejecución) │
│ Task Runner, State Machine, Checkpoint Manager │
└─────────────────────────────────────────────────────────┘
 ↕
┌─────────────────────────────────────────────────────────┐
│ 4. COMPILATION LAYER (Traducción) │
│ WorkGraph Compiler, Adapter Registry, Optimizer │
└─────────────────────────────────────────────────────────┘
 ↕
┌─────────────────────────────────────────────────────────┐
│ 3. GOVERNANCE LAYER (Políticas) │
│ Policy Kernel, Validation Engine, Approval Gates │
└─────────────────────────────────────────────────────────┘
 ↕
┌─────────────────────────────────────────────────────────┐
│ 2. SPECIFICATION LAYER (Esquemas) │
│ WorkGraph Spec, Task Contracts, Schema Validator │
└─────────────────────────────────────────────────────────┘
 ↕
┌─────────────────────────────────────────────────────────┐
│ 1. DECLARATION LAYER (Coordinador) │
│ Intent Analyzer, WorkGraph Designer, Optimizer │
└─────────────────────────────────────────────────────────┘
```

### 2.3 Flujo Completo End-to-End

```
FASE 1: DECLARACIÓN
 Usuario → "Investiga efectividad de ClO2 contra COVID-19"
 ->
 Coordinador analiza intención
 ->
 Coordinador diseña WorkGraph:
 {
 "project": {...},
 "tasks": [
 {
 "id": "quimica-molecular",
 "role": "ChemistAgent",
 "contract": {
 "inputs": [],
 "outputs": ["quimica_molecular_clo2.md"],
 "quality_checks": [...]
 }
 },
 ...
 ],
 "dependencies": [[...]],
 "gates": [...]
 }

FASE 2: VALIDACIÓN
 WorkGraph → Policy Kernel
 ->
 Valida contra:
 - Schema de WorkGraph
 - Políticas de seguridad
 - Límites de recursos
 - Permisos por rol
 ->
 Si falla → Rechaza y reporta errores
 Si pasa → Continúa

FASE 3: COMPILACIÓN
 WorkGraph válido → Compiler
 ->
 Genera Execution Plan:
 - Orden de ejecución (topological sort del DAG)
 - Checkpoints entre tareas
 - Rutas de outputs
 - Adaptadores necesarios
 ->
 Execution Plan optimizado

FASE 4: EJECUCIÓN
 Execution Plan → Task Runner
 ->
 Para cada tarea:
 1. Crea checkpoint
 2. Prepara ambiente
 3. Ejecuta (via adapter)
 4. Valida output contra contrato
 5. Persiste artefactos
 6. Registra evidencia
 7. Actualiza estado
 ->
 Si falla → Recovery automático desde último checkpoint
 Si pasa → Siguiente tarea

FASE 5: EVIDENCIA
 Cada paso → Evidence Ledger
 ->
 Registro inmutable de:
 - Inputs usados
 - Outputs generados
 - Logs de ejecución
 - Decisiones tomadas
 - Validaciones pasadas
 - Aprobaciones obtenidas
 ->
 Evidencia completa y auditable

FASE 6: SÍNTESIS
 Todas las tareas completas → Coordinador
 ->
 Sintetiza hallazgos
 ->
 Presenta a usuario
```

---

## PARTE III: ESPECIFICACIÓN FORMAL DE COMPONENTES

### 3.1 WorkGraph Specification (Capa 2)

**Esquema JSON:**

```json
{
 "$schema": "https://forge-framework.org/schemas/workgraph-v1.json",
 "version": "1.0.0",
 "project": {
 "id": "string (auto-generated)",
 "name": "string",
 "description": "string",
 "goal": "string",
 "constraints": {
 "deadline": "ISO8601 date (optional)",
 "budget": "number (optional)",
 "max_parallel_tasks": "number (default: 5)"
 },
 "metadata": {
 "created": "ISO8601 timestamp",
 "created_by": "string",
 "tags": ["string"]
 }
 },
 "tasks": [
 {
 "id": "string (kebab-case)",
 "role": "string (agent role)",
 "objective": "string",
 "contract": {
 "inputs": [
 {
 "name": "string",
 "type": "string (file|data|config)",
 "schema": "JSON Schema (optional)",
 "required": "boolean"
 }
 ],
 "outputs": [
 {
 "name": "string (filename)",
 "type": "string (markdown|json|code|image)",
 "schema": "JSON Schema (optional)",
 "path": "string (relative path)"
 }
 ],
 "quality_checks": [
 {
 "type": "string (length|schema|regex|custom)",
 "config": "object",
 "message": "string (error message if fails)"
 }
 ]
 },
 "execution": {
 "timeout": "number (seconds, default: 3600)",
 "retry_policy": {
 "max_retries": "number (default: 3)",
 "backoff": "string (linear|exponential)",
 "retry_on": ["error_type"]
 },
 "checkpoint_after": "boolean (default: true)",
 "rollback_on_fail": "boolean (default: false)"
 },
 "tools_allowed": ["string (tool names)"],
 "evidence_required": ["string (log|screenshot|metrics)"],
 "gate": "string (gate_id, optional)"
 }
 ],
 "dependencies": [
 {
 "from": "string (task_id)",
 "to": "string (task_id)",
 "type": "string (strict|soft)",
 "condition": "string (optional, JS expression)"
 }
 ],
 "gates": [
 {
 "id": "string",
 "type": "string (human_approval|auto_validation)",
 "when_task": "string (task_id)",
 "when_phase": "string (before|after)",
 "config": {
 "approvers": ["string (user IDs)"],
 "timeout": "number (seconds)",
 "auto_approve_if": "string (condition)"
 },
 "required": "boolean"
 }
 ],
 "triggers": [
 {
 "id": "string",
 "type": "string (schedule|event|webhook)",
 "config": "object",
 "target_task": "string (task_id)"
 }
 ],
 "policies": {
 "security": {
 "allowed_tools": ["string"],
 "forbidden_actions": ["string"],
 "sandbox_level": "string (strict|moderate|relaxed)"
 },
 "resources": {
 "max_cost": "number",
 "max_duration": "number (seconds)",
 "max_storage": "number (bytes)"
 },
 "approval": {
 "require_human_review": "boolean",
 "auto_approve_threshold": "number (risk score)"
 }
 }
}
```

### 3.2 Task Contract Specification

```typescript
interface TaskContract {
 inputs: InputSchema[];
 outputs: OutputSchema[];
 quality_checks: QualityCheck[];
 preconditions?: Condition[];
 postconditions?: Condition[];
}

interface InputSchema {
 name: string;
 type: "file" | "data" | "config" | "reference";
 schema?: JSONSchema;
 required: boolean;
 default?: any;
 validation?: ValidationRule[];
}

interface OutputSchema {
 name: string;
 type: "markdown" | "json" | "code" | "image" | "binary";
 path: string;
 schema?: JSONSchema;
 mandatory: boolean;
 validation?: ValidationRule[];
}

interface QualityCheck {
 type: "length" | "schema" | "regex" | "custom" | "ai_review";
 config: {
 min?: number;
 max?: number;
 pattern?: string;
 schema?: JSONSchema;
 validator?: string; // Function name or AI prompt
 };
 severity: "error" | "warning";
 message: string;
}

interface Condition {
 expression: string; // JS expression or rule
 message: string;
 required: boolean;
}
```

### 3.3 Task State Machine

```
Estados posibles:
 - DECLARED: Tarea declarada en WorkGraph
 - VALIDATED: Tarea validada por Policy Kernel
 - READY: Dependencias cumplidas, lista para ejecutar
 - RUNNING: Ejecución en progreso
 - CHECKPOINT: Checkpoint creado
 - VALIDATING: Validando outputs contra contrato
 - BLOCKED: Esperando gate de aprobación
 - REVIEW: En revisión humana
 - COMPLETED: Finalizada exitosamente
 - FAILED: Falló (con posibilidad de retry)
 - ROLLED_BACK: Revertida por fallo
 - CANCELLED: Cancelada por usuario/sistema

Transiciones válidas:
 DECLARED → VALIDATED (si pasa validación)
 DECLARED → FAILED (si falla validación)

 VALIDATED → READY (si dependencias cumplidas)
 VALIDATED → BLOCKED (si hay gate pre-ejecución)

 READY → RUNNING (cuando se inicia ejecución)

 RUNNING → CHECKPOINT (en puntos definidos)
 CHECKPOINT → RUNNING (continúa)

 RUNNING → VALIDATING (al terminar ejecución)
 VALIDATING → COMPLETED (si outputs válidos)
 VALIDATING → FAILED (si outputs inválidos)

 RUNNING → FAILED (si error durante ejecución)
 FAILED → RUNNING (si retry permitido)
 FAILED → ROLLED_BACK (si rollback activado)

 VALIDATING → REVIEW (si gate post-ejecución)
 REVIEW → COMPLETED (si aprobado)
 REVIEW → FAILED (si rechazado)

 * → CANCELLED (en cualquier momento)
```

---

## PARTE IV: MÓDULOS CORE DEL RUNTIME

### 4.1 ForgeKernel (Núcleo central)

**Responsabilidades:**
- Orquestación de todas las capas
- Gestión del ciclo de vida de WorkGraphs
- Coordinación de componentes
- API pública del framework

**Interfaz:**

```python
class ForgeKernel:
 def __init__(self, config: ForgeConfig):
 self.policy_kernel = PolicyKernel(config.policies)
 self.compiler = WorkGraphCompiler()
 self.runner = TaskRunner()
 self.evidence = EvidenceLedger(config.evidence_store)

 def submit_workgraph(self, workgraph: WorkGraph) -> ExecutionHandle:
 """Recibe WorkGraph, valida y ejecuta"""
 # 1. Validar estructura
 if not self.policy_kernel.validate_workgraph(workgraph):
 raise ValidationError(...)

 # 2. Compilar a execution plan
 plan = self.compiler.compile(workgraph)

 # 3. Ejecutar
 execution_id = self.runner.execute(plan)

 # 4. Retornar handle para tracking
 return ExecutionHandle(execution_id, self)

 def get_execution_status(self, execution_id: str) -> ExecutionStatus:
 """Obtiene estado actual de ejecución"""
 pass

 def get_task_output(self, execution_id: str, task_id: str) -> TaskOutput:
 """Recupera output de tarea específica"""
 pass

 def pause_execution(self, execution_id: str):
 """Pausa ejecución (en gate o checkpoint)"""
 pass

 def resume_execution(self, execution_id: str):
 """Reanuda ejecución pausada"""
 pass

 def rollback_to_checkpoint(self, execution_id: str, checkpoint_id: str):
 """Revierte a checkpoint anterior"""
 pass

 def get_evidence(self, execution_id: str) -> Evidence:
 """Obtiene evidencia completa de ejecución"""
 pass
```

### 4.2 PolicyKernel (Gobernanza)

**Responsabilidades:**
- Validar WorkGraphs contra políticas
- Aplicar reglas de seguridad
- Gestionar permisos
- Validar contratos de tareas

```python
class PolicyKernel:
 def __init__(self, policies: PolicyConfig):
 self.policies = policies
 self.validators = self._load_validators()

 def validate_workgraph(self, wg: WorkGraph) -> ValidationResult:
 """Valida WorkGraph completo"""
 errors = []

 # Validar estructura
 errors.extend(self._validate_schema(wg))

 # Validar políticas de seguridad
 errors.extend(self._validate_security(wg))

 # Validar límites de recursos
 errors.extend(self._validate_resources(wg))

 # Validar contratos de tareas
 for task in wg.tasks:
 errors.extend(self._validate_task_contract(task))

 # Validar DAG (no ciclos)
 errors.extend(self._validate_dag(wg))

 return ValidationResult(
 valid=len(errors) == 0,
 errors=errors
 )

 def validate_task_output(self, task: Task, output: Any) -> ValidationResult:
 """Valida output contra contrato"""
 pass

 def check_permission(self, task: Task, action: str) -> bool:
 """Verifica si tarea tiene permiso para acción"""
 pass
```

### 4.3 WorkGraphCompiler (Compilación)

**Responsabilidades:**
- Compilar WorkGraph a ExecutionPlan
- Optimizar orden de ejecución
- Resolver dependencias
- Asignar adaptadores

```python
class WorkGraphCompiler:
 def compile(self, wg: WorkGraph) -> ExecutionPlan:
 """Compila WorkGraph a plan ejecutable"""

 # 1. Topological sort de DAG
 execution_order = self._topological_sort(wg)

 # 2. Identificar puntos de paralelización
 parallel_groups = self._identify_parallel_groups(execution_order)

 # 3. Insertar checkpoints
 checkpointed_plan = self._insert_checkpoints(parallel_groups)

 # 4. Asignar adaptadores
 plan_with_adapters = self._assign_adapters(checkpointed_plan)

 # 5. Calcular rutas de outputs
 final_plan = self._resolve_output_paths(plan_with_adapters)

 return ExecutionPlan(
 tasks=final_plan,
 checkpoints=...,
 adapters=...,
 estimated_duration=...
 )
```

### 4.4 TaskRunner (Ejecución)

**Responsabilidades:**
- Ejecutar ExecutionPlan
- Gestionar estado de tareas
- Crear checkpoints
- Manejar fallos y recovery

```python
class TaskRunner:
 def __init__(self):
 self.state_machine = TaskStateMachine()
 self.checkpoint_mgr = CheckpointManager()
 self.adapter_registry = AdapterRegistry()

 def execute(self, plan: ExecutionPlan) -> str:
 """Ejecuta plan y retorna execution_id"""
 execution_id = self._generate_execution_id()

 # Iniciar ejecución en thread separado
 thread = Thread(target=self._execute_plan, args=(execution_id, plan))
 thread.start()

 return execution_id

 def _execute_plan(self, execution_id: str, plan: ExecutionPlan):
 """Ejecuta plan en thread dedicado"""
 try:
 for task in plan.tasks:
 # Transición de estado
 self.state_machine.transition(task.id, State.RUNNING)

 # Ejecutar
 result = self._execute_task(task)

 # Validar output
 if not self._validate_output(task, result):
 raise OutputValidationError(...)

 # Crear checkpoint
 if task.execution.checkpoint_after:
 self.checkpoint_mgr.create(execution_id, task.id, result)

 # Transición a completado
 self.state_machine.transition(task.id, State.COMPLETED)

 except Exception as e:
 # Recovery logic
 self._handle_failure(execution_id, task, e)

 def _execute_task(self, task: Task) -> TaskResult:
 """Ejecuta tarea individual usando adapter"""
 adapter = self.adapter_registry.get(task.role)
 return adapter.execute(task)
```

### 4.5 EvidenceLedger (Auditoría)

**Responsabilidades:**
- Registrar evidencia inmutable
- Almacenar artefactos
- Generar audit trail

```python
class EvidenceLedger:
 def __init__(self, store: EvidenceStore):
 self.store = store

 def record_event(self, execution_id: str, event: Event):
 """Registra evento en ledger inmutable"""
 entry = EvidenceEntry(
 execution_id=execution_id,
 timestamp=datetime.now(),
 event_type=event.type,
 event_data=event.data,
 hash=self._compute_hash(event)
 )
 self.store.append(entry)

 def store_artifact(self, execution_id: str, artifact: Artifact):
 """Almacena artefacto con metadata"""
 path = self.store.save(artifact.content)
 self.record_event(execution_id, ArtifactCreatedEvent(
 artifact_name=artifact.name,
 path=path,
 hash=hash(artifact.content),
 size=len(artifact.content)
 ))

 def get_audit_trail(self, execution_id: str) -> AuditTrail:
 """Genera audit trail completo"""
 entries = self.store.query(execution_id=execution_id)
 return AuditTrail(entries)
```

---

## PARTE V: ADAPTADORES Y EXTENSIBILIDAD

### 5.1 Adapter Registry

El framework se integra con herramientas externas via adaptadores:

```
AgentAdapter (ejecuta agentes con Task tool de Claude Code)
 - ClaudeCodeAdapter: Usa Task tool
 - CustomAgentAdapter: Agentes custom

WorkflowAdapter (integra con engines de workflow)
 - N8nAdapter: n8n workflows
 - TemporalAdapter: Temporal.io
 - AirflowAdapter: Apache Airflow

RepositoryAdapter (integra con repos)
 - GitHubAdapter: GitHub repos
 - GitLabAdapter: GitLab repos

CIAdapter (integra con CI/CD)
 - GitHubActionsAdapter: GitHub Actions
 - JenkinsAdapter: Jenkins

MCPAdapter (Model Context Protocol servers)
 - CustomMCPAdapter: Cualquier MCP server
```

**Interfaz de Adapter:**

```python
class TaskAdapter(ABC):
 @abstractmethod
 def can_handle(self, task: Task) -> bool:
 """¿Puede este adapter ejecutar esta tarea?"""
 pass

 @abstractmethod
 async def execute(self, task: Task) -> TaskResult:
 """Ejecuta la tarea"""
 pass

 @abstractmethod
 def cancel(self, task_id: str):
 """Cancela tarea en ejecución"""
 pass
```

**Ejemplo: ClaudeCodeAdapter**

```python
class ClaudeCodeAdapter(TaskAdapter):
 def can_handle(self, task: Task) -> bool:
 return task.role.endswith("Agent")

 async def execute(self, task: Task) -> TaskResult:
 # Construir prompt para agente
 prompt = self._build_agent_prompt(task)

 # Lanzar con Task tool
 task_id = Task(
 subagent_type="general-purpose",
 description=task.objective,
 prompt=prompt,
 run_in_background=True
 )

 # Esperar completion (con timeout)
 result = await self._wait_for_completion(
 task_id,
 timeout=task.execution.timeout
 )

 # Validar outputs
 outputs = self._collect_outputs(task, result)

 return TaskResult(
 task_id=task.id,
 status="completed",
 outputs=outputs,
 logs=result.logs
 )
```

---

## PARTE VI: COMPARACIÓN CON ARQUITECTURA ACTUAL

```
ANTES (v2.2): DESPUÉS (Forge v1.0):

Coordinador Coordinador
 -> (imperativo) -> (declarativo)
ProjectManager WorkGraph Designer
 -> ->
create_task() submit_workgraph()
 -> ->
Task tool directo Policy Kernel → Validación
 -> ->
Agente ejecuta Compiler → ExecutionPlan
 -> ->
¿Guarda output? TaskRunner → Ejecución garantizada
 -> ->
Si falla → perdido Evidence Ledger → Registro
 ->
No recovery Checkpoints → Recovery automático

PROBLEMAS RESUELTOS:

1. Outputs perdidos
 ANTES: Si agente no guarda → perdido
 AHORA: TaskRunner garantiza persistencia

2. Sin tracking
 ANTES: No se registran task IDs
 AHORA: Execution_id y estado completo

3. Sin recovery
 ANTES: Si falla → empezar de cero
 AHORA: Checkpoints automáticos, rollback

4. Sin contratos
 ANTES: Validación manual
 AHORA: Task Contracts formales

5. Sin gobernanza
 ANTES: No hay políticas aplicadas
 AHORA: Policy Kernel obligatorio

6. Sin auditoría
 ANTES: Logs dispersos o ausentes
 AHORA: Evidence Ledger inmutable

7. Ejecución imperativa
 ANTES: Coordinador ejecuta directamente
 AHORA: Coordinador declara, runtime ejecuta
```

---

## PARTE VII: IMPLEMENTACIÓN PRÁCTICA

### 7.1 Migración desde v2.2

**Paso 1: Instalar Forge Core**

```bash
pip install forge-framework
```

**Paso 2: Configurar**

```yaml
# forge.config.yaml
version: 1.0.0
runtime:
 max_parallel_tasks: 5
 default_timeout: 3600
 checkpoint_interval: 300

policies:
 security:
 sandbox_level: strict
 allowed_tools:
 - web_search
 - docs_writer
 - code_executor
 resources:
 max_cost_per_execution: 100
 max_duration: 86400

evidence:
 store_type: local
 store_path: ./evidence_store
 retention_days: 90

adapters:
 - type: claude_code
 config:
 model: sonnet
```

**Paso 3: Actualizar Coordinador**

```python
# ANTES (v2.2):
from core.project_manager import ProjectManager

pm = ProjectManager()
project = pm.create_project(...)
task = pm.create_task(...)

# Lanzar agente directamente
Task(prompt=..., run_in_background=True)

# DESPUÉS (Forge v1.0):
from forge import ForgeKernel, WorkGraph

forge = ForgeKernel.from_config("forge.config.yaml")

# Diseñar WorkGraph
workgraph = WorkGraph(
 project={
 "name": "Investigación ClO2",
 "goal": "Analizar efectividad contra COVID-19"
 },
 tasks=[
 {
 "id": "quimica-molecular",
 "role": "ChemistAgent",
 "objective": "Analizar química molecular del ClO2",
 "contract": {
 "inputs": [],
 "outputs": [
 {
 "name": "quimica_molecular_clo2.md",
 "type": "markdown",
 "path": "reports/quimica_molecular_clo2.md"
 }
 ],
 "quality_checks": [
 {"type": "length", "config": {"min": 1000}}
 ]
 }
 }
 ]
)

# Ejecutar
execution = forge.submit_workgraph(workgraph)

# Tracking
status = execution.get_status()
outputs = execution.get_outputs()
evidence = execution.get_evidence()
```

### 7.2 Estructura de Directorios Nueva

```
forge-framework/
├── forge/ # Core framework
│ ├── kernel.py # ForgeKernel
│ ├── policy.py # PolicyKernel
│ ├── compiler.py # WorkGraphCompiler
│ ├── runner.py # TaskRunner
│ ├── evidence.py # EvidenceLedger
│ ├── adapters/ # Adaptadores
│ │ ├── claude_code.py
│ │ ├── github.py
│ │ └── ...
│ └── schemas/ # JSON Schemas
│ └── workgraph-v1.json
├── projects/ # Proyectos (compatible v2.2)
│ └── [project-id]/
│ ├── workgraph.json # WorkGraph declarado
│ ├── execution_plan.json # Plan compilado
│ ├── execution_log.json # Log de ejecución
│ ├── checkpoints/ # Checkpoints
│ ├── evidence/ # Evidencia
│ └── artifacts/ # Outputs finales
├── forge.config.yaml # Configuración
└── README.md
```

---

## PARTE VIII: CONCLUSIÓN Y PRÓXIMOS PASOS

### 8.1 Resumen de Innovaciones

**Forge Framework introduce:**

1. **A2WG Protocol**: Primer protocolo declarativo de trabajo para agentes
2. **Task Contracts**: Contratos formales con validación automática
3. **Policy Kernel**: Gobernanza integrada desde el diseño
4. **Evidence Ledger**: Auditoría inmutable completa
5. **Checkpoint System**: Recovery automático sin pérdida
6. **Adapter Architecture**: Extensibilidad sin modificar core

**Ventajas sobre arquitecturas existentes:**

- Más robusto que frameworks multiagente tradicionales
- Más escalable que soluciones ad-hoc
- Más auditable que sistemas imperativos
- Más seguro que ejecución directa
- Más eficiente que reinventar tooling

### 8.2 Implementación Incremental

**Fase 1 (Semana 1-2): Core Specification**
- Finalizar WorkGraph JSON Schema
- Implementar PolicyKernel básico
- Crear validadores de contrato

**Fase 2 (Semana 3-4): Runtime Mínimo**
- Implementar ForgeKernel
- Implementar WorkGraphCompiler
- Implementar TaskRunner básico

**Fase 3 (Semana 5-6): Adapters**
- ClaudeCodeAdapter (prioritario)
- FileSystemAdapter
- GitHubAdapter

**Fase 4 (Semana 7-8): Evidence & Recovery**
- Implementar EvidenceLedger
- Implementar CheckpointManager
- Implementar recovery automático

**Fase 5 (Semana 9-10): Testing & Docs**
- Suite de tests completa
- Documentación de API
- Guías de migración

### 8.3 Decisión Siguiente

**Propongo que procedamos a:**

1. **Especificación Formal v1.0** (próximo paso)
 - WorkGraph Schema completo en JSON Schema
 - Task Contract Schema completo
 - State Machine formalmente definida
 - Policy Kernel rules especificadas

2. **Implementación Proof-of-Concept** (después)
 - ForgeKernel mínimo funcional
 - ClaudeCodeAdapter funcional
 - Migrar 1 proyecto existente como test

---

**Versión:** 1.0.0
**Fecha:** 2025-12-26
**Estado:** Especificación completa - Pendiente aprobación
**Próximo:** Especificación Formal JSON Schemas v1.0

---

¿Procedo con la Especificación Formal de JSON Schemas?
