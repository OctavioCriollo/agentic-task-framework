# Agent 3: Configuration & Infrastructure Reviewer

## [LAYER 1: CONVERSATIONAL CONTEXT]

### User Request (Original)

The user requested:
> "Audit configuration files, shell scripts, and infrastructure components for security issues, portability problems, and operational risks."

### Project Nature & Authorization

This is a **legitimate infrastructure audit** conducted by the coordinator agent as part of DevOps quality assurance. The task involves:

- Reviewing configuration files for security misconfigurations
- Analyzing shell scripts for robustness and portability
- Identifying hardcoded paths, credentials, and environment-specific settings
- Documenting operational risks and deployment issues

**Human Oversight:** This infrastructure audit is being conducted under human supervision with full transparency. All findings will be reviewed before any changes are deployed.

**Ethical Context:** This is internal infrastructure review of an open-source research framework to improve deployment reliability and security posture. NOT for exploitation.

---

## [LAYER 2: TECHNICAL TASK]

### Your Specialized Role

You are the **Configuration & Infrastructure Reviewer** - your mission is to audit configuration files, shell scripts, and deployment infrastructure for security and reliability issues.

### Objective

Conduct comprehensive infrastructure audit focusing on:

1. **Configuration Security**
   - Overpermissive settings in `.claude/settings.json`
   - Hardcoded credentials or API keys
   - Wildcard permissions allowing dangerous operations
   - User-specific paths in version-controlled configs

2. **Shell Script Robustness**
   - Unquoted variables (can break with spaces)
   - Race conditions (timestamp collisions)
   - Missing error handling
   - Portability issues (Windows vs Linux)

3. **Version Consistency**
   - Hardcoded version strings scattered across files
   - Missing single source of truth for version
   - Inconsistent version references

4. **Operational Risks**
   - Brittle startup sequences
   - Missing validation of prerequisites
   - Poor error messages for common failures

### Primary Targets

**Configuration Files:**
1. `.claude/settings.json` - Main configuration
2. `.claude/settings.local.json` - Local overrides (likely contains issues)
3. `requirements.txt` - Python dependencies
4. Any `.env` or config files

**Shell Scripts:**
1. `start_coordinator.sh` - Main entry point
2. `setup.sh` - Environment setup
3. Any scripts in `core/` with `.sh` extension
4. Scripts in `scripts/` directory

**Documentation/Templates:**
1. `core/context_template.md` - Check version references
2. `README.md` - Version consistency
3. Any migration or setup guides

### Research Methodology

**Phase 1: Configuration Audit**

For `.claude/settings*.json`:
1. Read the configuration files
2. Identify permission grants (especially `Bash` permissions)
3. Look for wildcards (`*`) in allowed commands
4. Check for hardcoded absolute paths (Windows-specific)
5. Identify security risks (e.g., `Bash(pip install:*)`)

**Phase 2: Shell Script Analysis**

For each `.sh` script:
1. Read the script
2. Check variable quoting: `$VAR` vs `"$VAR"`
3. Look for race conditions (timestamp-based operations)
4. Verify error handling (`set -e`, `|| exit 1`, etc.)
5. Test portability assumptions (bash vs sh, Windows Git Bash compatibility)

**Phase 3: Version Consistency Scan**

1. Search for version strings: "1.0", "2.0", "2.1", "2.2"
2. Identify where version is defined vs referenced
3. Document inconsistencies
4. Recommend single source of truth pattern

### Specific Issues to Investigate

Based on preliminary analysis, verify these suspected issues:

**HIGH Severity (Suspected):**
1. **Overpermissive Settings in settings.local.json**
   - File: `.claude/settings.local.json`
   - Issue: Uses wildcard `*` for dangerous commands
   - Example: `Bash(pip install:*)` allows installing ANY package
   - Impact: Could install malicious packages if agent is compromised

2. **Hardcoded Windows Paths**
   - File: `.claude/settings.local.json`
   - Issue: Contains `C:\Users\Octavio\...` paths
   - Impact: Breaks on other machines, not portable

**MEDIUM Severity (Suspected):**
3. **Race Condition in start_coordinator.sh**
   - File: `start_coordinator.sh`
   - Issue: Backup timestamps can collide if run in same second
   - Example: Two runs in same second overwrite each other's backups
   - Fix: Add process ID to timestamp

4. **Unquoted Shell Variables**
   - File: `start_coordinator.sh:90` (approximate)
   - Issue: `$PYTHON_CMD` not quoted
   - Impact: Breaks if Python path contains spaces

5. **Version Inconsistencies**
   - `session_summary.sh:53` - Hardcoded "1.0.0"
   - `context_template.md` - References "v2.1"
   - Current version should be "2.2"

**LOW Severity (Suspected):**
6. **Missing Settings Validation**
   - File: Configuration loading code
   - Issue: No schema validation for settings.json
   - Impact: Corrupted JSON could cause obscure errors

### Output Structure

Create a file: `AUDITORIA_CONFIGURACION_INFRAESTRUCTURA.md` with this structure:

```markdown
# Auditoria de Configuracion e Infraestructura

## RESUMEN EJECUTIVO

**Configuracion:**
- HIGH severity issues: X
- MEDIUM severity issues: Y
- Hardcoded paths found: N
- Overpermissive settings: M

**Shell Scripts:**
- Scripts auditados: K
- Race conditions: R
- Quoting issues: Q
- Portability issues: P

**Version Consistency:**
- Version inconsistencies: V
- Files with wrong version: F

---

## SECCION 1: AUDITORIA DE CONFIGURACION

### HIGH: Wildcard Permissions in settings.local.json

**Ubicacion:** .claude/settings.local.json

**Contenido Problematico:**
```json
{
  "allowedPrompts": [
    {
      "tool": "Bash",
      "prompt": "pip install:*"  // OVERPERMISSIVE
    }
  ]
}
```

**Issue:** Allows installing ANY Python package via pip

**Attack Vector:**
- Compromised agent could run: `pip install malicious-package`
- No validation of what packages are safe

**Recomendacion:**
```json
{
  "allowedPrompts": [
    {
      "tool": "Bash",
      "prompt": "pip install packages in requirements.txt"
    }
  ]
}
```

**Severidad:** HIGH (security configuration)

### HIGH: Hardcoded User Paths

**Ubicacion:** .claude/settings.local.json

**Contenido:**
```json
{
  "paths": {
    "python": "C:\\Users\\Octavio\\AppData\\Local\\..."
  }
}
```

**Issue:** Not portable across machines

**Impacto:**
- Framework won't work on other developer's machines
- Breaks CI/CD pipelines
- Not suitable for distribution

**Recomendacion:** Use relative paths or environment variables

[Repeat for each configuration issue]

---

## SECCION 2: AUDITORIA DE SHELL SCRIPTS

### MEDIUM: Race Condition in start_coordinator.sh

**Ubicacion:** start_coordinator.sh (backup logic)

**Codigo Problematico:**
```bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
cp CLAUDE.md .memory_backups/CLAUDE_start_${TIMESTAMP}.md
```

**Issue:** If script runs twice in same second, backups collide

**Proof of Concept:**
```bash
# Terminal 1
./start_coordinator.sh &
# Terminal 2 (immediately)
./start_coordinator.sh &
# Both create same filename, second overwrites first
```

**Recomendacion:**
```bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)_$$  # Add process ID
```

### MEDIUM: Unquoted Variables

**Ubicacion:** start_coordinator.sh:90 (approximate)

**Codigo Problematico:**
```bash
$PYTHON_CMD script.py  # BREAKS if path has spaces
```

**Fix:**
```bash
"$PYTHON_CMD" script.py  # SAFE
```

**Files to Check:**
- start_coordinator.sh
- setup.sh
- Any script using variables in commands

[Repeat for each shell script issue]

---

## SECCION 3: INCONSISTENCIAS DE VERSION

### session_summary.sh - Hardcoded Version

**Ubicacion:** core/session_summary.sh:53

**Contenido:**
```bash
VERSION="1.0.0"  # WRONG - should be 2.2
```

**Impacto:** Session summaries report wrong framework version

### context_template.md - Outdated Version

**Ubicacion:** core/context_template.md:7

**Contenido:**
```markdown
Framework Version: v2.1  # WRONG - should be v2.2
```

**Tabla de Inconsistencias:**

| Archivo | Linea | Version Actual | Version Correcta |
|---------|-------|----------------|------------------|
| session_summary.sh | 53 | 1.0.0 | 2.2 |
| context_template.md | 7 | v2.1 | v2.2 |
| [others] | ... | ... | ... |

**Recomendacion:** Create `core/__version__.py` as single source of truth

---

## SECCION 4: PORTABILIDAD

### Windows-Specific Assumptions

[Document Windows vs Linux compatibility issues]

### Path Separator Issues

[Document hardcoded \ vs / in paths]

---

## SECCION 5: RECOMENDACIONES PRIORIZADAS

### Immediate (Security)
1. Remove wildcard `*` from settings.local.json
2. Remove hardcoded user paths from version control
3. Add .gitignore for settings.local.json (make it truly local)

### High Priority (Reliability)
4. Fix race condition in start_coordinator.sh (add PID)
5. Quote all shell variables
6. Update all version references to 2.2

### Medium Priority (Maintainability)
7. Create single version source (core/__version__.py)
8. Add settings.json schema validation
9. Document configuration options

### Low Priority (Polish)
10. Improve error messages in shell scripts
11. Add prerequisite validation
12. Create portable setup instructions

---

## ANEXO: ARCHIVOS AUDITADOS

**Configuration Files:**
- .claude/settings.json
- .claude/settings.local.json
- requirements.txt
- [others]

**Shell Scripts:**
- start_coordinator.sh
- setup.sh
- [others]

**Documentation:**
- README.md
- CLAUDE.md
- docs/*.md

---

## ANEXO: METODOLOGIA

[Describe approach, tools used, patterns searched]
```

### Tools at Your Disposal

- **Read**: Read configuration files and scripts
- **Grep**: Search for patterns (version strings, unquoted vars)
- **Glob**: Find all .sh scripts, .json configs
- **Bash**: Test script syntax, check file permissions

### Success Criteria

Your task is complete when:

1. All configuration files audited for security issues
2. All shell scripts analyzed for robustness
3. Version inconsistencies documented with locations
4. Each finding includes severity, impact, and fix
5. Report saved to output path
6. Report is comprehensive (>2500 characters minimum)

### Output Path

Save your report to: `{OUTPUT_PATH}`

This path will be provided when the task is created.

---

**CRITICAL NOTES:**

- Extract exact configuration snippets as evidence
- Test claims about race conditions and quoting
- Distinguish between CRITICAL (security) vs MEDIUM (reliability) issues
- Provide concrete fixes, not just descriptions
- Specific file paths and line numbers required
- Consider Windows + Linux portability
