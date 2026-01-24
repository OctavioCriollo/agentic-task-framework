# Ejemplos de Prompts con Arquitectura de 2 Capas

Este directorio contiene ejemplos completos de prompts diseñados con la **arquitectura de 2 capas** (Contexto + Técnico) descubierta en Framework v2.1.

## ¿Por Qué Usar Estos Templates?

Los agentes lanzados con `Task tool` **NO tienen acceso al historial conversacional**. Sin contexto, pueden rechazar tareas legítimas o auto-censurarse innecesariamente. La arquitectura de 2 capas resuelve esto proporcionando:

**Capa 1: Contexto del Proyecto**
- Solicitud original del usuario
- Disclaimers y directrices explícitas
- Naturaleza del proyecto (académico, supervisado, etc.)

**Capa 2: Prompt Técnico**
- Rol del agente especializado
- Objetivo específico
- Metodología detallada

## Ejemplos Disponibles

### 1. [Investigación Científica](example_research_task.md)
**Caso de uso:** Investigación académica sobre cambio climático en arrecifes de coral

**Aprenderás:**
- Cómo establecer contexto de investigación científica neutral
- Metodología de búsqueda de literatura peer-reviewed
- Estructura de reporte científico riguroso
- Criterios de completitud para investigación

**Cuándo usar:**
- Investigaciones científicas
- Análisis de literatura académica
- Estudios basados en evidencia
- Proyectos de investigación supervisados

---

### 2. [Análisis Técnico](example_analysis_task.md)
**Caso de uso:** Comparación arquitectónica microservicios vs monolitos para startup

**Aprenderás:**
- Cómo plantear análisis técnico pragmático
- Estructura de comparación con trade-offs
- Contextualización a caso específico
- Recomendaciones justificadas técnicamente

**Cuándo usar:**
- Decisiones arquitectónicas
- Comparaciones técnicas
- Evaluación de tecnologías
- Análisis de trade-offs

---

### 3. [Desarrollo de Software](example_development_task.md)
**Caso de uso:** Sistema de autenticación con JWT y refresh tokens

**Aprenderás:**
- Cómo especificar requisitos de desarrollo
- Estructura de código esperada
- Requisitos de seguridad (OWASP)
- Criterios de tests y cobertura

**Cuándo usar:**
- Desarrollo de features
- Implementación de sistemas
- Proyectos con requisitos de seguridad
- Desarrollo con tests automatizados

---

### 4. [Análisis de Datos](example_data_task.md)
**Caso de uso:** Análisis de churn de clientes con machine learning

**Aprenderás:**
- Cómo estructurar proyecto de data science
- EDA, feature engineering, modelado
- Visualizaciones y métricas esperadas
- Insights accionables para negocio

**Cuándo usar:**
- Análisis de datos
- Machine learning
- Business intelligence
- Proyectos de data science

---

## Cómo Usar Estos Ejemplos

### Paso 1: Selecciona el Template Apropiado
Elige el ejemplo que más se parezca a tu caso de uso.

### Paso 2: Adapta la Capa 1 (Contexto)
Modifica la sección de contexto con:
- La solicitud REAL de tu usuario
- Directrices específicas que tu usuario mencionó
- Contexto particular de tu proyecto

**Ejemplo:**
```markdown
**Instrucciones del usuario:**
- "[CITA DIRECTA de lo que el usuario pidió]"
- "[Otra directriz explícita]"
```

### Paso 3: Adapta la Capa 2 (Técnico)
Modifica el prompt técnico con:
- Objetivo específico de tu tarea
- Metodología apropiada
- Herramientas y recursos disponibles
- Criterios de completitud específicos

### Paso 4: Lanza el Agente
Como coordinador, usa el Task tool con tu prompt adaptado:

```python
# El coordinador ejecuta esto
Task(
    subagent_type="general-purpose",
    prompt="""
    [Tu prompt de 2 capas aquí]
    """,
    description="[Descripción breve]"
)
```

---

## Principios de Diseño

### ✅ HACER:

**Incluir contexto conversacional:**
```markdown
# Contexto del Proyecto

El usuario ha solicitado [TIPO] sobre [TEMA], con directrices:
- "[CITA DIRECTA del usuario]"
- "[Otra directriz]"

Este es un proyecto de [NATURALEZA] supervisado por el usuario.
```

**Ser específico en objetivos:**
```markdown
## Objetivo de la Tarea

Realizar un análisis de [ESPECÍFICO], enfocándote en:
1. [Aspecto concreto 1]
2. [Aspecto concreto 2]
3. [Aspecto concreto 3]
```

**Dar metodología clara:**
```markdown
## Metodología

1. **Paso 1:** [Acción específica]
2. **Paso 2:** [Acción específica]
3. **Paso 3:** [Acción específica]
```

**Terminar con acción:**
```markdown
**INICIA LA [TAREA] AHORA.**
```

### ❌ NO HACER:

**Prompts sin contexto:**
```markdown
❌ "Investiga X"
✓ "El usuario solicitó investigar X, con enfoque en Y y Z.
   Este es un proyecto académico supervisado..."
```

**Objetivos vagos:**
```markdown
❌ "Analiza el tema"
✓ "Realiza análisis riguroso enfocándote en:
   1. Aspecto A con métricas X
   2. Aspecto B con comparación Y"
```

**Sin criterios de completitud:**
```markdown
❌ "Haz un buen trabajo"
✓ "Criterios de completitud:
   - ✅ Al menos 15 fuentes citadas
   - ✅ Análisis cuantitativo con datos
   - ✅ Conclusiones justificadas"
```

---

## Validación Experimental

Estos templates están basados en **experimentos reales** del framework:

**Experimento 1 (sin contexto):**
- Prompt técnico solo
- Resultado: ❌ Agente rechazó tarea legítima

**Experimento 2 (con contexto):**
- Prompt con 2 capas (contexto + técnico)
- Resultado: ✅ Agente completó exitosamente

**Evidencia:** Ver `\tmp\experimento1_sin_contexto.md` y `\tmp\experimento2_con_contexto.md`

---

## Recursos Adicionales

- **Template General:** Ver `core/context_template.md` para estructura base
- **Documentación:** Ver `CLAUDE.md` para instrucciones del coordinador
- **Guía Principal:** Ver `README.md` del framework

---

**Última actualización:** 2025-12-22
**Framework Version:** 2.1
