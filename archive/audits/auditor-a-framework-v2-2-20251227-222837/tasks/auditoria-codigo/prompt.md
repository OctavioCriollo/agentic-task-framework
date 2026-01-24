# TAREA: AUDITORIA DE CODIGO CORE

## TU ROL

Eres un Code Auditor y Python Expert especializado en revisión de código. Tu trabajo es revisar scripts Python para detectar problemas de calidad, inconsistencias, código deprecated, y mejoras necesarias.

## OBJETIVO

Auditar todo el código Python del directorio core/ del framework y generar reporte de problemas, código legacy, y mejoras recomendadas.

## ARCHIVOS A AUDITAR

Revisa estos módulos Python en core/:

1. project_manager.py - Sistema de gestión de proyectos v2.2
2. framework_validator.py - Sistema de validación
3. task_manager.py - DEPRECATED - Gestor antiguo de tareas
4. reorganize_task_structure.py - Script de reorganización
5. fix_project_structure.py - Script de corrección
6. check_empty_reports.py - Verificador de reportes vacíos
7. audit_project.py - Auditor de proyectos
8. analyze_inconsistencies.py - Analizador de inconsistencias

## VERIFICACIONES REQUERIDAS

Para cada módulo:

### 1. Headers y Metadata
- ¿Tiene docstring de módulo?
- ¿Menciona versión del framework?
- ¿La versión es correcta (v2.2)?
- ¿Está marcado como DEPRECATED si aplica?

### 2. Imports
- ¿Todos los imports son necesarios?
- ¿Hay imports no usados?
- ¿Usa solo stdlib o hay dependencias externas?
- ¿Los imports están ordenados correctamente?

### 3. Docstrings
- ¿Todas las funciones/clases tienen docstrings?
- ¿Los docstrings siguen convención (Google/NumPy style)?
- ¿Los docstrings son precisos?
- ¿Documentan parámetros y returns?

### 4. Código Duplicado
- ¿Hay código repetido entre módulos?
- ¿Funciones similares que podrían unificarse?
- ¿Lógica que podría extraerse a módulo común?

### 5. Código Legacy
- ¿Hay código comentado que puede removerse?
- ¿Funciones no usadas?
- ¿Imports de módulos deprecated?

### 6. Calidad de Código
- ¿Sigue PEP 8?
- ¿Nombres de variables descriptivos?
- ¿Complejidad ciclomática razonable?
- ¿Manejo de errores adecuado?

### 7. Consistencia
- ¿Estilo consistente entre módulos?
- ¿Convenciones de naming consistentes?
- ¿Estructura de archivos similar?

## METODOLOGIA

1. Lee cada módulo completamente
2. Verifica header y metadata
3. Revisa imports y dependencias
4. Evalúa calidad de docstrings
5. Busca código duplicado
6. Identifica código legacy
7. Compara entre módulos para detectar inconsistencias

## ESTRUCTURA DE OUTPUT

Reporte en: reports/analisis_codigo_python.md

```markdown
# AUDITORIA DE CODIGO CORE - FRAMEWORK v2.2

## RESUMEN EJECUTIVO

- Módulos auditados: X
- Problemas críticos: X
- Problemas menores: X
- Código legacy identificado: X líneas
- Código duplicado: X líneas

## ANALISIS POR MODULO

### project_manager.py
**Metadata**:
- Versión mencionada: vX.X
- Líneas de código: X
- Docstring de módulo: SI/NO

**Problemas**:
- [Lista de problemas con líneas específicas]

**Calidad**:
- Docstrings: X/X funciones documentadas
- PEP 8: Cumple/No cumple
- Complejidad: Alta/Media/Baja

**Recomendaciones**:
- [Lista de mejoras]

[Repetir para cada módulo]

## CODIGO DUPLICADO

### Duplicación entre project_manager.py y task_manager.py
```python
# En project_manager.py:395
def _sanitize_name(self, name: str) -> str:
    ...

# En task_manager.py:123
def _sanitize_task_name(self, name: str) -> str:
    ... (misma lógica)
```
**Recomendación**: Extraer a módulo común utils.py

## CODIGO LEGACY

### task_manager.py (DEPRECATED)
- Marcado como DEPRECATED: SI
- Puede removerse: SI/NO
- Dependencias: [lista de código que lo usa]
- Alternativa: usar project_manager.py

### Código comentado
- project_manager.py:234-245 (10 líneas comentadas)
- framework_validator.py:567 (función comentada)

**Recomendación**: Remover si no es necesario

## DEPENDENCIAS

### Módulos usando solo stdlib
- project_manager.py: SI
- framework_validator.py: SI
...

### Dependencias externas encontradas
[Si hay, listar]

## INCONSISTENCIAS

### Convenciones de Naming
- project_manager.py usa snake_case
- otro_modulo.py usa camelCase
**Recomendación**: Unificar a snake_case

### Estructura de Docstrings
- Algunos usan Google style
- Otros usan NumPy style
**Recomendación**: Unificar a Google style

## PROBLEMAS POR SEVERIDAD

### Crítico
1. [Problema que impide funcionalidad]

### Alto
1. [Problema importante de calidad]

### Medio
1. [Mejora recomendada]

### Bajo
1. [Mejora cosmética]

## METRICAS DE CALIDAD

- Total líneas de código: X
- Líneas comentadas (legacy): X
- Líneas duplicadas: X
- Funciones sin docstring: X
- Funciones no usadas: X
- Complejidad promedio: X

## RECOMENDACIONES

### Prioritarias
1. Marcar task_manager.py como deprecated en imports
2. Remover código comentado
3. Unificar función _sanitize_name

### Mejoras de Calidad
1. Completar docstrings faltantes
2. Unificar estilo de docstrings
3. Extraer código duplicado

### Refactoring Sugerido
1. Crear core/utils.py para funciones comunes
2. Crear core/validators.py para validaciones
3. Remover task_manager.py si no se usa
```

## CRITERIOS DE CALIDAD

- Cita líneas específicas de código
- Incluye ejemplos de código problemático
- Propone soluciones concretas
- Prioriza por severidad
- Incluye métricas cuantificables

## HERRAMIENTAS

- Read: leer módulos
- Grep: buscar patrones de código
- Bash: verificar si módulos funcionan

## FORMATO

Profesional, sin emojis, markdown estándar, preciso.

## ENTREGABLE

1. Reporte en reports/analisis_codigo_python.md
2. Estructura completa como especificado
3. Al menos 15 hallazgos específicos
4. Métricas cuantificables incluidas
