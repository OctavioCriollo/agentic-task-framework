# Estándares para Listas y Checklists

**Version:** 1.0
**Fecha:** 2026-01-20
**Framework:** Agentic Task Framework v2.2

---

## 1. Guía de Selección: Árbol de Decisión

```
¿Necesitas listar items?
│
├─ ¿Importa el orden/secuencia?
│  ├─ SÍ → Lista Numerada
│  └─ NO → Continuar...
│
├─ ¿Necesitas rastrear estado/progreso?
│  ├─ SÍ → ¿Es interactivo (GitHub/issues)?
│  │  ├─ SÍ → Checklist Interactiva (- [ ])
│  │  └─ NO → Lista con Símbolos de Estado
│  └─ NO → Continuar...
│
├─ ¿Necesitas indicar prioridad?
│  ├─ SÍ → Lista con Prioridad (☆ o texto)
│  └─ NO → Lista Simple (bullets)
```

**Resumen rápido:**

| Caso de Uso | Tipo de Lista | Símbolo |
|-------------|---------------|---------|
| Items sin orden especial | Simple | - o • |
| Procedimiento paso a paso | Numerada | 1. 2. 3. |
| Rastrear progreso (docs) | Con Estado | ✅ ❌ 🟡 etc. |
| Tareas interactivas (GitHub) | Checklist | - [ ] - [x] |
| Roadmap con prioridad | Con Prioridad | ☆★ o HIGH/MED/LOW |
| Opciones mutuamente excluyentes | Radio | ⚪ ⚫ 🔘 |

---

## 2. Listas Simples (Bullets)

### Cuándo Usar

- Items sin orden jerárquico o secuencial
- Características, capacidades, propiedades
- Puntos de discusión equivalentes
- Listados de archivos, componentes, herramientas

### Formato Estándar

**USAR:**
```markdown
- Item uno
- Item dos
- Item tres
```

**ALTERNATIVA (bullets Unicode):**
```markdown
• Item uno
• Item dos
• Item tres
```

**REGLA:** Elegir UN estilo y mantenerlo consistente en el documento completo.

### Anidación

**Máximo 3 niveles:**
```markdown
- Nivel 1
  - Nivel 2
    - Nivel 3
```

**PROHIBIDO:**
```markdown
- Nivel 1
  - Nivel 2
    - Nivel 3
      - Nivel 4 ❌ DEMASIADO PROFUNDO
```

### Cuándo NO Usar

❌ No usar bullets si:
- El orden importa (usar numerada)
- Necesitas rastrear estado (usar con símbolos)
- Son pasos de un procedimiento (usar numerada)

---

## 3. Listas Numeradas

### Cuándo Usar

- Procedimientos paso a paso
- Instrucciones secuenciales
- Rankings o jerarquías ordenadas
- Referencias cruzadas ("ver paso 3")
- Cronología de eventos

### Formato Estándar

```markdown
1. Primer paso
2. Segundo paso
3. Tercer paso
```

**AUTOMÁTICO (recomendado para documentos largos):**
```markdown
1. Primer paso
1. Segundo paso (Markdown auto-incrementa)
1. Tercer paso
```

### Anidación con Bullets

**PERMITIDO (max 2 niveles):**
```markdown
1. Paso principal
   - Detalle A
   - Detalle B
2. Siguiente paso
   - Detalle C
```

**PROHIBIDO (mezclar numeradas anidadas):**
```markdown
1. Paso principal
   1. Sub-paso ❌ CONFUSO
   2. Otro sub-paso ❌
```

**ALTERNATIVA CLARA:**
```markdown
1. Paso principal
   a. Sub-paso (usar letras)
   b. Otro sub-paso
```

### Cuándo NO Usar

❌ No usar numeradas si:
- El orden no importa (usar bullets)
- Los items pueden reordenarse sin problema
- Solo necesitas agrupar conceptos relacionados

---

## 4. Listas con Símbolos de Estado

### Cuándo Usar

- Reportes de progreso
- Dashboards de tareas
- Resultados de validación
- Status de componentes/servicios
- Logs de auditoría

### Símbolos Permitidos (según CLAUDE.md v3.1)

**Checkmarks/X-marks:**
- ✅ Completado, exitoso, validado
- ❌ Fallido, error, rechazado
- ✓ Validado (versión simple)
- ✗ Invalidado (versión simple)

**Status circles (sistema de 4 colores):**
- 🟢 Completado, activo, éxito
- 🟡 En progreso, pendiente, advertencia
- 🔴 Error, bloqueado, fallido
- 🟠 Atención necesaria, parcialmente completado

**Warning/Attention:**
- ⚠️ Advertencia crítica

**Priority:**
- ⚡ Alta prioridad
- ☆ Baja prioridad
- ★ Alta prioridad (filled)

**Selection:**
- ⚪ No seleccionado
- ⚫ Seleccionado
- 🔘 Radio button

### Formato Estándar

**POSICIÓN:** Símbolo al INICIO de la línea:

```markdown
✅ Tarea completada
🟡 Tarea en progreso
❌ Tarea fallida
```

**CON PREFIJO TEXTUAL (más claro):**
```markdown
✅ COMPLETADO: Análisis de código
🟡 EN_PROGRESO: Refactorización módulo X
❌ ERROR: Tests fallando en CI/CD
```

### Consistencia de Símbolos

**REGLA ABSOLUTA:** Dentro de un mismo contexto, usar UN SOLO estilo de símbolo.

**CORRECTO (consistente):**
```markdown
### Estado de Tareas

✅ Tarea A completada
✅ Tarea B completada
❌ Tarea C fallida
🟡 Tarea D en progreso
```

**INCORRECTO (inconsistente):**
```markdown
### Estado de Tareas

✅ Tarea A completada
✓ Tarea B completada ❌ INCONSISTENTE
☑ Tarea C completada ❌ INCONSISTENTE
DONE: Tarea D ❌ MEZCLA ESTILOS
```

### Cuándo NO Usar

❌ No usar símbolos de estado si:
- Los items no tienen estado (usar bullets simples)
- Es contenido decorativo (símbolos deben ser funcionales)
- El documento será parseado automáticamente (preferir texto plano)

---

## 5. Checklists Interactivas

### Cuándo Usar

- Issues de GitHub
- Pull requests
- Task tracking en Markdown compatible
- Planes de ejecución que el usuario marcará

### Formato GitHub

**SINTAXIS:**
```markdown
- [ ] Tarea pendiente
- [x] Tarea completada
- [ ] Otra tarea pendiente
```

**RENDERIZADO (GitHub/compatible):**
- [ ] Tarea pendiente (checkbox vacío)
- [x] Tarea completada (checkbox marcado)
- [ ] Otra tarea pendiente

### Con Anidación

```markdown
- [ ] Fase principal
  - [x] Sub-tarea 1 completada
  - [ ] Sub-tarea 2 pendiente
  - [ ] Sub-tarea 3 pendiente
- [ ] Siguiente fase
```

### Texto Descriptivo

**FORMATO RECOMENDADO:**
```markdown
- [ ] **Setup inicial**
  - [ ] Crear virtual environment
  - [ ] Instalar dependencias
  - [ ] Configurar variables de entorno
- [ ] **Desarrollo**
  - [x] Implementar módulo core
  - [ ] Agregar tests unitarios
  - [ ] Documentar API
```

### Cuándo NO Usar

❌ No usar checklists interactivas si:
- El documento es estático (usar símbolos de estado)
- No hay interacción del usuario
- El tracking es solo visual (usar ✅ ❌)

---

## 6. Listas con Prioridad

### Cuándo Usar

- Roadmaps de desarrollo
- Backlog de tareas priorizado
- Clasificación de issues/bugs
- Matriz de decisiones

### Símbolos de Prioridad

**Estrellas (ratings):**
- ★★★ Alta prioridad
- ★★☆ Media prioridad
- ★☆☆ Baja prioridad

**Texto explícito (RECOMENDADO):**
```markdown
- HIGH: Funcionalidad crítica
- MEDIUM: Mejora importante
- LOW: Nice to have
```

**Círculos de color:**
```markdown
🔴 CRÍTICO: Seguridad comprometida
🟠 URGENTE: Bug en producción
🟡 IMPORTANTE: Feature bloqueada
🟢 NORMAL: Mejora general
```

### Formato Estándar

**OPCIÓN A (símbolos + texto):**
```markdown
### Roadmap Q1 2026

⚡ HIGH: Implementar autenticación OAuth
★★ MEDIUM: Optimizar rendimiento DB
☆ LOW: Actualizar UI componentes
```

**OPCIÓN B (solo texto, más claro):**
```markdown
### Roadmap Q1 2026

- PRIORITY_1: Implementar autenticación OAuth
- PRIORITY_2: Optimizar rendimiento DB
- PRIORITY_3: Actualizar UI componentes
```

### Combinación con Estado

**PERMITIDO:**
```markdown
- ⚡ HIGH: Implementar autenticación OAuth 🟡 EN_PROGRESO
- ★★ MEDIUM: Optimizar rendimiento DB ✅ COMPLETADO
- ☆ LOW: Actualizar UI componentes ⚪ PENDIENTE
```

**ALTERNATIVA MÁS CLARA (tabla):**

| Prioridad | Tarea | Estado |
|-----------|-------|--------|
| ⚡ HIGH | Implementar autenticación OAuth | 🟡 EN_PROGRESO |
| ★★ MEDIUM | Optimizar rendimiento DB | ✅ COMPLETADO |
| ☆ LOW | Actualizar UI componentes | ⚪ PENDIENTE |

---

## 7. Jerarquía y Anidación

### Reglas Generales

**MÁXIMO 3 NIVELES:**
```markdown
- Nivel 1
  - Nivel 2
    - Nivel 3 (MÁXIMO)
```

**INDENTACIÓN:** 2 espacios por nivel (consistente con markdown estándar).

### Mezclar Tipos

**PERMITIDO:**
```markdown
1. Paso principal (numerada)
   - Detalle A (bullet)
   - Detalle B (bullet)
2. Siguiente paso
   - Detalle C
```

**PERMITIDO:**
```markdown
- Categoría principal (bullet)
  1. Elemento secuencial
  2. Otro elemento secuencial
- Otra categoría
```

**PROHIBIDO (confuso):**
```markdown
1. Paso principal
   1. Sub-paso ❌ USAR LETRAS O BULLETS
   2. Otro sub-paso
```

### Símbolos en Sub-items

**CONSISTENCIA VERTICAL:**

```markdown
✅ Módulo A completado
  ✅ Componente A1
  ✅ Componente A2
❌ Módulo B fallido
  ✅ Componente B1
  ❌ Componente B2 (causa del fallo)
```

**REGLA:** Los sub-items heredan el tipo de símbolo del padre, o no usan símbolos.

**INCORRECTO (inconsistente):**
```markdown
✅ Módulo A completado
  - Componente A1 ❌ SÍMBOLO DIFERENTE
  ✓ Componente A2 ❌ SÍMBOLO INCONSISTENTE
```

---

## 8. Consistencia de Símbolos: Tabla de Uso Correcto

### Símbolos de Completitud

| Símbolo | Significado | Contexto de Uso |
|---------|-------------|-----------------|
| ✅ | Completado (con caja verde) | Reports, dashboards, status general |
| ✓ | Validado (simple) | Checklists, validaciones rápidas |
| ❌ | Error (con X roja) | Fallos, errores, rechazos |
| ✗ | Invalidado (simple) | Checks fallidos |

**REGLA:** Elegir UN símbolo para "completado" por documento:
- ✅ o ✓ (NO mezclar)
- ❌ o ✗ (NO mezclar)

### Símbolos de Estado

| Símbolo | Significado | Uso |
|---------|-------------|-----|
| 🟢 | Activo, completado, éxito | Estado actual positivo |
| 🟡 | En progreso, pendiente, advertencia | Estado transitorio |
| 🔴 | Error, bloqueado, fallido | Estado crítico negativo |
| 🟠 | Atención necesaria, parcial | Estado intermedio |

**REGLA:** Usar el sistema de 4 colores COMPLETO o NO usarlo. No mezclar con otros símbolos de estado.

### Símbolos de Selección

| Símbolo | Significado | Uso |
|---------|-------------|-----|
| ⚪ | No seleccionado | Opciones, radio buttons |
| ⚫ | Seleccionado | Opción activa |
| 🔘 | Radio button | Alternativas mutuamente excluyentes |

### Símbolos de Prioridad

| Símbolo | Significado | Uso |
|---------|-------------|-----|
| ⚡ | Prioridad crítica | Tareas urgentes |
| ★★★ | Alta prioridad | Roadmaps, clasificaciones |
| ★★☆ | Media prioridad | Roadmaps |
| ★☆☆ | Baja prioridad | Roadmaps |

**ALTERNATIVA TEXTO (más profesional):**
- HIGH, MEDIUM, LOW
- P1, P2, P3
- CRITICAL, IMPORTANT, NORMAL

---

## 9. Ejemplos por Caso de Uso

### Caso 1: Reporte de Auditoría

**CORRECTO:**
```markdown
### Resultados de Auditoría

✅ COMPLETADO: Análisis de código core/
✅ COMPLETADO: Revisión de dependencias
🟡 EN_PROGRESO: Tests de integración
❌ ERROR: Documentación incompleta

**Detalles:**

- **Análisis de código:**
  ✅ Sin errores de sintaxis
  ✅ PEP 8 compliance
  ⚠️ WARNING: 3 funciones con complejidad alta

- **Dependencias:**
  ✅ Todas instaladas correctamente
  ✅ Sin vulnerabilidades conocidas
```

### Caso 2: Procedimiento de Setup

**CORRECTO:**
```markdown
### Setup del Proyecto

1. Clonar repositorio
   ```bash
   git clone <repo-url>
   ```

2. Crear virtual environment
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```

3. Instalar dependencias
   - Ejecutar: `pip install -r requirements.txt`
   - Verificar: `pip list`

4. Configurar variables de entorno
   a. Copiar `.env.example` a `.env`
   b. Editar valores según entorno
   c. Validar con `python check_config.py`

5. Ejecutar tests iniciales
   ```bash
   pytest tests/
   ```
```

### Caso 3: GitHub Issue con Checklist

**CORRECTO:**
```markdown
### Implementation Plan: OAuth Integration

**Objetivo:** Agregar autenticación OAuth2 para GitHub y Google.

**Checklist:**

- [ ] **Research & Design**
  - [x] Investigar librerías OAuth2 para Python
  - [x] Diseñar flujo de autenticación
  - [ ] Documentar endpoints necesarios

- [ ] **Backend Implementation**
  - [ ] Instalar `authlib` en venv
  - [ ] Implementar rutas OAuth
  - [ ] Agregar modelos de usuario
  - [ ] Escribir tests unitarios

- [ ] **Frontend Integration**
  - [ ] Agregar botones de login
  - [ ] Manejar callbacks
  - [ ] Gestionar tokens en localStorage

- [ ] **Testing & Deployment**
  - [ ] Tests end-to-end
  - [ ] Actualizar documentación
  - [ ] Deploy a staging
  - [ ] Validación en producción
```

### Caso 4: Roadmap con Prioridades

**CORRECTO:**
```markdown
### Product Roadmap Q1 2026

**Alta Prioridad (⚡):**
- ⚡ Implementar autenticación multi-factor
- ⚡ Optimizar queries de base de datos (bottleneck actual)
- ⚡ Migrar a Python 3.12

**Media Prioridad (★★):**
- ★★ Agregar export a PDF
- ★★ Mejorar UI de dashboard
- ★★ Implementar caché con Redis

**Baja Prioridad (★):**
- ★ Refactorizar módulo legacy de reportes
- ★ Agregar tema oscuro
- ★ Internacionalización (i18n)
```

**ALTERNATIVA (tabla más clara):**

```markdown
### Product Roadmap Q1 2026

| Prioridad | Feature | Estado | Asignado |
|-----------|---------|--------|----------|
| ⚡ HIGH | Autenticación multi-factor | 🟡 EN_PROGRESO | @dev-team |
| ⚡ HIGH | Optimizar DB queries | ⚪ PENDIENTE | @backend-team |
| ★★ MEDIUM | Export a PDF | ✅ COMPLETADO | @frontend-team |
| ★ LOW | Tema oscuro | ⚪ PENDIENTE | @ui-team |
```

### Caso 5: Comparación de Opciones

**CORRECTO:**
```markdown
### Comparación de Frameworks

**Opción A: Django**
- ✅ Ventajas:
  - ORM robusto incluido
  - Admin panel automático
  - Gran comunidad
- ❌ Desventajas:
  - Más pesado para APIs simples
  - Curva de aprendizaje alta

**Opción B: FastAPI**
- ✅ Ventajas:
  - Alto rendimiento (async)
  - Documentación automática (OpenAPI)
  - Tipado moderno (Pydantic)
- ❌ Desventajas:
  - Sin admin panel built-in
  - Menos maduro que Django

**Decisión:** 🔘 FastAPI seleccionado por performance y modernidad.
```

---

## 10. Anti-Patrones: Inconsistencias a Evitar

### Anti-Patrón 1: Mezcla de Símbolos de Completitud

**INCORRECTO:**
```markdown
✅ Tarea A completada
✓ Tarea B completada ❌ INCONSISTENTE
☑ Tarea C completada ❌ SÍMBOLO DIFERENTE
DONE: Tarea D ❌ CAMBIA A TEXTO
```

**CORRECTO:**
```markdown
✅ Tarea A completada
✅ Tarea B completada
✅ Tarea C completada
✅ Tarea D completada
```

### Anti-Patrón 2: Símbolos Redundantes

**INCORRECTO:**
```markdown
✅ COMPLETADO: Tarea A ✅ ❌ REDUNDANTE
🟢 SUCCESS: Deploy exitoso ✅ ❌ MEZCLA ESTILOS
```

**CORRECTO:**
```markdown
✅ COMPLETADO: Tarea A
✅ SUCCESS: Deploy exitoso
```

O alternativamente:
```markdown
🟢 Tarea A completada
🟢 Deploy exitoso
```

### Anti-Patrón 3: Símbolos Decorativos (PROHIBIDO)

**INCORRECTO:**
```markdown
🚀 Lanzamiento del proyecto ❌ PICTOGRÁFICO
📊 Análisis de datos ❌ DECORATIVO
💻 Desarrollo de backend ❌ NO FUNCIONAL
```

**CORRECTO:**
```markdown
LANZAMIENTO: Proyecto en producción
ANÁLISIS: Procesamiento de datos
DESARROLLO: Backend API implementado
```

O con símbolos funcionales:
```markdown
✅ LANZAMIENTO: Proyecto en producción
🟡 ANÁLISIS: Procesamiento de datos en curso
🟢 DESARROLLO: Backend API activo
```

### Anti-Patrón 4: Anidación Excesiva

**INCORRECTO:**
```markdown
- Nivel 1
  - Nivel 2
    - Nivel 3
      - Nivel 4 ❌ DEMASIADO PROFUNDO
        - Nivel 5 ❌ ILEGIBLE
```

**CORRECTO (refactorizar):**
```markdown
### Categoría Principal

**Subcategoría A:**
- Item 1
- Item 2

**Subcategoría B:**
- Item 3
- Item 4
```

### Anti-Patrón 5: Mezcla de Bullets y Numeradas sin Lógica

**INCORRECTO:**
```markdown
- Paso 1 ❌ DEBERÍA SER NUMERADA
- Paso 2
1. Item aleatorio ❌ INCONSISTENTE
- Paso 3
```

**CORRECTO:**
```markdown
1. Paso 1
2. Paso 2
3. Paso 3
```

O si no hay orden:
```markdown
- Item A
- Item B
- Item C
```

### Anti-Patrón 6: Símbolos sin Significado Claro

**INCORRECTO:**
```markdown
🔵 Tarea X ❌ ¿QUÉ SIGNIFICA AZUL?
🟣 Tarea Y ❌ ¿Y PÚRPURA?
⭕ Tarea Z ❌ AMBIGUO
```

**CORRECTO:**
```markdown
🟢 COMPLETADO: Tarea X
🟡 EN_PROGRESO: Tarea Y
🔴 BLOQUEADO: Tarea Z
```

### Anti-Patrón 7: Formato Inconsistente de Checklists

**INCORRECTO:**
```markdown
- [x] Tarea 1
- [ ] Tarea 2
☑ Tarea 3 ❌ SÍMBOLO DIFERENTE
✅ Tarea 4 ❌ NO ES CHECKLIST INTERACTIVA
```

**CORRECTO:**
```markdown
- [x] Tarea 1
- [ ] Tarea 2
- [x] Tarea 3
- [ ] Tarea 4
```

---

## Resumen: Checklist de Validación

Antes de finalizar un documento, verificar:

- [ ] **Tipo de lista apropiado** para cada contexto
- [ ] **Símbolos consistentes** dentro del mismo contexto
- [ ] **Máximo 3 niveles** de anidación
- [ ] **Sin símbolos pictográficos** decorativos (🚀 📊 💻)
- [ ] **Símbolos funcionales** alineados con CLAUDE.md v3.1
- [ ] **Formato correcto** de checklists interactivas (- [ ])
- [ ] **Texto explícito** cuando símbolos puedan ser ambiguos
- [ ] **Jerarquía clara** sin mezclas confusas
- [ ] **Indentación consistente** (2 espacios)
- [ ] **Alternativas en texto plano** disponibles para parseo automático

---

## Herramientas de Validación

**Scripts disponibles:**
```bash
# Verificar símbolos prohibidos
python scripts/verificar_simbolos_no_permitidos.py <archivo>

# Limpiar emojis decorativos
python scripts/limpiar_emojis.py <archivo>

# Auditar uso de símbolos
python scripts/encontrar_simbolos.py <directorio>
```

**Checklist manual:** Ver `docs/CHECKLIST.md` para validación estructural.

---

**FIN DEL REPORTE**
