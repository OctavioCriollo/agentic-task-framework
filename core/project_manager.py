#!/usr/bin/env python
"""
Project Manager - Sistema de Gestion de Outputs

Este modulo gestiona la estructura de proyectos y outputs de agentes.
Usado por el coordinador para organizar resultados de investigaciones.
"""

import os
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import sys
from core.__version__ import get_version, get_version_full

# Configure logging
logger = logging.getLogger(__name__)

# Custom exceptions para validacion de outputs
class OutputNotFoundError(Exception):
    """Raised when output file does not exist"""
    pass

class InvalidOutputError(Exception):
    """Raised when output content is invalid"""
    pass

class DuplicateReportError(Exception):
    """Raised when report is already registered"""
    pass


class ValidationError(Exception):
    """Raised when validation fails"""
    pass


class ProjectManager:
    """
    Gestiona proyectos del framework agentico.

    Estructura de proyecto (v2.2):
        projects/
        └── [project-id]/
            ├── project_info.json      # Metadata del proyecto
            ├── context.md             # Contexto inicial del usuario
            ├── tasks/                 # Tareas ejecutadas por agentes
            │   ├── [nombre-tarea-descriptivo]/
            │   │   ├── task_info.json
            │   │   ├── prompt.md
            │   │   └── [reporte-descriptivo].md (o reports/)
            │   └── [otra-tarea]/
            │       └── ...
            └── synthesis/             # Sintesis del coordinador
                └── [nombre-descriptivo].md
    """

    def __init__(self, base_dir: str = "projects", log_level: str = 'INFO'):
        """
        Inicializa el gestor de proyectos.

        Args:
            base_dir: Directorio base para proyectos (default: 'projects')
            log_level: Nivel de logging (DEBUG, INFO, WARNING, ERROR)
        """
        # Forzar UTF-8 encoding en Windows para evitar problemas con caracteres especiales
        if sys.platform == 'win32':
            try:
                sys.stdout.reconfigure(encoding='utf-8')
                sys.stderr.reconfigure(encoding='utf-8')
            except AttributeError:
                # Python < 3.7 no tiene reconfigure
                pass

        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)

        # Configurar logging si no está configurado
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=getattr(logging, log_level.upper(), logging.INFO),
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

    def create_project(
        self,
        name: str,
        user_request: str,
        context: Optional[str] = None
    ) -> Dict:
        """
        Crea un nuevo proyecto con estructura completa.

        Args:
            name: Nombre descriptivo del proyecto (ej: "Investigacion ClO2")
            user_request: Solicitud original del usuario
            context: Contexto adicional del proyecto (opcional)

        Returns:
            Dict con informacion del proyecto creado

        Example:
            >>> pm = ProjectManager()
            >>> project = pm.create_project(
            ...     name="Investigacion ClO2",
            ...     user_request="Investiga efectividad contra COVID-19",
            ...     context="Enfoque cientifico neutral..."
            ... )
            >>> print(project['id'])
            'investigacion-clo2-20251222-193045'
        """
        # SECURITY: Validate inputs
        self._validate_identifier(name, "Project name")
        self._validate_identifier(user_request, "User request", max_length=2000)
        if context:
            self._validate_identifier(context, "Context", max_length=10000)

        # Generar ID unico
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        project_name_clean = self._sanitize_name(name)
        project_id = f"{project_name_clean}-{timestamp}"

        # Crear estructura de directorios
        project_dir = self.base_dir / project_id
        project_dir.mkdir(exist_ok=True)

        (project_dir / "tasks").mkdir(exist_ok=True)
        (project_dir / "synthesis").mkdir(exist_ok=True)

        # Crear metadata del proyecto
        project_info = {
            "id": project_id,
            "name": name,
            "created": datetime.now().isoformat(),
            "status": "in_progress",
            "user_request": user_request,
            "context": context,
            "tasks": {},
            "synthesis": None
        }

        # Guardar metadata
        self._save_project_info(project_id, project_info)

        # Guardar contexto si existe
        if context:
            context_file = project_dir / "context.md"
            context_file.write_text(
                self._format_context(user_request, context),
                encoding='utf-8'
            )

        return project_info

    
    def _generate_task_readme(self, task_name: str, description: str) -> str:
        """
        Genera README.md template para tarea.

        Args:
            task_name: Nombre de la tarea
            description: Descripcion de la tarea

        Returns:
            Contenido del README.md
        """
        # Formatear titulo (kebab-case a Title Case)
        title = task_name.replace('-', ' ').title()

        readme = f"""# {title}

## INTRODUCCION

{description}

## CONTENIDO DEL ANALISIS

### Documentos principales

(Los reportes se agregaran cuando la tarea se complete)

## HALLAZGOS CLAVE

(Se completara al finalizar la tarea)

## METODOLOGIA

(Se describira el enfoque usado)

---

**Tarea creada:** {task_name}
**Framework:** v{get_version_full()}
"""
        return readme

    def create_task(
        self,
        project_id: str,
        task_name: str,
        task_description: str,
        prompt: str
    ) -> Dict:
        """
        Crea una nueva tarea dentro de un proyecto.

        Args:
            project_id: ID del proyecto
            task_name: Nombre descriptivo de la tarea (ej: "analisis-quimica-molecular-clo2")
            task_description: Descripcion de lo que hace la tarea
            prompt: Prompt completo usado para el agente

        Returns:
            Dict con informacion de la tarea creada

        Example:
            >>> pm = ProjectManager()
            >>> task = pm.create_task(
            ...     project_id="investigacion-clo2-20251222-193045",
            ...     task_name="analisis-quimica-molecular-clo2",
            ...     task_description="Analisis de quimica molecular del ClO2",
            ...     prompt="[Prompt completo aqui...]"
            ... )
        """
        # SECURITY: Validate inputs (before FrameworkValidator call)
        self._validate_identifier(task_name, "Task name")
        self._validate_identifier(task_description, "Task description", max_length=1000)
        # Note: prompt validation happens via FrameworkValidator below

        # Validación automática antes de crear la tarea
        try:
            from core.framework_validator import FrameworkValidator
            validator = FrameworkValidator(self.base_dir.parent)

            valid, messages = validator.validate_task_creation(
                project_id=project_id,
                task_name=task_name,
                prompt=prompt,
                using_project_manager=True
            )

            if not valid:
                raise ValidationError(
                    f"Task creation failed validation:\n" + "\n".join(messages)
                )
        except ImportError:
            # Si FrameworkValidator no está disponible, continuar sin validar
            logger.warning("FrameworkValidator not available, skipping validation")

        task_name_clean = self._sanitize_name(task_name)

        # Crear directorio de la tarea
        task_dir = self.base_dir / project_id / "tasks" / task_name_clean
        task_dir.mkdir(parents=True, exist_ok=True)

        # Crear reports/ subdirectory (v2.2 ORGANIZED)
        reports_dir = task_dir / "reports"
        reports_dir.mkdir(exist_ok=True)

        # Generar README.md template
        readme_content = self._generate_task_readme(
            task_name=task_name,
            description=task_description
        )
        readme_path = task_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        # Metadata de la tarea
        task_info = {
            "task_name": task_name,
            "description": task_description,
            "created": datetime.now().isoformat(),
            "status": "in_progress",
            "prompt_file": "prompt.md",
            "reports": []
        }

        # Guardar prompt
        prompt_file = task_dir / "prompt.md"
        prompt_file.write_text(prompt, encoding='utf-8')

        # Guardar task_info
        task_info_file = task_dir / "task_info.json"
        with open(task_info_file, 'w', encoding='utf-8') as f:
            json.dump(task_info, f, indent=2, ensure_ascii=False)

        # Actualizar project_info
        project_info = self.get_project_info(project_id)
        project_info['tasks'][task_name_clean] = task_info
        self._save_project_info(project_id, project_info)

        return task_info

    def update_task_status(self, project_id: str, task_name: str, status: str):
        """
        Actualiza el status de una tarea.

        Args:
            project_id: ID del proyecto
            task_name: Nombre de la tarea
            status: Nuevo status (in_progress, completed, failed)

        Raises:
            ValueError: Si el status es inválido o la tarea no existe

        Example:
            >>> pm = ProjectManager()
            >>> pm.update_task_status(
            ...     project_id="investigacion-20251222-193045",
            ...     task_name="analisis-quimica-molecular-clo2",
            ...     status="completed"
            ... )
        """
        valid_statuses = ['in_progress', 'completed', 'failed']
        if status not in valid_statuses:
            raise ValueError(
                f"Invalid status: '{status}'. Must be one of {valid_statuses}"
            )

        project_info = self.get_project_info(project_id)
        task_name_clean = self._sanitize_name(task_name)

        if task_name_clean not in project_info['tasks']:
            raise ValueError(f"Task not found: '{task_name}' (sanitized: '{task_name_clean}')")

        # Actualizar status
        project_info['tasks'][task_name_clean]['status'] = status

        # Si se marca como completed, agregar timestamp
        if status == 'completed':
            project_info['tasks'][task_name_clean]['completed_at'] = datetime.now().isoformat()

        self._save_project_info(project_id, project_info)

        logger.info("Task '%s' status updated to: %s", task_name, status)

    def register_task_report(self, project_id: str, task_name: str, report_filename: str):
        """
        Registra reporte de tarea VALIDANDO existencia.

        Args:
            project_id: ID del proyecto
            task_name: Nombre de la tarea
            report_filename: Nombre del archivo de reporte

        Raises:
            OutputNotFoundError: Si archivo no existe
            DuplicateReportError: Si reporte ya esta registrado
            InvalidOutputError: Si contenido es invalido
        """
        # SECURITY: Validate report filename for path traversal attacks
        self._validate_report_filename(report_filename)

        # Sanitize task_name for consistency
        task_name_clean = self._sanitize_name(task_name)

        # Cargar task_info
        task_info_path = self.base_dir / project_id / "tasks" / task_name_clean / "task_info.json"

        if not task_info_path.exists():
            raise FileNotFoundError(f"task_info.json no encontrado: {task_info_path}")

        import json
        with open(task_info_path, 'r', encoding='utf-8') as f:
            task_info = json.load(f)

        # VALIDAR que archivo EXISTA
        # Buscar primero en reports/ (v2.2 ORGANIZED) y luego en raiz de tarea (legacy)
        task_dir = self.base_dir / project_id / "tasks" / task_name_clean
        report_path_v22 = task_dir / "reports" / report_filename
        report_path_legacy = task_dir / report_filename

        # Determinar cual path usar
        if report_path_v22.exists():
            report_path = report_path_v22
            relative_path = f"reports/{report_filename}"
        elif report_path_legacy.exists():
            # Backward compatibility: aceptar reportes en raiz de tarea
            report_path = report_path_legacy
            relative_path = report_filename
            logger.warning(
                "Report '%s' found in task root (legacy structure). "
                "Consider moving to reports/ subdirectory for v2.2 ORGANIZED compliance.",
                report_filename
            )
        else:
            raise OutputNotFoundError(
                f"Reporte no encontrado en:\n"
                f"  - {report_path_v22} (v2.2 ORGANIZED)\n"
                f"  - {report_path_legacy} (legacy)\n"
                f"Tarea: {task_name}\n"
                f"Proyecto: {project_id}"
            )

        # VALIDAR contenido minimo
        content = report_path.read_text(encoding='utf-8')
        if len(content.strip()) < 100:
            raise InvalidOutputError(
                f"Reporte muy corto (< 100 chars): {report_path}"
            )

        # VALIDAR no duplicacion
        if "reports" not in task_info:
            task_info["reports"] = []

        # Verificar duplicacion usando relative_path o filename (backward compatibility)
        if relative_path in task_info["reports"] or report_filename in task_info["reports"]:
            raise DuplicateReportError(
                f"Reporte ya registrado: {report_filename} (stored as {relative_path})"
            )

        # Registrar usando relative path consistente
        task_info["reports"].append(relative_path)

        # Guardar
        with open(task_info_path, 'w', encoding='utf-8') as f:
            json.dump(task_info, f, indent=2, ensure_ascii=False)

        return task_info

    
    def get_task_prompt_path(self, project_id: str, task_name: str) -> str:
        """
        Obtiene la ruta donde se guardo el prompt de una tarea.

        Args:
            project_id: ID del proyecto
            task_name: Nombre de la tarea

        Returns:
            Ruta absoluta al archivo prompt.md
        """
        task_name_clean = self._sanitize_name(task_name)
        return str(self.base_dir / project_id / "tasks" / task_name_clean / "prompt.md")

    def get_task_report_path(
        self,
        project_id: str,
        task_name: str,
        report_filename: str
    ) -> str:
        """
        Obtiene la ruta donde un agente debe guardar su reporte.

        Args:
            project_id: ID del proyecto
            task_name: Nombre de la tarea
            report_filename: Nombre descriptivo del reporte

        Returns:
            Ruta absoluta para el archivo de reporte
        """
        task_name_clean = self._sanitize_name(task_name)
        reports_dir = self.base_dir / project_id / "tasks" / task_name_clean / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)  # Asegurar que reports/ existe
        return str(reports_dir / report_filename)

    def get_task_reports_dir(self, project_id: str, task_name: str) -> str:
        """
        Obtiene la ruta del directorio reports/ para multiples archivos.

        Args:
            project_id: ID del proyecto
            task_name: Nombre de la tarea

        Returns:
            Ruta absoluta al directorio reports/
        """
        task_name_clean = self._sanitize_name(task_name)
        reports_dir = self.base_dir / project_id / "tasks" / task_name_clean / "reports"
        reports_dir.mkdir(exist_ok=True)
        return str(reports_dir)

    def get_synthesis_path(
        self,
        project_id: str,
        synthesis_filename: str = "sintesis_final.md"
    ) -> str:
        """
        Obtiene la ruta donde el coordinador debe guardar la sintesis.

        Args:
            project_id: ID del proyecto
            synthesis_filename: Nombre descriptivo de la sintesis

        Returns:
            Ruta absoluta para el archivo de sintesis
        """
        return str(self.base_dir / project_id / "synthesis" / synthesis_filename)

    def register_synthesis(
        self,
        project_id: str,
        synthesis_filename: str
    ):
        """
        Registra que el coordinador completo la sintesis.

        Args:
            project_id: ID del proyecto
            synthesis_filename: Nombre del archivo de sintesis
        """
        project_info = self.get_project_info(project_id)

        # Usar Path.as_posix() para paths portables (forward slashes)
        synthesis_path = Path(self.get_synthesis_path(project_id, synthesis_filename))
        portable_path = synthesis_path.as_posix()

        project_info['synthesis'] = {
            "filename": synthesis_filename,
            "path": portable_path,
            "completed_at": datetime.now().isoformat()
        }
        project_info['status'] = "completed"
        project_info['completed_at'] = datetime.now().isoformat()
        self._save_project_info(project_id, project_info)

    def get_project_info(self, project_id: str) -> Dict:
        """
        Obtiene la informacion de un proyecto.

        Args:
            project_id: ID del proyecto

        Returns:
            Dict con informacion del proyecto

        Raises:
            FileNotFoundError: Si el proyecto no existe
        """
        info_file = self.base_dir / project_id / "project_info.json"
        if not info_file.exists():
            raise FileNotFoundError(f"Proyecto no encontrado: {project_id}")

        with open(info_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_projects(self, status: Optional[str] = None) -> List[Dict]:
        """
        Lista todos los proyectos.

        Args:
            status: Filtrar por estado (in_progress, completed, failed, etc.)

        Returns:
            Lista de diccionarios con informacion de proyectos
        """
        projects = []

        for project_dir in self.base_dir.iterdir():
            if project_dir.is_dir():
                try:
                    info = self.get_project_info(project_dir.name)
                    if status is None or info.get('status') == status:
                        projects.append(info)
                except FileNotFoundError:
                    continue

        # Ordenar por fecha de creacion (mas reciente primero)
        projects.sort(key=lambda x: x['created'], reverse=True)
        return projects

    def get_project_summary(self, project_id: str) -> str:
        """
        Genera un resumen legible de un proyecto.

        Args:
            project_id: ID del proyecto

        Returns:
            String con resumen formateado del proyecto
        """
        info = self.get_project_info(project_id)

        summary = f"""
# Proyecto: {info['name']}

**ID:** {info['id']}
**Estado:** {info['status']}
**Creado:** {info['created']}

## Solicitud del Usuario
{info['user_request']}

## Tareas Completadas
"""

        # Listar tareas
        for task_name, task_data in info['tasks'].items():
            status_icon = "[OK]" if task_data['status'] == 'completed' else "[...]"
            summary += f"- {status_icon} {task_data['description']}\n"
            for report in task_data.get('reports', []):
                summary += f"  - {report}\n"

        # Sintesis
        if info['synthesis']:
            summary += f"\n## Sintesis Final\n[OK] {info['synthesis']['filename']}\n"
        else:
            summary += f"\n## Sintesis Final\n[...] Pendiente\n"

        return summary

    def _sanitize_name(self, name: str) -> str:
        """
        Sanitiza un nombre para uso en filesystem.

        Args:
            name: Nombre a sanitizar

        Returns:
            Nombre sanitizado (lowercase, sin espacios, sin caracteres especiales)
        """
        import re
        # Convertir a lowercase
        name = name.lower()
        # Reemplazar espacios y caracteres especiales con guiones
        name = re.sub(r'[^a-z0-9]+', '-', name)
        # Eliminar guiones al inicio/final
        name = name.strip('-')
        return name

    def _validate_report_filename(self, filename: str) -> None:
        """
        Validate report filename for security.

        Args:
            filename: Report filename to validate

        Raises:
            ValueError: If filename contains path traversal attempts
            ValueError: If filename has invalid extension
            ValueError: If filename is empty or too long
        """
        # Check for empty
        if not filename or not filename.strip():
            raise ValueError("Report filename cannot be empty")

        # Check length (prevent filesystem issues)
        if len(filename) > 255:
            raise ValueError(f"Report filename too long (max 255 chars): {len(filename)}")

        # Check for path traversal attempts
        if '..' in filename:
            raise ValueError(f"Invalid report filename (contains '..'): {filename}")

        if filename.startswith(('/', '\\')):
            raise ValueError(f"Invalid report filename (absolute path): {filename}")

        # Check for directory separators (should be filename only, not path)
        if '/' in filename or '\\' in filename:
            raise ValueError(f"Invalid report filename (contains path separators): {filename}")

        # Whitelist valid extensions
        valid_extensions = {'.md', '.txt', '.json', '.csv', '.html'}
        if not any(filename.endswith(ext) for ext in valid_extensions):
            raise ValueError(
                f"Invalid file extension. Allowed: {', '.join(valid_extensions)}"
            )

    def _validate_identifier(self, identifier: str, field_name: str, max_length: int = 200) -> None:
        """
        Validate project/task identifier for safety.

        Args:
            identifier: The identifier to validate (project name, task name, etc.)
            field_name: Human-readable field name for error messages
            max_length: Maximum allowed length

        Raises:
            ValueError: If identifier is invalid
        """
        # Check for empty
        if not identifier or not identifier.strip():
            raise ValueError(f"{field_name} cannot be empty")

        # Check length
        if len(identifier) > max_length:
            raise ValueError(
                f"{field_name} too long (max {max_length} chars): {len(identifier)}"
            )

        # Check for forbidden characters (filesystem-unsafe)
        forbidden_chars = '<>|:"/\\*?'
        found_forbidden = [char for char in forbidden_chars if char in identifier]
        if found_forbidden:
            raise ValueError(
                f"{field_name} contains forbidden characters: {', '.join(found_forbidden)}"
            )

        # Check for control characters
        if any(ord(char) < 32 for char in identifier):
            raise ValueError(f"{field_name} contains control characters")

    def _save_project_info(self, project_id: str, info: Dict):
        """
        Guarda la informacion de un proyecto.

        Args:
            project_id: ID del proyecto
            info: Diccionario con informacion del proyecto
        """
        info_file = self.base_dir / project_id / "project_info.json"
        with open(info_file, 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=2, ensure_ascii=False)

    def _format_context(self, user_request: str, context: str) -> str:
        """
        Formatea el contexto del proyecto para guardar.

        Args:
            user_request: Solicitud del usuario
            context: Contexto adicional

        Returns:
            String formateado en markdown
        """
        return f"""# Contexto del Proyecto

## Solicitud del Usuario

{user_request}

## Contexto Adicional

{context}

---

**Creado:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""


# ============================================================================
# CLI para uso directo (opcional)
# ============================================================================

def main():
    """CLI para gestion de proyectos."""
    import argparse

    parser = argparse.ArgumentParser(description="Project Manager CLI")
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')

    # Comando: list
    list_parser = subparsers.add_parser('list', help='Listar proyectos')
    list_parser.add_argument('--status', help='Filtrar por estado')

    # Comando: get
    get_parser = subparsers.add_parser('get', help='Ver informacion de proyecto')
    get_parser.add_argument('project_id', help='ID del proyecto')

    args = parser.parse_args()

    pm = ProjectManager()

    if args.command == 'list':
        projects = pm.list_projects(status=args.status)
        print(f"\n{'='*60}")
        print(f"Proyectos encontrados: {len(projects)}")
        print(f"{'='*60}\n")

        for project in projects:
            print(f"[{project['status']}] {project['name']}")
            print(f"  ID: {project['id']}")
            print(f"  Creado: {project['created']}")
            print(f"  Tareas: {len(project.get('tasks', {}))}")
            print()

    elif args.command == 'get':
        try:
            summary = pm.get_project_summary(args.project_id)
            print(summary)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1

    else:
        parser.print_help()
        return 1

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
