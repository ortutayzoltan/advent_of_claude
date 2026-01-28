# Solutions: Days 6-10 (Core Workflows)

## Day 6: Git Workflow - Commits

### Example Interaction
```
You: Review my changes and create a commit

Claude: I'll check what changes you have and create an appropriate commit.

Looking at git diff, I see you've:
- Added error handling to the greet() function
- Added input validation for empty names
- Updated docstring

I'll create a commit with the message:
"feat: add input validation and error handling to greet function"

[Stages and commits changes]
```

### Key Concepts
- Claude reads git diff to understand changes
- Writes descriptive commit messages
- Follows conventional commit format (if in CLAUDE.md)

---

## Day 7: Understanding Your Codebase

### Example Interaction
```
You: Explain the current project structure and what each file does

Claude: Here's an overview of your project:

advent-project/
├── README.md      - Project documentation
├── CLAUDE.md      - Claude Code configuration
├── hello.py       - Main entry point with CLI
├── utils.py       - Utility functions (greet)
└── requirements.txt - Dependencies

The flow is:
1. hello.py parses CLI arguments
2. Calls create_greeting() from utils.py
3. Prints the result

Next features you could add:
- Unit tests
- More greeting styles
- Web API endpoint
```

---

## Day 8: Multi-file Edits

### Before
```python
# hello.py (everything in one file)
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

### After Refactoring
```python
# utils.py
def create_greeting(name: str) -> str:
    """Create a greeting message."""
    return f"Hello, {name}!"
```

```python
# hello.py
from utils import create_greeting

if __name__ == "__main__":
    print(create_greeting("World"))
```

### Key Concepts
- Claude edits multiple files atomically
- Maintains consistency across imports
- Updates all references when refactoring

---

## Day 9: Clearing Context with `/clear`

### When to Use
- Context window getting full
- Starting a new sub-task
- Claude seems confused about current state
- After major milestone completion

### What Persists After /clear
- CLAUDE.md contents (reloaded automatically)
- File system state
- Git state

### What's Lost
- Previous conversation
- In-memory context about recent changes
- Clarifications you provided earlier

---

## Day 10: Plan Mode (Extended Thinking)

### Entering Plan Mode
Press `Shift + Tab + Tab`

### Example Plan Output
```
You: [Plan Mode] Plan a Flask REST API that provides greeting endpoints

Claude's Plan:

## Architecture Overview
A RESTful API with the following structure:

### Endpoints
1. GET /greet - Default greeting
2. GET /greet/<name> - Personalized greeting
3. POST /greet - Custom greeting with options

### Project Structure
```
api/
├── app.py              # Flask app factory
├── routes/
│   └── greetings.py    # Greeting endpoints
├── services/
│   └── greeting_service.py  # Business logic
├── tests/
│   ├── test_routes.py
│   └── test_services.py
└── requirements.txt
```

### Implementation Steps
1. Set up Flask app with factory pattern
2. Create greeting service with business logic
3. Implement routes as Blueprint
4. Add input validation
5. Create tests
6. Add error handling

### Considerations
- Use Blueprint for route organization
- Separate business logic from routes
- Return JSON for all responses
- Include proper HTTP status codes
```

### Key Concepts
- Plan Mode uses extended thinking
- Great for architecture decisions
- Save plans to files for reference
- Don't skip straight to implementation for complex tasks
