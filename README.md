# Agentic Task Framework

Sistema profesional de gestión de tareas agénticas con múltiples agentes especializados y memoria persistente.

## Descripción

Este framework implementa un sistema multi-agente donde:
- **Coordinador Principal**: Mantiene conversación de alto nivel y visión general
- **Agentes Especializados**: Se crean dinámicamente para tareas específicas que requieren profundidad
- **Memoria Persistente**: Sistema automático de respaldo y recuperación de contexto
- **Prompts Dinámicos**: Cada tarea recibe un prompt diseñado específicamente para sus necesidades

## Arquitectura

```
agentic-task-framework/
├── start_coordinator.sh          # 🚀 Lanzador del coordinador principal
├── CLAUDE.md                     # 🧠 Memoria del coordinador
├── .claude/                      # ⚙️ Configuración
│   ├── settings.json            # Configuración compartida
│   └── settings.local.json      # Configuración personal
├── core/                         # 🔧 Núcleo del sistema
│   ├── task_manager.py          # Gestor de tareas
│   ├── task_launcher.sh         # Lanzador de agentes
│   ├── init_memory.sh           # Inicialización de memoria
│   └── update_memory.sh         # Actualización de memoria
├── tasks/                        # 📋 Tareas activas
│   └── [task-id]/               # Cada tarea es independiente
│       ├── CLAUDE.md            # Memoria de la tarea
│       ├── .memory_backups/     # Backups automáticos
│       ├── context/             # Contexto inicial
│       └── output/              # Resultados
├── .memory_backups/              # 💾 Backups del coordinador
└── .task_registry.json           # 📊 Registro de tareas
```

## Características

### ✨ Coordinador Inteligente

El coordinador NO es un bot con templates rígidos. Es un agente inteligente que:
- Conversa naturalmente
- Analiza necesidades específicas
- Diseña prompts personalizados para cada tarea
- Valida diseños con el usuario
- Mantiene visión general del proyecto

### 🔒 Memoria Persistente

Sistema robusto de preservación de contexto:
- Backups automáticos al iniciar y cerrar sesiones
- Recuperación automática de cierres accidentales
- Historial completo de sesiones
- Sin pérdida de información

### 🤖 Multi-Agente

Arquitectura distribuida:
- Múltiples agentes trabajando en paralelo
- Cada tarea con su contexto independiente
- Sin contaminación de contexto entre tareas
- Escalabilidad ilimitada

### 📝 Prompts Dinámicos

No usa templates estáticos:
- Cada prompt se diseña específicamente para la tarea
- Considera contexto, nivel de expertise, objetivos
- Validación con el usuario antes de ejecutar

## Instalación y Uso

### Primera Vez - Todo Automático

```bash
# Solo ejecuta esto:
./start_coordinator.sh
```

**El script detecta primera ejecución y configura TODO automáticamente:**
- ✓ Detecta Python en tu sistema
- ✓ Crea entorno virtual automáticamente
- ✓ Instala dependencias (si las hay)
- ✓ Activa el entorno virtual
- ✓ Inicializa memoria del coordinador
- ✓ Lanza Claude Code

**NO necesitas ejecutar ningún script de setup.** Todo se configura solo.

### Siguiente Veces

```bash
# Mismo comando:
./start_coordinator.sh
```

**El script detecta que ya está configurado:**
- ✓ Activa entorno virtual (silenciosamente)
- ✓ Carga memoria del coordinador
- ✓ Crea backup de seguridad
- ✓ Lanza Claude Code

---

## Requisitos

**Solo necesitas:**
- Python 3.8 o superior instalado
- Git Bash (Windows) o Terminal (Linux/Mac)

**El framework se encarga del resto automáticamente.**

---

## Inicio Rápido

### Uso Normal

```bash
./start_coordinator.sh
```

### 2. Conversación con el Coordinador

```
Tú: "Quiero aprender sobre arquitectura de microservicios"

Coordinador: [Conversación general, visión amplia]

Tú: "Quiero profundizar en patrones de comunicación entre servicios"

Coordinador: "Entiendo que quieres profundizar en patrones de
              comunicación. Para diseñar la tarea óptima:

              - ¿Te interesa más teoría o implementación?
              - ¿Qué tecnologías usas? (gRPC, REST, mensajería...)
              - ¿Qué nivel de profundidad buscas?"

Tú: [Respondes detalles]

Coordinador: "Perfecto. He diseñado un plan para esta tarea:

              [Muestra diseño del prompt]

              ¿Procedemos?"

Tú: "Sí"

Coordinador: [Crea tarea y lanza nueva terminal]
             ✓ Tarea: patrones-comunicacion-microservicios-a1b2c3d4
             ✓ Agente especializado lanzado
```

### 3. Trabajo en Paralelo

Mientras el agente especializado trabaja en la tarea específica:
- Puedes continuar conversando con el coordinador
- Puedes crear más tareas especializadas
- Cada una trabaja independientemente

## Gestión de Tareas

### Listar Tareas Activas

```bash
python3 core/task_manager.py list
```

Output:
```
============================================================
Tareas Activas: 3
============================================================

1. patrones-comunicacion-microservicios (patrones-comunicacion-microservicios-a1b2c3d4)
   Tipo: technical-analysis
   Estado: active
   Creada: 2025-11-24T10:30:45
   Directorio: tasks/patrones-comunicacion-microservicios-a1b2c3d4/

2. kubernetes-deployment (kubernetes-deployment-e5f6g7h8)
   Tipo: implementation
   Estado: active
   Creada: 2025-11-24T11:15:20
   Directorio: tasks/kubernetes-deployment-e5f6g7h8/

3. database-optimization (database-optimization-i9j0k1l2)
   Tipo: research
   Estado: active
   Creada: 2025-11-24T12:00:10
   Directorio: tasks/database-optimization-i9j0k1l2/
```

### Ver Detalles de una Tarea

```bash
python3 core/task_manager.py get [task-id]
```

### Actualizar Estado de Tarea

```bash
python3 core/task_manager.py update-status [task-id] completed
```

## Sistema de Memoria

### Coordinador Principal

**Ubicación**: `CLAUDE.md`

Contiene:
- Instrucciones permanentes del coordinador
- Principios de operación
- Proceso de gestión de tareas
- Historial de sesión (actualizado automáticamente)

**Backups**: `.memory_backups/CLAUDE_*.md`

### Tareas Especializadas

**Ubicación**: `tasks/[task-id]/CLAUDE.md`

Contiene:
- Prompt diseñado específicamente para esa tarea
- Contexto específico
- Instrucciones detalladas
- Progreso (actualizado automáticamente)

**Backups**: `tasks/[task-id]/.memory_backups/CLAUDE_*.md`

### Recuperación de Cierres Accidentales

Si cierras una terminal por accidente:
- ✓ La memoria se guarda automáticamente
- ✓ Se crea backup final
- ✓ Próxima vez que abras, todo el contexto está preservado

## Flujo de Trabajo Completo

### Ejemplo: Investigación sobre Machine Learning

```
1. Inicias coordinador:
   $ ./start_coordinator.sh

2. Conversación general:
   Tú: "Estoy aprendiendo ML"
   Coordinador: [Conversación amplia sobre ML]

3. Necesitas profundizar:
   Tú: "Quiero entender transformers en detalle"
   Coordinador: [Hace preguntas de clarificación]

4. Coordinador diseña tarea:
   - Analiza tus necesidades
   - Diseña prompt específico
   - Valida contigo

5. Tarea creada:
   ✓ Nueva terminal abierta
   ✓ Agente especializado trabajando en transformers
   ✓ Tú sigues en terminal principal

6. Trabajo en paralelo:
   - Terminal principal: Visión general, otras consultas
   - Terminal de tarea: Análisis profundo de transformers

7. Más tareas:
   Tú: "También quiero investigar GANs"
   Coordinador: [Crea segunda tarea]
   ✓ Otra terminal para GANs

8. Al cerrar:
   - Cada terminal guarda su memoria
   - Backups automáticos
   - Contexto preservado
```

## Comandos Útiles

### Crear Tarea Manualmente

```bash
# Preparar prompt en archivo
cat > /tmp/my_task_prompt.md << 'EOF'
# Tarea: Mi Investigación

## Objetivo
[...]

## Metodología
[...]
EOF

# Crear tarea
python3 core/task_manager.py create \
  --name "mi-investigacion" \
  --type "research" \
  --prompt "/tmp/my_task_prompt.md" \
  --description "Investigación sobre tema X"
```

### Ver Estructura de Tareas

```bash
ls -la tasks/
```

### Ver Backups

```bash
ls -la .memory_backups/
ls -la tasks/[task-id]/.memory_backups/
```

## Principios del Sistema

### Coordinador

**✓ Dinámico e inteligente**: No sigue scripts rígidos
**✓ Conversacional**: Interactúa naturalmente
**✓ Analítico**: Entiende antes de actuar
**✓ Validación**: Confirma diseños con usuario
**✓ Visión general**: Mantiene contexto principal

### Tareas

**✓ Especializadas**: Cada una enfocada en tema específico
**✓ Independientes**: Contextos aislados
**✓ Prompts únicos**: Diseñados dinámicamente
**✓ Memoria propia**: Sin interferencia

### Sistema

**✓ Robusto**: Recuperación automática
**✓ Escalable**: Ilimitadas tareas en paralelo
**✓ Profesional**: Arquitectura bien diseñada
**✓ Automático**: Mínima intervención manual

## Casos de Uso

### Investigación Técnica
- Investigar múltiples tecnologías en paralelo
- Cada una con agente especializado
- Comparaciones centralizadas en coordinador

### Desarrollo de Software
- Coordinador: Arquitectura general
- Tareas: Implementación de componentes específicos
- Cada componente con su contexto aislado

### Aprendizaje
- Coordinador: Ruta de aprendizaje general
- Tareas: Profundización en temas específicos
- Construcción gradual de conocimiento

### Análisis de Datos
- Coordinador: Visión general del proyecto
- Tareas: Análisis específicos (limpieza, visualización, modelado)
- Resultados coordinados

## Solución de Problemas

### Error: "mintty not found"

El script intentará usar bash directo como fallback. Si eso falla:
```bash
# Edita core/task_launcher.sh
# Cambia mintty por tu emulador de terminal preferido
```

### Tarea no se lanza

Verifica:
```bash
# Permisos de ejecución
chmod +x core/task_launcher.sh
chmod +x start_coordinator.sh

# Python disponible
python3 --version
```

### Memoria no se guarda

Verifica:
```bash
# Permisos de escritura
ls -la .memory_backups/

# Script de actualización
bash core/update_memory.sh .
```

## Mantenimiento

### Limpiar Backups Antiguos

```bash
# Mantener solo últimos 50 backups
cd .memory_backups
ls -t CLAUDE_*.md | tail -n +51 | xargs rm -f
```

### Archivar Tareas Completadas

```bash
# Mover tareas completadas a archivo
mkdir -p tasks_archive
mv tasks/[task-id] tasks_archive/
```

### Limpiar Registro de Tareas

```bash
# Editar .task_registry.json
# Remover entradas de tareas archivadas
```

## Contribución y Personalización

### Modificar Instrucciones del Coordinador

Edita `CLAUDE.md` con tus propias instrucciones, principios y workflows.

### Añadir Hooks Personalizados

Edita `.claude/settings.json` para añadir hooks en SessionStart, SessionEnd, etc.

### Personalizar Estructura de Tareas

Modifica `core/task_manager.py` en el método `create_task()` para cambiar la estructura de directorios de tareas.

## Licencia

MIT

## Soporte

Para problemas o preguntas:
- Consulta el CLAUDE.md para entender el sistema
- Revisa los backups en `.memory_backups/`
- Verifica el registro de tareas en `.task_registry.json`

---

**Framework creado con principios de Agentic AI**
Inspirado en los patrones de Andrew Ng: Reflection, Planning, Tool Use, Multi-Agent Collaboration
