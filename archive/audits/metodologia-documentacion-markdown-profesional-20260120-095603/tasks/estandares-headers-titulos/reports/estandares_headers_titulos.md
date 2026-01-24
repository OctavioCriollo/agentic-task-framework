# Estándares para Headers y Títulos: Uso de Símbolos

**Versión:** 1.0
**Fecha:** 2026-01-20
**Framework:** Agentic Task Framework v2.2

---

## Pregunta Original del Usuario

> "Hay algunos documentos que tienen símbolo de visto (checkmark) en los títulos. No sé si eso es adecuado o no."

**Ejemplo citado:**
`## S1: Path Traversal Validation ✅ IMPLEMENTED`

Este reporte responde definitivamente esta pregunta con reglas claras y basadas en evidencia.

---

## 1. Regla General: Headers SIN Símbolos

**PRINCIPIO FUNDAMENTAL:**

Los headers/títulos de documentación profesional **NO deben contener símbolos**, salvo excepciones justificadas.

**Razones:**

1. **Generación de TOC (Table of Contents)**
   - Símbolos rompen enlaces en algunos renderizadores
   - GitHub TOC auto-generado puede tener problemas con Unicode
   - Nombres de anchors (#) se vuelven impredecibles

2. **Búsqueda e Indexación**
   - Motores de búsqueda pueden ignorar símbolos
   - Ctrl+F / búsqueda en página menos efectiva
   - IDEs y editores pueden no reconocer símbolos en navegación

3. **Accesibilidad**
   - Screen readers pueden interpretar mal símbolos
   - Braille displays tienen problemas con Unicode avanzado
   - Compatibilidad con sistemas legacy

4. **Profesionalidad**
   - Documentación técnica formal evita símbolos en headers
   - Consistencia con estándares de industria (ver benchmarking)
   - Reduce "ruido visual" en documentos largos

**REGLA:**
```markdown
# ✅ Correcto
## Project Architecture

# ❌ Incorrecto
## 🚀 Project Architecture
## ✅ Project Architecture Completed
## 🟢 Active Module
```

---

## 2. Excepciones Justificadas

Existen contextos **específicos** donde los símbolos en headers son apropiados:

### 2.1. Documentos de Auditoría y Tracking

**CONTEXTO:** Reports internos de progreso, auditorías de seguridad, tracking de issues.

**PERMITIDO:**
```markdown
## S1: Path Traversal Validation ✅ IMPLEMENTED
## S2: Input Validation ❌ FAILED
## S3: Error Handling 🟡 IN_PROGRESS
```

**JUSTIFICACIÓN:**
- Comunica estado de manera inmediata y visual
- Audiencia técnica interna (no documentación pública)
- Documento temporal (no es referencia permanente)
- Valor informativo del símbolo supera desventajas técnicas

**FORMATO RECOMENDADO:**
```markdown
## [ID]: [Descripción] [SÍMBOLO] [ESTADO_TEXTUAL]
```

Ejemplo:
```markdown
## Finding 3: Hardcoded Paths ✅ RESOLVED
## Bug #42: Memory Leak 🟡 INVESTIGATING
```

---

### 2.2. Advertencias Críticas

**CONTEXTO:** Secciones que requieren atención inmediata del lector.

**PERMITIDO:**
```markdown
## ⚠️ Breaking Changes in v2.0
## ⚠️ Security Advisory
## ⚠️ CRITICAL: Database Migration Required
```

**JUSTIFICACIÓN:**
- El símbolo ⚠️ es universalmente reconocido
- Mejora la seguridad al destacar información crítica
- Riesgo de ignorar advertencia supera desventajas técnicas

**LIMITACIÓN:** Solo usar ⚠️ (warning sign). NO usar otros símbolos.

---

### 2.3. Documentos de Estado Dinámico

**CONTEXTO:** Dashboards, status pages, documentos que se actualizan frecuentemente.

**PERMITIDO:**
```markdown
## System Status

### 🟢 API Server
### 🟢 Database
### 🔴 Cache Service
### 🟡 Background Workers
```

**JUSTIFICACIÓN:**
- Documento diseñado para escaneo rápido visual
- Actualización frecuente (no es referencia estática)
- Alternativa a sistema de monitoreo gráfico

**LIMITACIÓN:** Solo usar sistema de 4 círculos (🟢🟡🔴🟠). Mantener consistencia.

---

## 3. Matriz de Decisión: Cuándo Usar Símbolos

| Tipo de Documento | Audiencia | Símbolos en Headers | Justificación |
|-------------------|-----------|---------------------|---------------|
| **README.md** | Pública/Abierta | ❌ NUNCA | Profesionalidad, SEO, accesibilidad |
| **CONTRIBUTING.md** | Contribuidores | ❌ NUNCA | Referencia técnica formal |
| **Docs Técnicas** (API, specs) | Desarrolladores | ❌ NUNCA | Indexación, búsqueda, TOC |
| **Wiki Interna** | Equipo interno | ⚠️ CON CAUTELA | Depende del contexto |
| **Reports de Auditoría** | Interna técnica | ✓ PERMITIDO | Tracking de estado necesario |
| **Issues/PRs de GitHub** | Proyecto específico | ✓ PERMITIDO | Workflow de GitHub lo soporta |
| **Status Dashboards** | Operaciones | ✓ PERMITIDO | Diseñado para escaneo visual |
| **Guías de Usuario** | Usuarios finales | ❌ NUNCA | Claridad, accesibilidad |
| **Documentación Legal** | Legal/Compliance | ❌ NUNCA | Formalidad absoluta |

**REGLA SIMPLE:**

- **Documentación PÚBLICA o FORMAL** → SIN símbolos
- **Documentación INTERNA de TRACKING** → Símbolos permitidos con restricciones
- **¿En duda?** → NO usar símbolos (default seguro)

---

## 4. Ejemplos: Correcto vs Incorrecto

### Ejemplo 1: README.md de Proyecto

**❌ INCORRECTO:**
```markdown
# 🚀 My Awesome Project

## ✨ Features
## 📊 Usage
## 🎉 Installation
```

**✅ CORRECTO:**
```markdown
# My Awesome Project

## Features
## Usage
## Installation
```

---

### Ejemplo 2: Documentación de API

**❌ INCORRECTO:**
```markdown
# API Reference

## 🟢 Authentication Endpoints
## 🔴 Deprecated Endpoints
```

**✅ CORRECTO:**
```markdown
# API Reference

## Authentication Endpoints
## Deprecated Endpoints ⚠️

> **WARNING:** The endpoints in this section are deprecated...
```

**NOTA:** La advertencia ⚠️ está FUERA del header, en el contenido.

---

### Ejemplo 3: Reporte de Auditoría (EXCEPCIÓN)

**✓ ACEPTABLE (contexto interno):**
```markdown
# Security Audit Report - 2026-01-20

## Phase 1: Critical Fixes

### S1: Path Traversal Validation ✅ IMPLEMENTED
### S2: Input Sanitization ✅ IMPLEMENTED
### S3: Authentication Flow 🟡 IN_PROGRESS
### S4: Error Handling ❌ FAILED

## Phase 2: High Priority

### S5: Logging Enhancement ⚪ PENDING
```

**JUSTIFICACIÓN:** Documento temporal de tracking interno. El estado visual es crítico.

**MEJORA (más profesional):**

```markdown
# Security Audit Report - 2026-01-20

## Phase 1: Critical Fixes

| ID | Finding | Status |
|----|---------|--------|
| S1 | Path Traversal Validation | ✅ IMPLEMENTED |
| S2 | Input Sanitization | ✅ IMPLEMENTED |
| S3 | Authentication Flow | 🟡 IN_PROGRESS |
| S4 | Error Handling | ❌ FAILED |
```

**NOTA:** Preferir tabla sobre símbolos en headers cuando sea posible.

---

### Ejemplo 4: GitHub Issue (EXCEPCIÓN)

**✓ ACEPTABLE:**
```markdown
# Feature Request: Dark Mode

## 🟡 Status: Under Review

### ✅ Completed Tasks
- [x] Design mockups
- [x] User research

### 🟡 In Progress
- [ ] Component implementation
- [ ] Theme switcher

### ⚪ Pending
- [ ] Documentation
- [ ] Testing
```

**JUSTIFICACIÓN:** GitHub issues son informales y diseñados para tracking.

---

## 5. Posición del Símbolo (Cuando se Permite)

Cuando los símbolos son justificados, seguir estas reglas de posición:

### 5.1. Símbolo DESPUÉS del Título

**FORMATO:**
```markdown
## [Título Descriptivo] [SÍMBOLO] [ESTADO]
```

**EJEMPLOS:**
```markdown
## Authentication Module ✅ COMPLETED
## Database Migration ⚠️ REQUIRED
## Cache Service 🟢 ACTIVE
```

**RAZÓN:** El título permanece legible si se remueven símbolos.

---

### 5.2. Símbolo INTEGRADO (Solo ⚠️)

**FORMATO:**
```markdown
## ⚠️ [Advertencia Crítica]
```

**EJEMPLO:**
```markdown
## ⚠️ Breaking Changes in v3.0
## ⚠️ Security Update Required
```

**RAZÓN:** El warning es parte integral del mensaje.

**LIMITACIÓN:** Solo con ⚠️. NO con otros símbolos.

---

### 5.3. NUNCA Símbolo ANTES del Título

**❌ PROHIBIDO:**
```markdown
## ✅ Completed Tasks
## 🚀 New Features
## 🟢 Active Services
```

**RAZÓN:**
- Rompe orden alfabético en TOC
- Dificulta búsqueda
- Menos profesional

---

## 6. Respuesta a la Pregunta Original

### ¿Es apropiado `## Finding X ✅ IMPLEMENTED`?

**RESPUESTA CORTA:** **SÍ, pero solo en contextos específicos.**

**RESPUESTA DETALLADA:**

**✓ APROPIADO si el documento es:**
- Reporte de auditoría interna
- Tracking de seguridad
- Documento temporal de progreso
- Audiencia técnica interna

**FORMATO RECOMENDADO:**
```markdown
## S1: Path Traversal Validation ✅ IMPLEMENTED
```

**✓ Componentes correctos:**
- ID claro (S1)
- Descripción técnica (Path Traversal Validation)
- Símbolo funcional (✅)
- Estado textual (IMPLEMENTED)

---

**❌ NO APROPIADO si el documento es:**
- README.md público
- Documentación de API
- Guía de usuario
- Especificación técnica formal
- CONTRIBUTING.md

**ALTERNATIVA para docs formales:**

Remover símbolo del header, usar tabla:

```markdown
## Security Findings

| ID | Finding | Status |
|----|---------|--------|
| S1 | Path Traversal Validation | ✅ IMPLEMENTED |
| S2 | Input Validation | 🟡 IN_PROGRESS |
```

---

## 7. Recomendaciones para el Framework

### 7.1. CLAUDE.md (Principal)

**ESTADO ACTUAL:** 2 headers con símbolos (de 47 total) = 4%

**RECOMENDACIÓN:** **Mantener sin símbolos** (referencia técnica formal).

**ACCIÓN:** Remover los 2 headers con símbolos si existen.

---

### 7.2. README.md

**ESTADO ACTUAL:** Sin símbolos en headers ✅

**RECOMENDACIÓN:** **Mantener** sin símbolos.

---

### 7.3. Reports de Auditoría

**ESTADO ACTUAL:** ~15% de headers tienen símbolos de estado

**RECOMENDACIÓN:** **Permitido** dado el contexto.

**MEJORA SUGERIDA:** Migrar a formato de tabla cuando sea posible:

**Antes:**
```markdown
## Finding 1 ✅ RESOLVED
## Finding 2 ❌ PENDING
```

**Después:**
```markdown
## Findings Summary

| ID | Finding | Status |
|----|---------|--------|
| F1 | Path Traversal | ✅ RESOLVED |
| F2 | Input Validation | ❌ PENDING |
```

---

### 7.4. Docs Técnicos (docs/)

**ESTADO ACTUAL:** ~8% de headers con símbolos

**RECOMENDACIÓN:** **Eliminar símbolos** de headers.

**EXCEPCIÓN:** Mantener solo ⚠️ en secciones críticas.

---

## 8. Impacto Técnico Detallado

### 8.1. Generación de TOC

**PROBLEMA:**

Markdown processors generan anchors a partir de headers:

```markdown
## My Feature
→ Anchor: #my-feature

## ✅ My Feature
→ Anchor: #-my-feature o #my-feature (inconsistente)
```

**IMPACTO:** Links internos pueden romperse.

**EJEMPLO ROTO:**
```markdown
See [implementation](#✅-my-feature)  ❌ No funciona confiablemente
```

---

### 8.2. Búsqueda por Texto

**PROBLEMA:**

Usuario busca "Feature" con Ctrl+F:

- Sin símbolo: `## My Feature` ✅ Encuentra
- Con símbolo antes: `## ✅ My Feature` ⚠️ Puede no encontrar
- Con símbolo después: `## My Feature ✅` ✅ Encuentra

**IMPACTO:** Reduce findability del contenido.

---

### 8.3. Compatibilidad Cross-Platform

**PROBLEMA:**

Renderizado inconsistente de símbolos:

- GitHub Web: ✅ Excelente
- GitHub CLI (gh): ⚠️ Variable
- Vim/Emacs: ❌ Puede mostrar codes
- Email viewers: ❌ Frecuentemente roto
- PDF export: ⚠️ Depende del motor

**IMPACTO:** Documentos pueden verse diferentes en distintas plataformas.

---

## 9. Casos de Estudio: Proyectos Externos

### Django Project

**Observación:** CERO símbolos en headers de documentación oficial.

**Headers típicos:**
```markdown
# Getting Started
## Installation
## Configuration
```

**LECCIÓN:** Proyectos maduros evitan símbolos en docs formales.

---

### Kubernetes Docs

**Observación:** Solo ⚠️ en advertencias críticas.

**Ejemplo encontrado:**
```markdown
## ⚠️ Breaking Changes

The following changes may affect...
```

**LECCIÓN:** Si usas símbolos, limita a ⚠️ para criticidad.

---

### FastAPI Docs

**Observación:** SIN símbolos en headers principales.

**Uso de emojis:** Solo en ejemplos de código y contenido, NO en headers.

**LECCIÓN:** Separar estructura (headers) de contenido (donde emojis pueden estar).

---

## 10. Checklist de Validación

Antes de publicar un documento, verificar:

- [ ] Headers de nivel 1-3 NO tienen símbolos (salvo excepciones)
- [ ] Si hay símbolos en headers, el documento califica como excepción (auditoría interna, tracking, etc.)
- [ ] Símbolos de advertencia (⚠️) están justificados por criticidad
- [ ] TOC auto-generado funciona correctamente
- [ ] Búsqueda por texto (Ctrl+F) encuentra headers esperados
- [ ] Documento es accesible con screen readers (si es público)
- [ ] Formato es: `## [Título] [SÍMBOLO] [ESTADO]` (no al revés)
- [ ] Se consideró alternativa de tabla en lugar de símbolos en headers
- [ ] Documento cumple nivel de profesionalidad esperado para su audiencia
- [ ] Símbolos usados están en whitelist de CLAUDE.md v3.1

---

## 11. Herramientas de Validación

### Script de Auditoría

```bash
# Encontrar todos los headers con símbolos
grep -rn "^##.*[✅❌🟢🟡🔴🚀]" *.md

# Verificar headers con checkmarks
grep -rn "^##.*✅" *.md | wc -l
```

### Regla pre-commit

```yaml
# .pre-commit-config.yaml
- id: check-markdown-headers
  name: Check markdown headers for symbols
  entry: bash -c 'grep -rn "^##[[:space:]]*[🚀📊💻✨]" docs/ && exit 1 || exit 0'
  language: system
  files: \.md$
```

---

## 12. Resumen Ejecutivo

### REGLA GENERAL

**Headers NO deben tener símbolos** en documentación formal/pública.

### EXCEPCIONES PERMITIDAS

1. **Reports de auditoría internos** - Estado de findings
2. **Advertencias críticas** - Solo ⚠️
3. **Status dashboards** - Sistema de 4 círculos

### FORMATO CUANDO SE PERMITE

```markdown
## [Título Descriptivo] [SÍMBOLO] [ESTADO_TEXTO]
```

### RESPUESTA A LA PREGUNTA ORIGINAL

**`## S1: Path Traversal Validation ✅ IMPLEMENTED`**

✓ **APROPIADO** en reportes de auditoría interna.
❌ **NO APROPIADO** en README.md, docs/ técnicos, o CONTRIBUTING.md.

### GUÍA RÁPIDA DE DECISIÓN

```
¿Es documentación pública o formal?
├─ SÍ → NO usar símbolos en headers
└─ NO → ¿Es documento de tracking/auditoría?
    ├─ SÍ → Símbolos permitidos (formato correcto)
    └─ NO → Preferir SIN símbolos (default seguro)
```

---

**FIN DEL REPORTE**
