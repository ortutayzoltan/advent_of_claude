# Greeting API

A Flask REST API for the Advent of Claude Code curriculum (Days 10-15).

## Overview

This project provides a RESTful API for greeting functionality, designed to teach Flask development with Claude Code assistance.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check / welcome message |
| GET | `/greet` | Get default greeting |
| GET | `/greet/<name>` | Get personalized greeting |
| POST | `/greet` | Create custom greeting |
| GET | `/goodbye/<name>` | Get farewell message (Day 15 exercise) |

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py

# Or use Flask CLI
flask run --debug
```

## API Examples

```bash
# Health check
curl http://localhost:5000/

# Default greeting
curl http://localhost:5000/greet

# Personalized greeting
curl http://localhost:5000/greet/Alice

# Custom greeting (POST)
curl -X POST http://localhost:5000/greet \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob", "style": "formal"}'
```

## Project Structure

```
days-10-15-flask-api/
├── app.py              # Main Flask application
├── routes/
│   └── greetings.py    # Greeting route handlers
├── services/
│   └── greeting_service.py  # Business logic
├── tests/
│   ├── test_app.py     # Integration tests
│   └── test_services.py # Unit tests
├── requirements.txt    # Dependencies
└── CLAUDE.md          # Claude Code configuration
```

## Learning Path

- **Day 10**: Plan the API architecture (Plan Mode)
- **Day 11**: Implement the Flask API
- **Day 12**: Write pytest tests
- **Day 13**: Model switching for code review
- **Day 14**: Create custom `/review` command
- **Day 15**: Git branching and PR creation

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_app.py -v
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| FLASK_ENV | development | Environment mode |
| FLASK_PORT | 5000 | Server port |
| DEBUG | True | Debug mode |
