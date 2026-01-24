# Archive - Proyectos Históricos

Este directorio contiene proyectos históricos, de desarrollo, y auditorías que ya cumplieron su propósito pero se conservan como referencia.

---

## Estructura

```
archive/
└── audits/                    # Auditorías del framework
    └── auditor-a-framework-v2-2-20251227-222837/
```

---

## Auditorías

### auditor-a-framework-v2-2-20251227-222837
**Fecha:** 2025-12-27
**Propósito:** Auditoría completa del Framework v2.2

**Tareas ejecutadas:**
1. **auditoria-documentacion** - Auditoría de documentación core
2. **auditoria-codigo** - Auditoría de código Python
3. **auditoria-estructura** - Auditoría de estructura de proyectos
4. **auditoria-arquitectura-sistema** - Auditoría arquitectónica
5. **identificacion-inconsistencias** - Análisis cross-system
6. **plan-correccion** - Plan detallado de correcciones (42 correcciones)
7. **validacion-final** - Suite de validación post-corrección

**Resultados:**
- Identificadas 42 inconsistencias en 4 categorías
- Generado plan de correcciones en 4 fases
- Creada suite de validación completa

**Estado:** ✅ Completada
- FASE 1: 8/8 correcciones aplicadas (Críticas)
- FASE 2: 5/15 correcciones aplicadas (Altas)
- Framework validado y operativo

**Reportes importantes:**
- `plan-correccion/reports/plan_completo_correcciones.md`
- `identificacion-inconsistencias/reports/reporte_inconsistencias.md`
- `validacion-final/reports/suite_validacion.md`

---

## Política de Archive

**Qué se archiva:**
- ✅ Proyectos de auditoría completados
- ✅ Proyectos de desarrollo/testing históricos
- ✅ Proyectos que generaron documentación valiosa
- ✅ Proyectos de investigación completados

**Qué NO se archiva:**
- ❌ Proyectos productivos activos (van en `projects/`)
- ❌ Proyectos temporales sin valor histórico (se eliminan)

**Cuándo archivar:**
- Proyecto completó su propósito
- Generó documentación/reportes valiosos
- No es necesario para trabajo diario
- Puede ser útil como referencia futura

---

## Acceso a Proyectos Archivados

Para consultar un proyecto archivado:

```bash
# Listar proyectos archivados
ls -la archive/audits/

# Ver estructura de un proyecto
ls -la archive/audits/auditor-a-framework-v2-2-20251227-222837/

# Leer un reporte
cat archive/audits/auditor-a-framework-v2-2-20251227-222837/tasks/plan-correccion/reports/plan_completo_correcciones.md
```

---

## Mantenimiento

**Revisar periódicamente:**
- Proyectos que llevan >6 meses archivados
- Reportes que ya fueron incorporados al framework
- Contenido que puede ser eliminado definitivamente

**Comprimir si es necesario:**
```bash
# Comprimir proyecto antiguo
tar -czf archivo-proyecto-fecha.tar.gz archive/audits/proyecto-antiguo/
rm -rf archive/audits/proyecto-antiguo/
```

---

**Última actualización:** 2026-01-02
**Proyectos archivados:** 1
**Espacio usado:** ~varios MB
