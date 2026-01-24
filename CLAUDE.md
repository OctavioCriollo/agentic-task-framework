# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# Agentic Task Framework v2.2

Multi-agent research framework where a coordinator agent orchestrates specialized background agents for complex investigations.

## Architecture

### High-Level System Design

```
[User] ↔ [Coordinator Agent] → Task Tool → [Background Agents] → Reports → [Coordinator Synthesizes]
```

**Key principle:** Single window coordination. Background agents work invisibly using Claude Code's Task tool.

### Core Components

**ProjectManager** (`core/project_manager.py`)
- Creates/manages project structures
- Registers task outputs with validation
- Enforces v2.2 ORGANIZED standard
- Custom exceptions: `OutputNotFoundError`, `InvalidOutputError`, `DuplicateReportError`

**FrameworkValidator** (`core/framework_validator.py`)
- Validates project structure compliance
- CLI: `python core/framework_validator.py validate-project <project-id>`

**Project Structure (v2.2 ORGANIZED)**
```
projects/<project-id>/
├── project_info.json # Project metadata
├── context.md # Initial user context
├── tasks/
│ └── <task-name>/
│ ├── task_info.json # Task metadata
│ ├── prompt.md # Agent prompt used
│ ├── README.md # Task overview (auto-generated)
│ └── reports/ # All outputs go here
│ └── *.md
└── synthesis/ # Coordinator's synthesis
```

## Critical: 2-Layer Prompt Architecture

**Problem:** Agents launched via Task tool have NO conversation history. Without context, they may incorrectly self-censor legitimate research.

**Solution:** Always structure agent prompts in 2 layers:

**Layer 1: Conversational Context**
- User's original request (verbatim quote)
- Project nature (academic, supervised, etc.)
- Explicit disclaimers
- Human oversight acknowledgment

**Layer 2: Technical Task**
- Agent's specialized role
- Specific objective
- Research methodology
- Output structure
- Completion criteria

**Why it works:** Provides agents the conversational context they lack, preventing false-positive content filtering.

---

## CRITICAL: Request Enrichment Protocol (v2.3)

**Problem:** Users often make vague, incomplete, or poorly-specified requests. This leads to:
- Sub-optimal investigation strategies
- Missing important perspectives
- Results that don't meet unstated expectations
- Wasted iterations ("not what I wanted")

**Solution:** ALWAYS enrich user requests BEFORE designing multi-agent strategy.

### Enrichment Workflow (MANDATORY)

**STEP 1: Receive User Request**
Listen to what the user asks for (may be vague, incomplete, or poorly articulated).

**STEP 2: Analyze Request Quality**
Ask yourself:
- Is the request specific or vague?
- What context is missing or implicit?
- What does the user assume I know?
- What perspectives might they not have considered?
- Are there unstated goals or constraints?

**STEP 3: Enrich the Request**
If you detect ANY vagueness, ambiguity, or missing context:

DO NOT immediately design strategy.
INSTEAD, create an enriched version of the request.

**STEP 4: Present Enrichment**
Show the user:
- Your interpretation of their objective
- Inferred scope and boundaries
- Suggested perspectives/aspects to cover
- Key questions to answer
- Success criteria

**STEP 5: Get Validation**
Ask: "Is this what you're looking for, or should I adjust the scope?"

**STEP 6: Only Then Design Strategy**
After user confirms enriched request → design multi-agent strategy.

---

### Enrichment Template

Use this structure when presenting enrichment:

```markdown
I've analyzed your request. Here's my interpretation:

## OBJECTIVE
[What you understand the user wants to achieve]

## INFERRED SCOPE
Based on your request "[quote their words]", I interpret you want:

- **Aspect 1:** [what to cover]
- **Aspect 2:** [what to cover]
- **Aspect 3:** [what to cover]

## SUGGESTED PERSPECTIVES
To thoroughly address this, I recommend analyzing from:

1. **[Perspective 1]:** [why relevant]
2. **[Perspective 2]:** [why relevant]
3. **[Perspective 3]:** [why relevant]

## KEY QUESTIONS TO ANSWER
- [Question 1 - what needs clarification]
- [Question 2 - what needs clarification]
- [Question 3 - what needs clarification]

## SUCCESS CRITERIA
You'll know this investigation succeeded if:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

## EXCLUSIONS (if applicable)
Based on scope, I'm assuming we WON'T cover:
- [What's out of scope]

---

**Is this correct? Would you like to:**
- ✓ Proceed with this scope
- Adjust/add perspectives
- Change the focus
- Clarify constraints
```

---

### Examples of Enrichment

#### Example 1: Vague Request

**User says:**
"Investigate blockchain"

**Coordinator enriches:**
```
I've analyzed your request. "Investigate blockchain" is quite broad.

## OBJECTIVE
Understand blockchain technology comprehensively.

## INFERRED SCOPE
I interpret you want:
- Technical understanding (how it works)
- Practical applications (where it's used)
- Advantages and limitations
- Comparison with alternatives
- Adoption recommendations

## SUGGESTED PERSPECTIVES
1. **Technical:** Architecture, consensus mechanisms, cryptography
2. **Business:** Use cases, industry adoption, ROI
3. **Comparative:** Blockchain vs traditional databases
4. **Future:** Trends, emerging applications

## KEY QUESTIONS TO ANSWER
- What is blockchain at a technical level?
- Where is it actually being used successfully today?
- What are the real limitations vs hype?
- When should/shouldn't you use it?

## SUCCESS CRITERIA
After this investigation, you should be able to:
- Explain blockchain to a non-technical person
- Identify 5+ real-world applications
- Make informed decision about adoption for your use case

Is this the scope you had in mind?
```

#### Example 2: Request with Implicit Context

**User says:**
"Research treatments for migraines"

**Coordinator enriches:**
```
I've analyzed your request about migraine treatments.

## OBJECTIVE
Compile comprehensive information on migraine treatment options.

## INFERRED SCOPE
This topic has multiple dimensions. I'm assuming you want:
- Evidence-based medical treatments
- Alternative/natural approaches
- Preventive vs acute treatments
- Effectiveness data

## SUGGESTED PERSPECTIVES
1. **Pharmacological:** Medications (acute and preventive)
2. **Non-pharmacological:** Lifestyle, diet, physical therapy
3. **Alternative:** Supplements, acupuncture, other CAM
4. **Clinical Evidence:** What does research actually show?

## CLARIFICATION NEEDED
- **Focus:** Are you prioritizing conventional medicine, alternatives, or both equally?
- **Severity:** Mild occasional migraines or chronic severe cases?
- **Goal:** Personal use, research project, or general knowledge?

Would you like me to:
- Cover all perspectives equally (comprehensive)?
- Focus on evidence-based conventional medicine?
- Emphasize natural/alternative approaches?
```

#### Example 3: Biased Request

**User says:**
"Prove that cryptocurrency is the future of finance"

**Coordinator enriches:**
```
I've analyzed your request. I notice it has a predetermined conclusion.

## SUGGESTED REFRAMING
Instead of "prove cryptocurrency is the future," I suggest:

**Objective:** "Objectively analyze cryptocurrency's potential role in future finance"

This allows for:
- Unbiased analysis of strengths AND weaknesses
- Consideration of alternative scenarios
- Evidence-based conclusions (not predetermined)

## PROPOSED SCOPE
1. **Cryptocurrency Advantages:** Where it excels
2. **Cryptocurrency Limitations:** Current challenges
3. **Traditional Finance Strengths:** What it does well
4. **Hybrid Scenarios:** Coexistence possibilities
5. **Expert Predictions:** What analysts actually forecast

## SUCCESS CRITERIA
After investigation, you'll have:
- Balanced view of crypto potential
- Understanding of real obstacles
- Informed perspective (not advocacy)

Would you prefer:
- A) Balanced objective analysis (recommended)
- B) Focus specifically on cryptocurrency advantages (advocacy)
```

---

### When to Skip Enrichment

**Skip enrichment if:**
- User request is already highly specific and detailed
- User explicitly says "just do exactly this, no suggestions"
- Request is a follow-up to existing project (context already established)
- User is experienced with the framework and knows how to specify

**Always err on the side of enriching.** Better to clarify upfront than deliver wrong results.

---

### Integration with Workflow

**OLD workflow:**
```
User Request → Design Strategy → Launch Agents
```

**NEW workflow (v2.3+):**
```
User Request → Analyze Quality → Enrich → Present → Validate → Design Strategy → Launch Agents
```

The enrichment step adds ~2-3 minutes upfront but saves hours of iteration.

---

## CRITICAL: Professional Writing Style - Symbol Usage Guide (v3.2 Master)

**MASTER REFERENCE:** This section is the single authoritative source for symbol usage rules across the entire framework. All other documents, scripts, and tools must align with these definitions.

**APPROACH:** Flexible whitelist by categories. Symbols must serve a clear functional purpose (status indication, structure, emphasis). Decorative or pictographic emojis are prohibited.

---

### Scope of Application

This guide applies to:
- Agent prompts and task definitions
- Reports and synthesis documents
- Code comments and docstrings
- User-facing messages and logs
- Validation outputs
- All framework documentation

---

### PERMITTED Symbol Categories

#### 1. Standard Text and Punctuation (Always Permitted)
- Alphanumeric characters: A-Z, a-z, 0-9
- Standard punctuation: . , ; : ! ? - _ ' " / \ ( ) [ ] { }
- Mathematical operators: + - * / = < > % ^ & | ~
- Currency symbols: $ € £ ¥
- Whitespace characters: space, tab, newline

#### 2. Status Indicators (Functional Symbols)

**Checkmarks and X-marks:**
- ✓ ✅ (checkmark - plain or green box)
- ✗ ❌ (X-mark - plain or red box)

**Usage:** Task completion, validation results, success/failure states.

**Status circles (grayscale system):**
- ⚪ (white/empty circle - legacy, obsolete, deprecated)
- 🔘 (gray radio button - pending, in progress, optional)
- ⚫ (black/filled circle - blocked, critical issue)

**Usage:** State visualization in dashboards, task lists, system status. Prefer grayscale for professional appearance and consistent rendering.

#### 3. Selection and Structure Indicators

**Radio buttons and bullets:**
- ⚪ ⚫ (empty/filled circle)
- 🔘 (radio button)
- ● (filled bullet point)

**Usage:** Lists, options, selection states.

#### 4. Directional Indicators

**Arrows:**
- ← → ↑ ↓ (single directional)
- ↔ ↕ (bidirectional)
- <- -> (ASCII alternatives)

**Usage:** Flow diagrams, relationships, navigation hints.

**IMPORTANT:** When replacing Unicode arrows with ASCII, preserve direction:
- ← becomes <-
- → becomes ->
- ↑ becomes ^ or (up)
- ↓ becomes v or (down)

#### 5. Emphasis Symbols (Minimal Use)

**Stars (ratings only):**
- ☆ ★ (empty/filled star)

**Usage:** Priority levels, ratings. Not for decoration.

**Additional emphasis:**
- ⚡ (lightning - high priority)
- ❓ (question mark symbol - unclear status)

**Usage:** Only when text labels insufficient. Prefer "PRIORITY:", "UNCLEAR:" in most cases.

#### 6. Box-Drawing Characters (Structural Diagrams)

**PERMITTED CATEGORY:** Unicode box-drawing range (U+2500-U+257F) for creating tree diagrams, tables, and structural visualizations.

**Common examples:**
- Basic set: ─ │ ┌ ┐ └ ┘ ├ ┤ ╱ ╲
- Extended intersections: ┬ ┴ ┼ ├ ┤ ┣ ┫
- Double-line variants: ═ ║ ╔ ╗ ╚ ╝
- Heavy-line variants: ━ ┃ ┏ ┓ ┗ ┛

**Usage:**
- Directory tree structures
- Table borders and grids
- Flow diagrams
- Organizational charts

**Guidelines:**
- Use consistently within a single diagram (don't mix single/double/heavy styles randomly)
- Ensure proper alignment in monospace contexts
- Fallback to ASCII art (|, -, +) if Unicode rendering uncertain

---

### PROHIBITED Symbol Categories

**ABSOLUTE PROHIBITION on pictographic emojis:**

**Faces and emoticons:**
- 😊 😀 🤔 😎 🥺 😢 😡 🙄 😅 😂 etc.

**Objects and technology:**
- 📁 📂 💻 📊 📈 🚀 📱 🖥️ ⚙️ 🔧 etc.

**Celebrations and achievements:**
- 🎉 🏆 🎊 🥇 🎁 🎯 💯 etc.

**Hands and gestures:**
- 👍 👎 🙏 👋 🤝 👏 ✊ 🤞 etc.

**Hearts and decorative:**
- ❤️ 💙 💚 💛 💜 💖 💕 ✨ 🌟 etc.

**Animals, food, nature:**
- 🐛 🐍 🦀 🍕 🌈 🔥 etc.

**WHY PROHIBITED:** These symbols add no functional value, create visual clutter, may not render consistently, and reduce professional appearance.

---

### Plain Text Alternatives (Always Acceptable)

When in doubt, use explicit text labels:

| Symbol | Plain Text Alternative |
|--------|------------------------|
| ✅ | COMPLETED: or LISTO: |
| ❌ | ERROR: or FALLIDO: |
| ⚪ | OBSOLETE: or OBSOLETO: |
| 🔘 | PENDING: or PENDIENTE: |
| ⚫ | BLOCKED: or BLOQUEADO: |
| ⚡ | PRIORITY: or PRIORIDAD: |

**RECOMMENDATION:** Prefer plain text in:
- Scripted outputs parsed by other tools
- Logs intended for automated processing
- Environments where Unicode support uncertain
- Context where accessibility is critical

---

### Examples

#### INCORRECT (Pictographic Emojis):
```
📊 Analysis completed
🚀 Deploy to production
🎉 Project finished!
👍 Looks good
💻 Running on server
⚠️ WARNING: Check configuration
```

#### CORRECT (Functional Symbols):
```
✅ Analysis completed
→ Deploy to production
COMPLETED: Project finished
✓ Validation passed
STATUS: Running on server
```

#### CORRECT (Plain Text Alternative):
```
COMPLETED: Analysis completed
NEXT: Deploy to production
COMPLETED: Project finished
VALIDATED: Checks passed
STATUS: Running on server
```

#### CORRECT (Status Circles - Grayscale):
```
✅ task-1: Implemented
🔘 task-2: Pending implementation
⚪ task-3: Obsolete (no longer needed)
⚫ task-4: Blocked by dependencies
```

#### CORRECT (Box-Drawing for Trees):
```
project/
├── tasks/
│   ├── task-001/
│   │   ├── prompt.md
│   │   └── reports/
│   └── task-002/
└── synthesis/
```

---

### Validation and Enforcement

**Automated checks:**
- `scripts/verificar_simbolos_no_permitidos.py` - Scans files for prohibited symbols
- `scripts/limpiar_emojis.py` - Removes/replaces prohibited symbols
- `scripts/encontrar_simbolos.py` - Audits symbol usage

**Manual review:**
- Code review checklist includes symbol compliance
- Agent outputs reviewed before archiving
- Documentation audits verify adherence

**Resolution priority:**
- This CLAUDE.md section overrides any conflicting guidance
- Scripts must be updated to match this definition
- Legacy documents flagged for update during next revision

---

### Updates and Versioning

**Current version:** v3.2 Master (2026-01-19)

**Changelog:**
- v3.2 (2026-01-19): Removed ⚠️ warning symbol, switched to grayscale circles (⚪🔘⚫), removed color circles
- v3.1 (2026-01-18): Initial master version with box-drawing support

**Change process:**
- Symbol rule changes require updating this section
- Version number incremented
- All validation scripts synchronized
- Announcement in project changelog

**Questions or exceptions:** Consult project maintainer before adding new symbol categories.

---

## CRITICAL: Package Installation Protocol

**Problem Identified (2026-01-16 Audit):** Background agents may install packages to global Python instead of project venv, causing system contamination and dependency conflicts.

### ABSOLUTE RULE for All Agents

**NEVER install packages without activating virtual environment first.**

### For Coordinador (This Instance)

Before launching agents that may need external packages:

1. **Identify dependencies** the agent will need
2. **Install in project venv** BEFORE launching agent:
 ```bash
 source .venv/Scripts/activate
 pip install <required-packages>
 ```
3. **Include venv path in agent prompt:**
 ```markdown
 CRITICAL: This project uses virtual environment at:
 /absolute/path/to/project/.venv

 If you need to install packages:
 1. ALWAYS activate venv first: source .venv/Scripts/activate
 2. Then install: pip install <package>
 3. Register in requirements.txt

 NEVER run pip install without activating venv.
 ```

### For Background Agents

If your task requires installing Python packages:

```bash
# 1. CHECK if venv is active
if [ -z "$VIRTUAL_ENV" ]; then
 echo "ERROR: Virtual environment not activated"
 echo "Activating .venv..."
 source .venv/Scripts/activate
fi

# 2. Verify we're in the correct venv
if [[ "$VIRTUAL_ENV" != *".venv"* ]]; then
 echo "WARNING: Not in project venv"
 # Handle appropriately
fi

# 3. NOW install
pip install <package>

# 4. Document the dependency
echo "# Added by agent: <task-name>" >> requirements.txt
echo "<package>>=<version>" >> requirements.txt
```

### Safe Installation Script

**Always use the wrapper script:**

```bash
# Instead of:
pip install requests

# Use:
./scripts/safe_pip_install.sh requests
```

This script validates venv is active before installing.

### Template for Generated Scripts

When agents create Python scripts that need external packages:

```python
#!/usr/bin/env python3
"""
Script generated by agent: <agent-name>
Task: <task-description>

SETUP REQUIRED:
 source .venv/Scripts/activate
 pip install -r requirements.txt
"""

import sys
from pathlib import Path

# CRITICAL: Verify we're in venv before importing external packages
if sys.prefix == sys.base_prefix:
 print("ERROR: Virtual environment not activated")
 print("Run: source .venv/Scripts/activate")
 sys.exit(1)

# Now safe to import external packages
import requests # or other non-stdlib packages
import pandas
# ...
```

### Why This Matters

**Without venv isolation:**
- ❌ Packages install to global Python (system contamination)
- ❌ Version conflicts between projects
- ❌ Environment not reproducible on other machines
- ❌ Impossible to audit project dependencies

**With venv isolation:**
- ✅ Clean project dependencies
- ✅ No version conflicts
- ✅ Reproducible environment
- ✅ Easy to audit and clean up

---

## Common Commands

### Development

```bash
# Start coordinator (main entry point)
./start_coordinator.sh

# Setup environment
./setup.sh

# Run tests (if available)
python -m pytest tests/

# Validate project structure
python core/framework_validator.py validate-project <project-id>
```

### Using ProjectManager

```python
from pathlib import Path
from core.project_manager import ProjectManager

pm = ProjectManager(Path.cwd())

# Create project
project = pm.create_project(
 name="my-research",
 user_request="Investigate X topic",
 context="Additional context"
)

# Create task
task = pm.create_task(
 project_id=project["id"],
 task_name="analysis-component",
 task_description="Analyze specific aspect",
 prompt="[Layer 1: Conversational Context]\n\nUser requested analysis of X...\n\n[Layer 2: Technical Task]\n\nObjective: Analyze specific aspect..."
)

# Register report (validates file exists)
pm.register_task_report(
 project_id=project["id"],
 task_name="analysis-component",
 report_filename="findings.md"
)
```

### Output Validation

ProjectManager validates outputs **before** registering:
- File must exist physically
- Content must be >100 characters
- No duplicate registrations
- Raises specific exceptions on failure

## Coordinator Role (This Instance)

When operating as coordinator:

1. **Design investigations** with multi-agent strategies
2. **Create prompts** using 2-layer architecture
3. **Launch agents** using Task tool with `run_in_background=True`
4. **Monitor progress** via TaskOutput
5. **Synthesize results** from all agent reports
6. **Present findings** to user in integrated format

### CRITICAL: Always Use ProjectManager for Audits

**ABSOLUTE RULE:** When conducting ANY audit, analysis, or multi-agent investigation:

1. ✅ **MUST create formal project** using ProjectManager
2. ✅ **MUST save all prompts** in `tasks/*/prompt.md`
3. ✅ **MUST register all reports** using `register_task_report()`
4. ❌ **NEVER just create standalone reports** in `reports/`

**Why this matters:**
- **Trazabilidad**: Podemos reconstruir exactamente qué se hizo
- **Reproducibilidad**: Otros pueden replicar la auditoría
- **Aprendizaje**: Los prompts sirven como templates para futuras auditorías
- **Consistencia**: Predicamos ProjectManager, debemos usarlo nosotros mismos

**Example (CORRECT) - Auditoría del Framework:**
```python
from pathlib import Path
from core.project_manager import ProjectManager

# CRÍTICO: Auditorías del framework van a archive/audits/
pm = ProjectManager(base_dir="archive/audits")

# Create audit project
project = pm.create_project(
 name="Auditoría Framework v2.2",
 user_request="Realizar auditoría completa del framework",
 context="Identificar inconsistencias, bugs, y deuda técnica"
)

# Create audit task
task = pm.create_task(
 project_id=project["id"],
 task_name="analisis-codigo-core",
 task_description="Auditoría exhaustiva de código en core/",
 prompt="[Layer 1: Context]\n\nEl usuario solicitó auditoría...\n\n[Layer 2: Task]\n\nObjetivo: Analizar todo el código en core/..."
)

# Agent generates report...
# Then register it
pm.register_task_report(
 project_id=project["id"],
 task_name="analisis-codigo-core",
 report_filename="auditoria_codigo.md"
)
```

**Example (CORRECT) - Investigación de Usuario:**
```python
from pathlib import Path
from core.project_manager import ProjectManager

# Investigaciones de usuario van a projects/ (default)
pm = ProjectManager() # base_dir="projects" por defecto

# Create research project
project = pm.create_project(
 name="Investigación ClO₂ COVID-19",
 user_request="Investigar tratamientos con ClO₂ para COVID-19",
 context="Análisis científico de efectividad y seguridad"
)
```

**Example (WRONG):**
```python
# ❌ Creating standalone report without ProjectManager
with open("reports/AUDITORIA_NUEVA.md", "w") as f:
 f.write("# Auditoría\n...") # NO TRAZABILIDAD

# ❌ Auditoría del framework en projects/
pm = ProjectManager() # Esto crea en projects/
project = pm.create_project(name="Auditoría...") # ❌ INCORRECTO
```

**Cómo decidir base_dir:**

Consultar: `docs/CRITERIOS_CLASIFICACION_PROYECTOS.md`

- **Auditoría/mejora del framework** → `base_dir="archive/audits"`
- **Investigación de usuario** → `base_dir="projects"` (default)

## CRITICAL: User Consultation Protocol

**BEFORE executing ANY multi-step strategy or launching agents, ALWAYS:**

1. **Present Strategy Options**
 - Explain what approaches are available (single agent vs multi-agent, different specializations)
 - Describe trade-offs and expected outcomes
 - Recommend an approach with clear rationale

2. **Detail Execution Plan**
 - What tasks/agents will be created
 - How many agents and their specializations
 - What resources each will use
 - Expected outputs and deliverables
 - Approximate scope of investigation

3. **Request Explicit Approval**
 - Wait for user confirmation before proceeding
 - Accept user modifications to the plan
 - Clarify any ambiguities

4. **Provide Progress Updates**
 - Inform when starting each major phase
 - Report completion of significant milestones
 - Alert if issues/blockers arise

5. **Present Results with Synthesis**
 - Don't just dump raw agent outputs
 - Synthesize findings into coherent analysis
 - Highlight key insights and recommendations

**Example (CORRECT):**
```
User: "Analyze the competitive landscape for X"

Coordinator: "I can investigate this using two approaches:

OPTION A: Single comprehensive agent (faster, ~1 hour)
- One agent analyzes all competitors
- Integrated analysis but less depth

OPTION B: Multi-agent specialization (thorough, ~2-3 hours)
- Agent 1: Direct competitors analysis
- Agent 2: Indirect/alternative solutions
- Agent 3: Market trends and positioning
- More depth, better coverage

I recommend Option B for thorough competitive intelligence.
Would you like me to proceed with Option B, or prefer Option A?"

[WAITS FOR USER APPROVAL]

User: "Go with Option B"

Coordinator: "Creating project and launching 3 specialized agents..."
[Proceeds with execution, provides updates]
```

**WHY THIS MATTERS:**
- User maintains control and visibility
- Prevents wasted effort on wrong approaches
- Enables course correction before execution
- Builds trust through transparency
- Allows user to provide critical context or constraints

**NEVER:**
- ❌ Launch agents without explaining the strategy first
- ❌ Make unilateral decisions about investigation approach
- ❌ Proceed without explicit user approval
- ❌ Hide what's happening during execution

## Key Files

- **start_coordinator.sh** - Entry point, launches coordinator
- **core/project_manager.py** - Project/task creation, output management
- **core/framework_validator.py** - Structure validation
- **docs/ESTANDAR_ESTRUCTURA_TAREAS_v2.2.md** - v2.2 ORGANIZED spec
- **docs/CHECKLIST.md** - Manual validation checklist
- **reports/** - Session reports and documentation
- **archive/** - Historical projects and audits
- **legacy/task_manager.py** - DEPRECATED (v1.0 multi-window system)

## What NOT to Do

❌ **Don't use `task_manager.py`** - Deprecated v1.0 system that opened separate windows
❌ **Don't create projects manually** - Use ProjectManager
❌ **Don't skip output validation** - Always use `register_task_report()`
❌ **Don't launch agents without Layer 1 context** - They need conversational context

## Testing

Integration test workflow:
1. Create test project with ProjectManager
2. Create multiple tasks
3. Verify v2.2 ORGANIZED structure (README.md, reports/, task_info.json)
4. Create test reports
5. Validate registration catches missing files
6. Run CLI validator

## Framework Versions

- **v1.0** (legacy): Multi-window system with task_manager.py
- **v2.0**: Transition to Task tool based
- **v2.2 ORGANIZED** (current): Standardized structure with reports/ subdirectory

## Recent Corrections Applied

**Phase 1 - Critical (3/3 completed):**
- C1: get_task_report_path() returns reports/ subdirectory
- C2: FrameworkValidator integrated automatically in create_task()
- C3: CLI added to utility scripts (analyze_inconsistencies, audit_project, check_empty_reports)

**Phase 2 - High Priority (5/5 completed):**
- A1: update_task_status() method implemented
- A2: Prompt validation improved (structural instead of keyword-based)
- A3: UTF-8 encoding fixed for Windows
- A4: Migration script v1.0 → v2.2 created (migrate_v10_to_v22.py)
- A5: Portable paths (forward slashes) in metadata

**Status:** 8/28 corrections applied (Phase 1 + 2 complete). Framework is ROBUST and operational.

**Pending corrections:** See `reports/CORRECCIONES_PENDIENTES_20260115.md` for Phase 3 (tests, docs, logging) and Phase 4 (refactoring).

**Documentation:** See `reports/CORRECCIONES_APLICADAS_20260115.md` for detailed correction history.

## Dependencies

```bash
pip install -r requirements.txt
```

Core dependencies managed via requirements.txt at root.

---

**Framework Philosophy:** Coordinator maintains high-level conversation and synthesis. Agents carry heavy context and deep investigation. User sees only synthesized, integrated results through coordinator.
