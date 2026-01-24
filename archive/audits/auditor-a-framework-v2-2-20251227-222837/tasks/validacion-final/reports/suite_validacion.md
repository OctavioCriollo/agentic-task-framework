# SUITE DE VALIDACION COMPLETA - FRAMEWORK v2.2 BASELINE

**Fecha**: 2025-12-27
**Version del Framework**: v2.2
**Proposito**: Confirmar que baseline v2.2 esta limpio, consistente y listo para migracion a Forge v1.0

---

## RESUMEN EJECUTIVO

Esta suite de validacion automatizada determina si el Framework v2.2 cumple con todos los criterios de calidad, consistencia y compliance antes de proceder con la migracion a Forge v1.0.

**Componentes de la Suite**:
- `tests/validate_docs.py` - Validador de documentacion
- `tests/validate_code.py` - Validador de codigo Python
- `tests/validate_structure.py` - Validador de estructura de proyectos
- `tests/validate_all.py` - Ejecutor maestro de toda la suite

**Criterios Evaluados**: 42 validaciones automaticas

---

## PARTE 1: CRITERIOS DE ACEPTACION

El baseline v2.2 es ACEPTABLE si cumple TODOS estos criterios:

### Criterio 1: Documentacion Consistente

**Validador**: `validate_docs.py`

**Requisitos**:
- [ ] Todas las versiones mencionadas son v2.2 (no v1.0, v2.0, v2.1)
- [ ] 0 referencias rotas a archivos
- [ ] Comandos Python consistentes (todos usan 'python' o 'py -3', no mezclados)
- [ ] 0 contradicciones entre documentos core
- [ ] Ejemplos de estructura muestran reportes en reports/ (no en root)
- [ ] Changelog dates consistentes entre README.md y CLAUDE.md
- [ ] FORGE docs NO estan en root (deben estar en docs/proposals/forge/)

**Umbral de Aceptacion**: 0 errores criticos

**Comando**:
```bash
python tests/validate_docs.py
```

**Archivos Validados**:
- CLAUDE.md
- README.md
- ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md
- CHECKLIST.md

---

### Criterio 2: Codigo Limpio

**Validador**: `validate_code.py`

**Requisitos**:
- [ ] 100% funciones publicas tienen docstrings
- [ ] task_manager.py NO existe O esta marcado DEPRECATED en header
- [ ] 0 bloques de codigo comentado (>10 lineas consecutivas)
- [ ] 0 imports de task_manager en modulos activos
- [ ] Scripts utilities NO tienen project_id hardcodeado (usan argparse)

**Umbral de Aceptacion**: 0 errores criticos

**Comando**:
```bash
python tests/validate_code.py
```

**Modulos Validados**:
- core/project_manager.py
- core/framework_validator.py
- core/reorganize_task_structure.py
- core/fix_project_structure.py
- core/check_empty_reports.py
- core/audit_project.py
- core/analyze_inconsistencies.py

---

### Criterio 3: Estructura Compliant

**Validador**: `validate_structure.py`

**Requisitos**:
- [ ] 100% tareas tienen archivos obligatorios: task_info.json, prompt.md, README.md, reports/
- [ ] 0 reportes .md en root de tarea (excepto README.md y prompt.md permitidos)
- [ ] task_info.json es JSON valido con campos requeridos
- [ ] Reportes listados en task_info.json EXISTEN
- [ ] Reportes existentes ESTAN LISTADOS en task_info.json
- [ ] Naming de reportes es snake_case minusculas (no SCREAMING_SNAKE_CASE)
- [ ] Nombres de tareas son kebab-case
- [ ] Tareas 'completed' tienen al menos 1 reporte

**Umbral de Aceptacion**:
- 0 tareas con archivos obligatorios faltantes
- Compliance rate >= 85%

**Comando**:
```bash
python tests/validate_structure.py [project-id]
```

**Estructura Validada** (ESTANDAR v2.2 ORGANIZED):
```
projects/[project-id]/tasks/[task-name]/
  ├── task_info.json          (REQUERIDO)
  ├── prompt.md               (REQUERIDO)
  ├── README.md               (REQUERIDO)
  └── reports/                (REQUERIDO)
      ├── [tema]_[aspecto]_[detalles].md
      └── ...
```

---

### Criterio 4: Consistencia Cross-System

**Validado por**: Suite completa (validate_all.py)

**Requisitos**:
- [ ] Features documentadas ESTAN implementadas en codigo
- [ ] Estructura creada por ProjectManager CUMPLE con ESTANDAR v2.2
- [ ] Validaciones documentadas en CHECKLIST FUNCIONAN
- [ ] Ejemplos en docs SON EJECUTABLES

**Umbral de Aceptacion**: 0 gaps criticos entre docs-codigo-estructura

---

### Criterio 5: Validadores Funcionando

**Requisitos**:
- [ ] validate_docs.py ejecuta sin errores de Python
- [ ] validate_code.py ejecuta sin errores de Python
- [ ] validate_structure.py ejecuta sin errores de Python
- [ ] validate_all.py genera reporte completo

**Umbral de Aceptacion**: Todos los validadores ejecutan exitosamente

**Comando**:
```bash
# Test de ejecucion
python tests/validate_docs.py
python tests/validate_code.py
python tests/validate_structure.py investigaci-n-clo-covid-19-20251222-195407
python tests/validate_all.py investigaci-n-clo-covid-19-20251222-195407
```

---

## PARTE 2: SUITE DE VALIDACION AUTOMATIZADA

### Validador 1: validate_docs.py

**Descripcion**: Valida consistencia de documentacion core

**Validaciones Implementadas**:

1. **Versiones Consistentes**
   - Busca menciones de v1.0, v2.0, v2.1 (incorrectas)
   - Verifica que solo se menciona v2.2 (correcta)
   - Excluye changelogs de validacion (menciones historicas permitidas)

2. **Referencias Validas**
   - Extrae referencias a archivos .py, .md, .json
   - Verifica existencia de cada archivo referenciado
   - Permite paths relativos comunes (core/, projects/, docs/)

3. **Comandos Python Consistentes**
   - Detecta variantes: python, python3, py -3, py
   - Verifica que TODOS los docs usan la MISMA forma
   - Reporta inconsistencia si hay mezcla

4. **FORGE Docs Ubicacion**
   - Verifica que FORGE_*.md NO esten en root
   - Deben estar en docs/proposals/forge/

5. **Ejemplos de Estructura Correctos**
   - Verifica que ejemplos muestren reportes en reports/
   - No deben mostrar reportes .md en root de tarea

6. **Changelog Dates**
   - Compara fechas de versiones entre README.md y CLAUDE.md
   - Reporta discrepancias

**Output**: (passed: bool, errors: List[str])

**Uso**:
```python
from validate_docs import validate_docs
passed, errors = validate_docs()
```

---

### Validador 2: validate_code.py

**Descripcion**: Valida calidad de codigo Python en core/

**Validaciones Implementadas**:

1. **Docstrings en Funciones Publicas**
   - Parsea cada modulo .py con ast
   - Detecta funciones que NO empiezan con _ (publicas)
   - Verifica que tengan docstring
   - Skip modulos marcados DEPRECATED

2. **Codigo Legacy Marcado**
   - Verifica si task_manager.py existe
   - Si existe, valida que tenga "DEPRECATED" en primeras 100 lineas
   - Warning si esta deprecated pero presente

3. **Sin Codigo Comentado Extenso**
   - Cuenta lineas consecutivas de comentarios
   - Reporta si >10 lineas consecutivas (posible codigo comentado)
   - Skip docstrings (usa deteccion de """ y ''')

4. **Sin Imports Legacy**
   - Busca imports de task_manager en modulos activos
   - Reporta si algun modulo importa codigo deprecated

5. **Scripts Parametrizados**
   - Verifica scripts utilities (fix_project_structure.py, etc.)
   - Detecta project_id hardcodeado
   - Verifica que usen argparse para CLI

**Output**: (passed: bool, errors: List[str])

**Uso**:
```python
from validate_code import validate_code
passed, errors = validate_code()
```

---

### Validador 3: validate_structure.py

**Descripcion**: Valida estructura de proyecto contra v2.2 ORGANIZED

**Validaciones Implementadas**:

1. **Archivos Obligatorios Existen**
   - task_info.json
   - prompt.md
   - README.md
   - reports/ (directorio)

2. **Sin Reportes en Root**
   - Verifica que NO haya .md en root
   - Permite solo README.md y prompt.md

3. **task_info.json Valido**
   - JSON parseeable
   - Campos requeridos: task_name, description, status, reports
   - Reportes listados EXISTEN en reports/
   - NO debe listar README.md como reporte
   - Reportes existentes ESTAN LISTADOS

4. **Naming de Reportes Correcto**
   - snake_case minusculas
   - NO SCREAMING_SNAKE_CASE
   - Pattern: ^[a-z0-9_]+\.md$

5. **Nombre de Tarea Correcto**
   - kebab-case
   - Pattern: ^[a-z0-9]+(-[a-z0-9]+)+$

6. **Tareas Completed Tienen Reportes**
   - Si status='completed', debe tener >=1 reporte en reports/

**Output**: (passed: bool, errors: List[str])

**Uso**:
```python
from validate_structure import validate_structure
passed, errors = validate_structure("investigaci-n-clo-covid-19-20251222-195407")
```

---

### Validador Master: validate_all.py

**Descripcion**: Ejecuta toda la suite y genera reporte consolidado

**Flujo**:
1. Ejecuta validate_docs()
2. Ejecuta validate_code()
3. Ejecuta validate_structure(project_id)
4. Consolida resultados
5. Evalua criterios de aceptacion
6. Genera reporte final

**Reporte Generado**:
```
======================================================================
  SUITE DE VALIDACION FRAMEWORK v2.2 BASELINE
======================================================================

Proyecto a validar: investigaci-n-clo-covid-19-20251222-195407
Fecha: 2025-12-27 23:45:00

[VALIDACION 1/3: DOCUMENTACION]
  (output de validate_docs)

[VALIDACION 2/3: CODIGO PYTHON]
  (output de validate_code)

[VALIDACION 3/3: ESTRUCTURA DEL PROYECTO]
  (output de validate_structure)

======================================================================
  RESULTADOS CONSOLIDADOS
======================================================================

[✓] DOCS            PASS       (0 errores)
[✗] CODE            FAIL       (3 errores)
      - project_manager.py: funcion 'main' sin docstring
      - task_manager.py esta deprecated pero presente
      - fix_project_structure.py: project_id hardcodeado
[✓] STRUCTURE       PASS       (0 errores)

----------------------------------------------------------------------
Total de errores: 3
----------------------------------------------------------------------

======================================================================
  CRITERIOS DE ACEPTACION
======================================================================

[✓] Documentacion consistente (v2.2)                      CUMPLE
[✗] Codigo limpio (sin deprecated activo)                 NO CUMPLE
[✓] Estructura compliant (v2.2 ORGANIZED)                 CUMPLE

======================================================================
  RESULTADO FINAL
======================================================================

            *** CORRECCIONES NECESARIAS ***

  Se identificaron 3 problemas que requieren atencion

  Acciones recomendadas:
    1. Revisar errores reportados arriba
    2. Aplicar correcciones segun plan de remediacion
    3. Re-ejecutar validate_all.py
    4. Repetir hasta alcanzar PASS

  Para ver errores detallados, ejecutar validadores individuales:
    - python tests/validate_docs.py
    - python tests/validate_code.py
    - python tests/validate_structure.py investigaci-n-clo-covid-19-20251222-195407

======================================================================
```

**Output**: bool (True si baseline es ACEPTABLE)

**Uso**:
```bash
python tests/validate_all.py investigaci-n-clo-covid-19-20251222-195407
```

**Exit Code**:
- 0 si PASS (baseline limpio)
- 1 si FAIL (correcciones necesarias)

---

## PARTE 3: CHECKLIST MANUAL DE VALIDACION

Ademas de validaciones automaticas, verificar manualmente:

### Documentacion

- [ ] README.md ejemplos son ejecutables (probar comandos)
- [ ] CLAUDE.md refleja comportamiento actual del coordinador
- [ ] ESTANDAR_v2.2.md es claro y sin ambiguedades
- [ ] FORGE docs tienen advertencia clara "PROPUESTA NO IMPLEMENTADA"

### Codigo

- [ ] project_manager.py crea estructura v2.2 completa (test manual)
- [ ] framework_validator.py detecta problemas correctamente (test con proyecto)
- [ ] Scripts de corrección funcionan sin errores (test dry-run)

### Proyecto COVID

- [ ] Navegacion via README.md funciona (leer y seguir links)
- [ ] Todos los reportes tienen contenido significativo (revisar muestreo)
- [ ] task_info.json refleja estado real de archivos (comparar)
- [ ] Naming consistente en todo el proyecto (revision visual)

---

## PARTE 4: METRICAS DE CALIDAD

| Metrica | Objetivo | Descripcion |
|---------|----------|-------------|
| Versiones consistentes | 100% | Todas menciones a v2.2 (no v1.0, v2.0, v2.1) |
| Referencias validas | 100% | Archivos mencionados existen |
| Funciones documentadas | 100% | Docstrings en funciones publicas |
| Tareas compliant | >=85% | Cumplen v2.2 ORGANIZED |
| Validadores passing | 100% | Suite completa PASS |
| Errores criticos | 0 | Sin problemas que bloqueen funcionalidad |
| Errores altos | <=5 | Problemas de calidad controlados |

**Metricas Detalladas por Area**:

### Documentacion
- Documentos validados: 4
- Referencias verificadas: 40+
- Comandos verificados: 15+
- Inconsistencias permitidas: 0 criticas

### Codigo
- Modulos validados: 8
- Funciones publicas: 40+
- Lineas de codigo: ~1,900
- Codigo legacy permitido: 0 activo (deprecated marcado OK)

### Estructura (Proyecto COVID)
- Tareas totales: 13
- Archivos obligatorios: 4 por tarea
- Reportes totales: ~25
- Compliance target: >=85%

---

## PARTE 5: PLAN DE EJECUCION

### Paso 1: Preparacion

```bash
# Navegar a directorio del framework
cd "D:\STARTUP\Proyectos\WORKING NOW\agentic-task-framework"

# Verificar que tests/ existe
ls tests/

# Verificar que scripts son ejecutables
python tests/validate_docs.py --help 2>&1 || echo "Script OK"
python tests/validate_code.py --help 2>&1 || echo "Script OK"
python tests/validate_structure.py --help 2>&1 || echo "Script OK"
```

### Paso 2: Ejecutar Validadores Individuales

```bash
# Validar documentacion
python tests/validate_docs.py > validation_results/docs.txt

# Validar codigo
python tests/validate_code.py > validation_results/code.txt

# Validar estructura (reemplazar con project_id real)
python tests/validate_structure.py investigaci-n-clo-covid-19-20251222-195407 > validation_results/structure.txt
```

### Paso 3: Ejecutar Suite Completa

```bash
# Suite maestra
python tests/validate_all.py investigaci-n-clo-covid-19-20251222-195407 | tee validation_results/full_suite.txt
```

### Paso 4: Analizar Resultados

```bash
# Revisar output
cat validation_results/full_suite.txt

# Contar errores criticos
grep "FAIL" validation_results/full_suite.txt | wc -l

# Extraer lista de errores
grep "  - " validation_results/full_suite.txt > validation_results/errors_list.txt
```

### Paso 5: Aplicar Correcciones

Si validacion FAIL:
1. Revisar `validation_results/errors_list.txt`
2. Aplicar correcciones segun tipo de error
3. Re-ejecutar suite
4. Repetir hasta PASS

### Paso 6: Verificacion Final

```bash
# Ejecutar suite final
python tests/validate_all.py investigaci-n-clo-covid-19-20251222-195407

# Verificar exit code
echo $?  # Debe ser 0 para PASS
```

---

## PARTE 6: REPORTE DE ESTADO FINAL

### Si Validacion PASA (exit code 0)

```
======================================================================
                    *** BASELINE LIMPIO ***
======================================================================

  El framework v2.2 esta LISTO para:
    - Uso en produccion con confianza
    - Migracion a Forge v1.0
    - Documentacion como referencia baseline

  Metricas finales:
    - Documentacion: 0 inconsistencias
    - Codigo: 0 problemas criticos
    - Estructura: 100% compliance
    - Validadores: PASS

  Proximos pasos recomendados:
    1. Crear tag git para baseline v2.2
       git tag -a v2.2-baseline -m "Baseline limpio v2.2 validado"

    2. Documentar lecciones aprendidas
       - Que funcionó bien
       - Que necesito corrección
       - Mejoras aplicadas

    3. Proceder con Forge v1.0
       - Revisar docs/proposals/forge/
       - Planificar migracion
       - Implementar componentes core

======================================================================
```

**Certificacion**:
- Framework: Agentic Task Framework v2.2
- Estado: BASELINE LIMPIO
- Fecha de validacion: [auto]
- Validado por: Suite automatica v1.0
- Criterios: 42 validaciones pasadas
- Proyecto de referencia: investigaci-n-clo-covid-19-20251222-195407

---

### Si Validacion FALLA (exit code 1)

```
======================================================================
            *** CORRECCIONES NECESARIAS ***
======================================================================

  Se identificaron [N] problemas que requieren atencion

  Distribucion de errores:
    - Criticos: [N]
    - Altos: [N]
    - Medios: [N]
    - Bajos: [N]

  Acciones prioritarias:
    1. Corregir errores criticos primero
    2. Corregir errores altos
    3. Opcional: corregir medios/bajos

  Para correccion detallada:
    - Revisar validation_results/errors_list.txt
    - Aplicar plan de remediacion
    - Re-ejecutar validadores

  Tiempo estimado de correccion:
    - Criticos: [X] horas
    - Altos: [Y] horas
    - Total: [Z] horas

======================================================================
```

**Plan de Remediacion**:

1. **Errores de Documentacion**:
   - Comando incorrecto → Actualizar en .md
   - Referencia rota → Crear archivo o corregir path
   - Version incorrecta → Buscar y reemplazar
   - FORGE en root → Mover a docs/proposals/forge/

2. **Errores de Codigo**:
   - Falta docstring → Agregar con Google style
   - Legacy code activo → Marcar DEPRECATED o remover
   - Codigo comentado → Eliminar o descomentar
   - project_id hardcoded → Agregar argparse

3. **Errores de Estructura**:
   - Archivo obligatorio falta → Crear con template
   - Reporte en root → Mover a reports/
   - Naming incorrecto → Renombrar archivo
   - task_info.json invalido → Corregir JSON
   - Metadata desincronizada → Actualizar reports[]

---

## PARTE 7: MANTENIMIENTO FUTURO

### Para Mantener Baseline Limpio

**Antes de cada cambio**:
```bash
# Ejecutar suite
python tests/validate_all.py [project-id]

# Solo proceder si PASS
```

**Despues de cada cambio**:
```bash
# Re-validar
python tests/validate_all.py [project-id]

# Verificar que no se introdujeron problemas
```

**En CI/CD** (futuro):
```yaml
# .github/workflows/validate.yml
name: Validate Framework
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run validation suite
        run: python tests/validate_all.py [project-id]
```

**Validaciones Regulares**:
- Semanal: Ejecutar suite completa
- Mensual: Revisar metricas de calidad
- Por release: Validacion exhaustiva + manual

---

## PARTE 8: CRITERIOS DE EXITO FINAL

### Baseline v2.2 es LIMPIO si:

1. **Validadores Automaticos**: PASS
   - validate_docs.py: PASS
   - validate_code.py: PASS
   - validate_structure.py: PASS

2. **Criterios de Aceptacion**: TODOS cumplen
   - Documentacion consistente: SI
   - Codigo limpio: SI
   - Estructura compliant: SI
   - Consistencia cross-system: SI
   - Validadores funcionando: SI

3. **Metricas de Calidad**: Cumplidas
   - Versiones 100% v2.2
   - Referencias 100% validas
   - Funciones 100% documentadas
   - Compliance >=85%
   - 0 errores criticos

4. **Checklist Manual**: Completado
   - Ejemplos ejecutables: SI
   - Navegacion funciona: SI
   - Contenido significativo: SI
   - Naming consistente: SI

5. **Sin Dependencias de Correccion**:
   - No se necesitan scripts de fix
   - Estructura se crea correctamente desde inicio
   - Metadata sincronizada automaticamente

### Certificacion Final

Cuando TODOS los criterios se cumplen:

```
================================================================
         FRAMEWORK AGENTIC TASK v2.2 - BASELINE CERTIFICADO
================================================================

Certifico que el Framework Agentic Task v2.2 ha pasado todas
las validaciones de calidad, consistencia y compliance.

El framework esta LISTO para:
  - Uso en produccion
  - Migracion a Forge v1.0
  - Referencia como baseline estable

Fecha de certificacion: [fecha]
Validado por: Suite automatica v1.0
Proyecto de referencia: [project-id]
Metricas: 42 validaciones pasadas

================================================================
```

---

## RESUMEN DE ARCHIVOS GENERADOS

```
tests/
├── validate_docs.py           # Validador de documentacion (350 lineas)
├── validate_code.py           # Validador de codigo (280 lineas)
├── validate_structure.py      # Validador de estructura (380 lineas)
└── validate_all.py            # Suite maestra (200 lineas)

Total: 1,210 lineas de codigo de validacion
```

**Capacidades**:
- Validaciones: 42 automaticas
- Lineas validadas: ~5,000 (docs + codigo)
- Archivos validados: ~60
- Tiempo de ejecucion: <30 segundos
- Cobertura: Documentacion, Codigo, Estructura

**Extensible**:
- Agregar nuevas validaciones es simple
- Modular (cada validador es independiente)
- Reutilizable para otros proyectos
- CI/CD ready

---

## CONCLUSION

Esta suite de validacion provee validacion automatica, exhaustiva y reproducible del Framework v2.2 baseline.

**Beneficios**:
- Detecta problemas antes de que lleguen a produccion
- Asegura consistencia entre docs-codigo-estructura
- Facilita migracion segura a Forge v1.0
- Mantiene calidad del framework a lo largo del tiempo

**Uso Recomendado**:
1. Ejecutar antes de cada release
2. Ejecutar despues de cambios significativos
3. Integrar en CI/CD
4. Usar como gate de calidad

**Proximos Pasos**:
1. Ejecutar suite en proyecto COVID actual
2. Aplicar correcciones necesarias
3. Iterar hasta lograr PASS
4. Certificar baseline limpio
5. Proceder con confianza a Forge v1.0

---

**Suite creada**: 2025-12-27
**Version**: 1.0
**Mantenedor**: QA Lead Especializado
**Framework Target**: Agentic Task Framework v2.2
