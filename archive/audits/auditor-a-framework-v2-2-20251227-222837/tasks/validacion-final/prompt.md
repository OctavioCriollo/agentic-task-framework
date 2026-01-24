# TAREA: VALIDACION POST-CORRECCION

## TU ROL

Eres un QA Lead especializado en diseño de test suites y criterios de aceptación. Tu trabajo es definir cómo validar que el framework v2.2 está limpio y listo para migración.

## OBJETIVO

Crear suite de validación completa y criterios de aceptación para confirmar que el baseline v2.2 está limpio, consistente, y listo para implementación de Forge v1.0.

## CONTEXTO REQUERIDO

LEE estos documentos para entender qué debe validarse:

1. **ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md** - Estándar a cumplir
2. **README.md** - Funcionalidad esperada
3. **CLAUDE.md** - Comportamiento del coordinador
4. **CHECKLIST.md** - Checklist existente

## INSUMOS

Lee todos los reportes previos:

1. **../auditoria-documentacion/reports/analisis_documentacion_core.md**
2. **../auditoria-codigo/reports/analisis_codigo_python.md**
3. **../auditoria-estructura/reports/validacion_proyecto_covid.md**
4. **../identificacion-inconsistencias/reports/matriz_inconsistencias.md**
5. **../plan-correccion/reports/plan_correcciones_detallado.md**

Estos te dirán qué problemas había y qué se corrigió.

## ESTRUCTURA DE OUTPUT

Reporte en: reports/suite_validacion.md

```markdown
# SUITE DE VALIDACION - FRAMEWORK v2.2 BASELINE

## OBJETIVO

Validar que el framework v2.2 está en estado limpio y consistente, listo para migración a Forge v1.0.

## CRITERIOS DE ACEPTACION

El baseline v2.2 es ACEPTABLE si y solo si:

### Criterio 1: Documentación Consistente
- [ ] Todas las referencias de versión son v2.2
- [ ] 0 referencias rotas a archivos
- [ ] 0 comandos documentados que no funcionan
- [ ] 0 contradicciones entre documentos
- [ ] Todos los ejemplos son ejecutables

### Criterio 2: Código Limpio
- [ ] 0 módulos deprecated sin marcar
- [ ] 0 código comentado legacy (más de 10 líneas)
- [ ] 0 imports no usados
- [ ] 100% de funciones públicas con docstrings
- [ ] 0 duplicación de código

### Criterio 3: Estructura Compliant
- [ ] 100% de tareas en proyecto COVID cumplen v2.2 ORGANIZED
- [ ] Todas las tareas tienen task_info.json válido
- [ ] Todas las tareas tienen README.md con contenido
- [ ] Todas las tareas tienen reports/ con al menos 1 archivo
- [ ] 0 archivos .md en root de tareas (excepto README.md, prompt.md)

### Criterio 4: Consistencia Cross-System
- [ ] Versiones en docs = versiones en código
- [ ] Features documentadas = features implementadas
- [ ] Estructura documentada = estructura real
- [ ] Convenciones documentadas = convenciones usadas

### Criterio 5: Validadores Funcionando
- [ ] framework_validator.py pasa 100% en proyecto COVID
- [ ] audit_project.py reporta 0 errores
- [ ] reorganize_task_structure.py ejecuta sin errores (dry-run)

## SUITE DE VALIDACION AUTOMATIZADA

### Validador 1: Documentación

**Archivo**: tests/validate_docs.py

```python
#!/usr/bin/env python3
"""
Valida consistencia de documentación
"""
import re
from pathlib import Path

def validate_docs():
    \"\"\"
    Valida documentación del framework

    Returns:
        tuple: (passed, errors)
    \"\"\"
    errors = []

    # Test 1: Versiones consistentes
    docs = [
        "CLAUDE.md",
        "README.md",
        "ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md"
    ]

    versions = {}
    for doc in docs:
        content = Path(doc).read_text(encoding='utf-8')
        # Buscar menciones de versión
        matches = re.findall(r'v(\d+\.\d+)', content)
        versions[doc] = matches

    # Verificar que todas sean v2.2
    for doc, vers in versions.items():
        for v in vers:
            if v != "2.2":
                errors.append(f"{doc}: versión incorrecta v{v} (esperada v2.2)")

    # Test 2: Referencias a archivos
    # ... código para verificar referencias ...

    # Test 3: Ejemplos ejecutables
    # ... código para verificar ejemplos ...

    passed = len(errors) == 0
    return passed, errors

if __name__ == "__main__":
    passed, errors = validate_docs()
    if passed:
        print("✓ Documentación: PASS")
    else:
        print("✗ Documentación: FAIL")
        for error in errors:
            print(f"  - {error}")
    exit(0 if passed else 1)
```

**Cómo ejecutar**:
```bash
python tests/validate_docs.py
```

**Output esperado**:
```
✓ Documentación: PASS
```

---

### Validador 2: Código

**Archivo**: tests/validate_code.py

```python
#!/usr/bin/env python3
"""
Valida calidad de código Python
"""
import ast
from pathlib import Path

def validate_code():
    \"\"\"
    Valida módulos en core/

    Returns:
        tuple: (passed, errors)
    \"\"\"
    errors = []

    # Test 1: Docstrings
    for module_path in Path("core").glob("*.py"):
        if module_path.name.startswith("__"):
            continue

        content = module_path.read_text(encoding='utf-8')
        tree = ast.parse(content)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    if not node.name.startswith("_"):
                        errors.append(
                            f"{module_path.name}:{node.lineno}: "
                            f"función {node.name} sin docstring"
                        )

    # Test 2: Imports no usados
    # ... código para detectar imports no usados ...

    # Test 3: Código deprecated marcado
    # ... código para verificar marcado deprecated ...

    passed = len(errors) == 0
    return passed, errors

if __name__ == "__main__":
    passed, errors = validate_code()
    if passed:
        print("✓ Código: PASS")
    else:
        print("✗ Código: FAIL")
        for error in errors:
            print(f"  - {error}")
    exit(0 if passed else 1)
```

**Cómo ejecutar**:
```bash
python tests/validate_code.py
```

---

### Validador 3: Estructura

**Archivo**: tests/validate_structure.py

```python
#!/usr/bin/env python3
"""
Valida estructura de proyecto COVID
"""
import json
from pathlib import Path

def validate_structure(project_id):
    \"\"\"
    Valida que proyecto cumple v2.2 ORGANIZED

    Args:
        project_id: ID del proyecto

    Returns:
        tuple: (passed, errors)
    \"\"\"
    errors = []

    project_dir = Path("projects") / project_id
    tasks_dir = project_dir / "tasks"

    for task_dir in tasks_dir.iterdir():
        if not task_dir.is_dir():
            continue

        task_name = task_dir.name

        # Test 1: Archivos obligatorios
        required_files = ["task_info.json", "prompt.md", "README.md"]
        for req_file in required_files:
            if not (task_dir / req_file).exists():
                errors.append(f"{task_name}: falta {req_file}")

        # Test 2: reports/ existe y tiene contenido
        reports_dir = task_dir / "reports"
        if not reports_dir.exists():
            errors.append(f"{task_name}: falta directorio reports/")
        else:
            reports = list(reports_dir.glob("*.md"))
            if len(reports) == 0:
                errors.append(f"{task_name}: reports/ vacío")

        # Test 3: No hay .md en root (excepto permitidos)
        allowed_in_root = {"README.md", "prompt.md"}
        for md_file in task_dir.glob("*.md"):
            if md_file.name not in allowed_in_root:
                errors.append(
                    f"{task_name}: {md_file.name} debe estar en reports/"
                )

        # Test 4: task_info.json válido
        task_info_path = task_dir / "task_info.json"
        if task_info_path.exists():
            try:
                with open(task_info_path, 'r', encoding='utf-8') as f:
                    task_info = json.load(f)

                # Verificar campos requeridos
                required_fields = ["task_name", "description", "status", "reports"]
                for field in required_fields:
                    if field not in task_info:
                        errors.append(f"{task_name}: task_info.json falta campo {field}")
            except json.JSONDecodeError:
                errors.append(f"{task_name}: task_info.json no es JSON válido")

    passed = len(errors) == 0
    return passed, errors

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python validate_structure.py [project-id]")
        exit(1)

    passed, errors = validate_structure(sys.argv[1])
    if passed:
        print("✓ Estructura: PASS")
    else:
        print("✗ Estructura: FAIL")
        for error in errors:
            print(f"  - {error}")
    exit(0 if passed else 1)
```

**Cómo ejecutar**:
```bash
python tests/validate_structure.py investigaci-n-clo-covid-19-20251222-195407
```

---

### Validador Master: validate_all.py

**Archivo**: tests/validate_all.py

```python
#!/usr/bin/env python3
"""
Ejecuta toda la suite de validación
"""
import sys
from validate_docs import validate_docs
from validate_code import validate_code
from validate_structure import validate_structure

def validate_all(project_id):
    \"\"\"
    Ejecuta todos los validadores

    Returns:
        bool: True si todos pasan
    \"\"\"
    print("="*60)
    print("SUITE DE VALIDACION FRAMEWORK v2.2")
    print("="*60)
    print()

    all_passed = True

    # Validar docs
    print("Validando documentación...")
    docs_passed, docs_errors = validate_docs()
    if docs_passed:
        print("✓ Documentación: PASS")
    else:
        print("✗ Documentación: FAIL")
        for error in docs_errors:
            print(f"  - {error}")
        all_passed = False
    print()

    # Validar código
    print("Validando código...")
    code_passed, code_errors = validate_code()
    if code_passed:
        print("✓ Código: PASS")
    else:
        print("✗ Código: FAIL")
        for error in code_errors:
            print(f"  - {error}")
        all_passed = False
    print()

    # Validar estructura
    print(f"Validando estructura de {project_id}...")
    struct_passed, struct_errors = validate_structure(project_id)
    if struct_passed:
        print("✓ Estructura: PASS")
    else:
        print("✗ Estructura: FAIL")
        for error in struct_errors:
            print(f"  - {error}")
        all_passed = False
    print()

    # Resultado final
    print("="*60)
    if all_passed:
        print("RESULTADO: BASELINE LIMPIO ✓")
        print("Framework v2.2 listo para migración a Forge v1.0")
    else:
        print("RESULTADO: BASELINE NO LIMPIO ✗")
        print("Correcciones adicionales necesarias")
    print("="*60)

    return all_passed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_all.py [project-id]")
        exit(1)

    passed = validate_all(sys.argv[1])
    exit(0 if passed else 1)
```

**Cómo ejecutar**:
```bash
python tests/validate_all.py investigaci-n-clo-covid-19-20251222-195407
```

**Output esperado si PASS**:
```
============================================================
SUITE DE VALIDACION FRAMEWORK v2.2
============================================================

Validando documentación...
✓ Documentación: PASS

Validando código...
✓ Código: PASS

Validando estructura de investigaci-n-clo-covid-19-20251222-195407...
✓ Estructura: PASS

============================================================
RESULTADO: BASELINE LIMPIO ✓
Framework v2.2 listo para migración a Forge v1.0
============================================================
```

## CHECKLIST MANUAL DE VALIDACION

Además de validadores automáticos, verificar manualmente:

### Documentación
- [ ] README.md tiene ejemplos ejecutables actualizados
- [ ] CLAUDE.md refleja comportamiento actual
- [ ] ESTANDAR_v2.2.md es claro y sin ambigüedades
- [ ] No hay TODOs pendientes en documentación

### Código
- [ ] Todos los scripts en core/ ejecutan sin errores
- [ ] project_manager.py crea estructura v2.2 completa
- [ ] framework_validator.py detecta todos los problemas
- [ ] No hay warnings de Python al importar módulos

### Proyecto COVID
- [ ] Puedes navegar todas las tareas vía README.md
- [ ] Todos los reportes tienen contenido significativo
- [ ] task_info.json refleja estado real
- [ ] Naming es consistente (kebab-case tareas, snake_case reportes)

### Integraciones
- [ ] Claude Code puede leer CLAUDE.md correctamente
- [ ] Settings.json está configurado correctamente
- [ ] Hooks funcionan si están configurados
- [ ] Git ignora archivos temporales

## REPORTE DE ESTADO FINAL

### Si Validación PASA

```markdown
## ESTADO FINAL: BASELINE LIMPIO ✓

El framework v2.2 ha sido auditado, corregido y validado exitosamente.

**Métricas finales**:
- Documentación: 0 inconsistencias
- Código: 0 problemas críticos
- Estructura: 100% compliance
- Validadores: PASS

**El framework está listo para**:
1. Uso en producción con confianza
2. Migración a Forge v1.0
3. Documentación como referencia

**Próximos pasos recomendados**:
1. Crear tag de git para esta versión baseline
2. Documentar lecciones aprendidas
3. Proceder con implementación de Forge v1.0
```

### Si Validación FALLA

```markdown
## ESTADO FINAL: CORRECCIONES ADICIONALES NECESARIAS ✗

La validación identificó problemas pendientes:

**Problemas encontrados**:
- [Lista de problemas por categoría]

**Acciones requeridas**:
1. [Corrección necesaria 1]
2. [Corrección necesaria 2]

**Bloqueadores para migración**:
- [Lista de problemas que bloquean Forge v1.0]

**Estimación de trabajo adicional**:
- X horas para completar correcciones
```

## METRICAS DE CALIDAD

Objetivo: todas las métricas en 100% o 0 errores

| Métrica | Objetivo | Actual | Status |
|---------|----------|--------|--------|
| Versiones consistentes | 100% | X% | PASS/FAIL |
| Referencias válidas | 100% | X% | PASS/FAIL |
| Código con docstrings | 100% | X% | PASS/FAIL |
| Tareas compliant | 100% | X% | PASS/FAIL |
| Validadores passing | 100% | X% | PASS/FAIL |

## RECOMENDACIONES POST-VALIDACION

### Si baseline está limpio
1. Crear snapshot/tag del estado actual
2. Documentar baseline como referencia
3. Comenzar implementación Forge v1.0
4. Mantener v2.2 como fallback

### Si hay problemas pendientes
1. Priorizar según bloqueadores
2. Ejecutar correcciones adicionales
3. Re-validar
4. Repetir hasta PASS completo

## MANTENIMIENTO FUTURO

Para mantener baseline limpio:
1. Ejecutar validadores antes de cada cambio
2. Actualizar docs cuando se modifica código
3. Validar nuevos proyectos contra v2.2
4. No permitir código sin docstrings

```

## CRITERIOS DE CALIDAD DE ESTE REPORTE

- Suite de validación es ejecutable (código real, no pseudo-código)
- Validadores cubren todos los criterios de aceptación
- Checklist es completo y verificable
- Scripts proporcionan output claro
- Métricas son cuantificables

## HERRAMIENTAS

- Write: crear scripts de validación
- Bash: ejecutar validadores existentes

## FORMATO

Profesional, sin emojis, markdown estándar.

## ENTREGABLE

1. Reporte en reports/suite_validacion.md
2. Suite completa de validadores automáticos (código Python funcional)
3. Checklist manual de validación
4. Criterios de aceptación claros
5. Scripts en directorio tests/ listos para ejecutar
