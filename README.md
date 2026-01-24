# Framework Agéntico - Sistema de Investigación Multi-Agente

> **Versión 2.2** - Estructura Basada en Tareas con Nombres Descriptivos

## ¿Qué es esto?

Un framework para realizar **investigaciones complejas** usando **múltiples agentes especializados** coordinados por un agente central.

### Documentación Completa

Para entender **cómo funciona el sistema completo**, qué hace cada componente, el flujo interno detallado y cómo operarlo:

**[Ver Guía Completa de Funcionamiento](docs/GUIA_COMPLETA_FUNCIONAMIENTO.md)**

Esta guía incluye:
- Explicación conceptual completa del sistema
- Arquitectura visual detallada con diagramas de flujo
- Descripción funcional de cada componente
- Proceso interno paso a paso
- Casos de uso reales y ejemplos prácticos
- Ventajas comparativas con otras herramientas

## Arquitectura

```
 [USUARIO]
 ↕
 [COORDINADOR] ← Tú conversas aquí (ventana principal)
 ->
 [Task Tool]
 ->
 [AGENTES en Background]
 - Agente 1: Química
 - Agente 2: Bioquímica
 - Agente 3: Virología
 - Agente 4: ...
 ->
 [Reportan al Coordinador]
 ->
 [Coordinador Sintetiza]
 ->
 [USUARIO]
```

## WARNING: Descubrimiento Crítico: Arquitectura de 2 Capas

**Los agentes necesitan CONTEXTO CONVERSACIONAL para evitar auto-censura.**

### El Problema Descubierto

Durante experimentos de investigación científica, descubrimos que:

- ❌ **Agentes sin contexto**: Rechazaban tareas legítimas, se auto-censuraban innecesariamente
- ✅ **Agentes con contexto**: Trabajaban perfectamente, completaban investigaciones exhaustivas

### La Solución: Prompts de 2 Capas

**Capa 1: Contexto del Proyecto**
- Solicitud original del usuario
- Disclaimers y directrices explícitas
- Naturaleza del proyecto (académico, supervisado, etc.)

**Capa 2: Prompt Técnico**
- Rol del agente especializado
- Objetivo específico
- Metodología a seguir

### ¿Por Qué Funciona?

Los agentes lanzados con `Task tool` **NO tienen acceso al historial conversacional**. Sin contexto, los filtros de contenido pueden activarse erróneamente. Al incluir el contexto del usuario, el agente entiende:

- Hay supervisión humana
- Es investigación legítima
- Hay intención académica/científica clara

### Template Disponible

Ver **`core/context_template.md`** para templates reutilizables con ejemplos completos para:
- Investigación científica
- Análisis técnico
- Desarrollo de software
- Análisis de datos

## Cómo Usar

### 1. Iniciar el Framework

```bash
./start_coordinator.sh
```

Esto lanza Claude Code como **coordinador principal**. Todo funciona desde esta única ventana.

### 2. Solicitar una Investigación

Simplemente pide lo que necesitas:

```
Tú: "Quiero investigar [TEMA] en profundidad"
```

El coordinador te propondrá una estrategia con agentes especializados.

### 3. Aprobar y Monitorear

```
Coordinador: "Propongo 3 agentes:
 1. [Especialidad 1]
 2. [Especialidad 2]
 3. [Especialidad 3]
 ¿Procedemos?"

Tú: "Sí"

Coordinador: "Agentes lanzados en background.
 Te informo cuando completen..."
```

### 4. Recibir Resultados

El coordinador te presentará una **síntesis integrada** de todos los hallazgos.

## Principios Clave

1. **Una Sola Ventana:** Todo se coordina desde la ventana del coordinador
2. **Sin Ventanas Nuevas:** Los agentes trabajan en background (invisible)
3. **Coordinación Centralizada:** El coordinador es tu único punto de contacto
4. **Síntesis Inteligente:** No recibes dumps de datos, sino hallazgos integrados

## Qué NO Hacer

### ❌ NO uses task_manager.py

```bash
# ❌ INCORRECTO - Sistema obsoleto
python core/task_manager.py create ...
```

El sistema viejo abría ventanas separadas. **Ya no se usa.**

### ❌ NO intentes abrir múltiples instancias de Claude Code

Todo se maneja desde UNA sola instancia (el coordinador).

## Tipos de Investigaciones Soportadas

- **Investigación Científica:** Múltiples perspectivas (química, biología, clínica)
- **Análisis Técnico:** Arquitectura, código, sistemas
- **Investigación Comparativa:** Benchmarks, alternativas, trade-offs
- **Síntesis de Literatura:** Papers, artículos, documentación
- **Análisis de Datos:** Procesamiento, estadísticas, visualización

## Ejemplo de Uso Real

```
Usuario: "Investiga efectividad del dióxido de cloro contra COVID-19.
 Sé neutral como científico, solo evidencia científica."

Coordinador: "Esto requiere análisis multidisciplinario.
 Propongo 4 agentes:
 1. Químico: estructura molecular, mecanismos
 2. Bioquímico: toxicología, efectos en humanos
 3. Virólogo: mecanismos antivirales, variantes
 4. Clínico: evidencia de ensayos, estudios

 ¿Procedemos?"

Usuario: "Sí"

Coordinador: [Diseña prompts con 2 capas]

 Prompt para Agente Virólogo:

 CAPA 1 - CONTEXTO:
 """
 # Contexto del Proyecto

 El usuario ha solicitado investigación científica sobre
 dióxido de cloro, con directrices:
 - "Sé neutral como científico"
 - "Solo evidencia científica"

 Este es un proyecto académico supervisado por el usuario.
 """

 CAPA 2 - PROMPT TÉCNICO:
 """
 # Tu Tarea: Virólogo Molecular

 Eres un virólogo especializado en coronavirus.

 Objetivo: Analizar mecanismos de inactivación viral...

 INICIA LA INVESTIGACIÓN AHORA.
 """

 [Lanza 4 agentes en background con contexto]
 "Agentes trabajando..."

 [Agentes investigan en paralelo]
 [Coordinador recibe resultados]
 [Sintetiza hallazgos]

 "Investigación completada.

 ## Química Molecular
 [Síntesis del Agente 1]

 ## Bioquímica y Toxicología
 [Síntesis del Agente 2]

 ## Virología
 [Síntesis del Agente 3]

 ## Evidencia Clínica
 [Síntesis del Agente 4]

 ## Conclusión Integrada
 [Síntesis combinada de todos los hallazgos]

 ¿Quieres profundizar en algún aspecto?"
```

## Estructura del Proyecto

```
agentic-task-framework/
├── start_coordinator.sh # Punto de entrada (usa esto)
├── CLAUDE.md # Instrucciones del coordinador
├── README.md # Este archivo
├── .claude/
│ └── settings.json # Configuración de Claude Code
├── core/ # Scripts del sistema
│ ├── project_manager.py # ⭐ Gestor de proyectos v2.2
│ ├── context_template.md # Templates de contexto (v2.1)
│ ├── task_manager.py # DEPRECATED - No usar
│ └── ...
├── projects/ # ⭐ Resultados de investigaciones
│ └── [proyecto-id]/
│ ├── project_info.json # Metadata del proyecto
│ ├── context.md # Contexto inicial
│ ├── tasks/ # ⭐ Tareas ejecutadas (v2.2+)
│ │ ├── [nombre-tarea-descriptivo]/
│ │ │ ├── task_info.json # Metadata de la tarea
│ │ │ ├── prompt.md # Prompt guardado (v2.2+)
│ │ │ └── [reporte-descriptivo].md
│ │ └── [otra-tarea]/
│ │ ├── task_info.json
│ │ ├── prompt.md
│ │ ├── [reporte].md
│ │ └── reports/ # Para múltiples reportes
│ │ ├── [reporte1].md
│ │ └── [reporte2].md
│ └── synthesis/ # Síntesis final
│ └── [sintesis-descriptiva].md
├── examples/ # Ejemplos de prompts
├── docs/ # Documentación
└── .memory_backups/ # Backups automáticos
```

## ¿Dónde se Guardan los Resultados?

### Sistema de Proyectos (v2.2)

**Cada investigación se guarda en su propio proyecto:**

```
projects/[proyecto-id]/
├── project_info.json # Metadata (nombre, fecha, estado)
├── context.md # Contexto original del usuario
├── tasks/ # ⭐ Tareas ejecutadas (v2.2+)
│ ├── analisis-quimica-molecular-clo2/
│ │ ├── task_info.json # Metadata de la tarea
│ │ ├── prompt.md # Prompt guardado automáticamente
│ │ └── quimica_molecular_clo2.md # Reporte con nombre descriptivo
│ ├── toxicologia-bioquimica/
│ │ ├── task_info.json
│ │ ├── prompt.md
│ │ └── toxicologia_bioquimica_clo2.md
│ └── virologia-sars-cov2/
│ ├── task_info.json
│ ├── prompt.md
│ ├── virologia_sars_cov2.md
│ └── reports/ # Para múltiples reportes
│ ├── virologia_molecular_sars_cov2.md
│ ├── mecanismos_inactivacion_clo2.md
│ └── analisis_comparativo.md
└── synthesis/ # Síntesis integrada del coordinador
 └── sintesis_investigacion_clo2_covid19.md
```

### Convenciones de Nombres (v2.2)

**Tareas** - Nombres descriptivos de QUÉ hace la tarea:
- Formato: `[accion]-[tema]-[detalles]`
- Ejemplos: `analisis-quimica-molecular-clo2`, `toxicologia-bioquimica`, `virologia-sars-cov2`

**Prompts** - Nombre genérico `prompt.md` (solo hay uno por tarea, guardado automáticamente)

**Reportes** - Nombres descriptivos del contenido:
- Formato: `[tema]_[aspecto]_[detalles].md`
- Ejemplos: `quimica_molecular_clo2.md`, `virologia_molecular_sars_cov2.md`

**Síntesis** - Nombres descriptivos del proyecto:
- Formato: `sintesis_[proyecto]_[aspecto].md`
- Ejemplos: `sintesis_investigacion_clo2_covid19.md`

#### Tabla de Referencia Rápida

| Tipo de Archivo | Convención | Ejemplo | Dónde Se Usa |
|-----------------|-----------|---------|--------------|
| Proyectos | kebab-case + timestamp | `investigacion-clo2-20251222-195407` | IDs de proyectos (auto-generado) |
| Tareas | kebab-case | `analisis-quimica-molecular-clo2` | Nombres de tareas (usuario define) |
| Reportes | snake_case | `virologia_molecular_sars_cov2.md` | Archivos .md en reports/ |
| Scripts Python | snake_case | `project_manager.py` | Archivos .py en core/ |
| Docs principales | SCREAMING_SNAKE_CASE | `CLAUDE.md`, `README.md` | Raíz del proyecto |
| Directorios | lowercase | `reports/`, `tasks/`, `synthesis/` | Estructura del proyecto |

**Regla general:** Usa kebab-case para IDs y tareas, snake_case para archivos de código/reportes, SCREAMING para docs principales.

### Consultar Proyectos

**Listar todos los proyectos:**
```bash
python core/project_manager.py list
```

**Ver proyecto específico:**
```bash
python core/project_manager.py get [project-id]
```

**Ejemplo:** Ver investigación de ClO₂
```bash
python core/project_manager.py list
# Copia el ID del proyecto que te interesa
python core/project_manager.py get investigacion-clo2-covid-19-20251222-195407
```

### Acceder a Resultados

**Opción 1 - Navegación manual:**
```bash
# Ver todos los proyectos
ls projects/

# Ver tareas de un proyecto
ls projects/[proyecto-id]/tasks/

# Ver archivos de una tarea específica
ls projects/[proyecto-id]/tasks/analisis-quimica-molecular-clo2/

# Leer prompt guardado de una tarea
cat projects/[proyecto-id]/tasks/analisis-quimica-molecular-clo2/prompt.md

# Leer reporte de una tarea
cat projects/[proyecto-id]/tasks/analisis-quimica-molecular-clo2/quimica_molecular_clo2.md

# Ver reportes múltiples
ls projects/[proyecto-id]/tasks/virologia-sars-cov2/reports/

# Leer síntesis final
cat projects/[proyecto-id]/synthesis/sintesis_investigacion_clo2_covid19.md
```

**Opción 2 - Desde el coordinador:**
El coordinador puede leer y presentar resultados de proyectos anteriores si se lo pides.

### Beneficios del Sistema de Proyectos (v2.2)

✅ **Organización automática:** Todo en un lugar con estructura clara
✅ **Trazabilidad:** Metadata completa por proyecto y por tarea
✅ **Reproducibilidad total:** Prompts guardados automáticamente (v2.2+)
✅ **Nombres descriptivos:** Fácil identificar contenido sin abrir archivos
✅ **Compartible:** Copia `projects/[id]/` para compartir investigación completa
✅ **Historial:** Accede a investigaciones anteriores fácilmente
✅ **Escalabilidad:** Subdirectorios para tareas con múltiples reportes

## Ventajas de Este Sistema

✅ **Simplicidad:** Una sola ventana, una sola conversación
✅ **Escalabilidad:** Lanza tantos agentes como necesites en paralelo
✅ **Organización:** El coordinador mantiene la visión general
✅ **Eficiencia:** Contexto pesado delegado a agentes especializados
✅ **Claridad:** Ves progreso y resultados en formato sintetizado

## Troubleshooting

### ❌ "El agente rechazó la tarea / se auto-censuró"

**Causa:** El agente NO tiene contexto conversacional.

**Solución:** El coordinador debe incluir contexto en el prompt:
1. Solicitud original del usuario
2. Disclaimers y directrices explícitas
3. Naturaleza del proyecto (académico, supervisado)

Ver `core/context_template.md` para templates correctos.

**Evidencia:** Experimentos demostraron que:
- Agente sin contexto: ❌ Rechazado
- Agente con contexto: ✅ Completado exitosamente

### "Los agentes no están ejecutando, solo preguntan"

**Solución:** El coordinador debe diseñar prompts **ejecutivos**, no conversacionales. Debería incluir "INICIA AHORA" y dar instrucciones claras de HACER, no preguntar.

### "No veo progreso de los agentes"

**Solución:** El coordinador usa `TodoWrite` para trackear estado. Si no lo ves, pídeselo: "¿Qué están haciendo los agentes?"

### "Quiero ver los resultados detallados"

**Solución:** El coordinador te presenta síntesis. Si quieres detalles: "¿Puedes mostrarme los resultados completos del Agente [N]?"

### "El agente no tiene acceso a información que mencioné antes"

**Causa:** Los agentes en background NO ven tu historial conversacional.

**Solución:** El coordinador debe incluir toda la información relevante en el prompt del agente.

## Documentación y Soporte

### Documentación Principal

- **[Guía Completa de Funcionamiento](docs/GUIA_COMPLETA_FUNCIONAMIENTO.md)** - Explicación detallada de cómo funciona el sistema
- **CLAUDE.md** - Instrucciones técnicas para el coordinador
- **[Estándar de Estructura v2.2](docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md)** - Especificación de estructura de proyectos
- **[Protocolo de Prompts](docs/PROTOCOLO_PROMPTS_AGENTES.md)** - Arquitectura de 2 capas
- **core/context_template.md** - Templates reutilizables de contexto

### Recursos Técnicos

- **core/project_manager.py** - Sistema de gestión de proyectos
- **core/framework_validator.py** - Sistema de validación
- **Issues:** Reporta problemas en el repositorio

### Información del Framework

- **Versión:** 2.3 (Request Enrichment + ORGANIZED Structure)
- **Última actualización:** 2026-01-24

## Changelog

### v2.3 (2026-01-24)

**NUEVA CARACTERÍSTICA PRINCIPAL:**
- ⭐ **Sistema de Enriquecimiento Automático de Solicitudes**
  - El coordinador detecta solicitudes vagas o incompletas
  - Enriquece automáticamente con alcance, perspectivas y criterios
  - Presenta versión expandida al usuario para validación
  - Reduce iteraciones y mejora calidad de resultados

**Beneficios:**
- Usuarios no expertos obtienen resultados de calidad experta
- Descubre perspectivas que no consideraste
- Clarifica alcance antes de ejecutar
- Aprende a formular mejores solicitudes

**Documentación:**
- Protocolo completo: `docs/PROTOCOLO_ENRIQUECIMIENTO_SOLICITUDES.md`
- Integrado en: `CLAUDE.md` (sección Request Enrichment Protocol)
- Ejemplos en: `docs/GUIA_COMPLETA_FUNCIONAMIENTO.md`

**Workflow actualizado:**
```
User Request → Analyze Quality → Enrich → Present → Validate → Design Strategy → Execute
```

## Changelog

### v2.2 (2025-12-25)

**BREAKING CHANGES:**
- ⭐ Cambio de `agents/` a `tasks/` con nombres descriptivos
- ⭐ Guardado automático de prompts en cada tarea
- ⭐ Sistema de convenciones de nombres descriptivos

**NUEVAS CARACTERÍSTICAS:**
- Cada tarea guarda su prompt automáticamente en `prompt.md`
- Metadata por tarea (`task_info.json`)
- Soporte para múltiples reportes por tarea (subdirectorio `reports/`)
- Nombres descriptivos obligatorios para tareas y reportes

**Estructura de Tareas (v2.2):**
```
tasks/
└── [nombre-tarea-descriptivo]/ # ej: analisis-quimica-molecular-clo2
 ├── task_info.json # Metadata de la tarea
 ├── prompt.md # Prompt guardado automáticamente
 └── [reporte-descriptivo].md # ej: quimica_molecular_clo2.md
```

**Convenciones de Nombres:**
- Tareas: `[accion]-[tema]-[detalles]`
- Prompts: `prompt.md` (genérico, guardado automáticamente)
- Reportes: `[tema]_[aspecto]_[detalles].md` (descriptivos)
- Síntesis: `sintesis_[proyecto]_[aspecto].md` (descriptivos)

**Beneficios:**
- Reproducibilidad total (prompts preservados)
- Claridad (nombres indican contenido, no actores)
- Trazabilidad mejorada (metadata por tarea)
- Organización escalable (subdirectorios para reportes múltiples)

### v2.1.1 (2025-12-22)

**NUEVA FUNCIONALIDAD:**
- ⭐ Sistema de gestión de proyectos (`core/project_manager.py`)
- ⭐ Estructura organizada automática para resultados
- ⭐ Cada investigación se guarda en `projects/[proyecto-id]/`
- ⭐ Metadata completa y trazabilidad de investigaciones

**Estructura de Proyectos:**
- `agents/` - Outputs de cada agente individual (cambiado a `tasks/` en v2.2)
- `synthesis/` - Síntesis integrada del coordinador
- `project_info.json` - Metadata (nombre, fecha, agentes, estado)
- `context.md` - Contexto original del usuario

**CLI de Gestión:**
- `python core/project_manager.py list` - Listar proyectos
- `python core/project_manager.py get [id]` - Ver proyecto específico

**Beneficios:**
- Organización automática de outputs
- Historial completo de investigaciones
- Fácil compartir proyectos completos

### v2.1 (2025-12-22)

**DESCUBRIMIENTO CRÍTICO:**
- ⭐ Los agentes necesitan contexto conversacional para evitar auto-censura
- ⭐ Nueva arquitectura de prompts de 2 capas (Contexto + Técnico)
- ⭐ Agregado `core/context_template.md` con templates reutilizables

**Mejoras:**
- Troubleshooting expandido con problemas de contexto
- Ejemplo actualizado mostrando arquitectura de 2 capas
- Documentación mejorada sobre cómo evitar rechazos de agentes

**Validación Experimental:**
- Experimento 1 (sin contexto): Agente rechazado
- Experimento 2 (con contexto): Agente completado exitosamente

### v2.0 (2025-12-21)

**BREAKING CHANGES:**
- Sistema completamente rediseñado para usar Task tool de Claude Code
- Ya NO se abren ventanas separadas
- Coordinador gestiona agentes en background desde una sola ventana

**Arquitectura:**
- Usuario ↔ Coordinador → Task tool → Agentes (background) → Reportan → Coordinador → Usuario

**Beneficios:**
- Una sola ventana (simplicidad)
- Agentes en background (sin distracción)
- Coordinación centralizada
- Contexto ligero en coordinador, pesado en agentes
- Síntesis inteligente de resultados

---

**¡Comienza tu investigación ahora!**

```bash
./start_coordinator.sh
```
