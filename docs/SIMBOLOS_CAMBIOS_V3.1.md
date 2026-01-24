# Cambios en Guía de Simbología v3.1 Master

**Fecha:** 2026-01-18
**Ubicación:** CLAUDE.md:71-309 (reemplaza líneas 71-161 anteriores)

---

## Resumen de Cambios

### Enfoque Actualizado

**ANTERIOR (v3.0):**
- Lista blanca estricta con símbolos individuales enumerados
- Enfoque restrictivo sin categorías claras

**NUEVO (v3.1 Master):**
- **Whitelist flexible por categorías funcionales**
- Permite rangos completos (ej: U+2500-U+257F para box-drawing)
- Énfasis en propósito funcional vs decorativo
- Guías de uso contextuales

---

## Cambios Principales

### 1. Box-Drawing Characters (Mayor Cambio)

**ANTES:** Solo 10 caracteres específicos listados
```
─ │ ┌ ┐ └ ┘ ├ ┤ ╱ ╲
```

**AHORA:** Categoría completa permitida (U+2500-U+257F)
```
Basic set: ─ │ ┌ ┐ └ ┘ ├ ┤ ╱ ╲
Extended: ┬ ┴ ┼ ├ ┤ ┣ ┫
Double-line: ═ ║ ╔ ╗ ╚ ╝
Heavy-line: ━ ┃ ┏ ┓ ┗ ┛
```

**Guía agregada:** Mantener consistencia dentro de un mismo diagrama.

### 2. Status Circles: 4 Colores Confirmados

**Confirmación explícita:** 🟡🟢🔴🟠 (4 colores)

**Uso definido:**
- 🟡 Yellow: In progress, pending, warning
- 🟢 Green: Completed, active, success
- 🔴 Red: Error, blocked, failed
- 🟠 Orange: Attention needed, partial completion

### 3. Directional Arrows: Reemplazo Correcto

**Nueva guía de conversión ASCII:**
- ← becomes <-
- → becomes ->
- ↑ becomes ^ or (up)
- ↓ becomes v or (down)

**Problema resuelto:** Anteriormente scripts convertían ↓ a -> (incorrecto).

### 4. Emphasis Symbols: Uso Clarificado y Corrección

**Antes:** Listados sin contexto claro, usando ⚠ (sin variant selector)

**Ahora:**
- ⚠️ (warning): U+26A0 + FE0F (emoji colorido) - Uso esporádico, solo advertencias críticas
- ⚡ (lightning): Alta prioridad
- ❓ (question): Estado incierto
- ☆★ (stars): Solo para ratings/prioridades

**Corrección importante:** Usar ⚠️ (con variant selector FE0F) para renderizado correcto como emoji amarillo/naranja, no el carácter texto plano ⚠.

**Recomendación:** Preferir texto plano ("WARNING:", "PRIORITY:") en mayoría de casos.

### 5. Plain Text Alternatives: Tabla de Referencia

**Nueva sección agregada:** Tabla de equivalencias símbolo → texto plano

| Símbolo | Alternativa |
|---------|-------------|
| ✅ | COMPLETED: |
| ❌ | ERROR: |
| ⚠️ | WARNING: |
| 🟡 | IN_PROGRESS: |
| 🟢 | SUCCESS: |
| 🔴 | FAILED: |
| 🟠 | ATTENTION: |
| ⚡ | PRIORITY: |

### 6. Scope of Application: Definido Explícitamente

**Nueva sección:** Dónde aplican estas reglas

- Agent prompts y task definitions
- Reports y synthesis documents
- Code comments y docstrings
- User-facing messages y logs
- Validation outputs
- All framework documentation

### 7. Validation and Enforcement: Prioridad de Resolución

**Nueva sección:** Cómo resolver conflictos

**Jerarquía:**
1. CLAUDE.md v3.1 Master (esta guía) - AUTORIDAD MÁXIMA
2. Scripts de validación (deben sincronizarse)
3. Documentos legacy (flagged para actualización)

---

## Inconsistencias Resueltas

### Conflicto CLAUDE.md vs CHECKLIST.md

**RESOLUCIÓN:** CLAUDE.md es autoridad. CHECKLIST.md debe actualizarse para:
- Permitir símbolos funcionales de la whitelist
- Mantener recomendación de texto plano como alternativa
- Eliminar prohibición absoluta de símbolos

### Conflicto en Scripts de Validación

**IDENTIFICADOS para actualización:**

1. **verificar_simbolos_no_permitidos.py**
   - Tiene 28 box-drawing chars vs 10 en v3.0
   - CORRECTO en v3.1 (categoría completa permitida)
   - NO requiere cambios

2. **limpiar_emojis.py**
   - REQUIERE CORRECCIÓN: Elimina ⚠ y ⚡ (ahora permitidos)
   - REQUIERE CORRECCIÓN: Conversión incorrecta de flechas (↓→->)
   - REQUIERE CORRECCIÓN: Elimina box-drawing doble (ahora permitido)

3. **encontrar_simbolos.py**
   - REQUIERE CORRECCIÓN: Lista aprobada incompleta (falta 🟡🟠)
   - Debe incluir los 4 círculos de estado

---

## Próximos Pasos (Recomendados)

### Prioridad Alta

1. **Actualizar scripts/limpiar_emojis.py**
   - Corregir conversiones de flechas
   - No eliminar ⚠ ⚡ (son permitidos)
   - Permitir box-drawing completo

2. **Actualizar scripts/encontrar_simbolos.py**
   - Agregar 🟡🟠 a lista aprobada
   - Ajustar categorización

3. **Actualizar docs/CHECKLIST.md**
   - Alinear con CLAUDE.md v3.1
   - Cambiar de "no symbols" a "functional symbols only"
   - Mantener recomendación de texto plano como alternativa

### Prioridad Media

4. **Auditar documentación existente**
   - Escanear con scripts actualizados
   - Flagear documentos con símbolos prohibidos
   - Planificar migración gradual

5. **Actualizar prompts de agentes**
   - Referenciar CLAUDE.md:71-309 como guía
   - Incluir tabla de alternativas texto plano
   - Enfatizar "functional over decorative"

### Prioridad Baja

6. **Crear tests de regresión**
   - Test suite para validar scripts
   - Casos de prueba con símbolos edge-case
   - CI/CD check para nuevos commits

7. **Documentar en CHANGELOG**
   - Anunciar cambios v3.1
   - Listar breaking changes
   - Guía de migración para usuarios

---

## Referencias

**Documento maestro:** CLAUDE.md:71-309
**Versión:** v3.1 Master
**Fecha efectiva:** 2026-01-18

**Archivos afectados:**
- `CLAUDE.md` (actualizado)
- `docs/CHECKLIST.md` (pendiente actualización)
- `scripts/limpiar_emojis.py` (pendiente corrección)
- `scripts/encontrar_simbolos.py` (pendiente corrección)
- `scripts/verificar_simbolos_no_permitidos.py` (compatible, no requiere cambios)

**Análisis completo de inconsistencias:** Ver reporte del agente Explore (ID: a04294e)

---

## Preguntas Frecuentes

**Q: ¿Puedo usar emojis decorativos si mi audiencia los espera?**
A: No. La guía prioriza profesionalismo y consistencia. Usa texto plano descriptivo.

**Q: ¿Qué pasa si necesito un símbolo no listado?**
A: Consulta al maintainer del proyecto antes de agregar nuevas categorías.

**Q: ¿Los scripts de validación rechazarán mis commits?**
A: Una vez actualizados, sí. Usa plain text alternatives si hay conflictos.

**Q: ¿Puedo mezclar estilos de box-drawing en el mismo documento?**
A: Sí, pero mantén consistencia dentro de un mismo diagrama.

**Q: ¿Cuándo uso símbolos vs texto plano?**
A: Símbolos para visualización rápida (dashboards, listas). Texto plano para logs, scripts, accesibilidad.
