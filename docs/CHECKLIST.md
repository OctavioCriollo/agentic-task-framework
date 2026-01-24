# Framework Validation Checklist v2.2

Manual reference for coordinators to ensure compliance with framework standards.

## Pre-Flight Checklist: Research Workflow

### Before Starting

- [ ] ProjectManager imported: `from core.project_manager import ProjectManager`
- [ ] FrameworkValidator imported: `from core.framework_validator import FrameworkValidator`
- [ ] User request clearly understood
- [ ] Project scope defined

### Phase 1: Project Setup

- [ ] Project name follows convention: [topic]-[date] or descriptive-kebab-case
- [ ] User request documented verbatim
- [ ] Project created using ProjectManager.create_project()
- [ ] Project structure validated: project_info.json, context.md, tasks/, synthesis/ exist
- [ ] Project ID recorded for session

### Phase 2: Task Design

For EACH task:

- [ ] Task name follows convention: [action]-[topic]-[details] (kebab-case)
- [ ] Task name validated with regex: ^[a-z0-9]+(-[a-z0-9]+)+$
- [ ] Prompt includes Layer 1 (Conversational Context):
  - [ ] User request quoted
  - [ ] Disclaimers included
  - [ ] Project overview provided
  - [ ] Supervision notes added
- [ ] Prompt includes Layer 2 (Technical Specification):
  - [ ] Agent role defined
  - [ ] Specific objectives listed
  - [ ] Methodology steps outlined
  - [ ] Deliverables specified
  - [ ] Output location EXPLICITLY stated (CRITICAL)
- [ ] Prompt length >= 200 characters
- [ ] Prompt style: Professional, no emojis, no decorative symbols
- [ ] Task description written
- [ ] Task created using ProjectManager.create_task()
- [ ] Report path obtained: ProjectManager.get_task_report_path()
- [ ] Report path added to prompt

### Phase 3: Pre-Launch Validation

For EACH task:

- [ ] Validation executed: `validator.validate_agent_launch(project_id, task_name)`
- [ ] Validation passed (if failed, review errors and fix)
- [ ] task_info.json exists in task directory
- [ ] prompt.md exists in task directory
- [ ] Agent prompt references correct report path

### Phase 4: Agent Launch

- [ ] Task tool used with appropriate subagent_type
- [ ] Prompt is executive (tells agent what to do, where to save)
- [ ] Background execution enabled (run_in_background=True if needed)
- [ ] Task ID recorded
- [ ] TodoWrite updated to track agent progress

### Phase 5: Monitoring

- [ ] Agent progress monitored with TaskOutput (non-blocking)
- [ ] Errors/blocks addressed promptly
- [ ] User informed of progress without excessive detail

### Phase 6: Completion

For EACH completed task:

- [ ] Report file exists at expected path
- [ ] Report content reviewed
- [ ] Task registered: ProjectManager.register_task_report()
- [ ] task_info.json updated with status='completed'
- [ ] TodoWrite updated to mark task completed

### Phase 7: Synthesis

- [ ] All task reports read and analyzed
- [ ] Key findings identified
- [ ] Synthesis document created in synthesis/ directory
- [ ] User presented with high-level summary
- [ ] Follow-up questions addressed

## Common Validation Failures

### Task Name Invalid

**Error:** "Task name does not follow convention: [action]-[topic]-[details]"

**Fix:**
- Use kebab-case (lowercase, hyphens only)
- Include action verb (analizar, investigar, evaluar, revisar)
- Include topic (selectividad, farmacocinetica, toxicologia)
- Include details if needed (clo2, covid-19, in-vitro)
- Examples: analizar-selectividad-clo2, investigar-farmacocinetica-oral

### Prompt Missing Layer 1 or Layer 2

**Error:** "Prompt does not follow 2-layer architecture"

**Fix:**
- Layer 1 must include: User request context, disclaimers, project overview
- Layer 2 must include: Role, objectives, methodology, deliverables
- Check for keywords: "contexto", "usuario solicit", "objetivo", "metodologia"

### Missing Metadata Files

**Error:** "Missing task_info.json" or "Missing prompt.md"

**Fix:**
- ALWAYS use ProjectManager.create_task() to create tasks
- NEVER create task directories manually
- NEVER save prompts to /tmp/ and launch agents directly
- ProjectManager auto-creates metadata files

### Report Path Not Specified

**Error:** Agent saves files in wrong location or asks where to save

**Fix:**
- ALWAYS use ProjectManager.get_task_report_path() before launching
- ALWAYS add report path to prompt explicitly
- Include in prompt: "IMPORTANTE: Debes guardar tu reporte final en: [path]"

### ProjectManager Not Used

**Error:** "Task must be created using ProjectManager.create_task()"

**Fix:**
- Import ProjectManager at start of research workflow
- Create project first: pm.create_project()
- Create tasks: pm.create_task()
- Get report paths: pm.get_task_report_path()
- Register completion: pm.register_task_report()

## Writing Style Validation

### Emojis and Symbols

**INCORRECT:**
```
Task completed successfully
Research findings ready
WARNING: Check this
ERROR: Failed validation
```

**CORRECT:**
```
COMPLETADO: Tarea finalizada exitosamente
LISTO: Hallazgos de investigacion disponibles
ADVERTENCIA: Revisar este aspecto
ERROR: Validacion fallida
```

**Rules:**
- No checkmarks, X marks, warning symbols, stars
- No arrows, boxes, decorative Unicode
- Use plain text status indicators: COMPLETADO, ERROR, ADVERTENCIA, INFO
- Use markdown formatting (bold, headers, lists) instead of symbols

## Quick Commands

### Validate Project Structure

```bash
python core/framework_validator.py validate-project [project-id]
```

### Get Validation Report

```bash
python core/framework_validator.py report
```

### Check Task Before Launch

```bash
python core/framework_validator.py check-task [project-id] [task-name]
```

### List Projects

```bash
python core/project_manager.py list
```

### Get Project Details

```bash
python core/project_manager.py get [project-id]
```

## Troubleshooting

### Validator Not Found

**Symptom:** "ModuleNotFoundError: No module named 'core.framework_validator'"

**Fix:**
- Ensure working directory is framework root
- Verify core/framework_validator.py exists
- Check Python path includes framework root

### Validation Always Fails

**Symptom:** All validations return False

**Fix:**
- Check .framework_session.json exists and is valid JSON
- Review validation_log in session file
- Run validator in debug mode with print statements
- Verify workflow_templates.json is valid

### Tasks Created But No Metadata

**Symptom:** Task directories exist but missing task_info.json or prompt.md

**Fix:**
- Tasks were NOT created with ProjectManager
- Recreate tasks using proper workflow
- Or manually create missing files (not recommended)

## Framework Version

**Current Version:** 2.2

**Validation System:** Framework Validation System (FVS)

**Last Updated:** 2025-12-26

## References

- CLAUDE.md: Complete coordinator instructions
- README.md: User-facing documentation
- core/framework_validator.py: Validation implementation
- core/workflow_templates.json: Workflow definitions
- core/project_manager.py: Project management implementation
