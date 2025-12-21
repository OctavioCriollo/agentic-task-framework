# Framework Agéntico - Sistema de Investigación Multi-Agente

> **Versión 2.0** - Basado en Task Tool de Claude Code

## ¿Qué es esto?

Un framework para realizar **investigaciones complejas** usando **múltiples agentes especializados** coordinados por un agente central.

## Arquitectura

```
      [USUARIO]
         ↕
   [COORDINADOR]  ← Tú conversas aquí (ventana principal)
         ↓
   [Task Tool]
         ↓
  [AGENTES en Background]
    - Agente 1: Química
    - Agente 2: Bioquímica
    - Agente 3: Virología
    - Agente 4: ...
         ↓
   [Reportan al Coordinador]
         ↓
   [Coordinador Sintetiza]
         ↓
      [USUARIO]
```

## Cómo Usar

### 1. Iniciar el Framework

```bash
./start_coordinator.sh
```

Esto lanza Claude Code como **coordinador principal**. Todo funciona desde esta única ventana.

### 2. Solicitar una Investigación

Simplemente pide lo que necesitas:

```
Tú: "Quiero investigar [TEMA] en profundidad"
```

El coordinador te propondrá una estrategia con agentes especializados.

### 3. Aprobar y Monitorear

```
Coordinador: "Propongo 3 agentes:
              1. [Especialidad 1]
              2. [Especialidad 2]
              3. [Especialidad 3]
              ¿Procedemos?"

Tú: "Sí"

Coordinador: "Agentes lanzados en background.
              Te informo cuando completen..."
```

### 4. Recibir Resultados

El coordinador te presentará una **síntesis integrada** de todos los hallazgos.

## Principios Clave

1. **Una Sola Ventana:** Todo se coordina desde la ventana del coordinador
2. **Sin Ventanas Nuevas:** Los agentes trabajan en background (invisible)
3. **Coordinación Centralizada:** El coordinador es tu único punto de contacto
4. **Síntesis Inteligente:** No recibes dumps de datos, sino hallazgos integrados

## Qué NO Hacer

### ❌ NO uses task_manager.py

```bash
# ❌ INCORRECTO - Sistema obsoleto
python core/task_manager.py create ...
```

El sistema viejo abría ventanas separadas. **Ya no se usa.**

### ❌ NO intentes abrir múltiples instancias de Claude Code

Todo se maneja desde UNA sola instancia (el coordinador).

## Tipos de Investigaciones Soportadas

- **Investigación Científica:** Múltiples perspectivas (química, biología, clínica)
- **Análisis Técnico:** Arquitectura, código, sistemas
- **Investigación Comparativa:** Benchmarks, alternativas, trade-offs
- **Síntesis de Literatura:** Papers, artículos, documentación
- **Análisis de Datos:** Procesamiento, estadísticas, visualización

## Ejemplo de Uso Real

```
Usuario: "Investiga efectividad del dióxido de cloro contra COVID-19"

Coordinador: "Esto requiere análisis multidisciplinario.
              Propongo 4 agentes:
              1. Químico: estructura molecular, mecanismos
              2. Bioquímico: toxicología, efectos en humanos
              3. Virólogo: mecanismos antivirales, variantes
              4. Clínico: evidencia de ensayos, estudios

              ¿Procedemos?"

Usuario: "Sí"

Coordinador: [Lanza 4 agentes en background]
              "Agentes trabajando..."

              [Agentes investigan en paralelo]
              [Coordinador recibe resultados]
              [Sintetiza hallazgos]

              "Investigación completada.

              ## Química Molecular
              [Síntesis del Agente 1]

              ## Bioquímica y Toxicología
              [Síntesis del Agente 2]

              ## Virología
              [Síntesis del Agente 3]

              ## Evidencia Clínica
              [Síntesis del Agente 4]

              ## Conclusión Integrada
              [Síntesis combinada de todos los hallazgos]

              ¿Quieres profundizar en algún aspecto?"
```

## Estructura del Proyecto

```
agentic-task-framework/
├── start_coordinator.sh          # Punto de entrada (usa esto)
├── CLAUDE.md                      # Instrucciones del coordinador
├── README.md                      # Este archivo
├── .claude/
│   └── settings.json             # Configuración de Claude Code
├── core/                          # Scripts del sistema
│   ├── task_manager.py           # DEPRECATED - No usar
│   ├── task_launcher.sh          # DEPRECATED - No usar
│   └── ...
└── .memory_backups/              # Backups automáticos
```

## Ventajas de Este Sistema

✅ **Simplicidad:** Una sola ventana, una sola conversación
✅ **Escalabilidad:** Lanza tantos agentes como necesites en paralelo
✅ **Organización:** El coordinador mantiene la visión general
✅ **Eficiencia:** Contexto pesado delegado a agentes especializados
✅ **Claridad:** Ves progreso y resultados en formato sintetizado

## Troubleshooting

### "Los agentes no están ejecutando, solo preguntan"

**Solución:** El coordinador debe diseñar prompts **ejecutivos**, no conversacionales. Debería incluir "INICIA AHORA" y dar instrucciones claras de HACER, no preguntar.

### "No veo progreso de los agentes"

**Solución:** El coordinador usa `TodoWrite` para trackear estado. Si no lo ves, pídeselo: "¿Qué están haciendo los agentes?"

### "Quiero ver los resultados detallados"

**Solución:** El coordinador te presenta síntesis. Si quieres detalles: "¿Puedes mostrarme los resultados completos del Agente [N]?"

## Soporte

- **Documentación completa:** Ver `CLAUDE.md`
- **Issues:** Reporta problemas en el repositorio
- **Versión:** 2.0 (Task Tool Based)
- **Última actualización:** 2025-12-21

---

**¡Comienza tu investigación ahora!**

```bash
./start_coordinator.sh
```
