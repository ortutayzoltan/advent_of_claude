# Solutions: Days 21-25 (Advanced Features)

## Day 21: Sub-Agents for Specialized Tasks

### Creating a Security Agent

**File: .claude/agents/security-auditor.md**
```markdown
# Security Auditor Agent

You are a security specialist focused on identifying vulnerabilities.

## Responsibilities
- OWASP Top 10 vulnerability detection
- Input validation review
- Authentication/authorization checks
- Secrets detection
- Dependency vulnerability scanning

## Review Checklist
1. SQL Injection
2. XSS (Cross-Site Scripting)
3. CSRF vulnerabilities
4. Insecure direct object references
5. Security misconfiguration
6. Sensitive data exposure
7. Missing access controls
8. Insecure deserialization
9. Known vulnerable components
10. Insufficient logging

## Output Format
For each finding:
- Severity: Critical/High/Medium/Low
- Location: file:line
- Description: What's wrong
- Recommendation: How to fix
- Reference: CWE/OWASP ID
```

### Usage
```
You: Have the security agent review the entire codebase

Claude: [Switches to security-auditor agent context]

## Security Audit Report

### Critical Findings
None

### High Severity
1. **Potential XSS in greeting output**
   - Severity: High
   - Location: routes/greetings.py:28
   - Description: User-supplied name rendered without escaping
   - Recommendation: Use markupsafe.escape() or return JSON only
   - Reference: CWE-79

[...]
```

---

## Day 22: Headless Mode & Automation

### Basic Headless Usage
```bash
# Simple prompt
claude -p "What is the purpose of this project?"

# Generate file
claude -p "Create a .gitignore for Python projects" > .gitignore

# Pipe input
cat error.log | claude -p "Summarize these errors"
```

### Changelog Generator Script
```bash
#!/bin/bash
# generate-changelog.sh

# Get commits from last 7 days
COMMITS=$(git log --since="7 days ago" --pretty=format:"%h %s (%an)")

# Generate changelog with Claude
echo "$COMMITS" | claude -p "Create a user-friendly changelog from these commits.
Group by type (Features, Fixes, Other).
Format in Markdown." > CHANGELOG.md

echo "Changelog generated!"
```

### CI/CD Integration Example
```yaml
# .github/workflows/pr-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Get diff
        run: git diff origin/main > changes.diff

      - name: AI Review
        run: |
          cat changes.diff | claude -p "Review this diff for:
          - Bugs
          - Security issues
          - Style problems
          Provide brief, actionable feedback." > review.md

      - name: Post Review
        uses: actions/github-script@v6
        with:
          script: |
            const review = require('fs').readFileSync('review.md', 'utf8');
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: review
            });
```

---

## Day 23: Hooks for Automatic Actions

### .claude/settings.json
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "command": "black $file && isort $file"
      },
      {
        "matcher": "Write(*.js)",
        "command": "prettier --write $file"
      },
      {
        "matcher": "Write(*.md)",
        "command": "markdownlint $file || true"
      }
    ],
    "PreCommit": [
      {
        "command": "pytest --tb=short"
      }
    ]
  }
}
```

### Hook Behavior
```
You: Create a new utils.py with helper functions

Claude: [Creates utils.py]

[Hook automatically runs:]
$ black utils.py
reformatted utils.py

$ isort utils.py
Fixing utils.py

File formatted automatically!
```

---

## Day 24: Status Line Customization

### Custom Status Line
```
You: /statusline add Model | Git Branch | Tokens | Directory

Claude: Status line configured. You'll now see:
┌─────────────────────────────────────────────────┐
│ sonnet │ main │ 1.2k tokens │ ~/advent-project │
└─────────────────────────────────────────────────┘
```

### Available Status Components
- Model name
- Git branch
- Token usage
- Current directory
- Project name
- Time elapsed
- Memory usage

---

## Day 25: Complete Project Integration

### Final Project Checklist

```markdown
## Project Setup
- [x] /init with comprehensive CLAUDE.md
- [x] .gitignore configured
- [x] requirements.txt with all dependencies
- [x] README.md with setup instructions

## Code Quality
- [x] All functions have type hints
- [x] All public functions have docstrings
- [x] Code formatted with black
- [x] Imports sorted with isort
- [x] No linting errors

## Testing
- [x] Unit tests for all services
- [x] Integration tests for all endpoints
- [x] 80%+ code coverage
- [x] All tests passing

## Documentation
- [x] API.md with all endpoints
- [x] CONTRIBUTING.md
- [x] Inline comments where needed

## Automation
- [x] Custom /review command
- [x] PostToolUse hooks for formatting
- [x] Security agent configured
- [x] Headless changelog script

## Git
- [x] Feature branches used
- [x] Conventional commits
- [x] PR descriptions detailed
- [x] Clean commit history
```

### Sample Final CLAUDE.md
```markdown
# Todo CLI Application

## Overview
A command-line todo application demonstrating Claude Code mastery.

## Tech Stack
- Python 3.10+
- Click for CLI
- SQLite for storage
- pytest for testing

## Architecture
- cli.py: Command definitions
- models.py: Database models
- services/: Business logic
- tests/: Test suite

## Commands
- Run: `python -m todo`
- Test: `pytest --cov`
- Format: `black . && isort .`
- Lint: `flake8`

## Conventions
- Type hints required
- Google docstrings
- Conventional commits
- 80%+ test coverage

## Agents
- /security: Security audit
- /perf: Performance review
- /docs: Documentation check

## Hooks
- Auto-format Python on save
- Run tests before commit
```
