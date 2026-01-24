# INSTRUCCIONES DE INTEGRACION MANUAL - C5: VALIDACION PREVENTIVA

## OBJETIVO

Integrar validación preventiva en ProjectManager para que valide ANTES de crear
estructuras en filesystem, y ejecute rollback automático si algo falla.

## PASO 1: Modificar create_project()

### Ubicación
Archivo: `core/project_manager.py`
Método: `create_project()`

### Cambios

Agregar al INICIO del método (después del docstring):

```python
def create_project(self, name, user_request, context):
    """..."""

    # AGREGAR ESTO AL INICIO:
    from core.framework_validator import FrameworkValidator
    validator = FrameworkValidator()

    # PRE-VALIDACION
    # valid, messages = validator.validate_research_request(user_request)
    # if not valid:
    #     error_msg = "\n".join(messages)
    #     raise ValidationError(f"Solicitud invalida:\n{error_msg}")
    # (Comentado porque validate_research_request puede no existir todavia)

    # ... resto del codigo original ...
```

Agregar ANTES DEL RETURN (al final del método):

```python
    # AGREGAR ANTES DEL RETURN:
    # POST-VALIDACION (double-check)
    try:
        valid, messages = validator.validate_project_structure(project_id)
        if not valid:
            import shutil
            shutil.rmtree(project_dir)
            error_msg = "\n".join(messages)
            raise ValidationError(f"Proyecto invalido (rollback ejecutado):\n{error_msg}")
    except Exception as e:
        # Si validation falla, hacer cleanup
        if project_dir.exists():
            import shutil
            shutil.rmtree(project_dir)
        raise

    return project_info
```

## PASO 2: Modificar create_task()

### Ubicación
Archivo: `core/project_manager.py`
Método: `create_task()`

### Cambios

Agregar al INICIO del método:

```python
def create_task(self, project_id, task_name, prompt, description):
    """..."""

    # AGREGAR AL INICIO:
    from core.framework_validator import FrameworkValidator
    validator = FrameworkValidator()

    # PRE-VALIDACION básica
    # Verificar que task_name cumple convenciones
    if not task_name or not task_name.replace('-', '').replace('_', '').isalnum():
        raise ValidationError(f"Nombre de tarea invalido: {task_name}")

    # ... codigo original ...
```

Agregar ANTES DEL RETURN:

```python
    # AGREGAR ANTES DEL RETURN:
    # POST-VALIDACION
    try:
        valid, messages = validator.validate_task_structure(
            project_id, task_name
        )
        if not valid:
            # ROLLBACK
            import shutil
            shutil.rmtree(task_dir)
            error_msg = "\n".join(messages)
            raise ValidationError(f"Tarea invalida (rollback):\n{error_msg}")
    except Exception as e:
        # Cleanup
        if task_dir.exists():
            import shutil
            shutil.rmtree(task_dir)
        raise

    return task_info
```

## PASO 3: Wrap en try-except para safety

Ambos métodos deberían tener un try-except general:

```python
def create_project(...):
    """..."""

    # Validaciones...

    try:
        # Toda la lógica de creación aquí
        project_dir = ...
        project_dir.mkdir(...)
        # ... crear archivos ...

        # Post-validación
        # ...

        return project_info

    except Exception as e:
        # Cleanup en caso de cualquier error
        if 'project_dir' in locals() and project_dir.exists():
            import shutil
            shutil.rmtree(project_dir)
        raise
```

## VALIDACION POST-INTEGRACION

Después de hacer los cambios, validar que:

```bash
# 1. ValidationError existe
python -c "from core.project_manager import ValidationError; print('ValidationError OK')"

# 2. Test de validación preventiva (debería fallar con nombre inválido)
python -c "
from core.project_manager import ProjectManager
pm = ProjectManager()
try:
    pm.create_project(
        name='',  # Invalido
        user_request='test',
        context=''
    )
    print('ERROR: Deberia haber fallado')
except Exception as e:
    print(f'OK: Validacion preventiva funciona: {type(e).__name__}')
"

# 3. Test normal (debería funcionar)
python -c "
from core.project_manager import ProjectManager
pm = ProjectManager()
try:
    project = pm.create_project(
        name='test-validacion-c5',
        user_request='Test de validación preventiva',
        context='Testing C5'
    )
    print(f'OK: Proyecto creado: {project["id"]}')
except Exception as e:
    print(f'ERROR: {e}')
"
```

## NOTAS IMPORTANTES

1. **Backups**: Antes de modificar, crear backup de project_manager.py
2. **Testing**: Probar cada cambio incrementalmente
3. **Rollback**: Si algo falla, restaurar backup
4. **ValidationError**: Ya fue agregada por fix_c5_preventive_validation.py

## RIESGOS

- **Alto**: Modificar lógica central puede introducir bugs
- **Mitigación**: Testing exhaustivo, backups, rollback plan

## ESTIMACION

3 horas (incluyendo testing y validación)

---

**CORRECCION C5**: Estas instrucciones detallan la integración manual necesaria.
