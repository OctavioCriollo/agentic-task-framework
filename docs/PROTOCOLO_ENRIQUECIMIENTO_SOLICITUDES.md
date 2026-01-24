# Protocolo de Enriquecimiento de Solicitudes v2.3

> **Versión:** 2.3
> **Fecha:** 2026-01-24
> **Propósito:** Transformar solicitudes vagas de usuarios en requerimientos claros y completos

---

## ÍNDICE

1. [¿Qué es el Enriquecimiento?](#qué-es-el-enriquecimiento)
2. [Por qué es necesario](#por-qué-es-necesario)
3. [Flujo de trabajo](#flujo-de-trabajo)
4. [Template de enriquecimiento](#template-de-enriquecimiento)
5. [Ejemplos prácticos](#ejemplos-prácticos)
6. [Cuándo enriquecer vs cuándo no](#cuándo-enriquecer-vs-cuándo-no)
7. [Métricas de éxito](#métricas-de-éxito)

---

## ¿Qué es el Enriquecimiento?

El **Enriquecimiento de Solicitudes** es un proceso donde el coordinador:

1. **Analiza** la solicitud original del usuario
2. **Detecta** vaguedad, ambigüedad o contexto faltante
3. **Expande** la solicitud con:
   - Interpretación del objetivo real
   - Alcance sugerido
   - Perspectivas relevantes no mencionadas
   - Criterios de éxito
   - Preguntas clave a responder

4. **Presenta** la versión enriquecida al usuario para validación
5. **Itera** si es necesario hasta tener claridad completa

**Resultado:** Una especificación clara que guía investigaciones exitosas.

---

## Por qué es Necesario

### Problema Actual

Los usuarios frecuentemente hacen solicitudes que son:
- **Vagas:** "Investiga IA" (¿qué aspecto de IA?)
- **Incompletas:** "Analiza competidores" (¿qué industria? ¿qué criterios?)
- **Ambiguas:** "Busca la mejor solución" (¿mejor en qué sentido?)
- **Con contexto implícito:** Asumen conocimiento que no explican

### Consecuencias sin Enriquecimiento

- Investigaciones que no cumplen expectativas
- Perspectivas importantes omitidas
- Iteraciones múltiples ("no era lo que quería")
- Tiempo y recursos desperdiciados
- Frustración del usuario

### Beneficios con Enriquecimiento

- Claridad desde el inicio
- Cobertura completa de aspectos relevantes
- Resultados que cumplen (o superan) expectativas
- Menos iteraciones de corrección
- Usuario aprende a especificar mejor

---

## Flujo de Trabajo

### Paso 1: Recepción de Solicitud

Usuario dice algo como:
```
"Investiga blockchain"
"Analiza el mercado"
"Busca información sobre X"
```

### Paso 2: Análisis de Calidad

El coordinador se pregunta:

**Sobre especificidad:**
- ¿La solicitud es específica o general?
- ¿Hay múltiples interpretaciones posibles?
- ¿Qué aspectos podrían estar implícitos?

**Sobre contexto:**
- ¿Por qué el usuario pide esto?
- ¿Qué hará con la información?
- ¿Qué nivel de profundidad necesita?

**Sobre alcance:**
- ¿Qué incluir y qué excluir?
- ¿Qué perspectivas son relevantes?
- ¿Hay restricciones implícitas?

### Paso 3: Decisión

**SI detectas vaguedad/ambigüedad:**
→ Proceder a enriquecer (Paso 4)

**SI la solicitud es clara y completa:**
→ Confirmar entendimiento brevemente
→ Proceder directo a diseño de estrategia

### Paso 4: Enriquecimiento

Crear versión expandida usando [Template](#template-de-enriquecimiento).

Incluir:
- Interpretación del objetivo
- Alcance inferido
- Perspectivas sugeridas
- Preguntas clave
- Criterios de éxito
- Exclusiones (si aplica)

### Paso 5: Presentación

Mostrar al usuario:
```
He analizado tu solicitud. Aquí está mi interpretación:

[ENRIQUECIMIENTO COMPLETO]

¿Es esto correcto? ¿Quieres ajustar algo?
```

### Paso 6: Validación

Esperar respuesta del usuario:

**Usuario aprueba:**
→ Proceder a diseño de estrategia multi-agente

**Usuario modifica:**
→ Ajustar enriquecimiento
→ Presentar versión revisada
→ Validar nuevamente

**Usuario rechaza completamente:**
→ Pedir aclaración sobre qué quiere realmente
→ Reintentar enriquecimiento

### Paso 7: Ejecución

Solo DESPUÉS de validación:
→ Diseñar estrategia multi-agente
→ Lanzar investigación

---

## Template de Enriquecimiento

### Template Base

```markdown
He analizado tu solicitud. Aquí está mi interpretación:

## OBJETIVO
[Una o dos frases describiendo lo que entiendes que el usuario quiere lograr]

## INFERRED SCOPE
Basándome en tu solicitud "[cita textual]", interpreto que buscas:

- **Aspecto 1:** [descripción del aspecto]
- **Aspecto 2:** [descripción del aspecto]
- **Aspecto 3:** [descripción del aspecto]
- **Aspecto N:** [descripción del aspecto]

## SUGGESTED PERSPECTIVES
Para abordar esto comprehensivamente, propongo analizar desde:

1. **[Perspectiva 1 - ej: Técnica]:** [Por qué es relevante]
2. **[Perspectiva 2 - ej: Económica]:** [Por qué es relevante]
3. **[Perspectiva 3 - ej: Práctica]:** [Por qué es relevante]
4. **[Perspectiva N]:** [Por qué es relevante]

## KEY QUESTIONS TO ANSWER
- [Pregunta fundamental 1 que debe responderse]
- [Pregunta fundamental 2 que debe responderse]
- [Pregunta fundamental 3 que debe responderse]
- [Pregunta fundamental N]

## SUCCESS CRITERIA
Sabrás que esta investigación fue exitosa si al finalizar puedes:
- [Criterio 1 - qué deberías poder hacer/saber]
- [Criterio 2 - qué deberías poder hacer/saber]
- [Criterio 3 - qué deberías poder hacer/saber]

## EXCLUSIONS (opcional)
Dado el alcance propuesto, NO cubriremos:
- [Aspecto excluido 1 - y por qué]
- [Aspecto excluido 2 - y por qué]

---

¿Es esto lo que buscas? ¿Quieres:
- ✓ Proceder con este alcance
- Agregar/quitar perspectivas
- Cambiar el enfoque
- Aclarar restricciones
```

### Variantes del Template

#### Cuando hay ambigüedad sobre objetivo

```markdown
He analizado tu solicitud y detecté que podría interpretarse de varias formas.

## POSIBLES INTERPRETACIONES

Tu solicitud "[cita]" podría significar:

**Interpretación A:** [primera interpretación]
- Enfoque: [descripción]
- Resultado esperado: [qué generaría]

**Interpretación B:** [segunda interpretación]
- Enfoque: [descripción]
- Resultado esperado: [qué generaría]

**Interpretación C:** [tercera interpretación]
- Enfoque: [descripción]
- Resultado esperado: [qué generaría]

¿Cuál de estas se acerca más a lo que necesitas?
O descríbeme con más detalle qué buscas lograr.
```

#### Cuando hay sesgo evidente

```markdown
He analizado tu solicitud y noté que tiene una conclusión predeterminada.

## SOLICITUD ORIGINAL
"[cita textual con el sesgo]"

## OBSERVACIÓN
Esta solicitud asume un resultado específico, lo cual puede limitar la objetividad.

## REFRAMING SUGERIDO
En lugar de "[solicitud sesgada]", propongo:

**"[versión neutral y objetiva]"**

Esto permite:
- Análisis imparcial de evidencia
- Consideración de perspectivas múltiples
- Conclusiones basadas en datos (no predeterminadas)

¿Preferirías:
- A) Análisis objetivo (recomendado)
- B) Enfoque que prioriza [la posición sesgada]
```

#### Cuando falta contexto crítico

```markdown
He analizado tu solicitud y necesito aclaración sobre el contexto.

## TU SOLICITUD
"[cita textual]"

## CONTEXTO NECESARIO
Para diseñar la mejor estrategia, ayúdame a entender:

1. **Propósito:** ¿Para qué usarás esta información?
   - Decisión de negocio
   - Proyecto académico
   - Curiosidad personal
   - Otro: [especifica]

2. **Nivel técnico:** ¿Qué tan técnico debe ser?
   - Alta especialización técnica
   - Intermedio (algún conocimiento previo)
   - Básico (explicar todo)

3. **Restricciones:** ¿Hay límites que deba considerar?
   - Tiempo
   - Presupuesto
   - Área geográfica
   - Otro: [especifica]

Con esta información podré diseñar una investigación mucho más útil.
```

---

## Ejemplos Prácticos

### Ejemplo 1: Solicitud Ultra-Vaga

**Usuario:**
```
Investiga IA
```

**Enriquecimiento:**
```markdown
He analizado tu solicitud. "Investiga IA" es muy amplia.

## OBJETIVO
Obtener comprensión comprehensiva del estado actual de la Inteligencia Artificial.

## INFERRED SCOPE
Interpreto que quieres entender:
- Qué es IA (definiciones, tipos)
- Cómo funciona (tecnologías principales)
- Dónde se usa (aplicaciones actuales)
- Hacia dónde va (tendencias futuras)
- Implicaciones (sociales, éticas, económicas)

## SUGGESTED PERSPECTIVES
1. **Técnica:** Algoritmos, modelos, arquitecturas (ML, DL, NLP, CV)
2. **Aplicaciones Prácticas:** Casos de uso por industria
3. **Ética y Sociedad:** Implicaciones, regulaciones, sesgos
4. **Económica:** Mercado, inversión, empresas líderes
5. **Futurista:** Tendencias, predicciones, roadmaps tecnológicos

## KEY QUESTIONS TO ANSWER
- ¿Qué puede hacer la IA HOY realmente vs. ciencia ficción?
- ¿Dónde se está usando exitosamente en el mundo real?
- ¿Cuáles son las limitaciones actuales?
- ¿Qué cambios se esperan en los próximos 5 años?
- ¿Cómo afectará mi industria/vida?

## SUCCESS CRITERIA
Al finalizar, deberías poder:
- Explicar IA a alguien sin conocimientos técnicos
- Identificar al menos 10 aplicaciones reales actuales
- Distinguir entre capacidades reales y hype
- Tomar decisiones informadas sobre aprendizaje/adopción

¿Este alcance es correcto o quieres enfocarte en un área específica de IA?
```

### Ejemplo 2: Solicitud con Contexto Implícito

**Usuario:**
```
Necesito información sobre dietas keto
```

**Enriquecimiento:**
```markdown
He analizado tu solicitud sobre dietas keto.

## OBJETIVO
Compilar información sobre la dieta ketogénica.

## CLARIFICACIÓN NECESARIA
Esta solicitud puede tener múltiples enfoques. ¿Buscas:

**A) Información para adoptar la dieta personalmente**
- Cómo empezar
- Qué comer/evitar
- Riesgos y precauciones
- Resultados esperados

**B) Investigación científica sobre efectividad**
- Estudios clínicos
- Mecanismos bioquímicos
- Evidencia de beneficios/riesgos
- Comparación con otras dietas

**C) Análisis crítico objetivo**
- Qué dice la ciencia
- Mitos vs realidad
- Para quién funciona/no funciona
- Alternativas similares

¿Cuál se acerca más a lo que necesitas?

Además, ¿tienes condiciones médicas que deba considerar en la investigación?
(Esta información es solo para dirigir la investigación, no sustituye consejo médico profesional)
```

### Ejemplo 3: Solicitud Técnica pero Incompleta

**Usuario:**
```
Analiza las mejores soluciones de CI/CD para mi proyecto
```

**Enriquecimiento:**
```markdown
He analizado tu solicitud sobre soluciones de CI/CD.

## OBJETIVO
Identificar la mejor solución de Continuous Integration/Continuous Deployment para tu proyecto.

## CONTEXTO NECESARIO
Para hacer una recomendación útil, necesito saber:

**Sobre tu proyecto:**
- ¿Qué stack tecnológico? (lenguajes, frameworks)
- ¿Tamaño del equipo?
- ¿Tipo de aplicación? (web, mobile, backend, microservicios)

**Sobre tu infraestructura:**
- ¿Cloud o on-premise?
- ¿Qué cloud provider? (AWS, Azure, GCP, otro)
- ¿Contenedores? (Docker, Kubernetes)

**Sobre restricciones:**
- ¿Presupuesto? (gratuito, presupuesto limitado, sin restricción)
- ¿Expertise del equipo? (necesitan algo simple o manejan complejidad)
- ¿Requisitos especiales? (compliance, seguridad, velocidad)

## PROPUESTA ALTERNATIVA
Si no tienes toda esta información, puedo:

**Opción A:** Análisis comparativo de las soluciones principales
- GitHub Actions, GitLab CI, Jenkins, CircleCI, Travis CI
- Pros/contras de cada una
- Casos de uso ideales
- Tú eliges después basado en tu contexto

**Opción B:** Esperas a darme el contexto completo
- Te haré las preguntas específicas
- Diseñaré análisis personalizado a tu caso

¿Cuál prefieres?
```

### Ejemplo 4: Solicitud de Negocio

**Usuario:**
```
Quiero entrar al mercado de e-commerce
```

**Enriquecimiento:**
```markdown
He analizado tu interés en e-commerce.

## OBJETIVO INFERIDO
Obtener información para iniciar un negocio de comercio electrónico.

## INFORMACIÓN CRÍTICA NECESARIA

Esta es una decisión de negocio importante. Para darte la mejor orientación:

**Sobre tu situación:**
- ¿Tienes producto/servicio definido o buscas ideas?
- ¿Presupuesto disponible? (bootstrap, inversión moderada, bien financiado)
- ¿Experiencia previa en e-commerce o negocios online?

**Sobre tu objetivo:**
- ¿Mercado objetivo? (local, nacional, internacional)
- ¿Nicho específico o tienda general?
- ¿Timeline? (cuándo quieres lanzar)

## PROPUESTA DE INVESTIGACIÓN

Basado en "quiero entrar al mercado", propongo investigar:

1. **Panorama del Mercado:**
   - Estado actual del e-commerce
   - Tendencias y oportunidades
   - Nichos saturados vs emergentes

2. **Modelos de Negocio:**
   - Inventario propio vs dropshipping vs marketplace
   - B2C vs B2B vs C2C
   - Pros/contras de cada modelo

3. **Aspectos Técnicos:**
   - Plataformas (Shopify, WooCommerce, custom)
   - Pagos, envíos, gestión
   - Costos de setup y operación

4. **Marketing y Adquisición:**
   - Estrategias de atracción de clientes
   - Presupuestos realistas
   - Canales efectivos

5. **Aspectos Legales/Financieros:**
   - Requisitos legales
   - Estructura fiscal
   - Gestión financiera

¿Este alcance es útil o quieres enfocarte en aspectos específicos?
```

---

## Cuándo Enriquecer vs Cuándo No

### SIEMPRE Enriquecer Si:

- Solicitud de UNA palabra ("Investiga X")
- Solicitud de una frase genérica ("Analiza el mercado")
- Múltiples interpretaciones posibles
- Falta contexto obvio (propósito, nivel técnico, restricciones)
- Solicitud con sesgo evidente
- Ámbito muy amplio sin delimitación
- Primera vez que el usuario usa el framework

### CONSIDERAR Enriquecer Si:

- Solicitud parece clara PERO podría tener matices
- Usuario es nuevo en el tema (puede no saber qué preguntar)
- Tema complejo que típicamente requiere especificación
- Podrías agregar perspectivas valiosas no consideradas
- Tienes dudas sobre alcance o prioridades

### SKIP Enriquecimiento Si:

- Solicitud extremadamente detallada y específica
- Usuario ya proporcionó:
  - Objetivo claro
  - Alcance definido
  - Perspectivas deseadas
  - Criterios de éxito

- Usuario dice explícitamente "solo haz exactamente esto"
- Es follow-up a proyecto existente (contexto ya establecido)
- Usuario demuestra experiencia con el framework

### Regla de Oro

**Cuando dudes, enriquece.**

Es mejor invertir 2-3 minutos aclarando que desperdiciar horas en investigación incorrecta.

---

## Métricas de Éxito

### Para el Sistema

**Indicadores de que el enriquecimiento funciona:**
- Reducción en iteraciones ("no era lo que quería")
- Aumento en satisfacción de usuario
- Menos solicitudes de clarificación mid-project
- Investigaciones más comprehensivas
- Usuarios aprenden a especificar mejor con el tiempo

**Cómo medir:**
- Track: % de proyectos que cumplen expectativas en primer intento
- Track: Número de ajustes solicitados post-resultados
- Survey: Calificación de utilidad de resultados (1-10)
- Observación: Usuario hace solicitudes más específicas en usos posteriores

### Para el Usuario

**Sabes que el enriquecimiento te ayudó si:**
- El coordinador identificó aspectos que no habías considerado
- La investigación cubrió perspectivas que no mencionaste
- Los resultados responden preguntas que no sabías que tenías
- Te ahorró tiempo al evitar investigación incorrecta
- Aprendiste a formular mejores solicitudes

---

## Notas de Implementación

### Para el Coordinador

1. **No asumas:** Lo que es obvio para ti puede no serlo para el usuario
2. **Sé específico:** En enriquecimiento, más detalle es mejor
3. **Sugiere, no impongas:** El usuario decide el alcance final
4. **Valida comprensión:** Asegúrate de que el usuario confirme
5. **Itera si es necesario:** No temas hacer múltiples rondas de clarificación

### Para el Usuario

1. **Aprovecha el enriquecimiento:** Es una oportunidad de mejorar tu solicitud
2. **Proporciona contexto:** Cuanto más compartas, mejor la investigación
3. **Sé honesto sobre limitaciones:** (tiempo, presupuesto, conocimiento previo)
4. **Haz preguntas:** Si el enriquecimiento tiene términos que no entiendes
5. **Ajusta sin miedo:** El coordinador puede refinar el alcance

---

## Versión y Changelog

**Versión actual:** 2.3
**Fecha:** 2026-01-24

**Changelog:**
- v2.3 (2026-01-24): Creación inicial del protocolo formal de enriquecimiento
- Integración con workflow del coordinador
- Templates reutilizables
- Ejemplos prácticos extensivos

---

**Este protocolo es parte integral del Framework Agéntico v2.3+**

Para más información, ver:
- CLAUDE.md - Sección "Request Enrichment Protocol"
- docs/GUIA_COMPLETA_FUNCIONAMIENTO.md - Guía de uso del framework
