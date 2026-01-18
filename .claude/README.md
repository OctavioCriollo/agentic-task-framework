# Claude Code Configuration

## Setup

1. Copy the template:
   ```bash
   cp .claude/settings.local.json.template .claude/settings.local.json
   ```

2. Edit `.claude/settings.local.json` to add machine-specific permissions if needed

## Security Guidelines

**CRITICAL:** Never use wildcard `*` for dangerous commands.

### Safe Permissions

Use explicit allow-lists for each operation:

```json
{
  "allow": [
    "Bash(pip list)",              // ✅ SAFE - specific command
    "Bash(pytest tests/ -v)",      // ✅ SAFE - specific arguments
    "Bash(git status)"             // ✅ SAFE - read-only
  ]
}
```

### Dangerous Permissions

**NEVER** use these patterns:

```json
{
  "allow": [
    "Bash(pip install:*)",         // ❌ DANGEROUS - allows any package
    "Bash(python:*)",              // ❌ DANGEROUS - arbitrary code execution
    "Bash(bash:*)",                // ❌ DANGEROUS - arbitrary shell commands
    "Bash(*)"                      // ❌ DANGEROUS - anything goes
  ]
}
```

### Ask Permissions

For risky operations, use `ask` to require user approval:

```json
{
  "ask": [
    "Bash(pip install *)",         // ✅ Requires approval per package
    "Bash(python -c *)",           // ✅ Requires approval for code execution
    "Bash(python:*)"               // ✅ Requires approval for any python command
  ]
}
```

## Portable Paths

**NEVER hardcode absolute paths** in settings.local.json.

### Bad (Not Portable):

```json
{
  "allow": [
    "Bash(C:\\Users\\YourName\\...)",           // ❌ Hardcoded Windows path
    "Bash(/home/username/...)",                 // ❌ Hardcoded Unix path
    "Bash(D:\\STARTUP\\Proyectos\\...)"         // ❌ Machine-specific
  ]
}
```

### Good (Portable):

```json
{
  "allow": [
    "Bash(./venv/Scripts/python)",              // ✅ Relative path
    "Bash(python core/project_manager.py)",     // ✅ Project-relative
    "Bash(source .venv/Scripts/activate)"       // ✅ Portable
  ]
}
```

## Allowed Commands

See `.claude/settings.local.json.template` for recommended permissions.

### Categories:

1. **Framework Core Scripts** - Project management, validation
2. **Testing** - pytest commands
3. **Dependency Management** - Read-only pip commands (install requires approval)
4. **File Operations** - ls, cat, grep, wc, tree
5. **Version Control** - git commands (safe subset)
6. **Environment** - Read-only version checks
7. **Web Access** - Restricted to whitelisted scientific domains

## Maintenance

- Keep `.claude/settings.local.json` out of version control (it's in .gitignore)
- Update template when adding new safe commands
- Review permissions regularly
- Remove unused permissions

## Troubleshooting

### "Permission denied" errors

If you get permission denied for a legitimate command:

1. Check if the command is in the template
2. Add it to your local settings.local.json
3. Use specific arguments (not wildcards)
4. Consider using `ask` permissions if the command is risky

### Settings not applying

1. Restart Claude Code session
2. Check JSON syntax is valid
3. Verify file is named correctly: `.claude/settings.local.json`

## Security Philosophy

**Principle of Least Privilege:**
- Only grant permissions actually needed
- Prefer `ask` over `allow` for risky operations
- Never use wildcards for dangerous commands
- Review and prune permissions regularly

**Defense in Depth:**
- Settings file provides first line of defense
- Code validation provides second layer
- User review provides final check
