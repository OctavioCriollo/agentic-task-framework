# Unicode Circles Reference Guide
**Purpose:** Visual reference for selecting circle symbols
**Date:** 2026-01-19

---

## 1. CÍRCULOS BÁSICOS (Basic Circles)

### Tamaño Estándar

| Symbol | Unicode | Name | Uso Recomendado |
|--------|---------|------|-----------------|
| ○ | U+25CB | White Circle | Vacío, sin relleno, estado neutro |
| ● | U+25CF | Black Circle | Lleno, completo, estado activo |
| ◯ | U+25EF | Large Circle | Círculo grande vacío, énfasis |
| ⚫ | U+26AB | Medium Black Circle | Negro mediano, estado crítico |
| ⚪ | U+26AA | Medium White Circle | Blanco mediano, obsoleto |

### Comparación Visual

```
○ ● ◯ ⚫ ⚪
```

---

## 2. CÍRCULOS CON PUNTO CENTRAL (Circles with Dot)

| Symbol | Unicode | Name | Uso Recomendado |
|--------|---------|------|-----------------|
| ◉ | U+25C9 | Fisheye | Círculo con punto central, enfoque |
| ⦿ | U+29BF | Circled Bullet | Círculo con bullet, ítem importante |
| ⊙ | U+2299 | Circled Dot Operator | Operador con punto, matemático |

### Comparación Visual

```
◉ ⦿ ⊙
```

---

## 3. CÍRCULOS SOMBREADOS (Shaded Circles)

### Diferentes Niveles de Gris

| Symbol | Unicode | Name | Nivel de Gris | Uso Recomendado |
|--------|---------|------|---------------|-----------------|
| ◔ | U+25D4 | Circle with Upper Right Quadrant Black | 25% negro | Progreso bajo |
| ◕ | U+25D5 | Circle with All But Upper Left Quadrant Black | 75% negro | Progreso alto |
| ◐ | U+25D0 | Circle with Left Half Black | 50% negro (izq) | Medio progreso |
| ◑ | U+25D1 | Circle with Right Half Black | 50% negro (der) | Medio progreso |
| ◒ | U+25D2 | Circle with Lower Half Black | 50% negro (abajo) | Medio progreso |
| ◓ | U+25D3 | Circle with Upper Half Black | 50% negro (arriba) | Medio progreso |

### Comparación Visual - Progreso

```
○ (0%)  ◔ (25%)  ◐ (50%)  ◕ (75%)  ● (100%)
```

### Comparación Visual - Todos los Sombreados

```
◔ ◕ ◐ ◑ ◒ ◓
```

---

## 4. CÍRCULOS DE DIFERENTES TAMAÑOS (Size Variations)

### Pequeños (Small)

| Symbol | Unicode | Name |
|--------|---------|------|
| · | U+00B7 | Middle Dot |
| • | U+2022 | Bullet |
| ‣ | U+2023 | Triangular Bullet |

### Medianos (Medium)

| Symbol | Unicode | Name |
|--------|---------|------|
| ⚪ | U+26AA | Medium White Circle |
| ⚫ | U+26AB | Medium Black Circle |
| 🔘 | U+1F518 | Radio Button |

### Grandes (Large)

| Symbol | Unicode | Name |
|--------|---------|------|
| ◯ | U+25EF | Large Circle |
| ⬤ | U+2B24 | Black Large Circle |

### Comparación Visual por Tamaño

```
Pequeños: · • ‣
Medianos: ○ ● ⚪ ⚫ 🔘
Grandes:  ◯ ⬤
```

---

## 5. CÍRCULOS CON CONTORNO (Outlined Circles)

### Diferentes Grosores de Borde

| Symbol | Unicode | Name | Grosor de Contorno |
|--------|---------|------|-------------------|
| ○ | U+25CB | White Circle | Fino |
| ◯ | U+25EF | Large Circle | Fino (más grande) |
| ⭕ | U+2B55 | Heavy Large Circle | Grueso (bold) |
| ⃝ | U+20DD | Combining Enclosing Circle | Combinable |

### Comparación Visual

```
○ (fino)  ◯ (fino grande)  ⭕ (grueso)
```

---

## 6. CÍRCULOS DOBLES Y ESPECIALES (Double & Special)

| Symbol | Unicode | Name | Uso Recomendado |
|--------|---------|------|-----------------|
| ◎ | U+25CE | Bullseye | Doble círculo, objetivo |
| ◙ | U+25D9 | Inverse White Circle | Cuadrado con círculo |
| ◘ | U+25D8 | Inverse Bullet | Cuadrado con bullet |

### Comparación Visual

```
◎ ◙ ◘
```

---

## 7. PROPUESTAS PARA ESTADOS (Status Indicators)

### Opción A: Simple (2 estados)

```
○ OBSOLETE / LEGACY
● PENDING / IN_PROGRESS
```

### Opción B: Tres Niveles (3 estados)

```
○ OBSOLETE / LEGACY       (vacío, sin importancia)
◐ PENDING / IN_PROGRESS   (medio lleno, en proceso)
● CRITICAL / BLOCKED      (lleno, atención máxima)
```

### Opción C: Progreso con Sombreado (4 estados)

```
○ OBSOLETE                (0% - vacío)
◔ LEGACY                  (25% - poco relevante)
◐ PENDING                 (50% - medio)
● BLOCKED                 (100% - lleno)
```

### Opción D: Con Radio Button (actual v3.2)

```
⚪ OBSOLETE / LEGACY       (blanco mediano)
🔘 PENDING / OPTIONAL     (radio button gris)
⚫ BLOCKED / CRITICAL      (negro mediano)
```

### Opción E: Tamaños Mixtos

```
○ OBSOLETE                (pequeño vacío)
◯ PENDING                 (grande vacío)
● BLOCKED                 (pequeño lleno)
```

### Opción F: Con Contorno Grueso

```
○ OBSOLETE                (fino)
⭕ PENDING                (grueso)
● BLOCKED                 (lleno)
```

---

## 8. CÍRCULOS CON RELLENO PARCIAL (Partial Fill)

### Cuadrantes

```
◔ Upper Right Black       ◕ All But Upper Left Black
◐ Left Half Black         ◑ Right Half Black
◒ Lower Half Black        ◓ Upper Half Black
```

### Visualización de Progreso

```
Estado 0%:   ○
Estado 25%:  ◔
Estado 50%:  ◐ o ◑
Estado 75%:  ◕
Estado 100%: ●
```

---

## 9. COMBINACIONES CON CHECKMARKS

### Para Documentación de Estado

```
✅ ○ IMPLEMENTED + OBSOLETE     → Ya no necesario
✅ ● IMPLEMENTED + ACTIVE       → Funcional y activo
❌ ◐ FAILED + IN_PROGRESS       → Falló durante implementación
⚪ ○ OBSOLETE + DEPRECATED      → Doble indicación de obsoleto
```

---

## 10. TABLA COMPARATIVA COMPLETA

### Ordenados por "Peso Visual" (Lightest → Darkest)

| Symbol | Peso Visual | Unicode | Tamaño | Contorno | Relleno |
|--------|-------------|---------|--------|----------|---------|
| · | 1/10 | U+00B7 | XS | Ninguno | Lleno |
| ○ | 2/10 | U+25CB | M | Fino | Vacío |
| ◯ | 2/10 | U+25EF | L | Fino | Vacío |
| ⭕ | 3/10 | U+2B55 | L | Grueso | Vacío |
| ◔ | 4/10 | U+25D4 | M | Fino | 25% |
| ◐ | 5/10 | U+25D0 | M | Fino | 50% |
| ◕ | 7/10 | U+25D5 | M | Fino | 75% |
| • | 8/10 | U+2022 | S | Ninguno | Lleno |
| ● | 9/10 | U+25CF | M | Ninguno | Lleno |
| ⬤ | 10/10 | U+2B24 | L | Ninguno | Lleno |

---

## 11. RECOMENDACIONES SEGÚN USO

### Para Documentación Técnica (Profesional)

**Minimalista:**
```
○ Obsoleto/Legacy
● Bloqueado/Crítico
```

**Con Estado Intermedio:**
```
○ Obsoleto/Legacy
◐ Pendiente/En Progreso
● Bloqueado/Crítico
```

**Con Énfasis en Contorno:**
```
○ Obsoleto (fino)
⭕ Pendiente (grueso, llama atención)
● Bloqueado (lleno)
```

### Para Dashboards (Visual)

**Progreso Claro:**
```
○ 0%
◔ 25%
◐ 50%
◕ 75%
● 100%
```

**Tres Niveles:**
```
○ Bajo
◐ Medio
● Alto
```

---

## 12. RENDERIZADO EN DIFERENTES CONTEXTOS

### En Listas

```markdown
- ○ Item obsoleto
- ◐ Item en progreso
- ● Item crítico
```

### En Tablas

| Estado | Symbol | Descripción |
|--------|--------|-------------|
| Obsolete | ○ | Ya no aplica |
| Pending | ◐ | En proceso |
| Blocked | ● | Requiere atención |

### En Headers

```markdown
## ○ Sección Deprecada
## ◐ Sección En Desarrollo
## ● Sección Crítica
```

---

## 13. COMPATIBILIDAD Y RENDERIZADO

### Alta Compatibilidad (Renderizan en todos lados)

```
○ ● • ·
```

### Buena Compatibilidad (Mayoría de sistemas)

```
◯ ⚪ ⚫ ◐ ◕
```

### Compatibilidad Variable (Depende del sistema)

```
⭕ ⬤ ◎ 🔘
```

---

## 14. MI RECOMENDACIÓN FINAL

### Sistema de 3 Estados (Limpio y Profesional)

```
○ LEGACY/OBSOLETE     (U+25CB - White Circle, fino, vacío)
◐ PENDING/OPTIONAL    (U+25D0 - Half Black, progreso)
● CRITICAL/BLOCKED    (U+25CF - Black Circle, lleno)
```

**Por qué funciona:**
- ✅ Alta compatibilidad en todos los sistemas
- ✅ Clara progresión visual: vacío → medio → lleno
- ✅ Tamaño consistente (todos medianos)
- ✅ Semántica clara sin explicación
- ✅ Profesional y técnico

**Aplicación en el framework:**

| Symbol | Estado | Uso |
|--------|--------|-----|
| ○ | LEGACY/OBSOLETE | Hallazgos que ya no aplican |
| ◐ | PENDING/OPTIONAL | Mejoras pendientes opcionales |
| ● | CRITICAL/BLOCKED | Problemas que requieren atención |

---

## 15. TESTING VISUAL

### Copiar y pegar para ver en tu sistema

```
Básicos:     ○ ● ◯ ⚫ ⚪
Sombreados:  ◔ ◕ ◐ ◑ ◒ ◓
Especiales:  ◎ ⭕ ⬤ ◙ ◘ 🔘
Pequeños:    · • ‣
```

### Prueba de Legibilidad

Texto antes ○ círculo vacío texto después
Texto antes ◐ círculo medio texto después
Texto antes ● círculo lleno texto después

---

## CONCLUSIÓN

El mejor sistema para el framework es el **Sistema de 3 Estados** usando:
- **○** para obsoleto (visualmente "apagado")
- **◐** para pendiente (visualmente "en proceso")
- **●** para crítico (visualmente "activo")

Estos tres símbolos tienen:
- Excelente compatibilidad
- Clara jerarquía visual
- Tamaño consistente
- Semántica intuitiva

---

**Última actualización:** 2026-01-19
**Para uso en:** Agentic Task Framework v2.2
**Estándar de símbolos:** v3.2+ Master
