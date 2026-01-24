#!/usr/bin/env python3
"""
Reconstrucción retroactiva de prompts de auditorías de Enero 2026

Este script crea un proyecto formal que documenta las auditorías del 14-17 de enero,
reconstruyendo los prompts basándose en el contenido de los reportes generados.

Objetivo: Establecer trazabilidad para auditorías que se hicieron antes de implementar
el protocolo de "Always Use ProjectManager for Audits".
"""

import sys
from pathlib import Path
from datetime import datetime

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.project_manager import ProjectManager


def reconstruct_audit_prompts():
    """Reconstruye los prompts de las auditorías de enero."""

    # CRÍTICO: Auditorías del framework van a archive/audits/
    pm = ProjectManager(base_dir="archive/audits")

    print("=" * 60)
    print("RECONSTRUCCIÓN DE PROMPTS - AUDITORÍAS ENERO 2026")
    print("=" * 60)
    print()

    # Create retroactive project
    print("Creando proyecto retroactivo para auditorías de enero...")
    project = pm.create_project(
        name="Auditorías Enero 2026 (Retroactivo)",
        user_request="""Documentar retroactivamente las auditorías realizadas del 14-17 de enero de 2026.

Estas auditorías se realizaron inmediatamente después de implementar ProjectManager,
por lo que los prompts no fueron guardados formalmente. Este proyecto reconstruye
los prompts basándose en el contenido de los reportes generados para establecer
trazabilidad completa.""",
        context="""Contexto histórico:
- 14 Enero: Primera auditoría completa (28 problemas identificados)
- 14 Enero: Auditoría sistémica del proyecto YouTube (5 fallos críticos)
- 15 Enero: Análisis exhaustivo con agente ae7984d (42 páginas)
- 16 Enero: Auditoría de virtual environment (problema sistémico)
- 17 Enero: Review completo histórico

Este proyecto es RETROACTIVO - los reportes ya existen en reports/,
este proyecto solo documenta los prompts que debieron haberse guardado."""
    )

    print(f"✓ Proyecto creado: {project['id']}")
    print()

    # Task 1: Auditoría Framework Completa (14 Enero)
    print("Reconstruyendo Tarea 1: Auditoría Framework Completa (14 Enero)...")

    prompt_auditoria_completa = """# Auditoría Completa del Framework v2.2

## Layer 1: Conversational Context

El usuario solicitó una auditoría completa del Agentic Task Framework v2.2 para identificar
todos los problemas, inconsistencias, bugs y deuda técnica antes de continuar con desarrollo.

**Contexto de la solicitud:**
- Framework en transición de v2.0 a v2.2 ORGANIZED
- Proyectos reales ejecutados (COVID-19, YouTube Extension)
- Necesidad de baseline limpio antes de producción
- Supervisión académica y de desarrollo
- Análisis exhaustivo autorizado

**Naturaleza del trabajo:**
Este es un análisis técnico de código, arquitectura y documentación de un framework
open-source en desarrollo. El objetivo es mejorar la calidad y robustez del sistema.

**Human oversight:**
El coordinador (Claude Sonnet 4.5) supervisa todo el proceso y sintetiza los hallazgos
para presentarlos al usuario de forma integrada.

## Layer 2: Technical Task

### Objective

Realizar auditoría exhaustiva del Agentic Task Framework v2.2 que identifique:
1. Bugs críticos de runtime
2. Inconsistencias entre código y documentación
3. Problemas de estructura de datos
4. Deuda técnica acumulada
5. Violaciones del estándar v2.2 ORGANIZED

### Scope

**Archivos a auditar:**
- `core/project_manager.py` (~600 líneas)
- `core/framework_validator.py` (~800 líneas)
- `CLAUDE.md` (~400 líneas)
- `README.md` (~300 líneas)
- Todos los `project_info.json` en `projects/`
- Estructura de directorios completa

**Áreas de análisis:**
1. **Estructura de directorios**: Validar conformidad v2.2 ORGANIZED
2. **Código Python**: Buscar bugs, métodos no implementados, encoding issues
3. **Documentación**: Identificar ejemplos incorrectos, información desactualizada
4. **Metadata**: Inconsistencias en project_info.json, task_info.json
5. **Nomenclatura**: Validar convenciones de nombres
6. **Validación**: Verificar que FrameworkValidator funciona correctamente

### Methodology

1. **Análisis de estructura**
   - Revisar todos los directorios en `projects/`
   - Verificar conformidad con v2.2 ORGANIZED
   - Identificar proyectos incompletos o mal formados

2. **Análisis de código**
   - Leer completamente project_manager.py
   - Leer completamente framework_validator.py
   - Buscar métodos no implementados (pass, NotImplementedError)
   - Verificar manejo de excepciones
   - Identificar hardcoded values

3. **Análisis de documentación**
   - Comparar ejemplos en CLAUDE.md con código real
   - Verificar que firmas de métodos coincidan
   - Identificar información desactualizada

4. **Análisis de metadata**
   - Revisar todos los project_info.json
   - Buscar inconsistencias en rutas
   - Verificar estructura de datos

5. **Clasificación y priorización**
   - Clasificar problemas: CRÍTICO, ALTO, MEDIO, BAJO
   - Estimar esfuerzo de corrección
   - Evaluar impacto de cada problema

### Expected Output

**Report structure:**

```markdown
# AUDITORÍA COMPLETA DEL FRAMEWORK AGÉNTICO v2.2

## RESUMEN EJECUTIVO
- Total de problemas encontrados
- Clasificación por criticidad
- Estado general del framework
- Recomendación principal

## 1. ESTRUCTURA DE DIRECTORIOS
[Hallazgos con ejemplos específicos]

## 2. CÓDIGO DEL CORE
[Bugs, métodos no implementados, issues]

## 3. DOCUMENTACIÓN
[Inconsistencias, ejemplos incorrectos]

## 4. METADATA Y ESTRUCTURA DE DATOS
[Problemas en JSON, rutas, nomenclatura]

## MATRIZ DE PRIORIZACIÓN COMPLETA
[Tabla con todos los problemas clasificados]

## PLAN DE CORRECCIÓN RECOMENDADO
- FASE 1: CRÍTICOS (inmediato)
- FASE 2: ALTOS (esta semana)
- FASE 3: MEDIOS (este mes)
- FASE 4: BAJOS (próximo mes)

## CONCLUSIÓN
[Estado general y recomendaciones]
```

**Criticality criteria:**
- **CRÍTICO**: Causa runtime crash, pérdida de datos, o violación total del estándar
- **ALTO**: Impacta usabilidad, portabilidad, o calidad significativamente
- **MEDIO**: Deuda técnica, inconsistencias menores
- **BAJO**: Mejoras opcionales, optimizaciones

**Minimum length:** 5,000 palabras (~10-15 páginas)

### Success Criteria

✅ Todos los archivos core analizados completamente
✅ Todos los proyectos en projects/ revisados
✅ Mínimo 20 problemas identificados con ejemplos específicos
✅ Cada problema tiene: ubicación, impacto, criticidad, solución propuesta
✅ Plan de corrección estructurado en fases
✅ Reporte guardado en ubicación correcta

### Output Location

**CRITICAL:** Save your complete report to:
`{report_path}`

This path is ABSOLUTE. Use it exactly as provided.

### Validation Checklist

Before completing, verify:
- [ ] Report file created at exact path specified
- [ ] Content > 5,000 words
- [ ] All sections completed
- [ ] Specific code examples included (file:line)
- [ ] Criticality justified for each problem
- [ ] Plan de corrección detallado
"""

    task1 = pm.create_task(
        project_id=project["id"],
        task_name="auditoria-framework-completa-20260114",
        task_description="Auditoría exhaustiva del framework v2.2 - 28 problemas identificados",
        prompt=prompt_auditoria_completa.format(
            report_path=str(Path.cwd() / "reports" / "AUDITORIA_FRAMEWORK_COMPLETA_20260114.md")
        )
    )

    print(f"✓ Tarea 1 creada: {task1['task_name']}")
    print(f"  ℹ Reporte original en: reports/AUDITORIA_FRAMEWORK_COMPLETA_20260114.md")
    print(f"  (No registrado - proyecto retroactivo)")
    print()

    # Task 2: Auditoría Sistémica (14 Enero)
    print("Reconstruyendo Tarea 2: Auditoría Sistémica (14 Enero)...")

    prompt_audit_sistemico = """# Auditoría Sistémica - Proyecto YouTube Ad-Skip Extension

## Layer 1: Conversational Context

Durante la ejecución del proyecto YouTube Ad-Skip Extension, se identificaron múltiples
fallos en el comportamiento de los agentes background que sugieren problemas sistémicos
en el framework v2.2.

**Contexto de la solicitud:**
- Proyecto real: YouTube Ad-Skip Extension (5 agentes lanzados)
- Agentes crearon proyectos duplicados
- Reportes no guardados correctamente
- Pérdida de trazabilidad

**El usuario autorizó:**
- Análisis post-mortem del proyecto
- Identificación de fallos sistémicos
- Documentación de antipatrones observados
- Propuesta de correcciones al protocolo

**Naturaleza del análisis:**
Este es un análisis técnico de un fallo operacional en un framework de desarrollo.
El objetivo es prevenir recurrencia mediante correcciones al sistema.

**Supervisión:**
El coordinador documenta el análisis para mejorar el framework.

## Layer 2: Technical Task

### Objective

Identificar y documentar todos los **fallos sistémicos** observados durante la ejecución
del proyecto YouTube Ad-Skip Extension que indican problemas arquitectónicos o de
protocolo en el framework v2.2.

### Context: What Happened

**Proyecto:** youtube-skip-ads-extension-20260113-200039
**Fecha:** 2026-01-14
**Comportamiento observado:**
1. Agentes background crearon proyectos duplicados
2. Rutas relativas en prompts causaron confusión
3. Agentes alcanzaron rate limit y no guardaron reportes
4. Coordinador no detectó el fallo
5. Coordinador no registró reportes con ProjectManager

### Scope

**Analizar:**
- Estructura de proyectos creada (verificar duplicados)
- Prompts enviados a agentes (buscar rutas relativas)
- Flujo de validación post-ejecución (¿existe?)
- Protocolo de registro de reportes (¿se siguió?)
- Logs/evidencia del comportamiento incorrecto

**NO analizar:**
- Contenido específico del proyecto YouTube (fuera de scope)
- Código de los agentes (enfocarse en protocolo del coordinador)

### Methodology

1. **Forensic Analysis**
   - Revisar estructura de directorios en `projects/youtube-*`
   - Contar proyectos duplicados
   - Examinar contenido de cada proyecto

2. **Root Cause Analysis**
   - ¿Por qué agentes crearon proyectos duplicados?
   - ¿Por qué rutas relativas fallaron?
   - ¿Por qué validación post-ejecución no existió?
   - ¿Qué parte del protocolo NO se siguió?

3. **Protocol Review**
   - Revisar CLAUDE.md: ¿Especifica cómo dar rutas a agentes?
   - Revisar CLAUDE.md: ¿Existe paso de validación post-agente?
   - Revisar CLAUDE.md: ¿Es explícito sobre register_task_report()?

4. **Impact Assessment**
   - ¿Qué datos se perdieron?
   - ¿Cuál es el riesgo de recurrencia?
   - ¿Esto afecta otros proyectos?

### Expected Output

**Report structure:**

```markdown
# Auditoría Sistémica del Framework v2.2
## Sesión: YouTube Ad-Skip Extension Project

## Resumen Ejecutivo
- Total de fallos sistémicos identificados
- Impacto crítico
- Acción requerida

## Problemas Identificados

### P1: [Nombre del fallo] [CRITICIDAD]
**Evidencia:** [Archivos, directorios, logs]
**Causa Raíz:** [Análisis de por qué ocurrió]
**Protocolo Violado:** [Qué parte de CLAUDE.md no se siguió]
**Impacto:** [Consecuencias]
**Solución Propuesta:** [Cómo prevenir]

[... para cada fallo]

## Correcciones Requeridas

### Código
[Cambios necesarios en project_manager.py, etc]

### Protocolo
[Actualizaciones necesarias en CLAUDE.md]

### Validaciones
[Nuevas validaciones a implementar]

## Conclusión
[Severidad, urgencia, próximos pasos]
```

**Minimum length:** 3,000 palabras

### Success Criteria

✅ Todos los fallos sistémicos documentados con evidencia
✅ Root cause analysis completo para cada fallo
✅ Soluciones propuestas concretas
✅ Priorización de correcciones
✅ Reporte guardado correctamente

### Output Location

**CRITICAL:** Save your complete report to:
`{report_path}`

### Validation Checklist

Before completing:
- [ ] Evidencia verificada (archivos existen)
- [ ] Root cause analysis profundo
- [ ] Soluciones son implementables
- [ ] Reporte > 3,000 palabras
"""

    task2 = pm.create_task(
        project_id=project["id"],
        task_name="auditoria-sistemica-youtube-20260114",
        task_description="Auditoría sistémica post-mortem del proyecto YouTube - 5 fallos críticos",
        prompt=prompt_audit_sistemico.format(
            report_path=str(Path.cwd() / "reports" / "AUDIT_SISTEMICO_20260114.md")
        )
    )

    print(f"✓ Tarea 2 creada: {task2['task_name']}")
    print(f"  ℹ Reporte original en: reports/AUDIT_SISTEMICO_20260114.md")
    print(f"  (No registrado - proyecto retroactivo)")
    print()

    # Task 3: Análisis Exhaustivo (15 Enero) - Agente ae7984d
    print("Reconstruyendo Tarea 3: Análisis Exhaustivo (15 Enero - Agente ae7984d)...")

    prompt_analisis_exhaustivo = """# Análisis Exhaustivo del Agentic Task Framework v2.2

## Layer 1: Conversational Context

El usuario, después de revisar las auditorías del 14 de enero, solicitó un análisis
EXHAUSTIVO y COMPLETO del framework para convertirse en experto absoluto del sistema
e identificar TODAS las inconsistencias e incongruencias.

**Contexto de la solicitud:**
- Ya se realizaron 2 auditorías previas (28 problemas + 5 fallos sistémicos)
- Usuario quiere análisis MÁS PROFUNDO que las anteriores
- Objetivo: Crear baseline completo antes de implementar correcciones
- Necesidad de documentación exhaustiva (40+ páginas)
- Análisis autorizado de código open-source en desarrollo

**El usuario específicamente pidió:**
> "Análisis exhaustivo y completo del proyecto, convertirte en experto del framework,
> identificar todas las inconsistencias e incongruencias"

**Naturaleza del trabajo:**
Análisis técnico profundo de arquitectura, código, documentación y conformidad
estructural de un framework de investigación multi-agente.

**Supervisión:**
El coordinador sintetizará los hallazgos y presentará roadmap al usuario.

## Layer 2: Technical Task

### Objective

Realizar el análisis MÁS EXHAUSTIVO posible del Agentic Task Framework v2.2:
- Comprender arquitectura completa
- Analizar TODO el código línea por línea
- Validar conformidad estructural de TODOS los proyectos
- Identificar inconsistencias cross-system
- Producir documentación de referencia completa
- Crear roadmap detallado de correcciones

### Scope (MÁXIMO)

**Código a analizar (línea por línea):**
- `core/project_manager.py` (TODAS las ~600 líneas)
- `core/framework_validator.py` (TODAS las ~800 líneas)
- `core/session_summary.sh`
- `core/init_memory.sh`
- Scripts en `scripts/`

**Documentación a analizar:**
- `CLAUDE.md` (COMPLETO)
- `README.md` (COMPLETO)
- `docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md`
- `docs/CHECKLIST.md`
- Todos los comentarios inline en código

**Proyectos a validar (TODOS):**
- `investigaci-n-clo-covid-19-20251222-195407/`
- `youtube-skip-ads-extension-*` (TODOS los duplicados)
- `interacciones-clo-in-vivo-*`
- Proyectos en `archive/audits/`

**Análisis cross-system:**
- ¿ProjectManager implementa lo que CLAUDE.md promete?
- ¿FrameworkValidator valida lo que especificación dice?
- ¿Proyectos reales cumplen v2.2 ORGANIZED?
- ¿Documentación refleja código actual?

### Methodology

1. **Architecture Deep Dive**
   - Diagramar flujo completo: User → Coordinator → ProjectManager → Agents → Reports
   - Identificar TODOS los componentes y sus interacciones
   - Documentar principios arquitectónicos
   - Evaluar solidez de la arquitectura

2. **Code Review Exhaustivo**
   - Leer project_manager.py completo
   - Analizar cada método: firma, docstring, implementación, edge cases
   - Buscar: bugs, métodos vacíos, TODOs, hardcoded values, encoding issues
   - Evaluar calidad: exception handling, logging, type hints

   - Leer framework_validator.py completo
   - Validar que cada validación funciona correctamente
   - Identificar validaciones faltantes

3. **Documentation Analysis**
   - Comparar cada ejemplo en CLAUDE.md con código real
   - Verificar firmas de métodos
   - Identificar información desactualizada
   - Buscar contradicciones entre README.md y CLAUDE.md

4. **Structural Validation**
   - Validar CADA proyecto contra v2.2 ORGANIZED
   - Crear matriz de conformidad
   - Identificar patrones de violación

5. **Cross-System Consistency Analysis**
   - Crear matriz de promesas vs realidad
   - Identificar gaps entre especificación e implementación
   - Documentar inconsistencias sistemáticas

6. **Quality Metrics**
   - Calcular scores: Code Quality, Documentation Quality, Architecture Quality
   - Evaluar estado general: ALPHA, BETA, PRODUCTION
   - Definir métricas objetivas

### Expected Output

**Report structure (40+ páginas):**

```markdown
# Análisis Exhaustivo del Agentic Task Framework v2.2

## SECCIÓN 1: RESUMEN EJECUTIVO
- ¿Qué es este proyecto?
- ¿Qué problema resuelve?
- Arquitectura de alto nivel
- Estado general
- Métricas de calidad

## SECCIÓN 2: ARQUITECTURA DETALLADA
- Componentes principales (con código)
- Flujos de datos
- Principios de diseño
- Evaluación arquitectónica

## SECCIÓN 3: ANÁLISIS DE CÓDIGO - ProjectManager
[Cada método analizado]

## SECCIÓN 4: ANÁLISIS DE CÓDIGO - FrameworkValidator
[Cada método analizado]

## SECCIÓN 5: ANÁLISIS DE DOCUMENTACIÓN
[CLAUDE.md vs Realidad]
[README.md vs Realidad]

## SECCIÓN 6: ANÁLISIS ESTRUCTURAL
[Cada proyecto validado contra v2.2]

## SECCIÓN 7: MATRIZ DE INCONSISTENCIAS
[Tabla cross-system]

## SECCIÓN 8: PROBLEMAS IDENTIFICADOS (TOP 10)
[Los 10 problemas MÁS CRÍTICOS con análisis profundo]

## SECCIÓN 9: PROBLEMAS COMPLETOS (TODOS)
[Lista exhaustiva categor izada]

## SECCIÓN 10: ROADMAP DE CORRECCIONES
- FASE 1: CRÍTICOS
- FASE 2: ALTOS
- FASE 3: MEDIOS
- FASE 4: BAJOS + TESTING

## SECCIÓN 11: CONCLUSIÓN Y RECOMENDACIONES
```

**Minimum length:** 10,000 palabras (40+ páginas)

**Evidence requirement:**
- Citar código específico (file:line)
- Screenshots de estructura
- Ejemplos de metadata incorrecta
- Comparaciones lado a lado

### Success Criteria

✅ TODOS los archivos de código analizados línea por línea
✅ TODOS los proyectos validados estructuralmente
✅ Mínimo 25 inconsistencias identificadas
✅ Cada problema tiene evidencia + análisis + solución
✅ Métricas de calidad calculadas
✅ Roadmap detallado en 4 fases
✅ Reporte > 10,000 palabras

### Output Location

**CRITICAL:** Save your complete report to:
`{report_path}`

### Note

Este análisis debe ser TAN EXHAUSTIVO que sirva como:
- Documentación de referencia del framework
- Base para TODAS las correcciones futuras
- Training material para nuevos coordinadores
- Evidencia de due diligence técnico
"""

    task3 = pm.create_task(
        project_id=project["id"],
        task_name="analisis-exhaustivo-framework-20260115",
        task_description="Análisis exhaustivo de 42 páginas por agente ae7984d",
        prompt=prompt_analisis_exhaustivo.format(
            report_path=str(Path.cwd() / "reports" / "ANALISIS_EXHAUSTIVO_FRAMEWORK_v22_20260115.md")
        )
    )

    print(f"✓ Tarea 3 creada: {task3['task_name']}")
    print(f"  (Este fue el agente ae7984d)")
    print(f"  ℹ Reporte original en: reports/ANALISIS_EXHAUSTIVO_FRAMEWORK_v22_20260115.md")
    print(f"  (No registrado - proyecto retroactivo)")
    print()

    print("=" * 60)
    print("RECONSTRUCCIÓN COMPLETADA")
    print("=" * 60)
    print()
    print(f"Proyecto ID: {project['id']}")
    print(f"Ubicación: projects/{project['id']}/")
    print()
    print("Tareas reconstruidas:")
    print("  1. auditoria-framework-completa-20260114")
    print("  2. auditoria-sistemica-youtube-20260114")
    print("  3. analisis-exhaustivo-framework-20260115")
    print()
    print("Cada tarea ahora tiene:")
    print("  ✓ prompt.md - Prompt reconstruido con arquitectura de 2 capas")
    print("  ✓ README.md - Auto-generado por ProjectManager")
    print("  ✓ task_info.json - Metadata con reporte registrado")
    print("  ✓ reports/ - Directorio (reportes ya existían en reports/)")
    print()
    print("PRÓXIMOS PASOS:")
    print("  1. Revisar prompts reconstruidos en:")
    print(f"     projects/{project['id']}/tasks/*/prompt.md")
    print("  2. Validar que prompts reflejan lo que se hizo")
    print("  3. Usar estos prompts como TEMPLATES para futuras auditorías")
    print()


if __name__ == "__main__":
    reconstruct_audit_prompts()
