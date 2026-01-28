# Solutions: Days 1-5 (Fundamentals)

## Day 1: Starting Your First Session

### Expected Output
```
$ claude
Welcome to Claude Code!

You: Create a README.md for a project called Advent of Claude Code
Claude: I'll create a README.md file for your project...
[Creates file]

$ cat README.md
# Advent of Claude Code
A learning project for mastering Claude Code features.
...
```

### Key Concepts
- `claude` starts an interactive session
- Claude can create and edit files directly
- First prompt sets the project context

---

## Day 2: File References & Context

### Example Prompts
```
Based on @README.md, create a hello.py file with a greeting function
```

### Expected Output
```python
# hello.py
def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Advent of Claude Code!"

if __name__ == "__main__":
    print(greet())
```

### Key Concepts
- `@filename` passes file content to Claude
- Claude reads the file and uses it for context
- Referenced files influence code style and naming

---

## Day 3: Running Commands with `!`

### Example Usage
```
!python hello.py
!python --version
!pip list
```

### Expected Output
```
You: !python hello.py
Hello, World! Welcome to Advent of Claude Code!

You: !python --version
Python 3.10.12
```

### Key Concepts
- `!` prefix runs shell commands directly
- Faster than asking Claude to run commands
- Useful for quick checks and tests

---

## Day 4: The `/help` Command

### Expected Output
```
You: /help

Available Commands:
  /help       - Show this help message
  /init       - Initialize project with CLAUDE.md
  /clear      - Clear conversation history
  /model      - Switch AI model
  /commit     - Create a git commit
  /pr         - Create a pull request
  /diff       - Show current changes
  ...
```

### Sample Cheat Sheet (created by Claude)
```markdown
# My Top 5 Claude Code Commands

1. `/init` - Set up project preferences
2. `/commit` - Quick git commits
3. `/clear` - Reset when context gets messy
4. `/model` - Switch models for different tasks
5. `/help` - When I forget something
```

---

## Day 5: Initializing Project Context with `/init`

### Expected CLAUDE.md
```markdown
# Project: advent-project

## Coding Standards
- Python 3.10+
- Use type hints for all functions
- Follow PEP 8 style guide
- Prefer composition over inheritance

## Documentation
- Use Google-style docstrings
- All public functions need docstrings

## Testing
- Use pytest
- Maintain 80%+ coverage

## Git
- Conventional commits (feat:, fix:, docs:)
```

### Key Concepts
- CLAUDE.md is loaded automatically each session
- Acts as "memory" for project preferences
- Can include coding standards, architecture notes, common commands

### Common Mistakes
- Making CLAUDE.md too long (keep it focused)
- Forgetting to update it as project evolves
- Not being specific enough about preferences
