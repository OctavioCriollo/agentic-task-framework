# Framework Agéntico v2.2 - Guía Completa de Funcionamiento

> **Última actualización:** 2026-01-24
> **Versión del Framework:** 2.2 ORGANIZED
> **Tipo de documento:** Guía funcional completa para usuarios

---

## TABLA DE CONTENIDOS

1. [¿Qué es este proyecto?](#1-qué-es-este-proyecto)
2. [¿Cómo funciona? (Arquitectura visual)](#2-cómo-funciona-arquitectura-visual)
3. [Componentes del sistema y qué hace cada uno](#3-componentes-del-sistema-y-qué-hace-cada-uno)
4. [Cómo operarlo (Uso práctico)](#4-cómo-operarlo-uso-práctico)
5. [Proceso interno detallado](#5-proceso-interno-detallado)
6. [Estructura de archivos generada](#6-estructura-de-archivos-generada)
7. [Casos de uso y ejemplos](#7-casos-de-uso-y-ejemplos)
8. [Características especiales](#8-características-especiales)
9. [Ventajas del sistema](#9-ventajas-del-sistema)
10. [Limitaciones y consideraciones](#10-limitaciones-y-consideraciones)

---

## 1. ¿QUÉ ES ESTE PROYECTO?

### Concepto Central

Es un **sistema de investigación inteligente** que funciona como una **agencia de investigadores especializados** coordinados por un director.

**Analogía del mundo real:**

Imagina que tienes una agencia de investigación donde:
- Tú eres el cliente
- El **Coordinador** es el director de la agencia
- Los **Agentes Especializados** son investigadores expertos en distintas áreas
- Todos trabajan en paralelo investigando diferentes aspectos
- El director te presenta un informe integrado al final

**La diferencia con otras herramientas:**

- **ChatGPT normal**: Una sola conversación, un solo "cerebro" trabajando
- **Este framework**: Múltiples "cerebros" especializados trabajando en paralelo, coordinados por un director que te presenta resultados integrados

### Principio Fundamental: "Una Ventana, Múltiples Investigadores"

- **Lo que ves:** Una sola ventana de Claude Code (el coordinador)
- **Lo que pasa detrás:** 3, 5, 10 agentes especializados investigando simultáneamente
- **Lo que recibes:** Una síntesis integrada, no datos en bruto

---

## 2. ¿CÓMO FUNCIONA? (ARQUITECTURA VISUAL)

### El Flujo Completo de Principio a Fin

```
┌─────────────────────────────────────────────────────────────┐
│                         USUARIO                              │
│  "Investiga la efectividad del ClO₂ contra COVID-19"        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    COORDINADOR (Claude Code)                 │
│  - Analiza la solicitud                                      │
│  - Diseña estrategia multi-agente                            │
│  - Propone plan al usuario                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  USUARIO APRUEBA                             │
│  "Sí, adelante con 4 agentes especializados"                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              CREACIÓN DE PROYECTO                            │
│  - Se crea carpeta: projects/investigacion-clo2-...          │
│  - Se guarda contexto del usuario                            │
│  - Se prepara estructura para recibir resultados             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              CREACIÓN DE TAREAS (una por agente)             │
│  Tarea 1: analizar-quimica-molecular-clo2                    │
│  Tarea 2: analizar-toxicologia-bioquimica-clo2               │
│  Tarea 3: analizar-virologia-sars-cov2-clo2                  │
│  Tarea 4: revisar-estudios-clinicos-clo2                     │
│                                                              │
│  Cada tarea recibe:                                          │
│  - Carpeta propia                                            │
│  - Prompt especializado (guardado automáticamente)           │
│  - Espacio para reportes (carpeta reports/)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         LANZAMIENTO DE AGENTES EN PARALELO                   │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Agente 1    │  │  Agente 2    │  │  Agente 3    │      │
│  │  Químico     │  │  Toxicólogo  │  │  Virólogo    │      │
│  │              │  │              │  │              │      │
│  │ Investigando │  │ Investigando │  │ Investigando │      │
│  │ en background│  │ en background│  │ en background│      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  (Trabajan invisiblemente usando herramientas como           │
│   búsqueda web, lectura de papers, análisis de datos)       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            GENERACIÓN DE REPORTES                            │
│                                                              │
│  Cada agente guarda su reporte:                              │
│  - tasks/quimica-molecular/reports/quimica_molecular.md      │
│  - tasks/toxicologia/reports/toxicologia_bioquimica.md       │
│  - tasks/virologia/reports/virologia_sars_cov2.md            │
│  - tasks/estudios-clinicos/reports/estudios_clinicos.md      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              COORDINADOR LEE TODO                            │
│  - Lee los 4 reportes completos                              │
│  - Identifica hallazgos clave                                │
│  - Encuentra consensos y discrepancias                       │
│  - Integra perspectivas                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              SÍNTESIS INTEGRADA                              │
│  El coordinador crea un documento maestro que combina:       │
│  - Hallazgos de química molecular                            │
│  - Hallazgos toxicológicos                                   │
│  - Hallazgos virológicos                                     │
│  - Evidencia clínica                                         │
│  - Conclusiones integradas                                   │
│                                                              │
│  Guardado en: synthesis/sintesis_investigacion_clo2.md       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            PRESENTACIÓN AL USUARIO                           │
│  El coordinador te muestra:                                  │
│  - Resumen ejecutivo                                         │
│  - Hallazgos por área                                        │
│  - Conclusiones integradas                                   │
│  - Puntos de consenso/discrepancia                           │
│  - Recomendaciones                                           │
│                                                              │
│  "¿Quieres profundizar en algún aspecto?"                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. COMPONENTES DEL SISTEMA Y QUÉ HACE CADA UNO

### A. El Coordinador (Tu Punto de Contacto)

**Qué es:**
- Es una instancia de Claude Code corriendo en tu computadora
- Es la ÚNICA ventana con la que interactúas
- Tiene memoria persistente entre sesiones

**Qué hace:**

1. **Escucha tu solicitud** de investigación
2. **Analiza la complejidad** y decide si necesita múltiples agentes
3. **Diseña una estrategia** de investigación multi-agente
4. **Te consulta** antes de proceder ("¿Te parece bien este plan?")
5. **Crea la estructura** del proyecto automáticamente
6. **Lanza los agentes** especializados en background
7. **Monitorea** el progreso de los agentes
8. **Lee y analiza** todos los reportes generados
9. **Sintetiza** los hallazgos en un formato coherente
10. **Te presenta** resultados integrados (no datos en bruto)

**Analogía:**
Es como el director de una agencia de investigación que:
- Escucha lo que necesitas
- Contrata investigadores especializados
- Supervisa el trabajo
- Lee todos los informes
- Te presenta un informe ejecutivo integrado

### B. ProjectManager (Sistema de Organización)

**Qué es:**
Un sistema automático que organiza todo lo que se genera durante una investigación.

**Qué hace:**

1. **Crea proyectos** con estructura estándar
   - Cada investigación = un proyecto separado
   - ID único con timestamp: `investigacion-clo2-20251222-195407`
   - Carpeta dedicada con estructura predefinida

2. **Organiza tareas** (una por agente)
   - Cada agente = una tarea con su carpeta
   - Nombres descriptivos: `analizar-quimica-molecular-clo2`
   - Guarda automáticamente el prompt usado (reproducibilidad)

3. **Valida reportes** antes de aceptarlos
   - Verifica que el archivo existe físicamente
   - Verifica que tiene contenido suficiente (>100 caracteres)
   - Previene duplicados
   - Registra en metadata

4. **Mantiene trazabilidad** completa
   - Metadata en JSON: quién hizo qué, cuándo, con qué prompt
   - Historial de todos los proyectos
   - Estado de cada tarea (en progreso, completada, fallida)

**Beneficio para ti:**
No tienes que organizar nada manualmente. Todo se guarda automáticamente en una estructura clara y consistente.

### C. FrameworkValidator (Control de Calidad)

**Qué es:**
Un sistema de validación que verifica que todo se haga correctamente ANTES de ejecutar.

**Qué hace:**

1. **Valida nombres** de proyectos y tareas
   - Verifica que sigan convenciones estándar
   - Previene nombres confusos o inválidos
   - Ejemplo: rechaza "analisis.md", acepta "analisis_quimica_molecular.md"

2. **Valida estructura** de prompts
   - Verifica que los prompts tengan las 2 capas necesarias (explicaré más adelante)
   - Asegura que agentes reciban contexto adecuado
   - Previene rechazos por falta de contexto

3. **Valida estructura** de carpetas
   - Verifica que sigan el estándar v2.2 ORGANIZED
   - Identifica archivos mal ubicados
   - Sugiere correcciones

4. **Mantiene un log** de todas las validaciones
   - Qué se validó
   - Cuándo
   - Si pasó o falló
   - Por qué

**Beneficio para ti:**
Previene errores antes de que ocurran. Si algo va a fallar, te lo dice ANTES de desperdiciar tiempo.

### D. Los Agentes Especializados (Investigadores Invisibles)

**Qué son:**
Instancias de Claude Code lanzadas en background, cada una con una especialización específica.

**Qué hacen:**

1. **Reciben un prompt especializado** con:
   - Contexto del proyecto completo (qué pidió el usuario, por qué)
   - Rol específico (ej: "Eres un virólogo especializado en coronavirus")
   - Tarea concreta (ej: "Analiza mecanismos antivirales del ClO₂")
   - Metodología a seguir
   - Estructura de output esperada

2. **Investigan usando herramientas:**
   - Búsqueda web (WebSearch)
   - Lectura de URLs (WebFetch para papers, artículos)
   - Búsqueda en archivos locales (Grep, Glob)
   - Lectura de documentos (Read)

3. **Generan reportes especializados** en Markdown:
   - Análisis detallado de su área
   - Hallazgos clave
   - Evidencia citada (con fuentes)
   - Conclusiones de su especialidad

4. **Trabajan en paralelo** (simultáneamente):
   - Agente 1 investiga química mientras Agente 2 investiga toxicología
   - No se esperan entre sí
   - Más rápido que investigación secuencial

5. **Guardan resultados** en ubicación específica:
   - El coordinador les dice exactamente dónde guardar
   - Estructura estándar: `tasks/[nombre-tarea]/reports/[nombre-reporte].md`

**Beneficio para ti:**
Múltiples perspectivas especializadas trabajando simultáneamente. Como tener un equipo de expertos en lugar de un solo investigador generalista.

### E. Sistema de Enriquecimiento de Solicitudes (NUEVO en v2.3)

**Qué es:**
Un mecanismo inteligente que transforma solicitudes vagas o incompletas en requerimientos claros y completos.

**El problema que resuelve:**

Los usuarios frecuentemente hacen solicitudes como:
- "Investiga IA" (¿qué aspecto?)
- "Analiza el mercado" (¿qué mercado? ¿qué criterios?)
- "Busca información sobre X" (¿para qué? ¿qué nivel de detalle?)

Estas solicitudes vagas resultan en investigaciones que no cumplen expectativas.

**Cómo funciona:**

1. **Intercepta tu solicitud** antes de diseñar la estrategia
2. **Analiza la calidad:**
   - ¿Es específica o vaga?
   - ¿Qué contexto falta?
   - ¿Qué perspectivas no mencionaste?
   - ¿Cuál es el objetivo real?

3. **Enriquece la solicitud** expandiéndola con:
   - Interpretación del objetivo
   - Alcance sugerido
   - Perspectivas relevantes que no consideraste
   - Preguntas clave a responder
   - Criterios de éxito claros

4. **Te presenta la versión enriquecida:**
   ```
   He analizado tu solicitud. Interpreto que buscas:

   OBJETIVO: [expandido]

   ALCANCE SUGERIDO:
   - Aspecto 1
   - Aspecto 2
   - Aspecto 3

   PERSPECTIVAS RELEVANTES:
   1. Técnica: [por qué]
   2. Práctica: [por qué]
   3. Comparativa: [por qué]

   ¿Es correcto o quieres ajustar?
   ```

5. **Espera tu validación** antes de proceder

**Ejemplo real:**

**Tu solicitud vaga:**
```
"Investiga blockchain"
```

**Enriquecimiento del coordinador:**
```
He analizado tu solicitud. "Investiga blockchain" es muy amplia.

OBJETIVO:
Comprender blockchain technology comprehensivamente.

ALCANCE SUGERIDO:
- Cómo funciona técnicamente
- Dónde se usa en el mundo real
- Ventajas vs limitaciones
- Comparación con alternativas
- Recomendaciones de adopción

PERSPECTIVAS PROPUESTAS:
1. Técnica: Arquitectura, consenso, criptografía
2. Negocios: Casos de uso, ROI, adopción
3. Comparativa: Blockchain vs bases de datos tradicionales
4. Futura: Tendencias emergentes

PREGUNTAS CLAVE:
- ¿Qué es blockchain realmente?
- ¿Dónde se usa exitosamente HOY?
- ¿Cuáles son las limitaciones reales?
- ¿Cuándo usarlo y cuándo NO?

CRITERIOS DE ÉXITO:
Al finalizar deberías poder:
- Explicarlo a alguien no técnico
- Identificar 5+ aplicaciones reales
- Decidir si es útil para tu caso de uso

¿Este alcance es correcto o quieres ajustarlo?
```

**Beneficio para ti:**

- **No necesitas ser experto** en formular solicitudes
- **Descubres perspectivas** que no habías considerado
- **Resultados más completos** desde el primer intento
- **Menos iteraciones** de "no era lo que quería"
- **Aprendes** a hacer mejores solicitudes con el tiempo

**Cuándo se activa:**

- Automáticamente cuando detecta vaguedad
- Cuando falta contexto obvio
- Cuando hay múltiples interpretaciones posibles
- Primera vez que usas el framework

**Cuándo NO se activa:**

- Tu solicitud ya es muy específica y detallada
- Dices explícitamente "solo haz exactamente esto"
- Es seguimiento a un proyecto existente

**Documentación completa:**
Ver `docs/PROTOCOLO_ENRIQUECIMIENTO_SOLICITUDES.md`

---

## 4. CÓMO OPERARLO (USO PRÁCTICO)

### Inicio del Sistema

**Paso 1: Lanzar el coordinador**

```bash
./start_coordinator.sh
```

**Qué pasa internamente:**

1. El script verifica si existe un entorno virtual Python
   - Si NO existe → lo crea automáticamente e instala dependencias
   - Si SÍ existe → lo activa

2. Verifica la memoria del coordinador (archivo CLAUDE.md)
   - Si es primera vez → inicializa memoria
   - Si ya existe → crea un backup de seguridad

3. Muestra estado del sistema:
   - Tamaño de memoria
   - Número de backups disponibles
   - Tareas activas (si hay)

4. Lanza Claude Code con el coordinador cargado

**Resultado visible:**
Una ventana de Claude Code se abre, lista para recibir tu solicitud.

### Flujo de Trabajo Normal

**Paso 2: Solicitar una investigación**

Tú escribes algo como:

```
"Quiero investigar la efectividad del dióxido de cloro contra COVID-19.
 Usa un enfoque científico neutral, solo analiza la evidencia disponible."
```

**Qué pasa:**

El coordinador:
1. Recibe tu solicitud
2. **[NUEVO v2.3]** Analiza la calidad de tu solicitud

**Paso 3: Enriquecimiento de la solicitud (NUEVO en v2.3)**

Si el coordinador detecta que tu solicitud podría ser más específica, te presenta un enriquecimiento:

```
Coordinador: "He analizado tu solicitud. Déjame confirmar que entiendo correctamente:

             OBJETIVO:
             Investigar la efectividad del dióxido de cloro (ClO₂) contra
             COVID-19 desde una perspectiva científica neutral.

             ALCANCE SUGERIDO:
             - Química molecular del ClO₂
             - Mecanismos antivirales
             - Toxicología y seguridad
             - Evidencia clínica disponible

             PERSPECTIVAS PROPUESTAS:
             1. Química: Propiedades y mecanismos
             2. Bioquímica/Toxicología: Efectos y seguridad
             3. Virología: Mecanismos contra SARS-CoV-2
             4. Clínica: Estudios y evidencia

             CRITERIOS DE ÉXITO:
             Al finalizar, tendrás:
             - Comprensión de mecanismos de acción
             - Evaluación de seguridad/toxicidad
             - Análisis de evidencia clínica
             - Conclusión basada en ciencia

             ¿Este alcance es correcto o quieres ajustar algo?"
```

**Tú respondes:**
- "Perfecto, procede" → Continúa con ese alcance
- "Agrega análisis de comparación con otros antivirales" → Ajusta alcance
- "Enfócate solo en seguridad y toxicología" → Reduce alcance

**Paso 4: El coordinador diseña la estrategia multi-agente**

Una vez validado el alcance enriquecido, el coordinador presenta el plan de ejecución:

```
Coordinador: "Esta investigación requiere análisis multidisciplinario.

             Propongo crear 4 agentes especializados:

             1. QUÍMICO MOLECULAR
                Analizará:
                - Estructura molecular del ClO₂
                - Propiedades químicas
                - Mecanismos de oxidación

             2. BIOQUÍMICO/TOXICÓLOGO
                Analizará:
                - Efectos en células humanas
                - Toxicidad y seguridad
                - Ventana terapéutica

             3. VIRÓLOGO
                Analizará:
                - Mecanismos antivirales
                - Efectividad contra SARS-CoV-2
                - Selectividad viral vs celular

             4. EPIDEMIÓLOGO CLÍNICO
                Analizará:
                - Estudios clínicos publicados
                - Evidencia de efectividad
                - Protocolos de administración

             Cada agente generará un reporte especializado.
             Al final sintetizaré todos los hallazgos.

             ¿Procedemos con esta estrategia?"
```

**Paso 5: Tú apruebas o modificas la estrategia**

Opciones:
- "Sí, adelante" → Procede con el plan
- "Agrega un agente que analice X" → Modifica el plan
- "Solo quiero 2 agentes: químico y clínico" → Ajusta el plan
- "Mejor hazlo con un solo agente comprehensivo" → Cambia la estrategia

**Paso 6: Ejecución (invisible para ti)**

Una vez aprobado, el coordinador:

1. **Crea el proyecto** automáticamente:
   ```
   projects/investigacion-clo2-covid-19-20251222-195407/
   ├── project_info.json  (metadata del proyecto)
   ├── context.md         (tu solicitud original guardada)
   ├── tasks/             (vacío, se llenará)
   └── synthesis/         (vacío, se llenará)
   ```

2. **Crea las tareas** (una por agente):
   ```
   tasks/analizar-quimica-molecular-clo2/
   ├── task_info.json  (metadata de la tarea)
   ├── prompt.md       (prompt completo guardado)
   ├── README.md       (índice generado automáticamente)
   └── reports/        (donde agente guardará resultados)

   tasks/analizar-toxicologia-bioquimica-clo2/
   ├── task_info.json
   ├── prompt.md
   ├── README.md
   └── reports/

   (y así para cada agente...)
   ```

3. **Lanza los agentes** en background (invisibles):
   - No ves nuevas ventanas
   - No ves su trabajo en tiempo real
   - Trabajan simultáneamente

4. **Te informa**:
   ```
   Coordinador: "Agentes lanzados exitosamente:

                ✓ Agente 1: Químico Molecular (investigando...)
                ✓ Agente 2: Bioquímico/Toxicólogo (investigando...)
                ✓ Agente 3: Virólogo (investigando...)
                ✓ Agente 4: Epidemiólogo Clínico (investigando...)

                Te informaré cuando completen sus investigaciones.
                Esto puede tomar 10-20 minutos dependiendo de la complejidad."
   ```

**Paso 7: Espera (puedes seguir conversando)**

Mientras los agentes trabajan:
- Puedes preguntarle al coordinador sobre el progreso
- Puedes pedirle que te muestre lo que llevan
- Puedes hacer otras preguntas no relacionadas
- Puedes cerrar y volver después (el trabajo continúa)

**Paso 8: Recepción de resultados**

Cuando los agentes terminan:

```
Coordinador: "Investigación completada.

             He recibido los 4 reportes especializados:
             ✓ Química Molecular (15 páginas)
             ✓ Toxicología/Bioquímica (12 páginas)
             ✓ Virología (18 páginas)
             ✓ Estudios Clínicos (20 páginas)

             Estoy sintetizando los hallazgos...

             [Unos minutos después]

             Listo. Aquí está la síntesis integrada:"
```

**Paso 9: Síntesis presentada**

El coordinador te muestra un documento integrado:

```
# SÍNTESIS: Efectividad del Dióxido de Cloro contra COVID-19

## RESUMEN EJECUTIVO

[Resumen de 2-3 párrafos con los hallazgos principales]

## QUÍMICA MOLECULAR (Agente 1)

### Hallazgos Clave:
- El ClO₂ es un oxidante fuerte con geometría molecular angular
- Mecanismo de acción: oxidación de proteínas y ácidos nucleicos
- Estabilidad limitada en solución acuosa

[Más detalles...]

## TOXICOLOGÍA Y BIOQUÍMICA (Agente 2)

### Hallazgos Clave:
- Toxicidad dependiente de concentración
- Ventana terapéutica estrecha según estudios in vitro
- Efectos en células humanas: [detalles]

[Más detalles...]

## VIROLOGÍA (Agente 3)

### Hallazgos Clave:
- Mecanismo antiviral: oxidación de proteína spike
- Efectividad in vitro contra SARS-CoV-2: [datos]
- Selectividad viral vs celular: [análisis]

[Más detalles...]

## EVIDENCIA CLÍNICA (Agente 4)

### Hallazgos Clave:
- Estudios disponibles: [lista con calidad metodológica]
- Resultados reportados: [resumen]
- Limitaciones metodológicas identificadas: [detalles]

[Más detalles...]

## CONCLUSIONES INTEGRADAS

### Consensos entre especialidades:
1. [Punto en el que todos coinciden]
2. [Otro punto de consenso]

### Discrepancias o incertidumbres:
1. [Áreas donde falta evidencia]
2. [Puntos de discusión]

### Evaluación Final:
[Conclusión integrada basada en todas las perspectivas]

## RECOMENDACIONES

[Basadas en la evidencia revisada]

## FUENTES Y REFERENCIAS

[Compilación de todas las fuentes citadas por los agentes]
```

**Paso 10: Interacción post-investigación**

Ahora puedes:
- Preguntar detalles: "¿Qué estudios clínicos específicos revisó el agente 4?"
- Pedir profundización: "Profundiza en el mecanismo antiviral"
- Solicitar comparaciones: "Compara con otros antivirales conocidos"
- Pedir reportes completos: "Muéstrame el reporte completo del virólogo"

### Consultar Investigaciones Anteriores

**Comando:**
```bash
python core/project_manager.py list
```

**Resultado:**
```
====================================
Proyectos encontrados: 3
====================================

[completed] Investigación ClO₂ COVID-19
  ID: investigacion-clo2-covid-19-20251222-195407
  Creado: 2025-12-22T19:54:07
  Tareas: 4

[in_progress] Análisis Competidores IA
  ID: analisis-competidores-ia-20251223-101523
  Creado: 2025-12-23T10:15:23
  Tareas: 3

[completed] Investigación Blockchain Escalabilidad
  ID: investigacion-blockchain-escalabilidad-20251220-143012
  Creado: 2025-12-20T14:30:12
  Tareas: 5
```

**Ver proyecto específico:**
```bash
python core/project_manager.py get investigacion-clo2-covid-19-20251222-195407
```

**Resultado:**
```
# Proyecto: Investigación ClO₂ COVID-19

**ID:** investigacion-clo2-covid-19-20251222-195407
**Estado:** completed
**Creado:** 2025-12-22T19:54:07

## Solicitud del Usuario
Investiga la efectividad del dióxido de cloro contra COVID-19

## Tareas Completadas
- [OK] Análisis de química molecular del ClO₂
  - reports/quimica_molecular_clo2.md

- [OK] Análisis de toxicología y bioquímica
  - reports/toxicologia_bioquimica_clo2.md

- [OK] Análisis virológico
  - reports/virologia_sars_cov2_clo2.md

- [OK] Revisión de estudios clínicos
  - reports/estudios_clinicos_clo2.md

## Síntesis Final
[OK] sintesis_investigacion_clo2_covid19.md
```

---

## 5. PROCESO INTERNO DETALLADO

### A. Creación de Proyecto

**Qué pasa cuando el coordinador crea un proyecto:**

1. **Genera ID único:**
   - Toma tu nombre: "Investigación ClO₂ COVID-19"
   - Lo sanitiza: "investigacion-clo2-covid-19"
   - Agrega timestamp: "investigacion-clo2-covid-19-20251222-195407"
   - Resultado: ID único que nunca se repetirá

2. **Crea estructura de carpetas:**
   ```
   projects/investigacion-clo2-covid-19-20251222-195407/
   ├── project_info.json
   ├── context.md
   ├── tasks/
   └── synthesis/
   ```

3. **Guarda metadata en project_info.json:**
   - Nombre del proyecto
   - Tu solicitud original (textual)
   - Contexto adicional
   - Fecha/hora de creación
   - Estado inicial: "in_progress"
   - Lista de tareas (vacía inicialmente)
   - Síntesis (null inicialmente)

4. **Guarda contexto en context.md:**
   - Tu solicitud original
   - Cualquier contexto adicional que diste
   - Timestamp

**Por qué importa:**
- **Trazabilidad:** Siempre puedes ver qué pediste exactamente
- **Reproducibilidad:** Tienes toda la información para repetir la investigación
- **Organización:** Cada investigación aislada en su carpeta

### B. Creación de Tareas

**Qué pasa cuando el coordinador crea una tarea:**

1. **Validación previa (automática):**
   - Verifica que el nombre siga convenciones
   - Verifica que el prompt tenga estructura adecuada
   - Verifica que el proyecto exista
   - Si algo falla → BLOQUEA la creación y te dice por qué

2. **Sanitiza el nombre:**
   - Entrada: "Analizar Química Molecular del ClO₂"
   - Salida: "analizar-quimica-molecular-clo2"
   - (lowercase, guiones en lugar de espacios, sin caracteres especiales)

3. **Crea carpeta de la tarea:**
   ```
   tasks/analizar-quimica-molecular-clo2/
   ├── task_info.json     (se crea ahora)
   ├── prompt.md          (se crea ahora)
   ├── README.md          (se crea ahora)
   └── reports/           (se crea ahora, vacía)
   ```

4. **Guarda el prompt COMPLETO en prompt.md:**
   - Todo el prompt que recibirá el agente
   - Incluye las 2 capas (contexto + técnico)
   - **Reproducibilidad total:** Puedes relanzar la tarea con el mismo prompt

5. **Genera README.md automático:**
   - Template predefinido con secciones estándar
   - Título formateado
   - Descripción de la tarea
   - Placeholder para reportes (se llena después)

6. **Guarda metadata en task_info.json:**
   - Nombre de la tarea
   - Descripción
   - Fecha/hora de creación
   - Estado: "in_progress"
   - Referencia al prompt guardado
   - Lista de reportes (vacía inicialmente)

7. **Actualiza project_info.json:**
   - Agrega la tarea a la lista de tareas del proyecto

**Por qué importa:**
- **Reproducibilidad:** El prompt guardado permite repetir exactamente la misma investigación
- **Trazabilidad:** Metadata completa de cada tarea
- **Organización:** Estructura estándar en todas las tareas

### C. Arquitectura de Prompts de 2 Capas (CRÍTICO)

**El problema que resuelve:**

Los agentes lanzados en background NO tienen acceso al historial de la conversación. Para ellos, el prompt es su ÚNICO contexto.

Sin contexto conversacional, los agentes pueden:
- Auto-censurarse innecesariamente
- Rechazar tareas legítimas
- No entender el propósito del trabajo

**La solución: Prompts de 2 Capas**

**CAPA 1: Contexto Conversacional** (Qué pidió el usuario, por qué, bajo qué supervisión)

```markdown
## CONTEXTO DEL PROYECTO

El usuario ha solicitado:

> "Investiga la efectividad del dióxido de cloro contra COVID-19.
>  Usa enfoque científico neutral, solo evidencia."

**Naturaleza del proyecto:**
- Investigación científica académica
- Supervisión humana activa del usuario
- Objetivo: Recopilar y analizar evidencia científica publicada
- Enfoque neutral (no promoción ni condena de tratamientos)

**Disclaimer:**
Este es un proyecto de investigación supervisado por el usuario.
No se está creando contenido para uso médico directo.
El objetivo es compilar evidencia científica disponible.

---
```

**CAPA 2: Tarea Técnica** (Qué hacer específicamente)

```markdown
## TU TAREA

**Tu Rol:** Químico Molecular Especializado

**Objetivo:**
Analizar la química molecular del dióxido de cloro (ClO₂) para
comprender sus propiedades y mecanismos de acción.

**Tareas Específicas:**
1. Estructura molecular del ClO₂
2. Propiedades químicas relevantes
3. Mecanismos de oxidación
4. Interacción con biomoléculas

**Metodología:**
- Revisar literatura científica peer-reviewed
- Citar fuentes con DOI cuando disponible
- Enfoque en evidencia experimental

**Estructura de Output:**
Guarda tu reporte en: [ruta específica]

Secciones requeridas:
- Resumen ejecutivo
- Análisis técnico detallado
- Conclusiones
- Referencias

**INICIA LA INVESTIGACIÓN AHORA.**
```

**Por qué funciona:**

Con la Capa 1, el agente entiende:
- Hay un usuario humano supervisando
- Es investigación legítima académica
- Hay intención científica clara
- No es para uso directo médico

Con la Capa 2, el agente sabe:
- Qué rol debe tomar
- Qué debe investigar exactamente
- Cómo debe hacerlo
- Dónde guardar resultados

**Evidencia experimental:**
- Agentes SIN Capa 1: Rechazaron tareas legítimas
- Agentes CON Capa 1: Completaron investigaciones exitosamente

### D. Lanzamiento de Agentes

**Qué pasa cuando el coordinador lanza un agente:**

1. **Prepara el prompt completo:**
   - Toma el prompt de 2 capas guardado
   - Agrega instrucciones específicas de ruta de output
   - Agrega instrucciones de formato

2. **Lanza con Task Tool:**
   - Tipo de agente: "general-purpose" (investigación)
   - Modo: background (invisible)
   - Prompt: el preparado con 2 capas
   - Descripción corta para tracking

3. **Registra el ID de tarea:**
   - Cada agente recibe un ID único
   - El coordinador lo guarda para monitoreo

4. **El agente comienza a trabajar (invisible):**
   - Lee su prompt completo
   - Usa herramientas disponibles:
     - WebSearch: buscar en internet
     - WebFetch: leer artículos, papers
     - Grep/Glob: buscar archivos locales
     - Read: leer documentos
   - Genera su reporte
   - Lo guarda en la ruta especificada

**Paralelización:**

Si lanzas 4 agentes:
- Los 4 inician simultáneamente
- Trabajan independientemente
- No se esperan entre sí
- Resultado: Investigación 4x más rápida que secuencial

### E. Monitoreo y Registro de Reportes

**Qué pasa mientras los agentes trabajan:**

1. **Coordinador monitorea progreso:**
   - Revisa periódicamente el estado de cada agente
   - Verifica si han terminado
   - Puede leer outputs parciales

2. **Cuando un agente termina:**

   **Paso 1: Verificación física del archivo**
   - El coordinador verifica que el archivo exista en el disco
   - Verifica que esté en la ubicación correcta
   - Si NO existe → Error específico con ruta completa

   **Paso 2: Validación de contenido**
   - Lee el archivo completo
   - Verifica que tenga contenido suficiente (>100 caracteres)
   - Si es muy corto → Error de contenido insuficiente

   **Paso 3: Validación de duplicados**
   - Verifica que no se haya registrado antes
   - Previene sobrescrituras accidentales

   **Paso 4: Registro en metadata**
   - Si todo OK → Registra en task_info.json
   - Agrega el nombre del archivo a la lista de reportes
   - Guarda timestamp de registro

   **Paso 5: Actualización de estado**
   - Marca la tarea como "completed"
   - Agrega timestamp de completado

3. **Si hay problemas:**
   - El coordinador te informa específicamente qué falló
   - Te da opciones de solución
   - Puede reintentar con el agente

### F. Síntesis Final

**Qué pasa cuando todos los agentes terminan:**

1. **Coordinador lee TODOS los reportes:**
   - Lee el reporte del químico completo
   - Lee el reporte del toxicólogo completo
   - Lee el reporte del virólogo completo
   - Lee el reporte del epidemiólogo completo
   - (Todos los reportes, texto completo)

2. **Análisis integrado:**
   - Identifica hallazgos clave de cada reporte
   - Encuentra puntos de consenso entre especialidades
   - Identifica discrepancias o contradicciones
   - Detecta brechas en la evidencia
   - Conecta hallazgos de diferentes áreas

3. **Generación de síntesis:**
   - Crea documento maestro estructurado
   - Resumen ejecutivo (2-3 párrafos de lo más importante)
   - Sección por cada especialidad con hallazgos clave
   - Sección de conclusiones integradas
   - Sección de consensos y discrepancias
   - Recomendaciones basadas en evidencia
   - Compilación de referencias

4. **Guarda síntesis:**
   - Archivo: `synthesis/sintesis_investigacion_clo2_covid19.md`
   - Formato: Markdown profesional
   - Registra en metadata del proyecto

5. **Marca proyecto como completado:**
   - Estado: "completed"
   - Timestamp de finalización
   - Referencia a la síntesis

6. **Te presenta los resultados:**
   - Muestra la síntesis completa
   - Ofrece profundizar en aspectos específicos
   - Permite acceso a reportes individuales

---

## 6. ESTRUCTURA DE ARCHIVOS GENERADA

### Proyecto Completo (después de investigación)

```
projects/investigacion-clo2-covid-19-20251222-195407/
│
├── project_info.json          ← Metadata del proyecto completo
├── context.md                 ← Tu solicitud original guardada
│
├── tasks/                     ← Una carpeta por cada agente
│   │
│   ├── analizar-quimica-molecular-clo2/
│   │   ├── task_info.json     ← Metadata de esta tarea
│   │   ├── prompt.md          ← Prompt COMPLETO guardado
│   │   ├── README.md          ← Índice de la tarea
│   │   └── reports/           ← Reportes generados
│   │       └── quimica_molecular_clo2.md  ← Reporte del agente
│   │
│   ├── analizar-toxicologia-bioquimica-clo2/
│   │   ├── task_info.json
│   │   ├── prompt.md
│   │   ├── README.md
│   │   └── reports/
│   │       └── toxicologia_bioquimica_clo2.md
│   │
│   ├── analizar-virologia-sars-cov2-clo2/
│   │   ├── task_info.json
│   │   ├── prompt.md
│   │   ├── README.md
│   │   └── reports/
│   │       └── virologia_sars_cov2_clo2.md
│   │
│   └── revisar-estudios-clinicos-clo2/
│       ├── task_info.json
│       ├── prompt.md
│       ├── README.md
│       └── reports/
│           └── estudios_clinicos_clo2.md
│
└── synthesis/                 ← Síntesis del coordinador
    └── sintesis_investigacion_clo2_covid19.md  ← Integración final
```

### Navegación Manual (si quieres explorar directamente)

**Ver todos tus proyectos:**
```bash
ls projects/
```

**Ver tareas de un proyecto:**
```bash
ls projects/investigacion-clo2-covid-19-20251222-195407/tasks/
```

**Leer un reporte específico:**
```bash
cat projects/investigacion-clo2-covid-19-20251222-195407/tasks/analizar-quimica-molecular-clo2/reports/quimica_molecular_clo2.md
```

**Leer el prompt que se usó:**
```bash
cat projects/investigacion-clo2-covid-19-20251222-195407/tasks/analizar-quimica-molecular-clo2/prompt.md
```

**Leer la síntesis final:**
```bash
cat projects/investigacion-clo2-covid-19-20251222-195407/synthesis/sintesis_investigacion_clo2_covid19.md
```

---

## 7. CASOS DE USO Y EJEMPLOS

### Caso 1: Investigación Científica

**Solicitud:**
"Investiga los mecanismos moleculares de la fatiga crónica post-viral"

**Estrategia del coordinador:**
- Agente 1: Neurólogo (analiza efectos neurológicos)
- Agente 2: Inmunólogo (analiza respuesta inmune prolongada)
- Agente 3: Metabolista (analiza disfunción metabólica)
- Agente 4: Investigador Clínico (revisa estudios de pacientes)

**Resultado:**
Síntesis integrando las 4 perspectivas con evidencia científica actual

### Caso 2: Análisis Competitivo de Mercado

**Solicitud:**
"Analiza el panorama competitivo de herramientas de IA para desarrollo de software"

**Estrategia del coordinador:**
- Agente 1: Analista de Competidores Directos (GitHub Copilot, Cursor, etc.)
- Agente 2: Analista de Tendencias de Mercado (adopción, crecimiento)
- Agente 3: Analista Técnico (capacidades, limitaciones)
- Agente 4: Analista de Precios y Modelos de Negocio

**Resultado:**
Análisis competitivo completo con benchmarks y recomendaciones

### Caso 3: Investigación Técnica

**Solicitud:**
"Investiga soluciones de escalabilidad para blockchain"

**Estrategia del coordinador:**
- Agente 1: Especialista en Layer 2 (Rollups, State Channels)
- Agente 2: Especialista en Sharding
- Agente 3: Especialista en Sidechains
- Agente 4: Analista de Trade-offs (seguridad vs escalabilidad)

**Resultado:**
Comparación técnica profunda con recomendaciones según caso de uso

### Caso 4: Análisis de Datos

**Solicitud:**
"Analiza el dataset de ventas del último año y encuentra insights"

**Estrategia del coordinador:**
- Agente 1: Analista de Tendencias Temporales
- Agente 2: Analista de Segmentación de Clientes
- Agente 3: Analista de Productos (qué se vende mejor)
- Agente 4: Analista Predictivo (proyecciones)

**Resultado:**
Dashboard de insights con visualizaciones y recomendaciones

---

## 8. CARACTERÍSTICAS ESPECIALES

### A. Reproducibilidad Total

**Qué significa:**
Cualquier investigación puede repetirse exactamente.

**Cómo:**
- El prompt completo está guardado en `prompt.md`
- La solicitud original está en `context.md`
- Metadata tiene timestamps y descripciones

**Beneficio:**
- Puedes relanzar la misma investigación en el futuro
- Puedes compartir el proyecto completo con otros
- Otros pueden reproducir tu investigación exactamente

### B. Trazabilidad Completa

**Qué significa:**
Puedes rastrear cada decisión y cada output hasta su origen.

**Cómo:**
- Metadata en cada nivel (proyecto, tarea, reporte)
- Prompts guardados (qué se le pidió a cada agente)
- Logs de validación (qué se validó y cuándo)
- Timestamps en todo

**Beneficio:**
- Auditable
- Transparente
- Debugging fácil si algo falla

### C. Sistema de Memoria Persistente

**Qué significa:**
El coordinador "recuerda" entre sesiones.

**Cómo:**
- Archivo CLAUDE.md contiene instrucciones y memoria
- Backups automáticos al iniciar y cerrar
- `.memory_backups/` guarda histórico

**Beneficio:**
- El coordinador aprende de proyectos anteriores
- Puede mejorar estrategias basándose en experiencia
- Puedes recuperar estados anteriores si algo sale mal

### D. Validación Multi-Capa

**Qué significa:**
Múltiples verificaciones antes de ejecutar y después de completar.

**Capas de validación:**

1. **Antes de crear tarea:**
   - Nombre válido
   - Prompt adecuado
   - Proyecto existe

2. **Antes de lanzar agente:**
   - Estructura de tarea correcta
   - Metadata presente
   - Rutas válidas

3. **Antes de registrar reporte:**
   - Archivo existe físicamente
   - Contenido suficiente
   - No duplicado

**Beneficio:**
- Previene errores antes de desperdiciar tiempo
- Feedback inmediato si algo está mal
- Calidad consistente

### E. Aislamiento de Entorno

**Qué significa:**
El framework usa su propio entorno Python aislado.

**Cómo:**
- Virtual environment en `.venv/`
- Dependencias específicas en `requirements.txt`
- Validación de venv activo antes de instalar paquetes

**Beneficio:**
- No contamina tu Python global
- Sin conflictos con otros proyectos
- Reproducible en otras máquinas

---

## 9. VENTAJAS DEL SISTEMA

### Comparado con ChatGPT Normal:

| Aspecto | ChatGPT Normal | Este Framework |
|---------|----------------|----------------|
| Investigadores | 1 (generalista) | N (especializados) |
| Paralelización | No | Sí (todos simultáneos) |
| Profundidad | Limitada | Alta por especialidad |
| Organización | Manual | Automática |
| Reproducibilidad | No | Total (prompts guardados) |
| Trazabilidad | No | Completa (metadata) |
| Síntesis | Directa | Integrada de múltiples fuentes |

### Comparado con Búsqueda Manual:

| Aspecto | Búsqueda Manual | Este Framework |
|---------|-----------------|----------------|
| Tiempo | Horas/días | Minutos (paralelo) |
| Organización | Tú la haces | Automática |
| Síntesis | Tú la haces | El coordinador la hace |
| Múltiples perspectivas | Difícil coordinar | Automático |
| Guardado de proceso | Manual | Automático |

### Ventajas Clave:

**Multiplicador de Productividad:**
- 4 agentes = 4x la capacidad investigativa
- Trabajando en paralelo = 4x más rápido que secuencial

**Calidad Superior:**
- Especialización por área
- Síntesis integrada (no solo concatenación)
- Validación automática

**Organización Sin Esfuerzo:**
- Estructura estándar automática
- Naming conventions consistentes
- Metadata completa

**Transparencia Total:**
- Prompts guardados (qué se pidió)
- Reportes completos (qué se encontró)
- Síntesis integrada (qué significa)

**Reproducibilidad:**
- Comparte el proyecto completo
- Otros pueden replicar exactamente
- Puedes relanzar en el futuro

---

## 10. LIMITACIONES Y CONSIDERACIONES

### Limitaciones Actuales:

1. **Requiere Claude Code:**
   - No funciona con ChatGPT o Claude web
   - Necesitas Claude Code instalado localmente

2. **Costo en Tokens:**
   - Múltiples agentes = más uso de API
   - Coordinar 4 agentes usa 4x tokens que 1 agente

3. **Tiempo de Ejecución:**
   - Investigaciones complejas: 10-30 minutos
   - Depende de la profundidad solicitada

4. **Conocimiento del Coordinador:**
   - El coordinador debe saber diseñar estrategias multi-agente
   - Calidad de resultados depende de la estrategia

### Mejores Prácticas:

1. **Sé específico en tu solicitud:**
   - Malo: "Investiga X"
   - Bueno: "Investiga X enfocándote en Y, con perspectiva Z"

2. **Revisa y aprueba la estrategia:**
   - No aceptes automáticamente
   - Pide modificaciones si algo no te convence

3. **Usa para investigaciones complejas:**
   - No uses 4 agentes para preguntas simples
   - Reserva para temas multidisciplinarios

4. **Explora los reportes individuales:**
   - La síntesis es el resumen
   - Los reportes individuales tienen todo el detalle

---

## RESUMEN FINAL

### ¿Qué es?
Un sistema que multiplica tu capacidad investigativa lanzando múltiples agentes especializados que trabajan en paralelo bajo la coordinación de un agente central.

### ¿Cómo funciona?
1. Tú pides una investigación
2. El coordinador diseña una estrategia multi-agente
3. Lanza agentes especializados en background
4. Cada agente investiga su área
5. El coordinador sintetiza todos los hallazgos
6. Recibes una síntesis integrada

### ¿Para qué sirve?
- Investigaciones científicas multidisciplinarias
- Análisis competitivo de mercado
- Investigación técnica profunda
- Análisis de datos desde múltiples ángulos
- Cualquier tema que beneficie de múltiples perspectivas especializadas

### ¿Por qué usarlo?
- **Más rápido:** Paralelización de trabajo
- **Más profundo:** Especialización por área
- **Más organizado:** Estructura automática
- **Más reproducible:** Todo guardado con metadata
- **Más transparente:** Trazabilidad completa

### Diferencia clave con otras herramientas:
**No es un chat más. Es una agencia de investigación coordinada que trabaja para ti.**

---

## REFERENCIAS ADICIONALES

Para información técnica más detallada, consulta:

- **README.md** - Guía de inicio rápido
- **CLAUDE.md** - Instrucciones completas para el coordinador
- **docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md** - Estándar de estructura de proyectos
- **docs/PROTOCOLO_PROMPTS_AGENTES.md** - Protocolo de prompts de 2 capas
- **core/project_manager.py** - Implementación del gestor de proyectos
- **core/framework_validator.py** - Sistema de validación

---

**Creado:** 2026-01-24
**Autor:** Framework Agéntico v2.2
**Licencia:** [Especifica la licencia de tu proyecto]
