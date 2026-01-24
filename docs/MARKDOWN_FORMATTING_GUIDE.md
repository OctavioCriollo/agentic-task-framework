# Guía de Formato Markdown Profesional
**Framework:** Agentic Task Framework v2.2
**Propósito:** Referencia completa para enriquecer la escritura técnica
**Fecha:** 2026-01-19

---

## Tabla de Contenidos

1. [Formato de Texto Básico](#1-formato-de-texto-básico)
2. [Checkmarks y Validación](#2-checkmarks-y-validación)
3. [Tablas de Comparación](#3-tablas-de-comparación)
4. [Listas y Checklists](#4-listas-y-checklists)
5. [Bloques de Código](#5-bloques-de-código)
6. [Citas y Callouts](#6-citas-y-callouts)
7. [Enlaces y Referencias](#7-enlaces-y-referencias)
8. [Combinaciones Avanzadas](#8-combinaciones-avanzadas)
9. [Best Practices](#9-best-practices)

---

## 1. FORMATO DE TEXTO BÁSICO

### 1.1 Negrilla (Bold)

**Sintaxis:**
```markdown
**texto en negrilla**
__texto en negrilla__
```

**Resultado:**
**texto en negrilla**

**Cuándo usar:**
- Términos clave o definiciones
- Encabezados inline
- Énfasis fuerte en conceptos críticos
- Nombres de archivos, métodos, clases

**Ejemplos:**

```markdown
El método **create_project()** es fundamental.
**IMPORTANTE:** Siempre validar las entradas.
Archivo: **core/project_manager.py**
```

**Renderizado:**

El método **create_project()** es fundamental.
**IMPORTANTE:** Siempre validar las entradas.
Archivo: **core/project_manager.py**

---

### 1.2 Cursiva (Italic)

**Sintaxis:**
```markdown
*texto en cursiva*
_texto en cursiva_
```

**Resultado:**
*texto en cursiva*

**Cuándo usar:**
- Énfasis suave
- Términos extranjeros o técnicos
- Variables o parámetros en texto
- Nombres de publicaciones

**Ejemplos:**

```markdown
El parámetro *project_id* es obligatorio.
Según *PEP 8*, usar snake_case.
Este es un concepto de *machine learning*.
```

**Renderizado:**

El parámetro *project_id* es obligatorio.
Según *PEP 8*, usar snake_case.
Este es un concepto de *machine learning*.

---

### 1.3 Negrilla + Cursiva (Bold + Italic)

**Sintaxis:**
```markdown
***texto en negrilla y cursiva***
___texto en negrilla y cursiva___
**_texto combinado_**
*__texto combinado__*
```

**Resultado:**
***texto en negrilla y cursiva***

**Cuándo usar:**
- Máximo énfasis en advertencias críticas
- Términos extremadamente importantes
- Uso limitado (pierde impacto si se sobreusa)

**Ejemplos:**

```markdown
***CRÍTICO:*** No ejecutar en producción.
***SECURITY WARNING:*** Path traversal detected.
```

**Renderizado:**

***CRÍTICO:*** No ejecutar en producción.
***SECURITY WARNING:*** Path traversal detected.

---

### 1.4 Tachado (Strikethrough)

**Sintaxis:**
```markdown
~~texto tachado~~
```

**Resultado:**
~~texto tachado~~

**Cuándo usar:**
- Marcar contenido obsoleto o deprecado
- Mostrar cambios en documentación
- Indicar features removidas
- Changelog con elementos eliminados

**Ejemplos:**

```markdown
~~task_manager.py~~ → Deprecado en v2.0
Método ~~old_function()~~ reemplazado por **new_function()**
~~Usar pip install requests~~ → Ahora incluido en requirements.txt
```

**Renderizado:**

~~task_manager.py~~ → Deprecado en v2.0
Método ~~old_function()~~ reemplazado por **new_function()**
~~Usar pip install requests~~ → Ahora incluido en requirements.txt

---

### 1.5 Código Inline (Monospace)

**Sintaxis:**
```markdown
`código inline`
```

**Resultado:**
`código inline`

**Cuándo usar:**
- Nombres de variables, funciones, métodos
- Comandos de terminal
- Rutas de archivo
- Valores literales
- Extensiones de archivo

**Ejemplos:**

```markdown
La función `register_task_report()` valida el archivo.
Ejecutar `pip install -r requirements.txt`
Ubicado en `core/project_manager.py:346`
El valor es `None` por defecto.
Archivos `.md` y `.json` son válidos.
```

**Renderizado:**

La función `register_task_report()` valida el archivo.
Ejecutar `pip install -r requirements.txt`
Ubicado en `core/project_manager.py:346`
El valor es `None` por defecto.
Archivos `.md` y `.json` son válidos.

---

## 2. CHECKMARKS Y VALIDACIÓN

### 2.1 Símbolos de Validación

**Símbolos disponibles:**

| Símbolo | Unicode | Markdown | Significado |
|---------|---------|----------|-------------|
| ✓ | U+2713 | `✓` | Check básico |
| ✅ | U+2705 | `✅` | Check con caja verde |
| ✗ | U+2717 | `✗` | X básica |
| ❌ | U+274C | `❌` | X con caja roja |
| ⚠️ | U+26A0 | `⚠️` | Warning (usar con moderación) |
| ○ | U+25CB | `○` | Neutral/vacío |
| ● | U+25CF | `●` | Marcado/activo |

---

### 2.2 Tablas de Validación

**Ejemplo 1: Tabla de Features**

```markdown
| Feature | Implementado | Testeado | Documentado |
|---------|--------------|----------|-------------|
| Path validation | ✅ | ✅ | ✅ |
| Input sanitization | ✅ | ✅ | ✅ |
| Logging system | ❌ | ❌ | ❌ |
| User auth | ○ | ○ | ○ |
```

**Renderizado:**

| Feature | Implementado | Testeado | Documentado |
|---------|--------------|----------|-------------|
| Path validation | ✅ | ✅ | ✅ |
| Input sanitization | ✅ | ✅ | ✅ |
| Logging system | ❌ | ❌ | ❌ |
| User auth | ○ | ○ | ○ |

---

**Ejemplo 2: Tabla de Compatibilidad**

```markdown
| Plataforma | Python 3.8 | Python 3.9 | Python 3.10 | Python 3.11 |
|------------|------------|------------|-------------|-------------|
| Windows | ✅ | ✅ | ✅ | ✅ |
| macOS | ✅ | ✅ | ✅ | ✅ |
| Linux | ✅ | ✅ | ✅ | ✅ |
| BSD | ❌ | ❌ | ○ | ○ |
```

**Renderizado:**

| Plataforma | Python 3.8 | Python 3.9 | Python 3.10 | Python 3.11 |
|------------|------------|------------|-------------|-------------|
| Windows | ✅ | ✅ | ✅ | ✅ |
| macOS | ✅ | ✅ | ✅ | ✅ |
| Linux | ✅ | ✅ | ✅ | ✅ |
| BSD | ❌ | ❌ | ○ | ○ |

---

**Ejemplo 3: Tabla de Validación de Tests**

```markdown
| Test Suite | Status | Coverage | Notes |
|------------|--------|----------|-------|
| Unit Tests | ✅ 49/49 | 60% | All passing |
| Integration Tests | ✅ 12/12 | 45% | Complete |
| E2E Tests | ❌ 0/5 | 0% | Not implemented |
| Security Tests | ✅ 28/28 | 100% | Critical paths |
```

**Renderizado:**

| Test Suite | Status | Coverage | Notes |
|------------|--------|----------|-------|
| Unit Tests | ✅ 49/49 | 60% | All passing |
| Integration Tests | ✅ 12/12 | 45% | Complete |
| E2E Tests | ❌ 0/5 | 0% | Not implemented |
| Security Tests | ✅ 28/28 | 100% | Critical paths |

---

### 2.3 Uso en Listas

**Sintaxis:**

```markdown
- ✅ Item completado
- ❌ Item fallido
- ○ Item pendiente
- ● Item en progreso
```

**Renderizado:**

- ✅ Item completado
- ❌ Item fallido
- ○ Item pendiente
- ● Item en progreso

---

### 2.4 Combinación con Texto

**Sintaxis:**

```markdown
**Status:** ✅ Production Ready
**Security:** ✅ All vulnerabilities fixed
**Documentation:** ○ In progress
**Performance:** ❌ Needs optimization
```

**Renderizado:**

**Status:** ✅ Production Ready
**Security:** ✅ All vulnerabilities fixed
**Documentation:** ○ In progress
**Performance:** ❌ Needs optimization

---

## 3. TABLAS DE COMPARACIÓN

### 3.1 Tabla Básica

**Sintaxis:**

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1 | Dato 2 | Dato 3 |
| Dato 4 | Dato 5 | Dato 6 |
```

**Renderizado:**

| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1 | Dato 2 | Dato 3 |
| Dato 4 | Dato 5 | Dato 6 |

---

### 3.2 Tabla con Alineación

**Sintaxis:**

```markdown
| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| Texto | Texto | 100 |
| Más texto | Más | 200 |
```

**Alineación:**
- `:---` = Alineado a la izquierda
- `:---:` = Centrado
- `---:` = Alineado a la derecha

**Renderizado:**

| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| Texto | Texto | 100 |
| Más texto | Más | 200 |

---

### 3.3 Tabla con Formato Mixto

**Sintaxis:**

```markdown
| Feature | Status | Priority | Owner |
|:--------|:------:|:--------:|------:|
| **Path Validation** | ✅ | ⭐⭐⭐ | @security |
| *Input Sanitization* | ✅ | ⭐⭐ | @core |
| ~~Old System~~ | ❌ | ⭐ | *deprecated* |
| `new_feature()` | ○ | ⭐⭐⭐ | @dev |
```

**Renderizado:**

| Feature | Status | Priority | Owner |
|:--------|:------:|:--------:|------:|
| **Path Validation** | ✅ | ⭐⭐⭐ | @security |
| *Input Sanitization* | ✅ | ⭐⭐ | @core |
| ~~Old System~~ | ❌ | ⭐ | *deprecated* |
| `new_feature()` | ○ | ⭐⭐⭐ | @dev |

---

### 3.4 Tabla Antes/Después

**Sintaxis:**

```markdown
| Aspecto | ❌ Antes | ✅ Después | Mejora |
|---------|----------|------------|--------|
| Security Score | 60/100 | 100/100 | +40 |
| Test Coverage | 40% | 60% | +20% |
| Code Quality | 70/100 | 92/100 | +22 |
| Documentation | Partial | Complete | ✓ |
```

**Renderizado:**

| Aspecto | ❌ Antes | ✅ Después | Mejora |
|---------|----------|------------|--------|
| Security Score | 60/100 | 100/100 | +40 |
| Test Coverage | 40% | 60% | +20% |
| Code Quality | 70/100 | 92/100 | +22 |
| Documentation | Partial | Complete | ✓ |

---

## 4. LISTAS Y CHECKLISTS

### 4.1 Listas No Ordenadas

**Sintaxis:**

```markdown
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
- Item 3
```

**Renderizado:**

- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
- Item 3

---

### 4.2 Listas Ordenadas

**Sintaxis:**

```markdown
1. Primer paso
2. Segundo paso
   1. Sub-paso 2.1
   2. Sub-paso 2.2
3. Tercer paso
```

**Renderizado:**

1. Primer paso
2. Segundo paso
   1. Sub-paso 2.1
   2. Sub-paso 2.2
3. Tercer paso

---

### 4.3 Checklists Interactivas (GitHub-flavored)

**Sintaxis:**

```markdown
- [ ] Tarea pendiente
- [x] Tarea completada
- [ ] Otra tarea pendiente
  - [x] Sub-tarea completada
  - [ ] Sub-tarea pendiente
```

**Renderizado:**

- [ ] Tarea pendiente
- [x] Tarea completada
- [ ] Otra tarea pendiente
  - [x] Sub-tarea completada
  - [ ] Sub-tarea pendiente

---

### 4.4 Listas con Símbolos Personalizados

**Sintaxis:**

```markdown
- ✅ Feature completada: Path validation
- ○ Feature en progreso: User authentication
- ❌ Feature bloqueada: Advanced analytics
- ● Feature crítica: Security hardening
```

**Renderizado:**

- ✅ Feature completada: Path validation
- ○ Feature en progreso: User authentication
- ❌ Feature bloqueada: Advanced analytics
- ● Feature crítica: Security hardening

---

### 4.5 Lista de Tareas con Prioridad

**Sintaxis:**

```markdown
1. ⭐⭐⭐ **HIGH:** Fix security vulnerability
   - [x] Identify the issue
   - [x] Write tests
   - [x] Implement fix
   - [x] Verify solution

2. ⭐⭐ **MEDIUM:** Improve documentation
   - [x] Update README
   - [ ] Add examples
   - [ ] Create video tutorial

3. ⭐ **LOW:** Refactor old code
   - [ ] Identify candidates
   - [ ] Plan refactoring
   - [ ] Execute changes
```

**Renderizado:**

1. ⭐⭐⭐ **HIGH:** Fix security vulnerability
   - [x] Identify the issue
   - [x] Write tests
   - [x] Implement fix
   - [x] Verify solution

2. ⭐⭐ **MEDIUM:** Improve documentation
   - [x] Update README
   - [ ] Add examples
   - [ ] Create video tutorial

3. ⭐ **LOW:** Refactor old code
   - [ ] Identify candidates
   - [ ] Plan refactoring
   - [ ] Execute changes

---

## 5. BLOQUES DE CÓDIGO

### 5.1 Código Inline

**Sintaxis:**
```markdown
Use la función `create_project()` para inicializar.
```

**Renderizado:**
Use la función `create_project()` para inicializar.

---

### 5.2 Bloques de Código con Sintaxis

**Sintaxis:**

````markdown
```python
def create_project(name: str, user_request: str):
    """Create a new project."""
    return {"name": name, "request": user_request}
```
````

**Renderizado:**

```python
def create_project(name: str, user_request: str):
    """Create a new project."""
    return {"name": name, "request": user_request}
```

---

### 5.3 Código con Números de Línea (comentados)

**Sintaxis:**

```markdown
```python
# Line 1: Import statement
from pathlib import Path

# Line 3: Function definition
def validate_path(filepath: str) -> bool:
    # Line 5: Validation logic
    return Path(filepath).exists()
```
```

**Renderizado:**

```python
# Line 1: Import statement
from pathlib import Path

# Line 3: Function definition
def validate_path(filepath: str) -> bool:
    # Line 5: Validation logic
    return Path(filepath).exists()
```

---

### 5.4 Comparación Código Antes/Después

**Sintaxis:**

````markdown
**❌ ANTES (Incorrecto):**
```python
except:
    pass
```

**✅ DESPUÉS (Correcto):**
```python
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f"Error: {e}")
```
````

**Renderizado:**

**❌ ANTES (Incorrecto):**
```python
except:
    pass
```

**✅ DESPUÉS (Correcto):**
```python
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f"Error: {e}")
```

---

### 5.5 Bloques de Código con Highlight

**Sintaxis:**

````markdown
```bash
# Comandos con output
$ pytest tests/ -v
===== 49 passed in 2.5s =====  # ✅ All tests passed
```
````

**Renderizado:**

```bash
# Comandos con output
$ pytest tests/ -v
===== 49 passed in 2.5s =====  # ✅ All tests passed
```

---

## 6. CITAS Y CALLOUTS

### 6.1 Citas Simples

**Sintaxis:**

```markdown
> Esto es una cita.
> Puede tener múltiples líneas.
```

**Renderizado:**

> Esto es una cita.
> Puede tener múltiples líneas.

---

### 6.2 Citas Anidadas

**Sintaxis:**

```markdown
> Nivel 1
>> Nivel 2
>>> Nivel 3
```

**Renderizado:**

> Nivel 1
>> Nivel 2
>>> Nivel 3

---

### 6.3 Callouts (Notas Especiales)

**Sintaxis:**

```markdown
> **✅ SUCCESS:**
> All security fixes have been implemented successfully.

> **❌ ERROR:**
> Path traversal vulnerability detected in line 346.

> **○ NOTE:**
> This feature is optional and can be skipped.

> **● IMPORTANT:**
> Always validate user input before processing.
```

**Renderizado:**

> **✅ SUCCESS:**
> All security fixes have been implemented successfully.

> **❌ ERROR:**
> Path traversal vulnerability detected in line 346.

> **○ NOTE:**
> This feature is optional and can be skipped.

> **● IMPORTANT:**
> Always validate user input before processing.

---

### 6.4 Callouts con Código

**Sintaxis:**

```markdown
> **EXAMPLE:**
> ```python
> validator.validate_input(user_data)
> ```
> This ensures safe processing of user input.
```

**Renderizado:**

> **EXAMPLE:**
> ```python
> validator.validate_input(user_data)
> ```
> This ensures safe processing of user input.

---

## 7. ENLACES Y REFERENCIAS

### 7.1 Enlaces Básicos

**Sintaxis:**

```markdown
[Texto del enlace](https://example.com)
[GitHub](https://github.com)
```

**Renderizado:**

[Texto del enlace](https://example.com)
[GitHub](https://github.com)

---

### 7.2 Enlaces con Título

**Sintaxis:**

```markdown
[GitHub](https://github.com "Visit GitHub")
```

**Renderizado:**

[GitHub](https://github.com "Visit GitHub")

---

### 7.3 Enlaces a Archivos Locales

**Sintaxis:**

```markdown
Ver [Project Manager](../core/project_manager.py)
Leer [Documentación](./ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md)
```

**Renderizado:**

Ver [Project Manager](../core/project_manager.py)
Leer [Documentación](./ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md)

---

### 7.4 Enlaces a Secciones (Anchors)

**Sintaxis:**

```markdown
Ver [Formato de Texto](#1-formato-de-texto-básico)
Ir a [Tablas](#3-tablas-de-comparación)
```

**Renderizado:**

Ver [Formato de Texto](#1-formato-de-texto-básico)
Ir a [Tablas](#3-tablas-de-comparación)

---

### 7.5 Referencias de Código

**Sintaxis:**

```markdown
Ver método `create_project()` en [project_manager.py:89](core/project_manager.py#L89)
Error en [start_coordinator.sh:202](start_coordinator.sh#L202)
```

**Renderizado:**

Ver método `create_project()` en [project_manager.py:89](core/project_manager.py#L89)
Error en [start_coordinator.sh:202](start_coordinator.sh#L202)

---

## 8. COMBINACIONES AVANZADAS

### 8.1 Tabla con Código y Checkmarks

**Sintaxis:**

```markdown
| Método | Sintaxis | Validación | Tests |
|--------|----------|------------|-------|
| `create_project()` | `pm.create_project(name, request)` | ✅ | ✅ |
| `create_task()` | `pm.create_task(proj_id, name, desc)` | ✅ | ✅ |
| ~~`old_method()`~~ | *deprecated* | ❌ | ❌ |
```

**Renderizado:**

| Método | Sintaxis | Validación | Tests |
|--------|----------|------------|-------|
| `create_project()` | `pm.create_project(name, request)` | ✅ | ✅ |
| `create_task()` | `pm.create_task(proj_id, name, desc)` | ✅ | ✅ |
| ~~`old_method()`~~ | *deprecated* | ❌ | ❌ |

---

### 8.2 Lista con Código, Links y Checkmarks

**Sintaxis:**

```markdown
1. ✅ **Path Validation** implementada
   - Archivo: [`project_manager.py:610-646`](core/project_manager.py#L610-L646)
   - Método: `_validate_report_filename()`
   - Tests: 11/11 passing

2. ○ **User Authentication** en progreso
   - Archivo: `auth_manager.py` (pendiente)
   - Método: `authenticate_user()` (diseño)
   - Tests: 0/5 pending

3. ❌ **Advanced Analytics** bloqueada
   - Razón: Requiere `pandas>=2.0`
   - Bloqueante: Dependencia no aprobada
   - Issue: [#123](https://github.com/example/issues/123)
```

**Renderizado:**

1. ✅ **Path Validation** implementada
   - Archivo: [`project_manager.py:610-646`](core/project_manager.py#L610-L646)
   - Método: `_validate_report_filename()`
   - Tests: 11/11 passing

2. ○ **User Authentication** en progreso
   - Archivo: `auth_manager.py` (pendiente)
   - Método: `authenticate_user()` (diseño)
   - Tests: 0/5 pending

3. ❌ **Advanced Analytics** bloqueada
   - Razón: Requiere `pandas>=2.0`
   - Bloqueante: Dependencia no aprobada
   - Issue: [#123](https://github.com/example/issues/123)

---

### 8.3 Callout con Tabla

**Sintaxis:**

```markdown
> **✅ VERIFICATION RESULTS:**
>
> | Check | Result | Details |
> |-------|--------|---------|
> | Syntax | ✅ | No errors |
> | Tests | ✅ | 49/49 passing |
> | Security | ✅ | No vulnerabilities |
> | Coverage | ○ | 60% (target: 80%) |
```

**Renderizado:**

> **✅ VERIFICATION RESULTS:**
>
> | Check | Result | Details |
> |-------|--------|---------|
> | Syntax | ✅ | No errors |
> | Tests | ✅ | 49/49 passing |
> | Security | ✅ | No vulnerabilities |
> | Coverage | ○ | 60% (target: 80%) |

---

### 8.4 Tabla Comparativa Completa

**Sintaxis:**

```markdown
| Feature | v1.0 | v2.0 | v2.2 | Status |
|---------|:----:|:----:|:----:|:------:|
| Multi-window | ✅ | ~~✅~~ | ❌ | *deprecated* |
| Task tool | ❌ | ✅ | ✅ | **active** |
| Reports subdir | ❌ | ❌ | ✅ | **new** |
| `README.md` auto | ❌ | ○ | ✅ | **enhanced** |
```

**Renderizado:**

| Feature | v1.0 | v2.0 | v2.2 | Status |
|---------|:----:|:----:|:----:|:------:|
| Multi-window | ✅ | ~~✅~~ | ❌ | *deprecated* |
| Task tool | ❌ | ✅ | ✅ | **active** |
| Reports subdir | ❌ | ❌ | ✅ | **new** |
| `README.md` auto | ❌ | ○ | ✅ | **enhanced** |

---

## 9. BEST PRACTICES

### 9.1 Jerarquía Visual

**✅ BUENO:**

```markdown
## Sección Principal

### Subsección

Texto explicativo con **términos clave** en negrilla.

- ✅ Item importante
- ○ Item secundario
```

**❌ MALO:**

```markdown
## ***SECCIÓN PRINCIPAL***

***Subsección***

***Texto*** con ***demasiado*** ***énfasis***.

- ***✅ Item importante***
- ***○ Item secundario***
```

---

### 9.2 Uso de Checkmarks

**✅ BUENO - Uso Consistente:**

```markdown
| Task | Status |
|------|--------|
| Implementation | ✅ |
| Testing | ✅ |
| Documentation | ○ |
```

**❌ MALO - Uso Mixto:**

```markdown
| Task | Status |
|------|--------|
| Implementation | DONE |
| Testing | ✅ |
| Documentation | In progress |
```

---

### 9.3 Formato de Código

**✅ BUENO - Código con Contexto:**

```markdown
El método `validate_input()` realiza las siguientes validaciones:

```python
def validate_input(data: str) -> bool:
    """Validate user input."""
    if not data or len(data) > 200:
        return False
    return True
```

Retorna `True` si la validación pasa.
```

**❌ MALO - Código sin Contexto:**

```markdown
```python
def validate_input(data: str) -> bool:
    if not data or len(data) > 200:
        return False
    return True
```
```

---

### 9.4 Tablas Legibles

**✅ BUENO - Columnas Alineadas:**

```markdown
| Short | Medium Length | Very Long Header Name |
|-------|---------------|----------------------|
| A | B | C |
```

**❌ MALO - Columnas Desbalanceadas:**

```markdown
| A | This is an extremely long cell with too much content that makes the table hard to read | C |
|---|---|---|
```

**SOLUCIÓN - Dividir contenido:**

```markdown
| Header | Description | Link |
|--------|-------------|------|
| A | Very long description | [Details](link) |
```

---

### 9.5 Combinaciones Efectivas

**✅ BUENO - Jerarquía Clara:**

```markdown
### ✅ Feature Completada: Path Validation

**Implementación:**
- Archivo: `core/project_manager.py:610-646`
- Método: `_validate_report_filename()`

**Validaciones:**
1. ✅ Path traversal (`../`)
2. ✅ Absolute paths (`/`, `\`)
3. ✅ Invalid extensions

**Tests:**
| Type | Count | Status |
|------|-------|--------|
| Unit | 11 | ✅ All passing |
```

---

### 9.6 Evitar Sobreformato

**❌ MALO - Demasiado Formato:**

```markdown
## ***✅ FEATURE COMPLETADA: PATH VALIDATION***

***IMPLEMENTACIÓN:***
- ***Archivo:*** ***`core/project_manager.py:610-646`***
- ***Método:*** ***`_validate_report_filename()`***
```

**✅ BUENO - Formato Balanceado:**

```markdown
## Feature Completada: Path Validation

**Implementación:**
- Archivo: `core/project_manager.py:610-646`
- Método: `_validate_report_filename()`
```

---

## 10. GUÍA RÁPIDA DE REFERENCIA

### Formato de Texto

| Sintaxis | Resultado | Uso |
|----------|-----------|-----|
| `**texto**` | **texto** | Énfasis fuerte |
| `*texto*` | *texto* | Énfasis suave |
| `***texto***` | ***texto*** | Énfasis máximo |
| `~~texto~~` | ~~texto~~ | Deprecado |
| `` `texto` `` | `texto` | Código inline |

### Símbolos de Estado

| Símbolo | Uso |
|---------|-----|
| ✅ | Completado/Válido |
| ❌ | Error/Inválido |
| ○ | Pendiente/Neutral |
| ● | En progreso/Activo |
| ✓ | Check simple |
| ✗ | X simple |

### Estructura

| Elemento | Sintaxis |
|----------|----------|
| Encabezado 1 | `# Título` |
| Encabezado 2 | `## Título` |
| Encabezado 3 | `### Título` |
| Lista | `- Item` |
| Lista numerada | `1. Item` |
| Checklist | `- [ ] Item` |
| Tabla | `\| Col1 \| Col2 \|` |
| Cita | `> Texto` |
| Código | ` ```python ` |
| Enlace | `[texto](url)` |

---

## CONCLUSIÓN

El formato Markdown efectivo combina:

1. **Jerarquía clara** - Headers bien estructurados
2. **Énfasis apropiado** - Negrilla/cursiva con propósito
3. **Símbolos consistentes** - Checkmarks y círculos usados uniformemente
4. **Código legible** - Bloques con sintaxis highlighting
5. **Tablas bien formadas** - Alineación y contenido balanceado

**Regla de oro:** Menos es más. Usa formato para mejorar claridad, no para decorar.

---

**Última actualización:** 2026-01-19
**Autor:** Agentic Task Framework Team
**Versión:** 1.0
