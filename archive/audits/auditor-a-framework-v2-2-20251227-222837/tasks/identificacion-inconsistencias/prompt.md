# TAREA: IDENTIFICACION DE INCONSISTENCIAS CROSS-SYSTEM

## TU ROL

Eres un Systems Analyst con visión holística. Tu trabajo es comparar auditorías de documentación, código y estructura para detectar inconsistencias entre lo documentado, lo implementado, y lo usado.

## OBJETIVO

Generar matriz de inconsistencias que muestre dónde la documentación, el código, y la estructura real del framework no coinciden.

## CONTEXTO REQUERIDO

ANTES de comenzar tu análisis, LEE estos documentos para entender el framework:

1. **ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md** - Estándar oficial
2. **README.md** - Documentación pública
3. **CLAUDE.md** - Instrucciones del coordinador
4. **CHECKLIST.md** - Checklist de validación

Estos documentos te darán el contexto de:
- Qué promete el framework
- Cómo se supone que funciona
- Qué estructura se espera

## INSUMOS DE TU ANALISIS

Debes leer los reportes de las 3 auditorías anteriores:

1. **../auditoria-documentacion/reports/analisis_documentacion_core.md**
   - Inconsistencias encontradas en docs
   - Versiones mencionadas
   - Referencias rotas

2. **../auditoria-codigo/reports/analisis_codigo_python.md**
   - Problemas de código
   - Versiones en módulos Python
   - Código deprecated

3. **../auditoria-estructura/reports/validacion_proyecto_covid.md**
   - Estado real del proyecto COVID
   - Tareas compliant vs non-compliant
   - Estructura real vs esperada

## ANALISIS REQUERIDO

### 1. Comparación Docs vs Código

**Pregunta**: ¿Lo que dicen los docs coincide con lo que hace el código?

Detecta:
- Features documentadas pero no implementadas
- Features implementadas pero no documentadas
- Versiones mencionadas en docs vs código
- Comandos documentados vs código real
- Ejemplos en docs vs implementación

### 2. Comparación Docs vs Estructura Real

**Pregunta**: ¿La estructura documentada coincide con la realidad?

Detecta:
- Estructura esperada según docs vs estructura real
- Convenciones de naming documentadas vs usadas
- Archivos obligatorios según docs vs presentes
- Estándar v2.2 vs cumplimiento real

### 3. Comparación Código vs Estructura Real

**Pregunta**: ¿Lo que hace el código genera la estructura correcta?

Detecta:
- project_manager.py crea estructura según v2.2?
- framework_validator.py valida correctamente?
- Scripts de reorganización funcionan bien?
- Código genera lo que promete?

### 4. Análisis de Versiones

Compara versiones mencionadas en:
- Documentación (CLAUDE.md, README.md, etc.)
- Código Python (headers de módulos)
- Configuraciones (settings.json)
- Proyectos reales (project_info.json)

### 5. Análisis de Convenciones

Compara convenciones de naming:
- Documentadas en ESTANDAR_v2.2.md
- Implementadas en project_manager.py (_sanitize_name)
- Usadas en proyecto COVID real
- Validadas por framework_validator.py

## METODOLOGIA

1. Lee documentos de contexto (ESTANDAR, README, CLAUDE.md)
2. Lee los 3 reportes de auditorías previas
3. Crea matriz de comparación
4. Identifica gaps entre documentación, código y realidad
5. Prioriza inconsistencias por impacto
6. Genera reporte consolidado

## ESTRUCTURA DE OUTPUT

Reporte en: reports/matriz_inconsistencias.md

```markdown
# IDENTIFICACION DE INCONSISTENCIAS CROSS-SYSTEM

## RESUMEN EJECUTIVO

- Inconsistencias críticas: X
- Inconsistencias altas: X
- Inconsistencias medias: X
- Áreas afectadas: [documentación, código, estructura]

## MATRIZ DE INCONSISTENCIAS

### Inconsistencia 1: [Título descriptivo]

**Tipo**: Docs vs Código / Docs vs Estructura / Código vs Estructura
**Severidad**: Crítica / Alta / Media / Baja

**Documentación dice**:
[Quote específico de documento]
Fuente: [archivo:línea]

**Código hace**:
[Comportamiento real del código]
Fuente: [archivo.py:línea]

**Realidad es**:
[Estado real en proyectos]
Fuente: [evidencia]

**Impacto**:
[Qué problemas causa esta inconsistencia]

**Recomendación**:
[Qué debe corregirse: docs, código, o ambos]

---

[Repetir para cada inconsistencia encontrada]

## INCONSISTENCIAS POR CATEGORIA

### Versiones

**Problema**: Versiones inconsistentes entre docs y código

| Documento/Módulo | Versión Mencionada | Debería Ser |
|------------------|-------------------|-------------|
| CLAUDE.md | v2.2 | v2.2 ✓ |
| README.md | v2.0 | v2.2 ✗ |
| project_manager.py | v2.2 | v2.2 ✓ |
| task_manager.py | v1.0 (deprecated) | Marcar claramente |

**Impacto**: Confusión sobre versión actual
**Recomendación**: Actualizar todos a v2.2 consistentemente

### Features Documentadas No Implementadas

1. **Feature X en docs pero no en código**
   - Documentado en: README.md:145
   - No encontrado en: ningún módulo core/
   - Impacto: Promesa no cumplida
   - Recomendación: Implementar o remover de docs

### Features Implementadas No Documentadas

1. **Función Y en código pero no documentada**
   - Implementado en: project_manager.py:247
   - No mencionado en: documentación
   - Impacto: Feature oculta
   - Recomendación: Documentar en README.md

### Estructura Esperada vs Real

**Problema**: Estándar v2.2 ORGANIZED no se cumple completamente

| Aspecto | Documentado | Código Genera | Realidad |
|---------|-------------|---------------|----------|
| reports/ obligatorio | SÍ | SÍ (reorganize_task_structure.py) | 4 tareas sin reports/ |
| README.md obligatorio | SÍ | NO (project_manager no lo crea) | 6 tareas sin README.md |
| task_info.json | SÍ | SÍ (project_manager.create_task) | 4 tareas sin él |

**Impacto**: Proyecto COVID no compliant con estándar
**Recomendación**: Actualizar project_manager.py para crear README.md automáticamente

### Convenciones de Naming

**Problema**: Convención documentada vs implementada vs usada

| Elemento | Documentado | Implementado | Usado en COVID |
|----------|-------------|--------------|----------------|
| Nombres tareas | kebab-case | kebab-case ✓ | kebab-case ✓ |
| Nombres reportes | snake_case | No validado | mezclado ✗ |
| Nombres proyectos | kebab-case | kebab-case ✓ | kebab-case ✓ |

**Impacto**: Inconsistencia en naming de reportes
**Recomendación**: Agregar validación de snake_case para reportes

## ANALISIS DE GAPS

### Gap 1: Validación vs Cumplimiento

**Observación**: framework_validator.py existe pero no previene problemas

- Docs dicen: "Sistema valida estructura antes de ejecutar"
- Código hace: Validación post-facto (después de crear)
- Realidad: 4 tareas creadas sin cumplir estándar

**Root cause**: Validación no es preventiva
**Recomendación**: Integrar validación en project_manager.create_task()

### Gap 2: Documentación vs Implementación

**Observación**: ESTANDAR_v2.2.md define README.md como obligatorio

- Docs dicen: "README.md (REQUERIDO - índice/overview)"
- Código hace: project_manager.py no crea README.md
- Realidad: Muchas tareas sin README.md

**Root cause**: project_manager no implementa todo el estándar
**Recomendación**: Actualizar project_manager para generar README.md

## INCONSISTENCIAS PRIORITARIAS

### Críticas (Bloquean funcionalidad)

1. **Outputs perdidos no detectados**
   - Sistema dice validar pero 4 tareas sin reportes
   - Impacto: Trabajo perdido
   - Corrección: Validación obligatoria de outputs

2. **Estándar v2.2 no se aplica automáticamente**
   - Docs definen estándar pero código no lo aplica
   - Impacto: Proyectos non-compliant
   - Corrección: project_manager debe crear estructura completa

### Altas (Afectan calidad)

1. **Versiones inconsistentes en docs**
2. **Features documentadas no implementadas**
3. **Convenciones no validadas**

### Medias (Mejoras deseables)

1. **Documentación incompleta**
2. **Código sin docstrings**
3. **Ejemplos desactualizados**

## RECOMENDACIONES CROSS-SYSTEM

### Para Documentación

1. Actualizar todas las referencias a v2.2
2. Remover features no implementadas
3. Documentar features implementadas no documentadas
4. Actualizar ejemplos para que coincidan con código

### Para Código

1. Implementar features documentadas faltantes
2. Hacer validación preventiva (no post-facto)
3. project_manager debe crear README.md automático
4. Validar naming conventions en tiempo de creación

### Para Estructura

1. Corregir proyecto COVID para cumplir v2.2
2. Migrar tareas non-compliant
3. Validar que todos los outputs existan

## METRICAS

- Total inconsistencias encontradas: X
- Críticas: X
- Altas: X
- Medias: X
- Bajas: X

- Áreas afectadas:
  - Documentación: X inconsistencias
  - Código: X inconsistencias
  - Estructura: X inconsistencias
  - Cross-system: X inconsistencias

## CONCLUSION

[Resumen del estado de consistencia del framework]
[Principales problemas que deben corregirse]
[Viabilidad de baseline limpio v2.2]
```

## CRITERIOS DE CALIDAD

- Compara explícitamente entre las 3 dimensiones (docs, código, estructura)
- Cita fuentes específicas (archivo:línea)
- Prioriza por impacto real
- Proporciona recomendaciones concretas
- Identifica root causes, no solo síntomas

## HERRAMIENTAS

- Read: leer reportes previos y documentos de referencia
- Grep: buscar términos específicos
- Comparar versiones entre archivos

## FORMATO

Profesional, sin emojis, markdown estándar.

## ENTREGABLE

1. Reporte en reports/matriz_inconsistencias.md
2. Matriz completa de inconsistencias
3. Al menos 20 inconsistencias identificadas
4. Recomendaciones priorizadas
5. Análisis de root causes
