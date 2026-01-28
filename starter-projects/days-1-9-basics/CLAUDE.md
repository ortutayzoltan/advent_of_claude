# Project Configuration for Claude Code

## Project Overview
This is a Python learning project for the Advent of Claude Code curriculum.

## Coding Standards

### Python Version
- Use Python 3.10+

### Style Guidelines
- Follow PEP 8 style guide
- Use type hints for all function parameters and return values
- Prefer composition over inheritance
- Maximum line length: 88 characters (Black formatter default)

### Documentation
- All modules must have docstrings
- All public functions must have docstrings with Args, Returns, and Examples sections
- Use Google-style docstrings

### Testing
- Use pytest for all tests
- Maintain test coverage above 80%
- Test files should be named `test_*.py`

### Git Conventions
- Use conventional commit messages (feat:, fix:, docs:, refactor:, test:)
- Keep commits atomic and focused
- Write descriptive commit messages

## Project Structure
```
├── hello.py       # Main entry point
├── utils.py       # Utility functions
├── tests/         # Test directory
└── requirements.txt
```

## Common Commands
- Run application: `python hello.py`
- Run tests: `pytest`
- Format code: `black .`
- Check types: `mypy .`
