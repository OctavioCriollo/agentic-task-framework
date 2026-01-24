# Estándares para Tablas Profesionales en Markdown

**Versión:** 1.0
**Fecha:** 2026-01-20
**Framework:** Agentic Task Framework v2.2

---

## 1. Anatomía de Tabla Profesional

### Componentes Esenciales

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Celda 1  | Celda 2  | Celda 3  |
| Celda 4  | Celda 5  | Celda 6  |
```

**Elementos:**
1. **Headers (fila superior):** Descripción concisa de columnas
2. **Separador (segunda fila):** Pipes y guiones, define alineación
3. **Contenido:** Filas de datos

**Reglas básicas:**
- Mínimo 2 columnas (1 columna = usar lista)
- Máximo recomendado: 5 columnas (6+ requiere justificación)
- Headers siempre en primera fila
- Una fila de separador obligatoria

---

## 2. Reglas de Headers

### 2.1. Contenido de Headers

**HACER:**
- ✅ Nombres concisos y descriptivos
- ✅ Capitalización consistente (Title Case o Sentence case)
- ✅ Sin símbolos decorativos

**NO HACER:**
- ❌ Símbolos en headers (salvo excepciones)
- ❌ Headers vacíos
- ❌ Abreviaciones oscuras

### Ejemplos

**✅ CORRECTO:**
```markdown
| Feature | Status | Priority |
|---------|--------|----------|
| Auth    | Done   | High     |
```

**❌ INCORRECTO:**
```markdown
| ✅ Feature | 🚀 Status | ⚡ Priority |  ← Símbolos decorativos en headers
|-----------|-----------|-------------|
| Auth      | Done      | High        |
```

**✓ ACEPTABLE (contexto interno):**
```markdown
| Feature | Status | Priority |
|---------|--------|----------|
| Auth    | ✅ Done | ⚡ High  |  ← Símbolos en CONTENIDO, no headers
```

---

### 2.2. Excepciones: Headers con Símbolos

**PERMITIDO solo en:**
- Tablas de estado con símbolos funcionales bien establecidos
- Documentos internos donde el símbolo es parte del sistema

**FORMATO:**
```markdown
| Feature | ✅ Completed | 🟡 In Progress | ❌ Failed |
|---------|-------------|----------------|----------|
| Auth    | 3           | 1              | 0        |
| API     | 5           | 2              | 1        |
```

**JUSTIFICACIÓN:** El símbolo es parte del nombre de la categoría, no decoración.

**MEJOR ALTERNATIVA:**
```markdown
| Feature | Completed (✅) | In Progress (🟡) | Failed (❌) |
|---------|---------------|-----------------|-------------|
| Auth    | 3             | 1               | 0           |
```

---

## 3. Reglas de Alineación

### 3.1. Sintaxis de Alineación

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| Izq  | Centro | Der   |
```

**Caracteres especiales:**
- `:---` = Izquierda (default)
- `:--:` = Centro
- `---:` = Derecha

---

### 3.2. Alineación por Tipo de Contenido

| Tipo de Contenido | Alineación | Razón |
|-------------------|------------|-------|
| **Texto** | Izquierda | Legibilidad, estándar occidental |
| **Números** | Derecha | Facilita comparación de magnitudes |
| **Símbolos** | Centro | Balance visual |
| **Código** | Izquierda | Legibilidad de sintaxis |
| **Booleanos** (Yes/No) | Centro | Simetría visual |
| **Fechas** | Centro o Izquierda | Depende del formato |
| **URLs/Links** | Izquierda | Previene truncamiento |

---

### 3.3. Ejemplos por Tipo

**Tabla de Configuración:**
```markdown
| Parameter | Type | Default | Required |
|:----------|:----:|--------:|---------:|
| api_key   | str  | None    | Yes      |
| timeout   | int  | 30      | No       |
| retries   | int  | 3       | No       |
```

**Tabla de Estado:**
```markdown
| Agent | Status | Tasks Completed | Uptime |
|:------|:------:|----------------:|-------:|
| agent-1 | 🟢 Active | 156 | 99.9% |
| agent-2 | 🟡 Busy | 89 | 98.2% |
| agent-3 | 🔴 Error | 45 | 67.3% |
```

**Tabla Comparativa:**
```markdown
| Feature | Django | FastAPI | Flask |
|:--------|:------:|:-------:|:-----:|
| ORM Built-in | ✅ | ❌ | ❌ |
| Async Support | ✓ | ✅ | ✓ |
| Performance | Medium | High | High |
```

---

## 4. Uso de Símbolos en Tablas

### 4.1. Regla General

**Símbolos deben estar en el CONTENIDO, NO en headers** (salvo excepciones documentadas).

### 4.2. Símbolos Permitidos (Whitelist)

**Estado/Completitud:**
- ✅ ❌ ✓ ✗ (checkmarks y X-marks)
- 🟢 🟡 🔴 🟠 (círculos de estado)

**Selección:**
- ⚪ ⚫ 🔘 (radio buttons)

**Prioridad:**
- ⚡ ★ ☆ (prioridad/rating)

**Advertencia:**
- ⚠️ (warning sign)

**Direccionales:**
- → ← ↑ ↓ (flechas)

---

### 4.3. Consistencia de Símbolos en Tablas

**REGLA ABSOLUTA:** Dentro de una misma columna, usar UN SOLO símbolo por estado.

**❌ INCORRECTO (inconsistente):**
```markdown
| Feature | Status |
|---------|--------|
| Auth    | ✅ Done |
| API     | ✓ Done |   ← Símbolo diferente
| Cache   | DONE   |   ← Cambio a texto
```

**✅ CORRECTO (consistente):**
```markdown
| Feature | Status |
|---------|--------|
| Auth    | ✅ Done |
| API     | ✅ Done |
| Cache   | ✅ Done |
```

---

### 4.4. Un Símbolo vs Múltiples por Celda

**UN SÍMBOLO (preferido):**
```markdown
| Feature | Status | Priority |
|---------|--------|----------|
| Auth    | ✅     | ⚡       |
| API     | 🟡     | ★★       |
```

**MÚLTIPLES SÍMBOLOS (aceptable si funcional):**
```markdown
| Feature | Platforms Supported |
|---------|---------------------|
| Auth    | 🐧 🪟 🍎           |
| API     | 🐧 🪟              |
```

**PROHIBIDO (decorativo):**
```markdown
| Feature | Status |
|---------|--------|
| Auth    | ✅ 🎉 🚀 |  ← Decoración excesiva
```

---

## 5. Formato Mixto: Combinaciones Permitidas

### 5.1. Símbolo + Texto

**✅ RECOMENDADO (máxima claridad):**
```markdown
| Task | Status |
|------|--------|
| Setup | ✅ COMPLETED |
| Tests | 🟡 IN_PROGRESS |
| Deploy | ⚪ PENDING |
```

**VENTAJA:** Redundancia asegura comprensión incluso si símbolos no renderizan.

---

### 5.2. Código + Símbolo

**✓ ACEPTABLE:**
```markdown
| Function | Status | Return Type |
|----------|--------|-------------|
| `auth_user()` | ✅ | `User \| None` |
| `get_token()` | 🟡 | `str` |
```

---

### 5.3. Negrilla + Código + Símbolo

**⚠️ USAR CON CAUTELA (puede ser excesivo):**
```markdown
| Feature | **Priority** | Code | Status |
|---------|-------------|------|--------|
| Auth    | ⚡ **HIGH** | `auth.py` | ✅ |
| Cache   | ★★ **MED** | `cache.py` | 🟡 |
```

**PREGUNTA CLAVE:** ¿El formato mixto mejora la claridad o solo añade ruido?

**GUÍA:** Si la tabla tiene >4 elementos de formato por celda, simplificar.

---

### 5.4. Links en Celdas

**✅ PERMITIDO:**
```markdown
| Document | Status | Link |
|----------|--------|------|
| API Spec | ✅ Done | [View](./api-spec.md) |
| Guide    | 🟡 Draft | [Edit](./guide.md) |
```

**NOTA:** Links pueden hacer celdas más anchas. Considerar usar URLs relativas cortas.

---

## 6. Límites de Complejidad

### 6.1. Número de Columnas

| Columnas | Clasificación | Recomendación |
|----------|---------------|---------------|
| 2-3      | ✅ ÓPTIMO     | Ideal para legibilidad |
| 4-5      | ✓ ACEPTABLE   | Aún legible |
| 6-7      | ⚠️ LÍMITE     | Considerar dividir |
| 8+       | ❌ EXCESIVO   | Dividir en múltiples tablas |

**EXCEPCIÓN:** Tablas técnicas (como comparación de APIs) pueden justificar 8+ columnas.

---

### 6.2. Texto por Celda

**LÍMITE RECOMENDADO:** 50-80 caracteres por celda.

**SI EXCEDE:**
- Usar abreviaciones (con glosario)
- Dividir en sub-filas
- Mover detalle a lista debajo de tabla

**❌ MAL:**
```markdown
| Feature | Description |
|---------|-------------|
| Auth | This feature provides comprehensive authentication including OAuth2, JWT, session-based, and multi-factor authentication with support for external providers like Google, GitHub, and Microsoft. |
```

**✅ MEJOR:**
```markdown
| Feature | Description | Details |
|---------|-------------|---------|
| Auth | Comprehensive authentication | OAuth2, JWT, MFA, External providers |

**Supported Providers:**
- Google OAuth2
- GitHub OAuth
- Microsoft Azure AD
```

---

### 6.3. Número de Filas

| Filas | Recomendación |
|-------|---------------|
| <10   | ✅ ÓPTIMO - Escaneo rápido |
| 10-20 | ✓ ACEPTABLE - Aún manejable |
| 20-50 | ⚠️ LARGO - Considerar paginación o agrupación |
| 50+   | ❌ EXCESIVO - Dividir por categorías o usar base de datos |

**SOLUCIÓN para tablas largas:**
- Agrupar por secciones con sub-headers
- Crear múltiples tablas temáticas
- Usar herramienta externa (Google Sheets + link)

---

### 6.4. Cuándo Dividir una Tabla

**INDICADORES de tabla demasiado compleja:**
- ⚠️ Requiere scroll horizontal en pantallas 1920px
- ⚠️ Celdas con >100 caracteres
- ⚠️ Lector tiene que mover cabeza para ver headers
- ⚠️ Más de 3 niveles de información en una celda

**SOLUCIÓN: Dividir por:**
1. **Temática** - Separar features core vs advanced
2. **Estado** - Tabla de completed vs in-progress
3. **Prioridad** - High-priority en tabla 1, low en tabla 2
4. **Cronología** - Tabla por fase/sprint

---

## 7. Ejemplos por Tipo de Tabla

### 7.1. Tabla de Estado (Status Table)

**USO:** Tracking de features, tasks, agents

```markdown
| Component | Status | Last Updated | Owner |
|:----------|:------:|-------------:|-------|
| API Gateway | 🟢 Active | 2026-01-20 | @backend |
| Database | 🟢 Active | 2026-01-20 | @backend |
| Cache | 🟡 Degraded | 2026-01-20 | @ops |
| Frontend | 🔴 Down | 2026-01-20 | @frontend |
```

**CARACTERÍSTICAS:**
- Status column con símbolos consistentes (sistema 4 círculos)
- Fechas alineadas a la derecha
- Owner como texto simple

---

### 7.2. Tabla Comparativa (Comparison Table)

**USO:** Decisiones entre alternativas, benchmarking

```markdown
| Feature | Django | FastAPI | Flask |
|:--------|:------:|:-------:|:-----:|
| **Performance** | Medium | High | High |
| **ORM Built-in** | ✅ | ❌ | ❌ |
| **Async Support** | ✓ | ✅ | ✓ |
| **Learning Curve** | Steep | Moderate | Easy |
| **Community** | ★★★ | ★★ | ★★★ |
```

**CARACTERÍSTICAS:**
- Primera columna con features (negrilla opcional)
- Columnas de alternativas centradas
- Símbolos y ratings para comparación rápida

---

### 7.3. Tabla de Referencia Técnica

**USO:** API reference, configuration parameters

```markdown
| Parameter | Type | Default | Required | Description |
|:----------|:----:|:-------:|:--------:|:------------|
| `api_key` | `str` | `None` | ✅ | Authentication key |
| `timeout` | `int` | `30` | ❌ | Request timeout (seconds) |
| `retries` | `int` | `3` | ❌ | Max retry attempts |
| `base_url` | `str` | `"https://api.example.com"` | ❌ | API base URL |
```

**CARACTERÍSTICAS:**
- Código inline para nombres técnicos
- Tipos centrados
- Defaults con valores específicos
- Descripción concisa (no exceder 80 chars)

---

### 7.4. Tabla de Validación

**USO:** Checklists, compliance tracking

```markdown
| Requirement | Status | Evidence | Notes |
|:------------|:------:|:---------|:------|
| Unit tests coverage >80% | ✅ | `coverage.txt` | 87% achieved |
| Security audit passed | ✅ | `audit-report.md` | No critical issues |
| Documentation updated | 🟡 | - | API docs pending |
| Performance benchmarked | ❌ | - | Blocked by infra |
```

**CARACTERÍSTICAS:**
- Status con checkmarks
- Evidence column con referencias
- Notes para contexto adicional

---

### 7.5. Matriz de Decisión

**USO:** Evaluación multi-criterio

```markdown
| Option | Cost | Time | Risk | **Score** |
|:-------|-----:|-----:|-----:|----------:|
| Option A | $10K | 2 weeks | Low | **8/10** |
| Option B | $5K | 4 weeks | Medium | **6/10** |
| Option C | $15K | 1 week | High | **5/10** |
```

**CARACTERÍSTICAS:**
- Criterios numéricos alineados derecha
- Score final en negrilla
- Permite ordenar por columna visualmente

---

## 8. Anti-Patrones: Qué Evitar

### 8.1. Tabla de Una Sola Columna

**❌ PROHIBIDO:**
```markdown
| Items |
|-------|
| Item 1 |
| Item 2 |
| Item 3 |
```

**✅ USAR LISTA:**
```markdown
- Item 1
- Item 2
- Item 3
```

---

### 8.2. Símbolos Decorativos en Headers

**❌ INCORRECTO:**
```markdown
| 🚀 Feature | 📊 Metrics | 🎉 Status |
|-----------|------------|----------|
```

**✅ CORRECTO:**
```markdown
| Feature | Metrics | Status |
|---------|---------|--------|
```

---

### 8.3. Inconsistencia de Símbolos

**❌ INCORRECTO:**
```markdown
| Task | Status |
|------|--------|
| A    | ✅ Done |
| B    | ✓ Done |   ← Símbolo diferente
| C    | DONE |     ← Sin símbolo
```

**✅ CORRECTO:**
```markdown
| Task | Status |
|------|--------|
| A    | ✅ Done |
| B    | ✅ Done |
| C    | ✅ Done |
```

---

### 8.4. Celdas Vacías Sin Indicador

**❌ CONFUSO:**
```markdown
| Feature | Status | Owner |
|---------|--------|-------|
| Auth    | Done   |       |   ← ¿Vacío o error?
```

**✅ CLARO:**
```markdown
| Feature | Status | Owner |
|---------|--------|-------|
| Auth    | Done   | - |     ← Explícitamente sin asignar
| API     | Done   | @dev |
```

**ALTERNATIVAS para celdas vacías:**
- `-` (sin valor)
- `N/A` (no aplica)
- `TBD` (to be determined)
- `⚪` (pending)

---

### 8.5. Mezcla de Formatos Sin Criterio

**❌ INCONSISTENTE:**
```markdown
| Feature | Status |
|---------|--------|
| Auth    | ✅ DONE |
| API     | Done |      ← Sin símbolo
| Cache   | 🟢 |        ← Sin texto
```

**✅ CONSISTENTE:**
```markdown
| Feature | Status |
|---------|--------|
| Auth    | ✅ DONE |
| API     | ✅ DONE |
| Cache   | ✅ DONE |
```

---

### 8.6. Tablas Demasiado Anchas

**❌ ILEGIBLE (10 columnas):**
```markdown
| F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 |
|----|----|----|----|----|----|----|----|----|-----|
```

**✅ DIVIDIR:**
```markdown
### Core Features
| F1 | F2 | F3 | F4 |
|----|----|----|----|

### Advanced Features
| F5 | F6 | F7 | F8 |
|----|----|----|----|
```

---

### 8.7. Redundancia Excesiva

**❌ REDUNDANTE:**
```markdown
| Status | Symbol | Text | Color |
|--------|--------|------|-------|
| Completed | ✅ | Completed | Green |   ← Info duplicada
```

**✅ CONCISO:**
```markdown
| Feature | Status |
|---------|--------|
| Auth    | ✅ Completed |
```

---

## 9. Template Recomendado para Copiar/Pegar

### Template 1: Tabla de Estado Simple

```markdown
| Item | Status | Priority | Owner |
|:-----|:------:|:--------:|------:|
| Name | 🟢 Active | ⚡ High | @user |
```

### Template 2: Tabla Comparativa

```markdown
| Feature | Option A | Option B | Option C |
|:--------|:--------:|:--------:|:--------:|
| Cost    | Low      | Medium   | High     |
| Time    | Fast     | Medium   | Slow     |
```

### Template 3: Tabla de Referencia Técnica

```markdown
| Parameter | Type | Default | Required | Description |
|:----------|:----:|:-------:|:--------:|:------------|
| `param`   | `str` | `None` | ✅ | Short description |
```

### Template 4: Tabla de Validación

```markdown
| Requirement | Status | Evidence | Notes |
|:------------|:------:|:---------|:------|
| Item 1      | ✅     | Link     | Details |
| Item 2      | 🟡     | -        | In progress |
| Item 3      | ❌     | -        | Blocked |
```

---

## 10. Checklist de Validación de Tablas

Antes de publicar una tabla, verificar:

- [ ] **Headers descriptivos** sin símbolos decorativos
- [ ] **Alineación apropiada** (texto izq, números der, símbolos centro)
- [ ] **Símbolos consistentes** dentro de cada columna
- [ ] **Máximo 5-6 columnas** (justificar si más)
- [ ] **Celdas <80 caracteres** de texto
- [ ] **Símbolos funcionales** solo de whitelist (CLAUDE.md v3.1)
- [ ] **Formato mixto justificado** (no decoración)
- [ ] **Sin símbolos pictográficos** (🚀 📊 💻)
- [ ] **Celdas vacías tienen indicador** (-, N/A, TBD)
- [ ] **Tabla no requiere scroll horizontal** en pantallas estándar
- [ ] **Alternativa de texto plano** considerada para datos complejos

---

## 11. Herramientas

### Generadores de Tablas

**Online:**
- TablesGenerator.com/markdown_tables
- tableconvert.com

**VS Code Extensions:**
- Markdown Table Prettifier
- Excel to Markdown Table

### Validadores

**markdownlint** puede verificar:
- Consistencia de separadores
- Headers presentes

**Script custom:**
```bash
# Verificar tablas con >6 columnas
grep -rn "^|" *.md | awk -F'|' '{print NF-2, $0}' | awk '$1 > 6'
```

---

## 12. Resumen Ejecutivo

### Principios Clave

1. **Claridad sobre decoración** - Símbolos deben ser funcionales
2. **Consistencia** - Un símbolo por estado en cada columna
3. **Simplicidad** - Máximo 5-6 columnas idealmente
4. **Alineación intencional** - Texto izq, números der, símbolos centro
5. **Headers limpios** - Sin símbolos decorativos

### Reglas de Oro

- ✅ Símbolos en CONTENIDO, no en headers
- ✅ Consistencia de símbolos por columna
- ✅ Dividir tablas complejas (>6 columnas)
- ✅ Texto + símbolo para máxima claridad
- ❌ Sin emojis pictográficos decorativos

### Cuándo Usar Tabla vs Lista

**USAR TABLA cuando:**
- Datos multidimensionales (2+ propiedades por item)
- Comparación de alternativas
- Tracking de estado estructurado

**USAR LISTA cuando:**
- Una sola dimensión de información
- Solo 1-2 columnas
- Orden secuencial más importante que comparación

---

**FIN DEL REPORTE**
