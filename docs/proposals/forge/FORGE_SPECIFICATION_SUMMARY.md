> **ADVERTENCIA:** Este es un documento de PROPUESTA. NO representa el estado actual del framework.
> Framework actual: v2.2 - Ver ../../../README.md
> Estado: ESPECIFICACION NO IMPLEMENTADA

---


# FORGE FRAMEWORK - ESPECIFICACION COMPLETA v1.0

## RESUMEN EJECUTIVO

El Forge Framework v1.0 es una reconstruccion completa del Agentic Task Framework basado en principios declarativos inspirados en A2UI (Agent-to-User-Interface) de Google.

**Concepto Central**: A2WG (Agent-to-Work-Graph)
- Coordinador DECLARA work graphs con contratos formales
- Sistema VALIDA contra politicas de gobernanza
- Runtime EJECUTA con garantias deterministicas
- Evidence Ledger AUDITA todo el proceso

**Problemas Resueltos**:
1. Outputs perdidos de agentes (4 tareas sin reportes)
2. No hay tracking de Task IDs durante ejecucion
3. No hay mecanismo de recuperacion ante fallos
4. Ejecucion imperativa sin contratos formales
5. No hay gobernanza ni validacion de politicas
6. No hay trail de auditoria completo

---

## DOCUMENTOS DE LA ESPECIFICACION

### 1. FORGE_ARCHITECTURE_v1.0.md

**Proposito**: Arquitectura completa del sistema

**Contenido**:
- Analisis de arquitectura actual (v2.2) y sus limitaciones
- Aplicacion de principios A2UI al contexto de work graphs
- Diseño de arquitectura de 7 capas
- Especificacion de componentes core
- Sistema de estados y transiciones
- Roadmap de implementacion

**Audiencia**: Arquitectos, desarrolladores senior

**Leer cuando**: Necesites entender la vision general y decisiones de diseño

---

### 2. FORGE_INTERFACES_v1.0.md

**Proposito**: Contratos formales entre todos los componentes

**Contenido**:
- Interfaces de cada capa (Declaration, Specification, Governance, etc.)
- Precondiciones y postcondiciones de cada operacion
- Tipos de datos compartidos
- Garantias del sistema (inmutabilidad, validacion, aislamiento, recuperabilidad)
- Flujos de datos completos con ejemplos
- Guias de extension

**Audiencia**: Desarrolladores implementando componentes

**Leer cuando**: Necesites implementar o integrar con un componente especifico

---

### 3. JSON Schemas (schemas/)

**Proposito**: Especificaciones formales validables automaticamente

**Archivos**:

#### workgraph_v1.0.schema.json
- Estructura de work graphs declarativos
- Tasks con contracts (inputs/outputs)
- Dependencies, gates, triggers
- Artifacts compartidos
- Configuraciones de ejecucion

#### policy_config_v1.0.schema.json
- Politicas de seguridad (allowed_tools, forbidden_paths, etc.)
- Limites de recursos (concurrent tasks, duration, memory, disk)
- Quality gates (mandatory checks, minimum lengths, references)
- Compliance (estructura v2.2, naming conventions, writing style)

#### execution_plan_v1.0.schema.json
- Plan compilado desde work graph
- Stages ordenados para ejecucion
- Configuraciones de agentes
- Runtime metrics y estado
- Sistema de checkpoints

#### evidence_record_v1.0.schema.json
- Registros inmutables de eventos
- Chain linkage para integridad
- Payloads especificos por tipo de evento
- Metadata de actor y contexto

**Audiencia**: Validadores, implementadores de parsers

**Leer cuando**: Necesites validar datos o generar/parsear JSON

---

## ARQUITECTURA DE 7 CAPAS

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: DECLARATION │
│ Coordinador declara WorkGraphs │
│ Interface: CoordinatorAPI │
└─────────────────────────────────────────────────────────────┘
 ->
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: SPECIFICATION │
│ JSON Schemas formales │
│ Interface: SchemaRegistry │
└─────────────────────────────────────────────────────────────┘
 ->
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: GOVERNANCE │
│ Validacion contra politicas │
│ Interface: PolicyKernel │
└─────────────────────────────────────────────────────────────┘
 ->
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: COMPILATION │
│ WorkGraph → ExecutionPlan │
│ Interface: WorkGraphCompiler │
└─────────────────────────────────────────────────────────────┘
 ->
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: EXECUTION │
│ Ejecucion de tareas con aislamiento │
│ Interface: TaskRunner │
└─────────────────────────────────────────────────────────────┘
 ->
┌─────────────────────────────────────────────────────────────┐
│ LAYER 6: EVIDENCE │
│ Audit trail inmutable │
│ Interface: EvidenceLedger │
└─────────────────────────────────────────────────────────────┘
 ->
┌─────────────────────────────────────────────────────────────┐
│ LAYER 7: INTEGRATION │
│ Adapters para herramientas externas │
│ Interface: ClaudeCodeAdapter, GitHubAdapter, etc. │
└─────────────────────────────────────────────────────────────┘
```

---

## FLUJO COMPLETO DE EJECUCION

### Fase 1: Declaracion

```python
# Coordinador crea work graph JSON
workgraph = {
 "version": "1.0",
 "project": {
 "id": "covid-research-001",
 "name": "Investigacion ClO2 COVID-19",
 "goal": "Analizar selectividad molecular del ClO2"
 },
 "tasks": [
 {
 "id": "quimica-molecular",
 "role": "QuimicoMolecular",
 "contract": {
 "inputs": [],
 "outputs": [
 {
 "name": "analisis_quimico",
 "path": "reports/quimica_molecular_clo2.md",
 "format": "markdown"
 }
 ],
 "quality_checks": [
 {"type": "length", "config": {"min": 2000}}
 ]
 }
 }
 ]
}

# Declarar
declaration = coordinator_api.declare_workgraph(
 project_id="covid-research-001",
 workgraph=workgraph
)
# → Estado: DECLARED
# → Evidencia: workgraph_declared event creado
```

### Fase 2: Validacion

```python
# Sistema valida contra schemas
validation = coordinator_api.validate_workgraph(declaration.workgraph_id)

# Validaciones realizadas:
# - Schema JSON (workgraph_v1.0.schema.json)
# - Politicas de seguridad (allowed_tools, etc.)
# - Limites de recursos (max_concurrent_tasks, etc.)
# - Quality requirements (mandatory_checks, etc.)
# - Compliance (naming conventions, estructura v2.2, etc.)

if not validation.valid:
 for error in validation.errors:
 print(f"{error.severity}: {error.message} at {error.path}")
 raise ValidationFailedError()

# → Estado: VALIDATED
# → Evidencia: workgraph_validated event creado
```

### Fase 3: Compilacion

```python
# Coordinador somete para ejecucion
execution_plan = coordinator_api.submit_workgraph(declaration.workgraph_id)

# WorkGraphCompiler internamente:
# 1. Analiza dependencias entre tasks
# 2. Detecta ciclos (error si existen)
# 3. Calcula orden topologico
# 4. Agrupa tasks en stages (paralelizables)
# 5. Asigna configuraciones de agentes
# 6. Identifica puntos de checkpoint

# execution_plan.stages = [
# Stage(stage_id=0, tasks=[
# TaskExecution(task_id="quimica-molecular", state=READY, ...)
# ])
# ]

# → Estado: SUBMITTED
# → Evidencia: execution_plan_created event creado
```

### Fase 4: Ejecucion

```python
# TaskRunner ejecuta stage por stage
for stage in execution_plan.stages:
 for task_exec in stage.tasks:
 # 1. Lanzar agente via adapter
 handle = claude_adapter.launch_agent(
 task_execution=task_exec,
 agent_config=task_exec.agent_config
 )
 # → Nueva terminal con Claude Code
 # → Lee prompt desde task_exec.agent_config.prompt_path
 # → Evidencia: task_started event

 # 2. Monitorear ejecucion
 while True:
 status = claude_adapter.monitor_agent(handle)
 if not status.running:
 break
 time.sleep(10)

 # 3. Recuperar outputs
 outputs = claude_adapter.retrieve_outputs(
 handle=handle,
 expected_outputs=task_exec.contract.outputs
 )
 # → Valida que existan todos los outputs esperados
 # → Calcula checksums
 # → Evidencia: artifact_created events

 # 4. Validar calidad
 for check in task_exec.contract.quality_checks:
 result = quality_validator.check(outputs, check)
 if not result.passed and check.severity == ERROR:
 raise QualityCheckFailedError(result.message)
 # → Evidencia: quality_check_performed events

 # 5. Actualizar estado
 task_exec.state = COMPLETED
 task_exec.outputs = outputs
 # → Evidencia: task_completed event

 # Checkpoint al final del stage
 checkpoint = create_checkpoint(execution_plan, stage.stage_id)
 execution_plan.checkpoints.append(checkpoint)
 # → Evidencia: checkpoint_created event

# → Estado final: COMPLETED
```

### Fase 5: Auditoria

```python
# Verificar integridad de evidencia
verification = evidence_ledger.verify_integrity(
 EventContext(workgraph_id=declaration.workgraph_id)
)

if not verification.valid:
 print(f"Broken chains: {verification.broken_chains}")
 print(f"Modified records: {verification.modified_records}")
 raise IntegrityViolationError()

# Obtener cadena completa
chain = evidence_ledger.get_chain(
 EventContext(workgraph_id=declaration.workgraph_id)
)

# chain = [
# EvidenceRecord(event_type=WORKGRAPH_DECLARED, ...),
# EvidenceRecord(event_type=WORKGRAPH_VALIDATED, ...),
# EvidenceRecord(event_type=EXECUTION_PLAN_CREATED, ...),
# EvidenceRecord(event_type=TASK_STARTED, ...),
# EvidenceRecord(event_type=ARTIFACT_CREATED, ...),
# EvidenceRecord(event_type=QUALITY_CHECK_PERFORMED, ...),
# EvidenceRecord(event_type=TASK_COMPLETED, ...),
# EvidenceRecord(event_type=CHECKPOINT_CREATED, ...)
# ]

# Audit trail completo e inmutable
```

---

## GARANTIAS DEL SISTEMA

### 1. Inmutabilidad de Evidencia

**Garantia**: Una vez creado, un EvidenceRecord no puede ser modificado ni eliminado.

**Mecanismo**:
- Append-only file storage
- Cada record incluye hash del record anterior (blockchain-like)
- verify_integrity() detecta modificaciones

**Verificacion**:
```python
assert ledger.verify_integrity(context).valid
```

---

### 2. Validacion Before Execution

**Garantia**: Ningun work graph se ejecuta sin validacion completa exitosa.

**Mecanismo**:
- submit_workgraph() verifica validation_result.valid
- PolicyKernel evalua en tiempo de declaracion
- TaskRunner verifica estado READY antes de ejecutar

**Verificacion**:
```python
# Sistema rechaza automaticamente
try:
 coordinator_api.submit_workgraph(workgraph_id)
except WorkGraphNotValidatedError:
 # No puede ejecutarse sin validacion
 pass
```

---

### 3. Aislamiento de Tareas

**Garantia**: Tareas no pueden interferir entre si excepto via artifacts declarados.

**Mecanismo**:
- Cada tarea ejecuta en directorio separado
- Cada tarea ejecuta en proceso separado (Claude Code instance)
- Solo artifacts declarados en work graph son compartidos

**Verificacion**:
```python
# Directorios unicos
assert task1.working_directory != task2.working_directory

# Comparticion explicita
shared_artifact = workgraph["artifacts"]["contexto-compartido"]
assert shared_artifact in task1.contract.inputs
assert shared_artifact in task2.contract.outputs
```

---

### 4. Recuperabilidad

**Garantia**: Cualquier ejecucion puede recuperarse desde ultimo checkpoint.

**Mecanismo**:
- Checkpoints automaticos despues de cada stage
- ExecutionSnapshot incluye estado completo
- Rollback restaura snapshot y re-ejecuta desde ahi

**Verificacion**:
```python
# En caso de fallo en stage 3
latest_checkpoint = execution_plan.checkpoints[-1] # Checkpoint de stage 2
assert latest_checkpoint.rollback_capable

# Restaurar
restored_plan = rollback_to_checkpoint(latest_checkpoint)
# → Stages 0,1,2 marcados como COMPLETED (no re-ejecutan)
# → Stage 3 marcado como PENDING (re-ejecuta)
```

---

## COMPARACION: v2.2 vs Forge v1.0

| Aspecto | v2.2 (Actual) | Forge v1.0 |
|---------|---------------|------------|
| **Paradigma** | Imperativo (ejecuta directamente) | Declarativo (declara, valida, ejecuta) |
| **Contratos** | Informales (comentarios) | Formales (JSON schemas) |
| **Validacion** | Manual (FrameworkValidator post-facto) | Automatica (pre-ejecucion) |
| **Gobernanza** | No existe | PolicyKernel con policies formales |
| **Tracking** | No hay registro de Task IDs | Task IDs registrados en execution plan |
| **Recuperacion** | No hay (outputs perdidos) | Checkpoints con rollback |
| **Auditoria** | Logs dispersos | Evidence Ledger inmutable |
| **Calidad** | Esperanza (agentes "deben" seguir estandar) | Garantia (quality checks obligatorios) |
| **Outputs Perdidos** | Problema actual (4 tareas) | Imposible (validacion de outputs) |

---

## MIGRACION DE v2.2 A FORGE v1.0

### Fase 1: Implementacion Core (Semanas 1-2)

**Entregables**:
- [ ] ForgeKernel (orchestrator principal)
- [ ] SchemaRegistry con 5 schemas
- [ ] PolicyKernel basico
- [ ] WorkGraphCompiler
- [ ] EvidenceLedger

**Criterio de Exito**: Puede parsear work graph, validar, compilar y generar execution plan

---

### Fase 2: Execution Layer (Semanas 3-4)

**Entregables**:
- [ ] TaskRunner
- [ ] ClaudeCodeAdapter
- [ ] Sistema de checkpoints
- [ ] Quality validators

**Criterio de Exito**: Puede ejecutar work graph simple de 1 tarea con validacion completa

---

### Fase 3: Integracion y Testing (Semanas 5-6)

**Entregables**:
- [ ] Suite de tests completa
- [ ] CLI para Forge (forge-cli)
- [ ] Migracion de proyecto existente (covid-research)
- [ ] Documentacion de usuario

**Criterio de Exito**: Proyecto covid-research se ejecuta completamente en Forge con evidencia verificable

---

### Fase 4: Produccion (Semana 7+)

**Entregables**:
- [ ] Coordinador actualizado para usar Forge
- [ ] Templates de work graphs
- [ ] Dashboards de monitoreo
- [ ] Politicas de produccion

**Criterio de Exito**: Forge es sistema de produccion, v2.2 deprecated

---

## EJEMPLO COMPLETO: COVID Research Project

### Work Graph Declarado

```json
{
 "version": "1.0",
 "project": {
 "id": "covid-research-20251227",
 "name": "Investigacion ClO2 vs COVID-19",
 "goal": "Analisis cientifico de selectividad molecular, farmacocinetica y ventana terapeutica del dioxido de cloro contra SARS-CoV-2"
 },
 "tasks": [
 {
 "id": "quimica-molecular",
 "role": "QuimicoMolecular",
 "contract": {
 "inputs": [],
 "outputs": [
 {"name": "analisis", "path": "reports/quimica_molecular_clo2.md"}
 ],
 "quality_checks": [
 {"type": "length", "config": {"min": 2000}},
 {"type": "reference_check", "config": {"min_references": 10}}
 ]
 }
 },
 {
 "id": "virologia-covid",
 "role": "VirologoSARSCoV2",
 "contract": {
 "inputs": [
 {"name": "quimica_base", "type": "artifact", "source": "quimica-molecular-output"}
 ],
 "outputs": [
 {"name": "analisis", "path": "reports/virologia_sarscov2.md"}
 ],
 "quality_checks": [
 {"type": "length", "config": {"min": 2000}}
 ]
 }
 },
 {
 "id": "sintesis-final",
 "role": "SintetizadorCientifico",
 "contract": {
 "inputs": [
 {"name": "quimica", "type": "artifact", "source": "quimica-molecular-output"},
 {"name": "virologia", "type": "artifact", "source": "virologia-covid-output"}
 ],
 "outputs": [
 {"name": "sintesis", "path": "reports/sintesis_selectividad_molecular.md"}
 ],
 "quality_checks": [
 {"type": "completeness", "config": {"required_sections": ["Resumen", "Hallazgos", "Conclusion"]}}
 ]
 }
 }
 ],
 "dependencies": [
 {"from": "quimica-molecular", "to": "virologia-covid"},
 {"from": "quimica-molecular", "to": "sintesis-final"},
 {"from": "virologia-covid", "to": "sintesis-final"}
 ],
 "artifacts": {
 "quimica-molecular-output": {
 "type": "file",
 "path": "tasks/quimica-molecular/reports/quimica_molecular_clo2.md"
 },
 "virologia-covid-output": {
 "type": "file",
 "path": "tasks/virologia-covid/reports/virologia_sarscov2.md"
 }
 }
}
```

### Execution Plan Compilado

```json
{
 "version": "1.0",
 "workgraph_id": "wg-a1b2c3d4",
 "state": "READY",
 "stages": [
 {
 "stage_id": 0,
 "tasks": [
 {
 "task_id": "quimica-molecular",
 "state": "READY",
 "agent_config": {
 "role": "QuimicoMolecular",
 "prompt_path": "projects/covid-research-20251227/tasks/quimica-molecular/prompt.md",
 "working_directory": "projects/covid-research-20251227/tasks/quimica-molecular/"
 }
 }
 ]
 },
 {
 "stage_id": 1,
 "tasks": [
 {
 "task_id": "virologia-covid",
 "state": "READY",
 "agent_config": {
 "role": "VirologoSARSCoV2",
 "prompt_path": "projects/covid-research-20251227/tasks/virologia-covid/prompt.md",
 "working_directory": "projects/covid-research-20251227/tasks/virologia-covid/"
 }
 }
 ]
 },
 {
 "stage_id": 2,
 "tasks": [
 {
 "task_id": "sintesis-final",
 "state": "READY",
 "agent_config": {
 "role": "SintetizadorCientifico",
 "prompt_path": "projects/covid-research-20251227/tasks/sintesis-final/prompt.md",
 "working_directory": "projects/covid-research-20251227/tasks/sintesis-final/"
 }
 }
 ]
 }
 ]
}
```

### Evidence Chain Generada

```
Record 1: WORKGRAPH_DECLARED
 - workgraph_id: wg-a1b2c3d4
 - actor: coordinator
 - timestamp: 2025-12-27T10:00:00Z

Record 2: WORKGRAPH_VALIDATED
 - validation_results: [all passed]
 - timestamp: 2025-12-27T10:00:01Z

Record 3: EXECUTION_PLAN_CREATED
 - total_stages: 3
 - total_tasks: 3
 - timestamp: 2025-12-27T10:00:02Z

Record 4: TASK_STARTED (quimica-molecular)
 - agent_id: agent-001
 - timestamp: 2025-12-27T10:00:05Z

Record 5: ARTIFACT_CREATED (quimica-molecular-output)
 - path: tasks/quimica-molecular/reports/quimica_molecular_clo2.md
 - checksum: sha256:abc123...
 - size: 4567 bytes
 - timestamp: 2025-12-27T10:15:30Z

Record 6: QUALITY_CHECK_PERFORMED (quimica-molecular, length)
 - passed: true
 - actual: 2456 words (> 2000 required)
 - timestamp: 2025-12-27T10:15:31Z

Record 7: QUALITY_CHECK_PERFORMED (quimica-molecular, references)
 - passed: true
 - actual: 15 references (> 10 required)
 - timestamp: 2025-12-27T10:15:32Z

Record 8: TASK_COMPLETED (quimica-molecular)
 - duration: 925 seconds
 - timestamp: 2025-12-27T10:15:33Z

Record 9: CHECKPOINT_CREATED (stage-0)
 - checkpoint_id: ckpt-001
 - trigger: stage_complete
 - timestamp: 2025-12-27T10:15:35Z

Record 10: TASK_STARTED (virologia-covid)
 ...

[Continua para todos los eventos]
```

---

## PROXIMOS PASOS

### Inmediato

1. **Revisar especificacion completa**
 - FORGE_ARCHITECTURE_v1.0.md
 - FORGE_INTERFACES_v1.0.md
 - Schemas JSON (schemas/)

2. **Aprobar o ajustar diseño**
 - Arquitectura de 7 capas
 - Interfaces propuestas
 - Garantias del sistema

3. **Decidir plan de implementacion**
 - Phased approach (4 fases)
 - Big bang (todo a la vez)
 - Hybrid (core primero, luego adapters)

### Implementacion (Si aprobado)

1. **Setup de desarrollo**
 ```bash
 # Crear estructura
 mkdir -p forge/{core,schemas,adapters,tests}

 # Copiar schemas
 cp schemas/*.json forge/schemas/

 # Inicializar modulos
 touch forge/core/{__init__,kernel,policy,compiler,runner,ledger}.py
 ```

2. **Test-Driven Development**
 - Escribir tests basados en interfaces
 - Implementar modulos para pasar tests
 - Iterar hasta cobertura completa

3. **Integracion incremental**
 - Empezar con work graph simple (1 task)
 - Añadir dependencias
 - Añadir gates y triggers
 - Escalar a proyecto completo

---

## CONCLUSIONES

### Fortalezas de Forge v1.0

1. **Determinismo**: Validacion antes de ejecucion elimina sorpresas
2. **Recuperabilidad**: Checkpoints permiten reanudar desde fallos
3. **Auditabilidad**: Evidence ledger proporciona trail completo
4. **Escalabilidad**: Arquitectura de capas permite extension
5. **Garantias**: Contratos formales proporcionan confianza

### Trade-offs

1. **Complejidad inicial**: Mas componentes que v2.2
2. **Overhead de declaracion**: Work graphs requieren mas especificacion
3. **Learning curve**: Desarrolladores deben aprender nuevos conceptos

### Recomendacion

**Proceder con implementacion** si:
- Proyectos requieren alta confiabilidad (outputs no pueden perderse)
- Equipos necesitan auditoria completa
- Escalabilidad futura es importante

**Mantener v2.2 mejorado** si:
- Proyectos son pequeños y ad-hoc
- Rapidez de iteracion es mas importante que garantias
- Equipo es pequeño (1-2 personas)

Para el caso de uso actual (investigacion cientifica con multiples agentes, outputs criticos), **Forge v1.0 es la opcion recomendada**.

---

**Version**: 1.0
**Fecha**: 2025-12-27
**Estado**: SPECIFICATION COMPLETE
**Autores**: Claude Sonnet 4.5 (Coordinador)
**Siguiente paso**: Aprobacion de usuario y inicio de implementacion
