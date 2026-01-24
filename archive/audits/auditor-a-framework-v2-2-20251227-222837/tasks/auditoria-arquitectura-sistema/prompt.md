# TAREA: AUDITORIA DE ARQUITECTURA ACTUAL v2.2

## TU ROL

Eres un Software Architect y System Designer especializado en análisis arquitectónico. Tu trabajo es analizar el diseño del framework v2.2 actual para identificar fortalezas, debilidades, y problemas arquitectónicos.

## OBJETIVO

Analizar la arquitectura del framework v2.2 actual (NO la propuesta Forge v1.0) para:
1. Entender cómo está diseñado el sistema
2. Identificar problemas arquitectónicos
3. Detectar violaciones de principios de diseño
4. Identificar fortalezas que deben preservarse
5. Recomendar qué rediseñar en la migración a Forge

## CONTEXTO REQUERIDO

LEE primero estos documentos para entender la arquitectura actual:

1. **README.md** - Visión general del framework v2.2
2. **CLAUDE.md** - Arquitectura del coordinador y agentes
3. **ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md** - Estructura de datos
4. **core/project_manager.py** - Componente principal
5. **core/framework_validator.py** - Sistema de validación
6. **core/task_manager.py** - Sistema deprecated

Estos documentos + código te darán la arquitectura completa.

## ANALISIS REQUERIDO

### 1. INVENTARIO DE COMPONENTES

Identifica todos los componentes del sistema:

**Componentes Core**:
- project_manager.py - ¿Qué responsabilidades tiene?
- framework_validator.py - ¿Qué valida y cuándo?
- task_manager.py (deprecated) - ¿Por qué fue reemplazado?
- reorganize_task_structure.py - ¿Qué problema resuelve?
- fix_project_structure.py - ¿Por qué es necesario?
- check_empty_reports.py - ¿Qué problema indica?
- audit_project.py - ¿Qué audita?
- analyze_inconsistencies.py - ¿Qué analiza?

**Componentes Conceptuales**:
- Coordinador (Claude principal)
- Agentes especializados
- Sistema de memoria (CLAUDE.md + backups)
- Sistema de hooks (settings.json)

Para cada componente:
- ¿Cuál es su responsabilidad principal?
- ¿Tiene una sola responsabilidad o múltiples?
- ¿Es necesario o es un "parche"?

### 2. RELACIONES ENTRE COMPONENTES

Analiza cómo se comunican:

**Dependencias**:
- ¿Qué módulo importa qué?
- ¿project_manager usa framework_validator?
- ¿framework_validator usa project_manager?
- ¿Hay dependencias circulares?

**Flujo de Datos**:
```
Usuario → Coordinador → ??? → Agentes → ???
```
Completa este flujo:
- ¿Cómo se crean proyectos?
- ¿Cómo se lanzan agentes?
- ¿Cómo se valida estructura?
- ¿Cómo se recuperan outputs?

**Acoplamiento**:
- ¿Los módulos están fuertemente acoplados?
- ¿Pueden funcionar independientemente?
- ¿Cambiar uno requiere cambiar otros?

### 3. SEPARACION DE CONCERNS

Analiza si se violan principios SOLID:

**Single Responsibility Principle**:
- ¿project_manager tiene una sola responsabilidad?
 - Crea proyectos
 - Crea tareas
 - Genera rutas
 - Registra outputs
 - Sanitiza nombres
 - Formatea contexto
 - ¿Demasiadas responsabilidades?

**Open/Closed Principle**:
- ¿Puedes agregar nuevos tipos de tareas sin modificar código?
- ¿Puedes agregar validaciones sin modificar framework_validator?

**Dependency Inversion**:
- ¿Los módulos dependen de abstracciones o de implementaciones concretas?

### 4. PROBLEMAS ARQUITECTONICOS CONOCIDOS

Analiza estos problemas conocidos:

**Problema 1: Outputs Perdidos**
- 4 tareas sin reportes
- ¿Por qué el sistema permite crear tareas sin outputs?
- ¿Dónde está la falla arquitectónica?
- ¿Es problema de validación? ¿De tracking? ¿De contratos?

**Problema 2: No Hay Tracking de Task IDs**
- No se registran agentes lanzados
- ¿Qué componente debería hacer esto?
- ¿Por qué no existe?
- ¿Es falta de un componente? ¿De diseño?

**Problema 3: Validación Post-Facto**
- framework_validator valida DESPUÉS de crear
- ¿Por qué no valida ANTES?
- ¿Dónde debería integrarse?
- ¿Es problema de arquitectura o de implementación?

**Problema 4: Múltiples Scripts de Corrección**
- reorganize_task_structure.py
- fix_project_structure.py
- check_empty_reports.py
- ¿Por qué son necesarios tantos scripts de corrección?
- ¿Indica que project_manager no crea estructura correcta?
- ¿Problema de diseño del componente?

**Problema 5: task_manager.py Deprecated**
- Fue reemplazado por project_manager.py
- ¿Por qué falló el diseño original?
- ¿Qué lecciones aprender?

### 5. FORTALEZAS ARQUITECTONICAS

Identifica qué SÍ funciona bien:

**Fortaleza Potencial 1: Separación Coordinador/Agentes**
- ¿Funciona bien la arquitectura multi-agente?
- ¿Los agentes son independientes?
- ¿El coordinador mantiene visión general?

**Fortaleza Potencial 2: Sistema de Memoria**
- CLAUDE.md + backups
- ¿Funciona bien?
- ¿Preserva contexto efectivamente?

**Fortaleza Potencial 3: Estructura de Proyectos**
- projects/[id]/tasks/[task]/
- ¿Es clara y navegable?
- ¿Escala bien?

**Fortaleza Potencial 4: project_manager API**
- create_project(), create_task(), get_task_report_path()
- ¿La API es clara?
- ¿Es fácil de usar?

### 6. PATRONES DE DISEÑO

Analiza patrones usados (o ausentes):

**Patrones Presentes**:
- ¿Usa Factory pattern?
- ¿Usa Repository pattern?
- ¿Usa Observer pattern?

**Patrones Ausentes que ayudarían**:
- ¿Necesita Strategy pattern?
- ¿Necesita Command pattern?
- ¿Necesita Observer para tracking?

### 7. ESCALABILIDAD Y MANTENIBILIDAD

**Escalabilidad**:
- ¿Puede manejar 100 tareas en un proyecto?
- ¿Puede manejar 10 proyectos simultáneos?
- ¿Qué se rompe primero al escalar?

**Mantenibilidad**:
- ¿Es fácil agregar features?
- ¿Es fácil corregir bugs?
- ¿Qué tan acoplado está el código?

## ESTRUCTURA DE OUTPUT

Reporte en: reports/analisis_arquitectura_sistema.md

```markdown
# AUDITORIA DE ARQUITECTURA - FRAMEWORK v2.2

## RESUMEN EJECUTIVO

Análisis arquitectónico del framework v2.2 actual para identificar fortalezas, debilidades, y guiar migración a Forge v1.0.

**Hallazgos principales**:
- Problemas arquitectónicos críticos: X
- Problemas de diseño: X
- Fortalezas identificadas: X
- Recomendaciones para migración: X

## ARQUITECTURA ACTUAL

### Diagrama de Componentes

```
┌─────────────────────────────────────────────┐
│ COORDINADOR (Claude principal) │
│ - Lee: CLAUDE.md │
│ - Gestiona: conversación de alto nivel │
└─────────────────┬───────────────────────────┘
 ->
 ┌────────────────┐
 │ ProjectManager │
 │ - create_project()
 │ - create_task()
 └────────┬───────┘
 ->
 [Completar diagrama basado en análisis]
```

### Responsabilidades por Componente

#### project_manager.py

**Responsabilidades actuales**:
1. Crear estructura de proyectos
2. Crear estructura de tareas
3. Generar rutas de archivos
4. Registrar outputs
5. Sanitizar nombres
6. Formatear contexto
7. [Lista completa]

**Análisis**:
- Responsabilidad principal: [identificar]
- Responsabilidades secundarias: [identificar]
- Violaciones SRP: [identificar si las hay]
- Acoplamiento: [bajo/medio/alto]

#### framework_validator.py

**Responsabilidades actuales**:
[Lista]

**Análisis**:
[Similar]

[Repetir para cada componente]

## PROBLEMAS ARQUITECTONICOS

### Problema 1: Outputs Perdidos (CRITICO)

**Descripción**:
4 tareas del proyecto COVID tienen reports/ vacío. Agentes ejecutaron pero outputs no se guardaron o se perdieron.

**Root Cause Arquitectónico**:
[Analizar la causa raíz desde perspectiva de diseño]

Posibles causas:
1. No hay contrato formal de outputs
 - project_manager no especifica outputs obligatorios
 - Agentes no saben qué deben producir
 - No hay validación de que outputs existan

2. No hay tracking de ejecución
 - Sistema no registra Task IDs
 - No hay forma de saber si agente completó
 - No hay validación post-ejecución

3. Validación post-facto inefectiva
 - framework_validator valida después de crear
 - No previene problemas, solo los detecta tarde

**Componentes Involucrados**:
- project_manager (no especifica contratos)
- framework_validator (validación tardía)
- Sistema de agentes (sin tracking)

**Impacto**:
- Trabajo perdido
- No hay confiabilidad
- Imposible depurar qué falló

**Recomendación Arquitectónica**:
[Qué rediseñar para resolver esto]

### Problema 2: No Hay Tracking de Agentes (CRITICO)

**Descripción**:
Sistema lanza agentes en nuevas terminales pero no registra Task IDs, Process IDs, o estado.

**Root Cause Arquitectónico**:
[Analizar]

**Recomendación Arquitectónica**:
[Qué componente nuevo necesita o qué rediseñar]

### Problema 3: Validación Reactiva en vez de Preventiva (ALTO)

**Descripción**:
framework_validator valida estructura DESPUÉS de crear, no ANTES.

**Root Cause Arquitectónico**:
[Analizar la separación entre creación y validación]

**Recomendación**:
[Cómo integrar validación en el flujo de creación]

### Problema 4: Proliferación de Scripts de Corrección (MEDIO)

**Descripción**:
Existen múltiples scripts para corregir estructura:
- reorganize_task_structure.py
- fix_project_structure.py
- check_empty_reports.py

**Root Cause Arquitectónico**:
Indica que project_manager.py no crea estructura correcta desde el inicio.

**Análisis**:
- ¿Por qué project_manager no crea README.md?
- ¿Por qué no crea reports/ subdirectory?
- ¿Por qué necesitamos scripts de corrección?

**Recomendación**:
[Qué debe hacer project_manager para no necesitar correcciones]

### Problema 5: task_manager.py Deprecated (ALTO)

**Descripción**:
Sistema original fue reemplazado por project_manager.

**Análisis**:
- ¿Qué falló en task_manager.py?
- ¿Por qué se necesitó reescribir?
- ¿Lecciones aprendidas?

**Recomendación**:
[Qué evitar en nueva arquitectura]

## FORTALEZAS ARQUITECTONICAS

### Fortaleza 1: [Título]

**Descripción**:
[Qué funciona bien]

**Por qué es una fortaleza**:
[Análisis]

**Preservar en Forge v1.0**:
[Cómo mantener esto en nueva arquitectura]

[Repetir para cada fortaleza]

## ANALISIS DE PRINCIPIOS DE DISEÑO

### Single Responsibility Principle (SRP)

**Componentes que CUMPLEN SRP**:
- [Lista]

**Componentes que VIOLAN SRP**:
- project_manager.py:
 - Hace: creación, validación, naming, formateo, registro
 - Debería: Solo gestionar ciclo de vida de proyectos
 - Validación debería: estar en componente separado
 - Naming debería: estar en componente separado

### Open/Closed Principle (OCP)

**Análisis**:
¿Puedes agregar nuevo tipo de tarea sin modificar project_manager?
- Actualmente: NO
- Para agregar validación custom: Modificar framework_validator
- Para agregar nuevo output format: Modificar project_manager

**Recomendación**:
[Cómo hacer sistema extensible]

### Dependency Inversion Principle (DIP)

**Análisis**:
¿Componentes dependen de abstracciones o de implementaciones?
- project_manager depende de: implementaciones concretas (Path, json, etc.)
- framework_validator depende de: implementaciones concretas

**Recomendación**:
[Introducir abstracciones donde sea necesario]

## ANALISIS DE PATRONES

### Patrones Presentes

**[Nombre del Patrón]**:
- Dónde se usa: [ubicación]
- Qué resuelve: [problema]
- Efectividad: [alta/media/baja]

### Patrones Ausentes que Ayudarían

**Repository Pattern**:
- Problema actual: Acceso directo a filesystem mezclado con lógica
- Beneficio: Separar persistencia de lógica de negocio
- Aplicación: Crear ProjectRepository, TaskRepository

**Command Pattern**:
- Problema actual: No hay registro de acciones ejecutadas
- Beneficio: Auditoría y rollback
- Aplicación: Cada operación como comando registrable

**Observer Pattern**:
- Problema actual: No hay tracking de estado de agentes
- Beneficio: Notificación de cambios de estado
- Aplicación: Agentes notifican cuando completan

## ESCALABILIDAD

### Análisis de Escalabilidad

**Escenario 1: 100 tareas en un proyecto**
- ¿Funciona?: [análisis]
- ¿Qué se rompe?: [identificar límites]
- ¿Solución?: [recomendación]

**Escenario 2: 10 proyectos simultáneos**
- ¿Funciona?: [análisis]
- ¿Límites?: [identificar]

**Escenario 3: Recuperación de 50 tareas fallidas**
- ¿Funciona?: NO (no hay mecanismo de recuperación)
- ¿Qué falta?: Sistema de checkpoints y rollback

## MANTENIBILIDAD

### Facilidad de Cambio

**Para agregar feature X**:
- Archivos a modificar: [X archivos]
- Complejidad: [alta/media/baja]
- Riesgo de romper existente: [alto/medio/bajo]

**Para corregir bug Y**:
- Facilidad de localizar: [fácil/difícil]
- Facilidad de corregir: [fácil/difícil]
- Riesgo de side effects: [alto/medio/bajo]

## RECOMENDACIONES PARA MIGRACION

### Componentes a PRESERVAR

1. **[Componente/Patrón]**
 - Por qué preservar: [razón]
 - Cómo migrar: [estrategia]

### Componentes a REDISEÑAR

1. **project_manager**
 - Problemas actuales: [lista]
 - Diseño propuesto: [separar responsabilidades]
 - Nueva arquitectura: [descripción]

2. **Sistema de Validación**
 - Problema actual: Post-facto
 - Diseño propuesto: Preventiva + Contratos formales
 - Nueva arquitectura: PolicyKernel de Forge

### Componentes a AGREGAR

1. **Task Tracker / Execution Manager**
 - No existe actualmente
 - Necesario para: Tracking de agentes, estado, outputs
 - Arquitectura propuesta: TaskRunner de Forge

2. **Evidence Ledger**
 - No existe actualmente
 - Necesario para: Auditoría completa
 - Arquitectura propuesta: EvidenceLedger de Forge

## COMPARACION: v2.2 vs Forge v1.0

### Problemas de v2.2 que Forge Resuelve

| Problema v2.2 | Cómo Forge lo Resuelve |
|---------------|------------------------|
| Outputs perdidos | Task Contracts + Validación obligatoria |
| No hay tracking | TaskRunner + Execution Plan |
| Validación tardía | PolicyKernel preventivo |
| No hay recuperación | Checkpoints + Rollback |
| No hay auditoría | Evidence Ledger |

### Fortalezas de v2.2 que Forge Preserva

| Fortaleza v2.2 | Cómo Forge la Preserva |
|----------------|------------------------|
| [Fortaleza 1] | [Mecanismo en Forge] |
| [Fortaleza 2] | [Mecanismo en Forge] |

## CONCLUSION

**Estado de la arquitectura v2.2**:
[Resumen de salud arquitectónica]

**Principales debilidades**:
1. [Debilidad crítica 1]
2. [Debilidad crítica 2]
3. [Debilidad crítica 3]

**Principales fortalezas**:
1. [Fortaleza 1]
2. [Fortaleza 2]

**Viabilidad de migración a Forge v1.0**:
[Alta/Media/Baja] - [Justificación]

**Recomendación final**:
[Proceder con migración / Mejorar v2.2 primero / Otro enfoque]
```

## CRITERIOS DE CALIDAD

- Análisis profundo, no superficial
- Identifica root causes, no solo síntomas
- Usa principios de diseño para justificar hallazgos
- Recomendaciones concretas y accionables
- Relaciona problemas actuales con soluciones Forge

## HERRAMIENTAS

- Read: leer código y documentación
- Grep: buscar patrones de diseño
- Análisis conceptual de arquitectura

## FORMATO

Profesional, sin emojis, markdown estándar.

## ENTREGABLE

1. Reporte en reports/analisis_arquitectura_sistema.md
2. Diagrama de componentes actual
3. Al menos 5 problemas arquitectónicos identificados
4. Al menos 3 fortalezas identificadas
5. Recomendaciones priorizadas para migración
