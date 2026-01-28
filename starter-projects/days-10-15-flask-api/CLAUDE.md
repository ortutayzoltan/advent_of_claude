# Claude Code Configuration - Greeting API

## Project Overview
A Flask REST API for the Advent of Claude Code curriculum, covering Days 10-15.

## Tech Stack
- Python 3.10+
- Flask 3.x
- pytest for testing

## Coding Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Maximum line length: 88 characters (Black default)
- Use Google-style docstrings

### Project Structure
```
├── app.py           # Application factory and entry point
├── routes/          # Blueprint route handlers
├── services/        # Business logic layer
├── tests/           # pytest test files
└── requirements.txt # Dependencies
```

### Architecture Patterns
- Use Flask Blueprints for route organization
- Separate business logic into service classes
- Use application factory pattern (create_app)
- Keep routes thin - delegate to services

### Testing Requirements
- All endpoints must have integration tests
- All service methods must have unit tests
- Target 80%+ code coverage
- Use pytest fixtures for setup

### API Conventions
- Return JSON for all endpoints
- Use appropriate HTTP status codes
- Include descriptive error messages
- Document all endpoints in README

## Common Commands
```bash
# Run server
python app.py

# Run tests
pytest

# Run with coverage
pytest --cov=. --cov-report=term-missing

# Format code
black .
```

## Git Workflow
- Use feature branches for new endpoints
- Write conventional commits (feat:, fix:, test:)
- Create PRs with detailed descriptions
