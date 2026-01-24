# TAREA: PLAN DE CORRECCION

## TU ROL

Eres un Solution Architect especializado en diseño de planes de corrección. Tu trabajo es tomar hallazgos de auditorías y diseñar un plan ejecutable, priorizado y detallado de correcciones.

## OBJETIVO

Generar plan detallado de correcciones para lograr un baseline limpio del framework v2.2, listo para migración a Forge v1.0.

## CONTEXTO REQUERIDO

LEE primero estos documentos para entender el estado deseado:

1. **ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md** - Estado objetivo
2. **README.md** - Funcionalidad esperada
3. **CLAUDE.md** - Comportamiento esperado del coordinador

## INSUMOS

Lee los 4 reportes previos:

1. **../auditoria-documentacion/reports/analisis_documentacion_core.md**
2. **../auditoria-codigo/reports/analisis_codigo_python.md**
3. **../auditoria-estructura/reports/validacion_proyecto_covid.md**
4. **../identificacion-inconsistencias/reports/matriz_inconsistencias.md**

Estos reportes contienen todos los problemas identificados.

## ESTRUCTURA DE OUTPUT

Reporte en: reports/plan_correcciones_detallado.md

```markdown
# PLAN DE CORRECCION - FRAMEWORK v2.2 BASELINE

## OBJETIVO

Corregir todas las inconsistencias identificadas para tener un baseline limpio y consistente del framework v2.2 antes de migrar a Forge v1.0.

## CRITERIOS DE EXITO

Al completar este plan, el framework debe:
- Todas las tareas del proyecto COVID cumplen v2.2 ORGANIZED
- 0 inconsistencias entre documentación y código
- 0 referencias rotas en documentación
- 0 código deprecated no marcado
- framework_validator.py pasa 100% en proyecto COVID
- Documentación refleja implementación actual

## CORRECCIONES PRIORIZADAS

### FASE 1: CRITICAS (Blocking - Deben hacerse primero)

#### Corrección C1: [Título]

**Problema**: [Descripción del problema]
**Impacto**: [Por qué es crítico]
**Fuente**: [De qué reporte viene]

**Pasos de corrección**:
1. [Paso específico 1]
2. [Paso específico 2]
3. [Paso específico 3]

**Archivos a modificar**:
- [archivo1.md]: [qué cambiar]
- [archivo2.py]: [qué cambiar]

**Comandos a ejecutar**:
```bash
# Si hay comandos específicos
python core/script.py --arg valor
```

**Scripts de migración** (si aplica):
```python
# Script específico para esta corrección
# Guardar como core/fix_c1.py
...código...
```

**Validación**:
- [ ] Verificar que [condición]
- [ ] Ejecutar [comando de validación]
- [ ] Confirmar que [resultado esperado]

**Estimación**: Simple / Moderada / Compleja
**Tiempo estimado**: X minutos/horas

---

[Repetir para cada corrección crítica]

### FASE 2: ALTAS (Important - Hacerse después de críticas)

[Similar estructura para correcciones de prioridad alta]

### FASE 3: MEDIAS (Nice to have - Mejoras de calidad)

[Similar estructura para correcciones de prioridad media]

### FASE 4: BAJAS (Optional - Mejoras cosméticas)

[Similar estructura para correcciones de prioridad baja]

## DEPENDENCIAS ENTRE CORRECCIONES

```
C1 (Crear README.md automático)
 ->
C2 (Regenerar proyecto COVID)
 ->
C3 (Validar estructura completa)

A1 (Actualizar versiones docs) puede ejecutarse en paralelo
A2 (Remover código deprecated) puede ejecutarse en paralelo
```

**Orden de ejecución recomendado**:
1. FASE 1 (Críticas): Secuencial según dependencias
2. FASE 2 (Altas): Algunas en paralelo
3. FASE 3 (Medias): En paralelo
4. FASE 4 (Bajas): Opcional, en paralelo

## SCRIPTS DE MIGRACION

### Script 1: fix_project_structure_complete.py

**Propósito**: Crear todos los archivos faltantes en proyecto COVID

```python
#!/usr/bin/env python3
"""
Crea archivos faltantes para cumplir v2.2 ORGANIZED
"""
import json
from pathlib import Path

def fix_task_structure(project_id, task_name):
 \"\"\"
 Crea task_info.json, README.md, y reports/ si faltan
 \"\"\"
 # Código específico aquí
 pass

# Uso
for task in tasks:
 fix_task_structure(project_id, task)
```

**Cómo ejecutar**:
```bash
python core/fix_project_structure_complete.py investigaci-n-clo-covid-19-20251222-195407
```

**Validación post-ejecución**:
```bash
python core/framework_validator.py validate investigaci-n-clo-covid-19-20251222-195407
```

---

[Similar para otros scripts necesarios]

### Script 2: update_versions_docs.py

**Propósito**: Actualizar todas las referencias de versión a v2.2

```python
# Código para actualizar versiones en todos los docs
```

### Script 3: remove_deprecated_code.py

**Propósito**: Remover código comentado y deprecated

```python
# Código para limpiar código legacy
```

## CORRECCIONES MANUALES

Algunas correcciones requieren intervención manual:

### Manual 1: Actualizar ejemplos en README.md

**Problema**: Ejemplos desactualizados
**Archivo**: README.md líneas 145-200
**Acción**: Reescribir ejemplos para que coincidan con project_manager.py actual
**Requiere**: Entender API de project_manager.py

### Manual 2: Mejorar docstrings en framework_validator.py

**Problema**: Docstrings incompletos
**Archivo**: core/framework_validator.py
**Acción**: Agregar docstrings a 5 funciones sin documentar
**Requiere**: Entender lógica de cada función

---

[Lista todas las correcciones manuales necesarias]

## CHECKLIST DE VALIDACION

Después de ejecutar todas las correcciones:

### Validación de Documentación
- [ ] Todas las referencias de versión son v2.2
- [ ] No hay referencias rotas a archivos
- [ ] Todos los ejemplos son ejecutables
- [ ] No hay contradicciones entre docs

### Validación de Código
- [ ] No hay código deprecated sin marcar
- [ ] No hay código comentado legacy
- [ ] Todos los módulos tienen docstrings
- [ ] No hay imports no usados

### Validación de Estructura
- [ ] Proyecto COVID: 100% de tareas COMPLIANT
- [ ] Todas las tareas tienen task_info.json
- [ ] Todas las tareas tienen README.md
- [ ] Todas las tareas tienen reports/ con contenido
- [ ] Ningún .md en root (excepto permitidos)

### Validación Automatizada
- [ ] `python core/framework_validator.py validate [project-id]` pasa 100%
- [ ] `python core/audit_project.py [project-id]` muestra 0 errores
- [ ] Todos los scripts en core/ ejecutan sin errores

## ESTIMACION TOTAL

### Por Fase
- FASE 1 (Críticas): X correcciones, Y horas
- FASE 2 (Altas): X correcciones, Y horas
- FASE 3 (Medias): X correcciones, Y horas
- FASE 4 (Bajas): X correcciones, Y horas (opcional)

### Total
- Correcciones automáticas: X (via scripts)
- Correcciones manuales: X
- Tiempo total estimado: Y horas
- Esfuerzo: Alto / Medio / Bajo

## RIESGOS Y MITIGACIONES

### Riesgo 1: Scripts de migración fallan

**Probabilidad**: Media
**Impacto**: Alto
**Mitigación**:
- Crear backups antes de ejecutar scripts
- Ejecutar en dry-run mode primero
- Validar cada paso

### Riesgo 2: Correcciones rompen funcionalidad existente

**Probabilidad**: Baja
**Impacto**: Crítico
**Mitigación**:
- Hacer correcciones en branch separado
- Validar después de cada corrección
- Tener rollback plan

## ROLLBACK PLAN

Si algo falla:

1. **Backups disponibles en**: .memory_backups/
2. **Restaurar con**: `git checkout -- [archivo]` (si en git)
3. **Validar restauración**: Ejecutar validators

## PROXIMOS PASOS DESPUES DE CORRECCION

Una vez baseline limpio:

1. Validar compliance 100%
2. Ejecutar Tarea 6 (Validación Post-Corrección)
3. Documentar estado final
4. Proceder con implementación Forge v1.0

## APENDICE: DETALLE DE CORRECCIONES

### Corrección C1 Detallada: project_manager debe crear README.md

**Análisis**:
- ESTANDAR_v2.2.md define README.md como REQUERIDO
- project_manager.py.create_task() no lo crea
- 6 tareas del proyecto COVID sin README.md

**Código actual** (project_manager.py:112-170):
```python
def create_task(self, project_id, task_name, task_description, prompt):
 # ... crea directorio
 # ... crea task_info.json
 # ... crea prompt.md
 # FALTA: crear README.md
```

**Código propuesto**:
```python
def create_task(self, project_id, task_name, task_description, prompt):
 # ... código existente ...

 # AGREGAR: Crear README.md
 readme_path = task_dir / "README.md"
 readme_content = self._generate_task_readme(
 task_name=task_name,
 description=task_description
 )
 readme_path.write_text(readme_content, encoding='utf-8')

 return task_info

def _generate_task_readme(self, task_name, description):
 return f\"\"\"# {task_name.upper()}

## INTRODUCCION

{description}

## CONTENIDO DEL ANALISIS

[Los reportes se listaran aquí cuando se generen]

## NAVEGACION RAPIDA

Revisa los documentos en el directorio reports/ según tu interés.

---

**Nota:** Esta tarea sigue el estándar v2.2 ORGANIZED del framework.
\"\"\"
```

**Testing**:
```python
# Test de la corrección
pm = ProjectManager()
task = pm.create_task(
 project_id="test",
 task_name="test-task",
 task_description="Test",
 prompt="Test prompt"
)
assert Path("projects/test/tasks/test-task/README.md").exists()
```

---

[Similar nivel de detalle para otras correcciones complejas]

```

## CRITERIOS DE CALIDAD

- Cada corrección tiene pasos específicos ejecutables
- Priorización clara con justificación
- Scripts de migración funcionan (si los propones, deben ser código real)
- Checklist completo y validable
- Estimaciones realistas

## HERRAMIENTAS

- Read: leer reportes previos
- Write: generar scripts de migración

## FORMATO

Profesional, sin emojis, markdown estándar.

## ENTREGABLE

1. Reporte en reports/plan_correcciones_detallado.md
2. Plan completo priorizado
3. Scripts de migración (código real)
4. Checklist de validación
5. Al menos 15 correcciones específicas
