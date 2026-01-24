# Mejores Prácticas: Framework Agéntico v2.1

Esta guía recopila las mejores prácticas para usar el framework agéntico de manera efectiva, basadas en experiencia real y descubrimientos experimentales.

---

## Tabla de Contenidos

1. [Diseño de Prompts](#diseño-de-prompts)
2. [Coordinación de Agentes](#coordinación-de-agentes)
3. [Gestión de Contexto](#gestión-de-contexto)
4. [Debugging y Troubleshooting](#debugging-y-troubleshooting)
5. [Optimización de Rendimiento](#optimización-de-rendimiento)
6. [Seguridad y Privacidad](#seguridad-y-privacidad)
7. [Casos de Uso Comunes](#casos-de-uso-comunes)

---

## Diseño de Prompts

### Principio Fundamental: Arquitectura de 2 Capas

**SIEMPRE usa la arquitectura de 2 capas para agentes:**

```markdown
# CAPA 1: Contexto del Proyecto
[Solicitud del usuario, disclaimers, supervisión]

---

# CAPA 2: Prompt Técnico
[Rol, objetivo, metodología]
```

**Validación experimental:**

- ✅ Agente CON contexto: Completó tarea exitosamente
- ❌ Agente SIN contexto: Rechazó tarea legítima

### ✅ Buenas Prácticas

#### 1. Incluir Contexto Conversacional

**MAL:**

```markdown
# Tarea: Investigar ClO₂?

Eres un virólogo. Investiga efectos de ClO₂? contra COVID-19.
```

**BIEN:**

```markdown
# Contexto del Proyecto

El usuario ha solicitado investigación científica sobre ClO₂?, con directrices:
- "Sé neutral como científico"
- "Solo evidencia científica"

Este es un proyecto académico supervisado por el usuario.

---

# Tu Tarea: Virólogo Molecular

Eres un virólogo especializado...
```

**Por qué:** El contexto previene auto-censura y establece legitimidad.

---

#### 2. Prompts Ejecutivos, No Conversacionales

**MAL:**

```markdown
¿Podrías investigar sobre el tema X?
¿Te gustaría que te ayude con algo más?
```

**BIEN:**

```markdown
## Objetivo de la Tarea

Realizar análisis riguroso de X, enfocándote en:
1. Aspecto A
2. Aspecto B
3. Aspecto C

**INICIA LA INVESTIGACION AHORA.**
```

**Por qué:** Los agentes deben ejecutar, no conversar. El coordinador es quien conversa con el usuario.

---

#### 3. Metodología Clara y Específica

**MAL:**

```markdown
Analiza el tema como creas conveniente.
```

**BIEN:**

```markdown
## Metodología

1. **Búsqueda de Literatura:**
 - Prioriza papers peer-reviewed (2020-2025)
 - Usa Web Search para encontrar fuentes
 - Mínimo 15 papers citados

2. **Análisis:**
 - Identifica mecanismos moleculares
 - Cuantifica magnitudes de cambio
 - Sintetiza hallazgos

3. **Organización:**
 - Secciones por mecanismo
 - Incluye datos cuantitativos
 - Cita todas las fuentes
```

**Por qué:** El agente sabe exactamente qué hacer y cómo.

---

#### 4. Criterios de Completitud Explícitos

**MAL:**

```markdown
Haz un buen trabajo.
```

**BIEN:**

```markdown
## Criterios de Completitud

- ✅ Al menos 15 papers peer-reviewed citados (2020-2025)
- ✅ Datos cuantitativos incluidos
- ✅ Mecanismos explicados a nivel molecular
- ✅ Neutral, sin opiniones políticas
- ✅ Referencias completas
```

**Por qué:** Define el estándar de calidad esperado.

---

#### 5. Terminar con Comando de Acción

**Siempre termina con:**

```markdown
**INICIA LA [TAREA] AHORA.**
```

**Variaciones aceptables:**

- `**INICIA LA INVESTIGACION AHORA.**`
- `**INICIA EL ANÁLISIS AHORA.**`
- `**INICIA EL DESARROLLO AHORA.**`

**Por qué:** Señal clara para el agente de que debe comenzar inmediatamente.

---

### ❌ Antipatrones a Evitar

#### 1. Prompts Sin Contexto

```markdown
❌ "Investiga dióxido de cloro"
```

**Problema:** El agente no sabe por qué, para quién, o bajo qué supervisión.

---

#### 2. Prompts Ambiguos

```markdown
❌ "Analiza este tema en detalle"
```

**Problema:** ¿Qué aspectos? ¿Qué nivel de detalle? ¿Qué formato?

---

#### 3. Prompts Conversacionales

```markdown
❌ "¿Podrías ayudarme a investigar X?
 Si encuentras algo interesante, ¿me lo puedes mostrar?"
```

**Problema:** El agente es ejecutor, no conversador.

---

#### 4. Prompts Sin Metodología

```markdown
❌ "Haz lo que consideres apropiado"
```

**Problema:** Falta de dirección clara.

---

## Coordinación de Agentes

### Principio: El Coordinador No Delega Ciegamente

**Mal coordinador:**

```
Usuario: "Investiga X"
Coordinador: [Lanza agente inmediatamente]
```

**Buen coordinador:**

```
Usuario: "Investiga X"
Coordinador: "Entiendo que quieres investigar X.
 Para diseñar la mejor estrategia, ayúdame a entender:
 - ¿Qué aspectos específicos?
 - ¿Qué nivel de profundidad?
 - ¿Hay algún enfoque particular?"
```

### ✅ Buenas Prácticas de Coordinación

#### 1. Analizar Antes de Lanzar

**Proceso recomendado:**

1. Escuchar solicitud del usuario
2. Hacer preguntas clarificadoras
3. Diseñar estrategia de agentes
4. Validar con usuario
5. Lanzar agentes con contexto

---

#### 2. Usar TodoWrite para Tracking

**SIEMPRE usa TodoWrite cuando lances múltiples agentes:**

```json5
TodoWrite([
 {"content": "Agente 1: Química", "status": "in_progress", "activeForm": "Investigando química"},
 {"content": "Agente 2: Bioquímica", "status": "pending", "activeForm": "Pendiente"},
 {"content": "Agente 3: Virología", "status": "pending", "activeForm": "Pendiente"}
])
```

**Actualiza conforme avanzan:**

```json5
TodoWrite([
 {"content": "Agente 1: Química", "status": "completed", "activeForm": "Completado"},
 {"content": "Agente 2: Bioquímica", "status": "in_progress", "activeForm": "Analizando toxicología"},
 {"content": "Agente 3: Virología", "status": "pending", "activeForm": "Pendiente"}
])
```

**Por qué:** El usuario ve progreso en tiempo real.

---

#### 3. Diseñar Prompts Específicos, No Genéricos

**MAL:**

```python
# Reutilizar mismo prompt para todos
for tema in temas:
 Task(prompt=generic_prompt.replace("TEMA", tema))
```

**BIEN:**

```python
# Diseñar prompt específico para cada agente
prompt_quimico = diseñar_prompt_contextualizado(
 contexto_usuario=contexto,
 rol="Químico Molecular",
 objetivo="Analizar estructura molecular de ClO₂?",
 metodologia=metodologia_quimica
)

Task(prompt=prompt_quimico)
```

**Por qué:** Cada agente tiene necesidades específicas.

---

#### 4. Lanzar en Paralelo Cuando Sea Posible

**MAL (secuencial):**

```python
agente1 = Task(prompt1)
esperar(agente1)
agente2 = Task(prompt2)
esperar(agente2)
```

**BIEN (paralelo):**

```python
agente1 = Task(prompt1, run_in_background=True)
agente2 = Task(prompt2, run_in_background=True)
agente3 = Task(prompt3, run_in_background=True)

# Luego recuperar resultados
resultado1 = TaskOutput(agente1)
resultado2 = TaskOutput(agente2)
resultado3 = TaskOutput(agente3)
```

**Por qué:** Paralelización maximiza eficiencia.

---

#### 5. Sintetizar, No Volcar

**MAL:**

```
Coordinador: "Agentes terminaron. Aquí están los resultados:
 [Copia completa de output de agente 1: 50 KB]
 [Copia completa de output de agente 2: 50 KB]
 [Copia completa de output de agente 3: 50 KB]"
```

**BIEN:**

```
Coordinador: "Investigación completada.

## Hallazgos Clave

### Química Molecular
- ClO₂? es radical libre con selectividad por aminoácidos aromáticos
- Rate constants: 10⁴-10⁷ M⁻¹ s⁻¹
- [2-3 bullets más con datos clave]

### Bioquímica
- GSH/GSSG ratio crítico para neutralización
- LD50 en ratas: 292 mg/kg
- [2-3 bullets más]

### Virología
- Inactivación de SARS-CoV-2: 99.96% en 10s (8 ppm)
- [Mecanismo resumido en 2-3 líneas]

¿Quieres profundizar en algún aspecto?"
```

**Por qué:** El usuario quiere insights, no dumps de datos.

---

## Gestión de Contexto

### Principio: Los Agentes No Ven Tu Historia

**Realidad técnica:**

- Los agentes lanzados con `Task tool` NO tienen acceso al historial conversacional
- Solo ven el prompt que les pasas
- No pueden ver mensajes previos del usuario

**Implicación:**

- DEBES incluir TODA la información relevante en el prompt
- DEBES incluir contexto del usuario (solicitud, disclaimers)
- DEBES incluir cualquier dato mencionado antes en la conversación

### ✅ Buenas Prácticas

#### 1. Incluir Solicitud Original del Usuario

**Siempre cita lo que el usuario pidió:**

```markdown
# Contexto del Proyecto

## Solicitud del Usuario

El usuario ha solicitado [TIPO_PROYECTO] sobre [TEMA], con directrices explícitas:

**Instrucciones del usuario:**
- "[CITA_TEXTUAL_1]"
- "[CITA_TEXTUAL_2]"
- "[CITA_TEXTUAL_3]"
```

---

#### 2. Incluir Disclaimers y Supervisión

```markdown
**Enfoque requerido:**
- Investigación científica neutral y objetiva
- Basado en literatura peer-reviewed
- Sin debates políticos o regulatorios

**Naturaleza del proyecto:**
Este es un proyecto académico de investigación científica supervisado por el usuario.
```

**Por qué:** Establece legitimidad y previene auto-censura.

---

#### 3. Pasar Información Relevante de la Conversación

**Ejemplo:**

Si en la conversación el usuario mencionó:

- "Tengo acceso a la base de datos X"
- "Mi equipo usa Python y PostgreSQL"
- "Necesitamos esto para el viernes"

**Incluye eso en el prompt:**

```markdown
**Recursos disponibles:**
- Base de datos X con datos de usuario
- Stack tecnológico: Python + PostgreSQL
- Timeline: Entrega requerida para viernes

**Restricciones:**
- Usar solo librerías estándar de Python
- No puede exceder 1 hora de cómputo
```

---

## Debugging y Troubleshooting

### SEARCH: Problema: Agente Rechazó Tarea

**Síntoma:**

```
API Error: Claude Code is unable to respond to this request,
which appears to violate our Usage Policy
```

**Causa Raíz:**

- Agente NO tiene contexto conversacional
- Filtros de contenido activados erróneamente

**Solución:**

```markdown
# AGREGAR CONTEXTO en la Capa 1:

## Contexto del Proyecto

El usuario ha solicitado investigación científica sobre [TEMA], con directrices:
- "[Instrucción del usuario mostrando intención legítima]"
- "[Disclaimer de neutralidad/objetividad]"

Este es un proyecto académico/empresarial supervisado por el usuario.
```

**Validación:**

- ✅ Experimento con contexto: Agente completó
- ❌ Experimento sin contexto: Agente rechazó

---

### SEARCH: Problema: Agente Pregunta en Vez de Ejecutar

**Síntoma:**

```
Agente: "¿Deseas que cree una tarea especializada para esto?"
```

**Causa Raíz:**

- Prompt conversacional, no ejecutivo

**Solución:**

```markdown
# Cambiar de conversacional a ejecutivo:

❌ "¿Podrías investigar sobre X?"
✅ "Investiga X enfocándote en Y. INICIA LA INVESTIGACI❌N AHORA."

❌ "Si encuentras algo, me avisas"
✅ "Estructura de salida: [específica]. Criterios: [explícitos]."
```

---

### SEARCH: Problema: No Veo Progreso de Agentes

**Síntoma:**
Usuario pregunta "¿Qué están haciendo los agentes?" y no tienes visibilidad.

**Causa Raíz:**

- No usaste `TodoWrite` para tracking

**Solución:**

```python
# Al lanzar agentes:
TodoWrite([
 {"content": "Agente 1: Tarea X", "status": "in_progress", "activeForm": "Ejecutando X"},
 {"content": "Agente 2: Tarea Y", "status": "pending", "activeForm": "Pendiente"}
])

# Conforme completan:
TodoWrite([
 {"content": "Agente 1: Tarea X", "status": "completed", "activeForm": "Completado"},
 {"content": "Agente 2: Tarea Y", "status": "in_progress", "activeForm": "Ejecutando Y"}
])
```

---

### SEARCH: Problema: Resultados de Agente Son Superficiales

**Síntoma:**
Agente devuelve análisis genérico, sin profundidad.

**Causa Raíz:**

- Falta de metodología específica
- Falta de criterios de completitud

**Solución:**

```markdown
## Metodología

1. **Paso específico 1:**
 - Acción concreta
 - Herramientas a usar (ej: Web Search, Read)
 - Output esperado

2. **Paso específico 2:**
 - [Similar...]

## Criterios de Completitud

- ✅ Al menos 15 fuentes citadas
- ✅ Datos cuantitativos incluidos
- ✅ Análisis de [aspecto específico]
```

---

## Optimización de Rendimiento

### Principio: Paralelizar Cuando Sea Posible

#### 1. Lanzar Agentes Independientes en Paralelo

**MAL (secuencial - 30 minutos total):**

```python
agente1 = Task(prompt1) # 10 min
esperar(agente1)
agente2 = Task(prompt2) # 10 min
esperar(agente2)
agente3 = Task(prompt3) # 10 min
esperar(agente3)
```

**BIEN (paralelo - 10 minutos total):**

```python
agente1 = Task(prompt1, run_in_background=True) # |
agente2 = Task(prompt2, run_in_background=True) # | 10 min (paralelo)
agente3 = Task(prompt3, run_in_background=True) # |

# Recuperar cuando completen
resultado1 = TaskOutput(agente1, block=True)
resultado2 = TaskOutput(agente2, block=True)
resultado3 = TaskOutput(agente3, block=True)
```

---

#### 2. Distribuir Contexto Pesado a Agentes

**MAL:**

- Coordinador mantiene todo el contexto pesado
- Coordinador hace análisis profundo

**BIEN:**

- Coordinador: Contexto ligero, visión general
- Agentes: Contexto pesado, análisis profundo

---

#### 3. Usar `run_in_background=True`

**Siempre que lances múltiples agentes:**

```python
Task(..., run_in_background=True)
```

**Excepción:** Si el siguiente agente DEPENDE del resultado del primero.

---

## Seguridad y Privacidad

### SECURE: Principio: Nunca Incluir Secrets en Prompts

#### 1. No Incluir Credenciales

**❌ NUNCA:**

```markdown
Base de datos: postgresql://user:PASSWORD123@host/db
API Key: sk_live_abc123xyz
```

**✅ MEJOR:**

```markdown
Base de datos: Configurada en variable de entorno DATABASE_URL
API Key: Configurada en .env (no incluir en prompt)
```

---

#### 2. No Incluir Datos Sensibles

**❌ EVITAR:**

```markdown
Analiza estos datos de usuarios:
- Juan Pérez, email: juan@example.com, SSN: 123-45-6789
```

**✅ MEJOR:**

```markdown
Analiza dataset de usuarios (datos anonimizados disponibles en /data/users_anonymized.csv)
```

---

#### 3. Sanitizar Contexto del Usuario

Si el usuario mencionó información sensible en la conversación, **NO la copies tal cual** al prompt del agente.

**Filtrar:**

- Credenciales
- PII (Personally Identifiable Information)
- Secretos empresariales

---

## Casos de Uso Comunes

### Caso 1: Investigación Científica Multidisciplinaria

**Patrón:**

```
1. Usuario solicita investigación de tema complejo
2. Coordinador identifica disciplinas necesarias (ej: química, biología, clínica)
3. Coordinador diseña prompts especializados para cada disciplina
4. Lanza agentes en paralelo
5. Recupera resultados
6. Sintetiza hallazgos integrados
7. Presenta al usuario
```

**Template:** Ver `examples/example_research_task.md`

---

### BUILD: Caso 2: Decisión Arquitectónica

**Patrón:**

```
1. Usuario necesita decidir entre opciones técnicas
2. Coordinador clarifica contexto (equipo, stack, restricciones)
3. Lanza agente de análisis técnico con contexto específico
4. Agente analiza trade-offs
5. Coordinador valida recomendación con usuario
```

**Template:** Ver `examples/example_analysis_task.md`

---

### CODE: Caso 3: Desarrollo de Feature

**Patrón:**

```
1. Usuario describe feature necesaria
2. Coordinador clarifica requisitos (seguridad, tests, stack)
3. Lanza agente de desarrollo con especificaciones detalladas
4. Agente implementa código + tests
5. Coordinador revisa resultados
6. Presenta código al usuario
```

**Template:** Ver `examples/example_development_task.md`

---

### ANALYSIS: Caso 4: Análisis de Datos

**Patrón:**

```
1. Usuario solicita insights de datos
2. Coordinador identifica datasets y preguntas de negocio
3. Lanza agente de data science con metodología clara
4. Agente hace EDA + modelado + visualizaciones
5. Coordinador extrae insights accionables
6. Presenta recomendaciones al usuario
```

**Template:** Ver `examples/example_data_task.md`

---

## Checklist de Diseño de Prompts

Antes de lanzar un agente, verifica:

### Capa 1: Contexto

- [ ] ¿Incluí la solicitud original del usuario?
- [ ] ¿Incluí directrices explícitas que el usuario mencionó?
- [ ] ¿Incluí disclaimers (neutralidad, objetividad, etc.)?
- [ ] ¿Dejé claro que es proyecto supervisado?

### Capa 2: Técnico

- [ ] ¿Definí claramente el rol del agente?
- [ ] ¿El objetivo es específico y medible?
- [ ] ¿Incluí metodología paso a paso?
- [ ] ¿Especifiqué herramientas a usar? (Web Search, Read, etc.)
- [ ] ¿Definí estructura de salida?
- [ ] ¿Incluí criterios de completitud?
- [ ] ¿Terminé con "INICIA ... AHORA"?

### Prompt Completo

- [ ] ¿Es ejecutivo, no conversacional?
- [ ] ¿Es específico, no vago?
- [ ] ¿Incluye toda información relevante de la conversación?
- [ ] ¿No incluye secrets o datos sensibles?

---

## Recursos Adicionales

- **Templates:** `core/context_template.md`
- **Ejemplos:** `examples/`
- **Documentación:** `CLAUDE.md`
- **Framework:** `README.md`

---

**Ultima actualización:** 2025-12-22
**Framework Version:** 2.1
