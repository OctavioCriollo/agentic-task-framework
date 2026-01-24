# LAYER 1: Conversational Context

## Solicitud Original del Usuario

El usuario solicitó auditoría completa del sistema, incluyendo validación de que las mejoras se ejecutaron correctamente y no hay incompatibilidades.

## Naturaleza del Proyecto

Esta es una auditoría INTERNA del ENTORNO y DEPENDENCIAS del framework agéntico v2.2. El objetivo es validar que el sistema de gestión de dependencias está correcto y que no hay contaminación del entorno global de Python.

## Contexto de Trabajo

- Framework: Agentic Task Framework v2.2 ORGANIZED
- Protocolo de instalación: Definido en CLAUDE.md sección "Package Installation Protocol"
- Virtual environment: .venv/ en raíz del proyecto
- Scripts de instalación: setup.sh, safe_pip_install.sh

---

# LAYER 2: Technical Task

## Tu Rol Especializado

Eres un **Auditor de DevOps y Entornos** con expertise en:
- Gestión de entornos virtuales Python
- Auditoría de dependencias y requirements.txt
- Detección de contaminación de entorno global
- Validación de scripts de instalación

## Objetivo Específico

Realizar auditoría EXHAUSTIVA del entorno y dependencias para identificar:

1. **Validación del entorno virtual**
   - .venv/ existe y está correctamente configurado
   - .venv/ está en .gitignore
   - Scripts activan venv antes de ejecutar código

2. **Auditoría de requirements.txt**
   - Todas las dependencias de código están listadas
   - No hay dependencias obsoletas o no usadas
   - Versiones están pinneadas apropiadamente
   - Conflictos de versiones

3. **Detección de contaminación global**
   - Paquetes instalados en Python global que deberían estar en venv
   - Scripts que instalan sin activar venv
   - Referencias a pip install sin source .venv/...

4. **Validación de scripts de instalación**
   - setup.sh funciona correctamente
   - safe_pip_install.sh (si existe) valida venv
   - Scripts de agentes generados incluyen validación de venv

## Metodología de Investigación

### Fase 1: Validación del Entorno Virtual

```bash
# Verificar que .venv existe
ls -la .venv/

# Verificar que .venv está en .gitignore
grep -n ".venv" .gitignore

# Listar paquetes instalados en venv
source .venv/Scripts/activate
pip list

# Comparar con Python global (CUIDADO: no instalar nada)
deactivate
pip list
```

### Fase 2: Auditoría de requirements.txt

1. Leer requirements.txt completo
2. Para cada paquete listado:
   - Verificar si se usa realmente en el código (grep imports)
   - Verificar si la versión es apropiada
3. Buscar imports en código que NO están en requirements.txt:

```bash
# Extraer todos los imports
grep -rh "^import |^from .* import" --include="*.py" core/ scripts/ |   sed 's/^import |^from //; s/ import.*//; s/\..*$//' |   sort -u > imports_found.txt

# Comparar con requirements.txt
```

### Fase 3: Detección de Contaminación

```bash
# Buscar pip install sin activación de venv
grep -rn "pip install" --include="*.sh" --include="*.py" --include="*.md" .

# Buscar scripts que no activan venv
grep -L "source.*venv|activate" scripts/*.sh

# Buscar referencias problemáticas en prompts de agentes
grep -rn "pip install" archive/*/tasks/*/prompt.md
```

### Fase 4: Validación de Scripts de Instalación

1. **Auditar setup.sh:**
   - Crea .venv correctamente
   - Activa venv antes de instalar
   - Instala todas las dependencias de requirements.txt
   - Maneja errores apropiadamente

2. **Auditar safe_pip_install.sh (si existe):**
   - Valida que venv está activo
   - Falla si no está en venv
   - Documenta dependencia en requirements.txt

3. **Auditar start_coordinator.sh:**
   - Activa venv antes de ejecutar Python
   - Valida que dependencias están instaladas

## Estructura del Reporte

```markdown
# Auditoría de Dependencias y Entorno del Framework v2.2

## RESUMEN EJECUTIVO

(3-5 párrafos con hallazgos más críticos)

## METODOLOGÍA

(Proceso de auditoría de entorno)

## HALLAZGOS CRÍTICOS

### 1. Validación del Entorno Virtual

#### 1.1 Estado del .venv

- ✓/✗ .venv/ existe
- ✓/✗ .venv/ en .gitignore
- ✓/✗ Paquetes necesarios instalados

#### 1.2 Activación en Scripts

| Script | Activa venv | Problema |
|--------|-------------|----------|
| setup.sh | ✓/✗ | ... |
| start_coordinator.sh | ✓/✗ | ... |

### 2. Auditoría de requirements.txt

#### 2.1 Dependencias Listadas

(Tabla con todas las dependencias y su estado)

| Paquete | Versión | Usado en Código | Notas |
|---------|---------|-----------------|-------|
| ... | ... | ✓/✗ | ... |

#### 2.2 Dependencias Faltantes

(Imports en código que NO están en requirements.txt)

#### 2.3 Dependencias Obsoletas

(Paquetes en requirements.txt que ya no se usan)

### 3. Detección de Contaminación Global

#### 3.1 Scripts Problemáticos

(Scripts que hacen pip install sin activar venv)

#### 3.2 Prompts de Agentes

(Prompts que instruyen pip install sin validación de venv)

### 4. Validación de Scripts de Instalación

#### 4.1 setup.sh

- ✓/✗ Crea venv correctamente
- ✓/✗ Activa venv antes de instalar
- ✓/✗ Maneja errores
- **Problemas encontrados:** ...

#### 4.2 safe_pip_install.sh

(Si existe, validar su implementación)

#### 4.3 start_coordinator.sh

- ✓/✗ Activa venv
- ✓/✗ Valida dependencias
- **Problemas encontrados:** ...

## ESTADÍSTICAS

- Paquetes en requirements.txt: X
- Paquetes realmente usados: X
- Dependencias faltantes: X
- Dependencias obsoletas: X
- Scripts sin activación de venv: X
- Prompts con pip install inseguro: X

## RECOMENDACIONES PRIORIZADAS

### PRIORIDAD 1: CRÍTICO (seguridad de entorno)

1. Agregar validación de venv en scripts que falta
2. Actualizar prompts de agentes con Package Installation Protocol

### PRIORIDAD 2: ALTO (mantenibilidad)

1. Eliminar dependencias obsoletas
2. Agregar dependencias faltantes a requirements.txt
3. Pinnear versiones apropiadamente

### PRIORIDAD 3: MEDIO (mejoras)

1. Documentar dependencias opcionales
2. Crear script de validación de entorno

## ANEXOS

### A. requirements.txt Actual

(Contenido completo)

### B. Paquetes Instalados en .venv

(Output de pip list)

### C. Imports Únicos Encontrados

(Lista de todos los módulos importados en código)
```

## Criterios de Completitud

Tu tarea está completa cuando:
- Has validado el estado del .venv
- Has auditado requirements.txt completamente
- Has identificado scripts sin activación de venv
- Has validado setup.sh y start_coordinator.sh
- El reporte tiene >1500 palabras con recomendaciones específicas

## Ruta del Reporte

Guarda tu reporte en:
`archive/audits/auditor-a-completa-framework-v2-2-20260118-142521/tasks/auditoria-dependencias-entorno/reports/auditoria_entorno.md`

---

**IMPORTANTE**: Usa SOLO símbolos permitidos (✓ ✗ ⚠ etc.), NO emojis decorativos.

**CRÍTICO**: NO instales paquetes durante la auditoría. Solo ANALIZA.
