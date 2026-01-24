> **ADVERTENCIA:** Este es un documento de PROPUESTA. NO representa el estado actual del framework.
> Framework actual: v2.2 - Ver ../../../README.md
> Estado: ESPECIFICACION NO IMPLEMENTADA

---


# FORGE FRAMEWORK - INTERFACES v1.0

## INTRODUCCION

Este documento especifica todas las interfaces y contratos entre componentes del Forge Framework. Define como los componentes se comunican, que datos intercambian, y que garantias proporciona cada interface.

## PRINCIPIOS DE DISENO

1. **Separacion de Concerns**: Cada interface tiene una responsabilidad unica y bien definida
2. **Contratos Formales**: Todas las interfaces especifican precondiciones, postcondiciones e invariantes
3. **Validacion Explicita**: Toda entrada se valida contra schemas formales
4. **Inmutabilidad**: Los datos que cruzan interfaces son inmutables o se copian
5. **Errores Explicitos**: Todas las interfaces documentan modos de fallo y manejo de errores

---

## CAPA 1: DECLARATION LAYER

### Interface: CoordinatorAPI

**Proposito**: Punto de entrada para el coordinador (Claude principal) para declarar work graphs

**Operaciones**:

```python
class CoordinatorAPI:
    def declare_workgraph(
        self,
        project_id: str,
        workgraph: Dict[str, Any]
    ) -> WorkGraphDeclaration:
        """
        Declara un nuevo work graph para ejecucion.

        Precondiciones:
        - project_id debe ser kebab-case valido
        - workgraph debe ser JSON valido

        Postcondiciones:
        - Retorna WorkGraphDeclaration con ID unico asignado
        - WorkGraph se registra en el sistema pero NO se ejecuta
        - Se crea registro de evidencia para la declaracion

        Errores:
        - InvalidProjectIDError: project_id no cumple formato
        - MalformedWorkGraphError: workgraph no es JSON valido
        - SchemaValidationError: workgraph no cumple schema
        """
        pass

    def validate_workgraph(
        self,
        workgraph_id: str
    ) -> ValidationResult:
        """
        Valida un work graph declarado contra todas las politicas.

        Precondiciones:
        - workgraph_id debe existir en el sistema

        Postcondiciones:
        - Retorna ValidationResult con lista completa de errores/warnings
        - No modifica el work graph
        - Crea registro de evidencia para la validacion

        Errores:
        - WorkGraphNotFoundError: workgraph_id no existe
        """
        pass

    def submit_workgraph(
        self,
        workgraph_id: str
    ) -> ExecutionPlan:
        """
        Somete un work graph validado para compilacion y ejecucion.

        Precondiciones:
        - workgraph_id debe existir
        - workgraph debe estar validado exitosamente

        Postcondiciones:
        - Retorna ExecutionPlan compilado
        - Cambia estado de workgraph a SUBMITTED
        - Dispara compilacion asíncrona

        Errores:
        - WorkGraphNotValidatedError: workgraph no ha sido validado
        - ValidationFailedError: workgraph tiene errores de validacion
        - CompilationError: fallo al compilar execution plan
        """
        pass
```

**Tipos de Datos**:

```python
@dataclass
class WorkGraphDeclaration:
    workgraph_id: str          # UUID generado por sistema
    project_id: str
    created_at: datetime
    state: WorkGraphState      # Enum: DECLARED, VALIDATED, SUBMITTED, etc.
    workgraph: Dict[str, Any]  # Work graph JSON completo

@dataclass
class ValidationResult:
    valid: bool
    errors: List[ValidationError]
    warnings: List[ValidationWarning]
    timestamp: datetime

@dataclass
class ValidationError:
    code: str
    message: str
    path: str                  # JSON path del error
    severity: Severity         # Enum: ERROR, WARNING, INFO
```

---

## CAPA 2: SPECIFICATION LAYER

### Interface: SchemaRegistry

**Proposito**: Registro centralizado de todos los schemas JSON para validacion

**Operaciones**:

```python
class SchemaRegistry:
    def get_schema(
        self,
        schema_type: SchemaType,
        version: str = "1.0"
    ) -> JSONSchema:
        """
        Obtiene schema JSON para un tipo especifico.

        Precondiciones:
        - schema_type debe ser un SchemaType valido
        - version debe existir para ese tipo

        Postcondiciones:
        - Retorna JSONSchema compilado y listo para validacion
        - Schema es inmutable (copia)

        Errores:
        - SchemaNotFoundError: schema no existe para tipo/version
        - SchemaCorruptedError: schema no se puede cargar
        """
        pass

    def validate_against_schema(
        self,
        data: Dict[str, Any],
        schema_type: SchemaType,
        version: str = "1.0"
    ) -> ValidationResult:
        """
        Valida datos contra un schema especifico.

        Precondiciones:
        - schema_type y version deben existir
        - data debe ser JSON-serializable

        Postcondiciones:
        - Retorna ValidationResult con errores detallados
        - No modifica data

        Errores:
        - SchemaNotFoundError: schema no existe
        """
        pass

# Schemas disponibles
class SchemaType(Enum):
    WORKGRAPH = "workgraph"
    TASK_CONTRACT = "task_contract"
    POLICY_CONFIG = "policy_config"
    EXECUTION_PLAN = "execution_plan"
    EVIDENCE_RECORD = "evidence_record"
```

---

## CAPA 3: GOVERNANCE LAYER

### Interface: PolicyKernel

**Proposito**: Aplicacion de politicas de gobernanza a work graphs y tareas

**Operaciones**:

```python
class PolicyKernel:
    def load_policies(
        self,
        policy_config_path: str
    ) -> PolicySet:
        """
        Carga configuracion de politicas desde archivo.

        Precondiciones:
        - policy_config_path debe existir
        - Archivo debe ser JSON valido

        Postcondiciones:
        - Retorna PolicySet compilado
        - Politicas se validan contra policy_config schema
        - Se crea registro de evidencia

        Errores:
        - PolicyFileNotFoundError
        - InvalidPolicyConfigError
        """
        pass

    def evaluate_workgraph(
        self,
        workgraph: Dict[str, Any],
        policies: PolicySet
    ) -> PolicyEvaluationResult:
        """
        Evalua un work graph contra todas las politicas.

        Precondiciones:
        - workgraph debe ser JSON valido
        - policies debe estar cargado

        Postcondiciones:
        - Retorna resultado con violaciones encontradas
        - No modifica workgraph ni policies
        - Crea registro de evidencia

        Errores:
        - PolicyEvaluationError: error durante evaluacion
        """
        pass

    def evaluate_task_execution(
        self,
        task_id: str,
        runtime_metrics: TaskMetrics,
        policies: PolicySet
    ) -> PolicyEvaluationResult:
        """
        Evalua ejecucion de tarea contra politicas de runtime.

        Precondiciones:
        - task_id debe existir
        - runtime_metrics debe ser valido

        Postcondiciones:
        - Retorna violaciones de politica en tiempo de ejecucion
        - Puede disparar acciones (abort, warn, log)

        Errores:
        - TaskNotFoundError
        """
        pass

@dataclass
class PolicyEvaluationResult:
    passed: bool
    violations: List[PolicyViolation]
    enforcement_actions: List[EnforcementAction]
    timestamp: datetime

@dataclass
class PolicyViolation:
    policy_type: PolicyType    # SECURITY, RESOURCE, QUALITY, COMPLIANCE
    policy_name: str
    rule: str
    severity: Severity
    message: str
    suggested_fix: Optional[str]

@dataclass
class EnforcementAction:
    action: ActionType         # ABORT, WARN, LOG
    reason: str
    applied: bool
    timestamp: datetime
```

---

## CAPA 4: COMPILATION LAYER

### Interface: WorkGraphCompiler

**Proposito**: Compilacion de work graphs declarativos a execution plans imperativos

**Operaciones**:

```python
class WorkGraphCompiler:
    def compile(
        self,
        workgraph: Dict[str, Any],
        validation_result: ValidationResult
    ) -> ExecutionPlan:
        """
        Compila work graph a execution plan ejecutable.

        Precondiciones:
        - workgraph debe estar validado (validation_result.valid == True)
        - Todas las dependencias entre tareas deben ser resolubles

        Postcondiciones:
        - Retorna ExecutionPlan con stages ordenados
        - Tareas se agrupan en stages basado en dependencias
        - Se asignan configuraciones de agentes
        - Se identifican puntos de checkpoint

        Errores:
        - CyclicDependencyError: hay ciclos en dependencias
        - UnresolvableDependencyError: dependencia referencia task inexistente
        - CompilationError: error generico de compilacion
        """
        pass

    def analyze_dependencies(
        self,
        workgraph: Dict[str, Any]
    ) -> DependencyGraph:
        """
        Analiza grafo de dependencias entre tareas.

        Precondiciones:
        - workgraph debe tener campo "tasks" y "dependencies"

        Postcondiciones:
        - Retorna DependencyGraph con analisis topologico
        - Identifica ciclos si existen
        - Calcula orden de ejecucion

        Errores:
        - MalformedWorkGraphError
        """
        pass

    def optimize_execution_plan(
        self,
        execution_plan: ExecutionPlan
    ) -> ExecutionPlan:
        """
        Optimiza execution plan para mejor rendimiento.

        Precondiciones:
        - execution_plan debe ser valido

        Postcondiciones:
        - Retorna execution plan optimizado
        - Maximiza paralelismo donde sea posible
        - Minimiza numero de stages
        - Preserva semantica de dependencias

        Errores:
        - None (optimizacion es best-effort)
        """
        pass

@dataclass
class DependencyGraph:
    nodes: List[str]           # Task IDs
    edges: List[Tuple[str, str]]  # (from, to)
    has_cycles: bool
    cycles: List[List[str]]    # Ciclos detectados
    topological_order: List[str]  # Orden de ejecucion valido
```

---

## CAPA 5: EXECUTION LAYER

### Interface: TaskRunner

**Proposito**: Ejecucion de tareas individuales con aislamiento y monitoreo

**Operaciones**:

```python
class TaskRunner:
    def execute_task(
        self,
        task_execution: TaskExecution,
        execution_plan: ExecutionPlan
    ) -> TaskResult:
        """
        Ejecuta una tarea individual.

        Precondiciones:
        - task_execution debe estar en estado READY
        - Todas las dependencias deben estar completadas
        - Recursos necesarios deben estar disponibles

        Postcondiciones:
        - Retorna TaskResult con estado final
        - Crea todos los outputs especificados en contrato
        - Actualiza estado de task a COMPLETED o FAILED
        - Crea registros de evidencia

        Errores:
        - TaskNotReadyError: dependencias no completadas
        - ResourceUnavailableError: recursos insuficientes
        - TaskTimeoutError: excedio timeout
        - TaskExecutionError: error durante ejecucion
        """
        pass

    def monitor_task(
        self,
        task_id: str
    ) -> TaskStatus:
        """
        Monitorea estado actual de una tarea.

        Precondiciones:
        - task_id debe existir

        Postcondiciones:
        - Retorna TaskStatus con metricas en tiempo real
        - No interrumpe ejecucion

        Errores:
        - TaskNotFoundError
        """
        pass

    def abort_task(
        self,
        task_id: str,
        reason: str
    ) -> TaskResult:
        """
        Aborta ejecucion de una tarea.

        Precondiciones:
        - task_id debe existir
        - Tarea debe estar en estado RUNNING

        Postcondiciones:
        - Detiene ejecucion inmediatamente
        - Retorna TaskResult con estado ABORTED
        - Limpia recursos
        - Crea registro de evidencia

        Errores:
        - TaskNotFoundError
        - TaskNotRunningError
        """
        pass

@dataclass
class TaskResult:
    task_id: str
    state: TaskState           # COMPLETED, FAILED, ABORTED
    outputs: Dict[str, OutputInfo]
    quality_results: List[QualityCheckResult]
    runtime_metrics: TaskMetrics
    errors: List[TaskError]
    completed_at: datetime

@dataclass
class TaskStatus:
    task_id: str
    state: TaskState
    progress_percentage: float
    current_operation: str
    metrics: TaskMetrics
    timestamp: datetime

@dataclass
class TaskMetrics:
    duration_seconds: float
    memory_used_mb: float
    disk_used_mb: float
    tool_calls: int
    network_calls: int
```

---

## CAPA 6: EVIDENCE LAYER

### Interface: EvidenceLedger

**Proposito**: Registro inmutable de todas las acciones del sistema

**Operaciones**:

```python
class EvidenceLedger:
    def record_event(
        self,
        event_type: EventType,
        actor: Actor,
        context: EventContext,
        payload: Dict[str, Any]
    ) -> EvidenceRecord:
        """
        Registra un evento en el ledger.

        Precondiciones:
        - event_type debe ser valido
        - payload debe ser JSON-serializable

        Postcondiciones:
        - Retorna EvidenceRecord con ID unico
        - Record se añade al ledger (inmutable)
        - Hash del record se calcula incluyendo hash del record previo
        - Record se persiste a disco

        Errores:
        - LedgerWriteError: fallo al escribir
        - PayloadSerializationError: payload no serializable
        """
        pass

    def get_chain(
        self,
        context: EventContext,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ) -> List[EvidenceRecord]:
        """
        Obtiene cadena de evidencia para un contexto.

        Precondiciones:
        - context debe especificar al menos workgraph_id o task_id

        Postcondiciones:
        - Retorna lista ordenada de records
        - Lista esta ordenada cronologicamente
        - Incluye solo records del contexto especificado

        Errores:
        - InvalidContextError
        """
        pass

    def verify_integrity(
        self,
        context: EventContext
    ) -> IntegrityVerificationResult:
        """
        Verifica integridad de cadena de evidencia.

        Precondiciones:
        - context debe ser valido

        Postcondiciones:
        - Retorna resultado de verificacion
        - Verifica hashes de toda la cadena
        - Detecta records faltantes o modificados

        Errores:
        - None (retorna resultado con errores encontrados)
        """
        pass

@dataclass
class EvidenceRecord:
    record_id: str             # UUID
    event_type: EventType
    timestamp: datetime
    actor: Actor
    context: EventContext
    payload: Dict[str, Any]
    chain: ChainInfo
    integrity: IntegrityInfo

@dataclass
class ChainInfo:
    previous_record_id: Optional[str]
    previous_record_hash: Optional[str]
    sequence_number: int

@dataclass
class IntegrityInfo:
    hash: str                  # SHA-256 de todo el record
    signature: Optional[str]   # Firma criptografica (futuro)

@dataclass
class IntegrityVerificationResult:
    valid: bool
    total_records: int
    verified_records: int
    broken_chains: List[str]   # Record IDs donde cadena se rompe
    modified_records: List[str]  # Record IDs con hash invalido
```

---

## CAPA 7: INTEGRATION LAYER

### Interface: ClaudeCodeAdapter

**Proposito**: Integracion con Claude Code para lanzamiento de agentes

**Operaciones**:

```python
class ClaudeCodeAdapter:
    def launch_agent(
        self,
        task_execution: TaskExecution,
        agent_config: AgentConfiguration
    ) -> AgentHandle:
        """
        Lanza una nueva instancia de Claude Code para ejecutar tarea.

        Precondiciones:
        - task_execution debe estar en estado READY
        - agent_config.working_directory debe existir
        - agent_config.prompt_path debe existir

        Postcondiciones:
        - Retorna AgentHandle para controlar el agente
        - Se abre nueva terminal con Claude Code
        - Claude Code carga prompt de agent_config.prompt_path
        - Agente empieza ejecucion automaticamente

        Errores:
        - AgentLaunchError: fallo al lanzar proceso
        - WorkingDirectoryNotFoundError
        - PromptFileNotFoundError
        """
        pass

    def monitor_agent(
        self,
        handle: AgentHandle
    ) -> AgentStatus:
        """
        Monitorea estado de agente en ejecucion.

        Precondiciones:
        - handle debe ser valido

        Postcondiciones:
        - Retorna AgentStatus con informacion actual
        - No interrumpe agente

        Errores:
        - AgentNotFoundError: agente no existe o termino
        """
        pass

    def retrieve_outputs(
        self,
        handle: AgentHandle,
        expected_outputs: List[ContractOutput]
    ) -> Dict[str, OutputInfo]:
        """
        Recupera outputs producidos por agente.

        Precondiciones:
        - handle debe ser valido
        - Agente debe haber completado

        Postcondiciones:
        - Retorna diccionario de outputs encontrados
        - Valida cada output contra su schema
        - Calcula checksums

        Errores:
        - AgentStillRunningError
        - OutputNotFoundError: output esperado no existe
        - OutputValidationError: output no cumple schema
        """
        pass

@dataclass
class AgentHandle:
    agent_id: str
    process_id: int
    task_id: str
    working_directory: str
    started_at: datetime

@dataclass
class AgentStatus:
    agent_id: str
    running: bool
    exit_code: Optional[int]
    last_activity: datetime
```

---

## CONTRATOS DE DATOS COMPARTIDOS

### Contract: Task Contract

**Proposito**: Especificacion formal de inputs y outputs de una tarea

```python
@dataclass
class TaskContract:
    inputs: List[ContractInput]
    outputs: List[ContractOutput]
    quality_checks: List[QualityCheck]
    constraints: TaskConstraints

@dataclass
class ContractInput:
    name: str
    type: InputType            # FILE, DIRECTORY, ARTIFACT, PARAMETER, CONTEXT
    required: bool
    schema: Optional[JSONSchema]
    source: Optional[str]      # Referencia a artifact, file, etc.

@dataclass
class ContractOutput:
    name: str
    type: OutputType           # FILE, DIRECTORY, ARTIFACT
    path: str                  # Path relativo en task directory
    schema: Optional[JSONSchema]
    format: OutputFormat       # MARKDOWN, JSON, YAML, TEXT, BINARY

@dataclass
class QualityCheck:
    type: QualityCheckType     # LENGTH, FORMAT, SCHEMA, CONTENT_VALIDATION, etc.
    config: Dict[str, Any]
    severity: Severity         # ERROR, WARNING, INFO

@dataclass
class TaskConstraints:
    max_tokens: Optional[int]
    max_files: Optional[int]
    allowed_tools: Optional[List[str]]
    forbidden_actions: Optional[List[str]]
```

### Contract: Checkpoint

**Proposito**: Punto de recuperacion en ejecucion

```python
@dataclass
class Checkpoint:
    checkpoint_id: str
    created_at: datetime
    trigger: CheckpointTrigger  # MANUAL, STAGE_COMPLETE, TASK_COMPLETE, ERROR
    state_snapshot: ExecutionSnapshot
    artifact_checksums: Dict[str, str]
    rollback_capable: bool
    size_mb: float

@dataclass
class ExecutionSnapshot:
    current_stage: int
    completed_tasks: List[str]
    failed_tasks: List[str]
    running_tasks: List[str]
    execution_plan: ExecutionPlan
```

---

## GARANTIAS DEL SISTEMA

### Garantia 1: Inmutabilidad de Evidencia

**Propiedad**: Una vez creado, un EvidenceRecord no puede ser modificado ni eliminado.

**Implementacion**:
- EvidenceLedger usa append-only file storage
- Cada record incluye hash del record anterior
- verify_integrity() detecta cualquier modificacion

**Verificacion**:
```python
# Antes de confiar en evidencia
result = ledger.verify_integrity(context)
assert result.valid, "Cadena de evidencia comprometida"
```

### Garantia 2: Validacion Before Execution

**Propiedad**: Ningun work graph se ejecuta sin validacion completa exitosa.

**Implementacion**:
- submit_workgraph() verifica validation_result.valid
- TaskRunner verifica que task este en estado READY
- PolicyKernel evalua en declaracion y en runtime

**Verificacion**:
```python
# Sistema verifica automaticamente
validation = coordinator.validate_workgraph(wg_id)
if not validation.valid:
    raise ValidationFailedError(validation.errors)
```

### Garantia 3: Aislamiento de Tareas

**Propiedad**: Tareas no pueden interferir entre si excepto via artifacts declarados.

**Implementacion**:
- Cada tarea ejecuta en su propio directorio
- Cada tarea ejecuta en proceso separado (Claude Code instance)
- Artifacts compartidos se especifican en work graph

**Verificacion**:
```python
# Cada task tiene working_directory unico
assert task1.working_directory != task2.working_directory
# Intercambio solo via artifacts
assert artifact_id in workgraph["artifacts"]
```

### Garantia 4: Recuperabilidad

**Propiedad**: Cualquier ejecucion puede recuperarse desde ultimo checkpoint.

**Implementacion**:
- Checkpoints se crean despues de cada stage
- ExecutionSnapshot incluye estado completo
- Rollback restaura snapshot y re-ejecuta desde ahi

**Verificacion**:
```python
# En caso de fallo
latest_checkpoint = plan.checkpoints[-1]
assert latest_checkpoint.rollback_capable
restored_state = restore_from_checkpoint(latest_checkpoint)
```

---

## FLUJO DE DATOS COMPLETO

### Ejemplo: Declaracion y Ejecucion de Work Graph

```python
# 1. Coordinador declara work graph
declaration = coordinator_api.declare_workgraph(
    project_id="covid-research-001",
    workgraph=workgraph_dict
)
# Estado: DECLARED
# Evidencia: workgraph_declared event

# 2. Sistema valida contra schemas y politicas
validation = coordinator_api.validate_workgraph(declaration.workgraph_id)
# Estado: VALIDATED (si valid=True)
# Evidencia: workgraph_validated event

# 3. Coordinador somete para ejecucion
execution_plan = coordinator_api.submit_workgraph(declaration.workgraph_id)
# Estado: SUBMITTED
# Evidencia: execution_plan_created event

# 4. Compiler genera stages
compiler = WorkGraphCompiler()
execution_plan = compiler.compile(
    workgraph=declaration.workgraph,
    validation_result=validation
)
# execution_plan tiene stages con tareas agrupadas

# 5. TaskRunner ejecuta stage por stage
runner = TaskRunner()
for stage in execution_plan.stages:
    # Ejecutar tareas del stage en paralelo
    for task_exec in stage.tasks:
        # 5a. Lanzar agente
        handle = adapter.launch_agent(task_exec, task_exec.agent_config)
        # Evidencia: task_started event

        # 5b. Monitorear
        status = adapter.monitor_agent(handle)

        # 5c. Recuperar outputs
        outputs = adapter.retrieve_outputs(handle, task_exec.contract.outputs)

        # 5d. Validar calidad
        quality_results = validate_quality(outputs, task_exec.contract.quality_checks)
        # Evidencia: quality_check_performed events

        # 5e. Registrar resultado
        result = TaskResult(
            task_id=task_exec.task_id,
            state=TaskState.COMPLETED,
            outputs=outputs,
            quality_results=quality_results,
            ...
        )
        # Evidencia: task_completed event

    # 5f. Crear checkpoint al final del stage
    checkpoint = create_checkpoint(execution_plan, stage.stage_id)
    # Evidencia: checkpoint_created event

# 6. Verificar integridad final
verification = ledger.verify_integrity(
    EventContext(workgraph_id=declaration.workgraph_id)
)
assert verification.valid
```

---

## EXTENSION DE INTERFACES

### Añadir Nuevo Adapter

Para integrar nueva herramienta externa:

```python
class NewToolAdapter(BaseAdapter):
    """
    Adapter para integrar [herramienta].

    Debe implementar:
    - launch_agent()
    - monitor_agent()
    - retrieve_outputs()
    """

    def launch_agent(self, task_execution, agent_config):
        # Implementacion especifica para lanzar en [herramienta]
        pass

    # ... otros metodos
```

Registrar en AdapterRegistry:

```python
adapter_registry.register("newtool", NewToolAdapter())
```

### Añadir Nuevo Quality Check

```python
class CustomQualityCheck(BaseQualityCheck):
    """
    Quality check personalizado.
    """

    def check(self, output: OutputInfo, config: Dict[str, Any]) -> QualityCheckResult:
        # Implementar logica de validacion
        passed = your_validation_logic(output, config)
        return QualityCheckResult(
            check_type="custom_check",
            passed=passed,
            severity=Severity.ERROR if not passed else Severity.INFO,
            message="..."
        )
```

Registrar:

```python
quality_registry.register("custom_check", CustomQualityCheck())
```

---

## TESTING DE INTERFACES

### Unit Tests

Cada interface debe tener tests que verifiquen:

```python
def test_coordinator_api_declare_workgraph():
    # Test precondiciones
    with pytest.raises(InvalidProjectIDError):
        api.declare_workgraph("Invalid ID!", workgraph)

    # Test happy path
    declaration = api.declare_workgraph("valid-id", workgraph)
    assert declaration.workgraph_id is not None
    assert declaration.state == WorkGraphState.DECLARED

    # Test evidencia creada
    records = ledger.get_chain(EventContext(workgraph_id=declaration.workgraph_id))
    assert len(records) == 1
    assert records[0].event_type == EventType.WORKGRAPH_DECLARED
```

### Integration Tests

Tests que verifican interaccion entre interfaces:

```python
def test_full_workgraph_execution():
    # Declarar
    declaration = coordinator_api.declare_workgraph(project_id, workgraph)

    # Validar
    validation = coordinator_api.validate_workgraph(declaration.workgraph_id)
    assert validation.valid

    # Someter
    execution_plan = coordinator_api.submit_workgraph(declaration.workgraph_id)

    # Ejecutar
    runner = TaskRunner()
    for stage in execution_plan.stages:
        for task in stage.tasks:
            result = runner.execute_task(task, execution_plan)
            assert result.state == TaskState.COMPLETED

    # Verificar evidencia completa
    verification = ledger.verify_integrity(
        EventContext(workgraph_id=declaration.workgraph_id)
    )
    assert verification.valid
```

---

## VERSION Y COMPATIBILIDAD

**Version Actual**: 1.0

**Politica de Versionado**:
- Cambios en signatures de metodos: Major version bump
- Nuevos metodos opcionales: Minor version bump
- Bug fixes sin cambio de interface: Patch version bump

**Retrocompatibilidad**:
- Interfaces v1.x garantizan compatibilidad con schemas v1.x
- Adapters son versionados independientemente

---

**Documento**: FORGE_INTERFACES_v1.0.md
**Fecha**: 2025-12-27
**Estado**: SPECIFICATION
**Siguiente**: Implementacion de modulos core
