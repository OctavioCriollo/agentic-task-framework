# Corrección de Estructura de Auditorías

**Fecha:** 2026-01-17
**Sesión:** Clarificación de criterios de clasificación de proyectos
**Estado:** ✅ COMPLETADO

---

## PROBLEMA IDENTIFICADO

El usuario preguntó: **"¿Cómo definimos cuándo un proyecto es auditoría del framework vs investigación de usuario?"**

Se identificó:
1. **Ambigüedad en criterios** - No había reglas claras de decisión
2. **Proyecto mal ubicado** - Reconstrucción de prompts estaba en `projects/` en vez de `archive/audits/`
3. **Documentación incompleta** - `ARQUITECTURA_JERARQUICA_PROYECTO.md` no clarificaba auditorías en progreso
4. **Ejemplos incorrectos** - `CLAUDE.md` no especificaba `base_dir` para auditorías

---

## SOLUCIÓN IMPLEMENTADA

### 1. ✅ Creado Documento de Criterios

**Archivo:** `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md` (19 KB)

**Contenido:**
- **Regla de Oro:** ¿El framework es HERRAMIENTA o OBJETO?
- **4 Criterios objetivos:**
 1. ¿Qué se analiza?
 2. ¿Cuál es el output?
 3. ¿Quién se beneficia?
 4. ¿Qué archivos se leen?
- **Árbol de decisión visual**
- **15+ ejemplos clasificados**
- **Casos ambiguos resueltos**
- **Protocolo operativo paso a paso**

**Resultado:** Criterios objetivos y no ambiguos para clasificar CUALQUIER solicitud.

### 2. ✅ Movido Proyecto Mal Ubicado

**Acción ejecutada:**
```bash
mv projects/auditor-as-enero-2026-retroactivo-20260117-125539 \
 archive/audits/auditor-as-enero-2026-retroactivo-20260117-125539
```

**Razón:**
- Proyecto = Reconstrucción de prompts de auditorías pasadas
- Objeto de análisis = Auditorías del framework (meta-trabajo)
- Según criterios → `archive/audits/`

**Verificación:**
```bash
$ ls -la archive/audits/
auditor-a-framework-v2-2-20251227-222837/ # 27 Dic
auditor-as-enero-2026-retroactivo-20260117-125539/ # 17 Ene ✓
```

### 3. ✅ Actualizado ARQUITECTURA_JERARQUICA_PROYECTO.md

**Archivo modificado:** `docs/ARQUITECTURA_JERARQUICA_PROYECTO.md`

**Cambios:**

**Sección 5 - `archive/`:**

Antes:
```markdown
## 5. DIRECTORIO `archive/` - HISTÓRICOS Y LEGACY

### REGLA:
- Proyectos **completados y archivados** → `archive/`
- Proyectos **activos o recientes** → mantener en `projects/`
```

Después:
```markdown
## 5. DIRECTORIO `archive/` - HISTÓRICOS Y AUDITORÍAS

### REGLA CRÍTICA:

**TODAS las auditorías del framework → `archive/audits/`**

- ✅ Auditorías en progreso
- ✅ Auditorías completadas
- ✅ Validaciones de conformidad
- ✅ Mejoras al framework
- ✅ Reconstrucción de prompts de auditorías

**Investigaciones de usuario → `projects/`**

- ✅ COVID-19, YouTube, ClO₂, etc.
- ❌ NUNCA auditorías del framework

### CÓMO DECIDIR:

**Ver:** `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md` para criterios detallados.

**Regla simple:** ¿Analizo el framework o CON el framework?
- Analizo EL framework → `archive/audits/`
- Analizo CON el framework → `projects/`
```

**Resultado:** Clarificado que auditorías EN PROGRESO también van a `archive/audits/`.

### 4. ✅ Actualizado CLAUDE.md

**Archivo modificado:** `CLAUDE.md`

**Cambios en sección "Always Use ProjectManager for Audits":**

Agregado:
```python
# CRÍTICO: Auditorías del framework van a archive/audits/
pm = ProjectManager(base_dir="archive/audits")
```

**Ejemplos agregados:**

1. **Example (CORRECT) - Auditoría del Framework:**
 - Usa `base_dir="archive/audits"`
 - Crea proyecto de auditoría en ubicación correcta

2. **Example (CORRECT) - Investigación de Usuario:**
 - Usa `ProjectManager()` (default = "projects")
 - Crea investigación en ubicación correcta

3. **Example (WRONG):**
 - Muestra error común: auditoría en `projects/`

**Agregado al final:**
```markdown
**Cómo decidir base_dir:**

Consultar: `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md`

- **Auditoría/mejora del framework** → `base_dir="archive/audits"`
- **Investigación de usuario** → `base_dir="projects"` (default)
```

**Resultado:** Ejemplos claros de código mostrando ubicación correcta.

### 5. ✅ Actualizado Script de Reconstrucción

**Archivo modificado:** `scripts/reconstruir_prompts_auditorias_enero.py`

**Cambio línea 26:**

Antes:
```python
pm = ProjectManager() # Crea en projects/ ❌
```

Después:
```python
# CRÍTICO: Auditorías del framework van a archive/audits/
pm = ProjectManager(base_dir="archive/audits") # ✓
```

**Resultado:** Futuras ejecuciones crearán proyectos en ubicación correcta.

---

## ESTADO FINAL

### Estructura Correcta

```
archive/audits/
├── auditor-a-framework-v2-2-20251227-222837/ # Multi-agente (27 Dic)
└── auditor-as-enero-2026-retroactivo-20260117-125539/ # Reconstrucción (17 Ene) ✓

projects/
├── investigaci-n-clo-covid-19-20251222-195407/ # Investigación usuario
├── youtube-skip-ads-extension-20260113-200039/ # Investigación usuario
└── (NO contiene auditorías del framework) ✓
```

### Documentación Actualizada

1. ✅ `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md` - Criterios objetivos creados
2. ✅ `docs/ARQUITECTURA_JERARQUICA_PROYECTO.md` - Sección archive/ clarificada
3. ✅ `CLAUDE.md` - Ejemplos de código corregidos
4. ✅ `scripts/reconstruir_prompts_auditorias_enero.py` - base_dir corregido

### Archivos de Proyecto Movidos

1. ✅ `archive/audits/auditor-as-enero-2026-retroactivo-20260117-125539/` - Ubicación correcta

---

## CRITERIOS FINALES DOCUMENTADOS

### Regla de Oro

> "Si analizas EL FRAMEWORK → `archive/audits/`
> Si analizas CON EL FRAMEWORK → `projects/`"

### Criterios Objetivos

**`archive/audits/` cuando:**
- Se analiza código del framework (`core/`, `scripts/`, `tests/`)
- Se analiza documentación del framework (`docs/`, `CLAUDE.md`)
- Se valida conformidad estructural (v2.2 ORGANIZED)
- Output son mejoras/correcciones al framework
- Beneficiario es el framework mismo

**`projects/` cuando:**
- Se investiga tema científico (COVID, ClO₂, virología)
- Se analiza tecnología externa (APIs, extensiones)
- Se usan papers, web, datos externos
- Output es conocimiento sobre tema externo
- Beneficiario es el usuario con información

### Árbol de Decisión

```
¿Analizo el framework mismo?
 ->
 SÍ → archive/audits/
 NO → ¿Investigo tema externo?
 ->
 SÍ → projects/
```

---

## PRÓXIMOS PASOS

### Validación

```bash
# Verificar estructura correcta
ls -la archive/audits/
ls -la projects/ | grep -v "investigaci\|youtube"

# Validar criterios están claros
cat docs/CRITERIOS_CLASIFICACION_PROYECTOS.md
```

### Uso Futuro

**Cuando el usuario solicita tarea:**

1. **Identificar:** ¿Analizo el framework o CON el framework?
2. **Consultar:** `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md` si hay duda
3. **Crear proyecto:**
 ```python
 # Auditoría del framework
 pm = ProjectManager(base_dir="archive/audits")

 # Investigación de usuario
 pm = ProjectManager() # default = "projects"
 ```
4. **Validar:** Proyecto está en ubicación correcta

---

## CONCLUSIÓN

**Problema resuelto:** ✅ Criterios objetivos establecidos y documentados

**Correcciones aplicadas:** ✅ 5/5 completadas
1. Criterios documentados
2. Proyecto movido
3. Arquitectura actualizada
4. CLAUDE.md corregido
5. Script actualizado

**Estado:** Framework tiene criterios claros y no ambiguos para clasificación de proyectos.

**Documentación:** Completa y consistente entre `docs/`, `CLAUDE.md`, y código.

---

**Correcciones aplicadas:** 2026-01-17
**Por:** Coordinador Claude
**Validado:** ✅
**Estado:** COMPLETADO
