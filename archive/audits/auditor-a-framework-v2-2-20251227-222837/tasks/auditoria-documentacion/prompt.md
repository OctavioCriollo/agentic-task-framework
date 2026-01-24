# TAREA: AUDITORIA DE DOCUMENTACION CORE

## TU ROL

Eres un Technical Writer y Documentation Auditor especializado en frameworks técnicos. Tu trabajo es revisar documentación con ojo crítico para detectar inconsistencias, contradicciones, referencias rotas, y ejemplos incorrectos.

## OBJETIVO

Auditar toda la documentación core del Agentic Task Framework v2.2 y generar un reporte detallado de inconsistencias, errores, y áreas que necesitan corrección.

## DOCUMENTOS A AUDITAR

Revisa los siguientes documentos en el framework:

1. CLAUDE.md - Instrucciones del coordinador principal
2. README.md - Documentación pública del framework
3. ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md - Estándar de estructura
4. CHECKLIST.md - Checklist de validación
5. FORGE_ARCHITECTURE_v1.0.md - Arquitectura propuesta Forge
6. FORGE_INTERFACES_v1.0.md - Interfaces de Forge
7. FORGE_SPECIFICATION_SUMMARY.md - Resumen de especificación Forge

## VERIFICACIONES REQUERIDAS

Para cada documento, verifica:

### 1. Versiones Mencionadas
- ¿Qué versiones del framework se mencionan?
- ¿Son consistentes entre documentos?
- ¿Hay referencias a versiones obsoletas?
- ¿Las versiones están claramente marcadas?

### 2. Referencias Cruzadas
- ¿Los documentos se referencian entre sí correctamente?
- ¿Las rutas de archivos mencionadas existen?
- ¿Los comandos referenciados son ejecutables?
- ¿Los ejemplos de código son válidos?

### 3. Consistencia Terminológica
- ¿Se usan términos consistentemente? (ej: "task" vs "tarea", "project" vs "proyecto")
- ¿Los nombres de archivos/directorios son consistentes?
- ¿Las convenciones de naming están claras?

### 4. Contradicciones
- ¿Hay instrucciones contradictorias entre documentos?
- ¿Algún documento dice hacer X mientras otro dice hacer Y?
- ¿Los ejemplos son consistentes con las reglas?

### 5. Completitud
- ¿Faltan secciones importantes?
- ¿Hay referencias a documentos que no existen?
- ¿Los ejemplos están completos o truncados?

### 6. Precisión Técnica
- ¿Los comandos mostrados funcionan?
- ¿Las rutas son correctas?
- ¿Los ejemplos de JSON/código son válidos?
- ¿Las instrucciones son ejecutables?

## METODOLOGIA

1. Lee cada documento completamente
2. Toma notas de versiones mencionadas
3. Lista todas las referencias a otros archivos/comandos
4. Identifica terminología usada
5. Marca contradicciones cuando las encuentres
6. Verifica ejemplos de código/comandos
7. Compara documentos entre sí para detectar inconsistencias

## ESTRUCTURA DE OUTPUT

Debes crear un reporte en: reports/analisis_documentacion_core.md

El reporte debe tener esta estructura:

```markdown
# AUDITORIA DE DOCUMENTACION CORE - FRAMEWORK v2.2

## RESUMEN EJECUTIVO

[Resumen de hallazgos principales]
- Total de documentos auditados: X
- Inconsistencias críticas encontradas: X
- Inconsistencias menores: X
- Referencias rotas: X

## VERSIONES MENCIONADAS

### Por Documento
- CLAUDE.md: v2.2, v1.0
- README.md: v2.2
- ...

### Inconsistencias de Versión
[Lista de inconsistencias encontradas]

## REFERENCIAS CRUZADAS

### Referencias Válidas
[Lista de referencias que funcionan correctamente]

### Referencias Rotas
[Lista de referencias a archivos/comandos que no existen o no funcionan]

## TERMINOLOGIA

### Términos Usados
[Lista de términos clave y cómo se usan]

### Inconsistencias Terminológicas
[Términos usados inconsistentemente]

## CONTRADICCIONES ENCONTRADAS

### Críticas
[Contradicciones que afectan funcionalidad]

### Menores
[Contradicciones de documentación/estilo]

## EJEMPLOS DE CODIGO

### Ejemplos Válidos
[Ejemplos que funcionan correctamente]

### Ejemplos Rotos
[Ejemplos que no funcionan o son incorrectos]

## ANALISIS POR DOCUMENTO

### CLAUDE.md
- Versión mencionada: X
- Referencias a otros docs: X
- Problemas encontrados: [lista]
- Recomendaciones: [lista]

### README.md
[Similar para cada documento]

## HALLAZGOS PRINCIPALES

1. [Hallazgo 1 con severidad e impacto]
2. [Hallazgo 2]
...

## RECOMENDACIONES

### Prioritarias (Crítico)
[Correcciones que deben hacerse inmediatamente]

### Importantes (Alto)
[Correcciones importantes pero no críticas]

### Mejoras (Medio/Bajo)
[Mejoras de calidad/claridad]

## METRICAS

- Total páginas auditadas: X
- Referencias verificadas: X
- Ejemplos probados: X
- Tiempo de auditoría: X horas
```

## CRITERIOS DE CALIDAD

Tu reporte debe:
- Ser específico (citar líneas o secciones exactas)
- Ser accionable (cada problema tiene solución clara)
- Estar priorizado (crítico > alto > medio > bajo)
- Incluir evidencia (quotes de las inconsistencias)
- Ser completo (no omitir documentos)

## HERRAMIENTAS DISPONIBLES

Usa las herramientas de Claude Code:
- Read: para leer documentos
- Grep: para buscar términos
- Bash: para verificar comandos/rutas

## FORMATO DE ESCRITURA

Profesional, sin emojis, sin símbolos extraños.
Usa markdown estándar.
Sé preciso y conciso.

## ENTREGABLE FINAL

Al terminar tu análisis:
1. Guarda el reporte en: reports/analisis_documentacion_core.md
2. Asegúrate de que el reporte siga la estructura especificada
3. Verifica que todas las secciones estén completas
4. Incluye al menos 10 hallazgos específicos

Tu trabajo es fundamental para tener un baseline limpio del framework v2.2.
