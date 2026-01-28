# Claude Code Cheat Sheet

A quick reference guide for all Claude Code commands, shortcuts, and patterns covered in the 25-day curriculum.

---

## Slash Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/help` | Show all available commands | `/help` |
| `/init` | Create CLAUDE.md project config | `/init` |
| `/clear` | Clear conversation context | `/clear` |
| `/model` | Switch AI model | `/model` then select |
| `/commit` | Create a git commit | `/commit` |
| `/pr` | Create a pull request | `/pr` |
| `/diff` | Show current changes | `/diff` |
| `/agents` | Manage sub-agents | `/agents` |
| `/statusline` | Configure status display | `/statusline add Git Branch` |

---

## Special Syntax

### File References
Use `@` to reference files and give Claude context:
```
@README.md explain this file
@src/app.py @src/utils.py compare these files
@. reference entire directory
```

### Shell Commands
Use `!` to execute commands directly:
```
!python app.py
!git status
!pytest -v
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift + Tab + Tab` | Enter Plan Mode (extended thinking) |
| `Ctrl + C` | Cancel current operation |
| `Ctrl + D` | Exit session |
| `Up Arrow` | Previous prompt |
| `Tab` | Autocomplete file names |

---

## Plan Mode

Enter with `Shift + Tab + Tab` for complex tasks:
- Architecture planning
- Multi-step implementations
- Strategic decisions
- Security audits

---

## Project Configuration (CLAUDE.md)

Create with `/init`. Include:
```markdown
# Project: MyApp

## Tech Stack
- Python 3.10+
- Flask

## Coding Standards
- Use type hints
- Follow PEP 8
- Google-style docstrings

## Common Commands
- Run: python app.py
- Test: pytest
```

---

## Custom Commands

Create in `.claude/commands/` directory:
```
.claude/
  commands/
    review.md    # Creates /review command
    deploy.md    # Creates /deploy command
```

Command file format:
```markdown
# Review Command

Review the code for:
- Style compliance
- Type safety
- Test coverage
```

---

## Sub-Agents

Create specialized agents in `.claude/agents/`:
- Security auditor
- Test generator
- Documentation writer
- Performance analyzer

Usage: Reference agent name in prompts after creation.

---

## Hooks Configuration

Configure in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "command": "black $file"
      }
    ]
  }
}
```

---

## Headless Mode

Run Claude non-interactively:
```bash
# Basic usage
claude -p "your prompt here"

# Pipe input
cat file.py | claude -p "review this code"

# Save output
claude -p "generate changelog" > CHANGELOG.md

# With git
git log --oneline -10 | claude -p "summarize commits"
```

---

## Common Workflows

### Quick Code Review
```
Review @src/module.py for:
- Security issues
- Performance problems
- Best practices
```

### Debugging
```
Here's the error I'm getting:
[paste error]
Please diagnose and fix it.
```

### Multi-file Refactor
```
Refactor the auth logic from @app.py into
a new @services/auth.py module
```

### Test Generation
```
Create pytest tests for @src/utils.py
with edge cases
```

### Documentation
```
Add docstrings to all public functions in @src/
```

---

## Model Selection Guide

| Model | Best For |
|-------|----------|
| **Sonnet** | Daily coding, quick tasks |
| **Opus** | Complex architecture, security audits |
| **Haiku** | Simple queries, fast responses |

---

## Git Workflow

```
# Stage and commit
Stage my changes and commit with a descriptive message

# Create feature branch
Create branch feature/new-feature and switch to it

# Create PR
Create a PR with detailed description for the current branch
```

---

## Tips & Tricks

1. **Context is key**: Always reference relevant files with `@`
2. **Be specific**: "Add error handling to the login function" > "improve code"
3. **Use Plan Mode**: For anything taking more than a few steps
4. **Check CLAUDE.md**: Keep it updated with project conventions
5. **Clear when stuck**: Use `/clear` if context becomes cluttered
6. **Save good prompts**: Turn repetitive tasks into custom commands

---

## Quick Diagnostics

If something isn't working:
1. Check `/help` for correct command syntax
2. Verify file paths in `@` references
3. Use `/clear` to reset context
4. Try `/model` to switch models
5. Check `.claude/` configuration files

---

*Keep this cheat sheet handy while working through the 25-day curriculum!*
