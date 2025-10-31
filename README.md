# 🎄 Advent of Claude Code
## 25 Days to Master AI-Powered Development

Welcome to your journey of mastering Claude Code! Each day introduces one core feature with a practical, real-world task. Complete these in order, as each builds on previous days.

---

## 📅 Day 1: Starting Your First Session
**Feature:** Basic session management with `claude` command

**Task:** Create a new project folder called "advent-project" and start your first Claude Code session. Ask Claude to create a simple README.md file explaining what this project is about.

**Hints:**
1. Navigate to where you want your project: `cd ~` or `cd /mnt/c/Users/YourName/`
2. Create a folder: `mkdir advent-project && cd advent-project`
3. Start Claude: `claude`
4. Try a prompt like: "Create a README.md for a project called Advent of Claude Code"

**What You'll Learn:** How to start and interact with Claude in your terminal

---

## 📅 Day 2: File References & Context
**Feature:** Using `@` to reference files

**Task:** You have a README from Day 1. Now create a Python file that implements a simple "Hello World" function. Reference your README to maintain consistency with the project description.

**Hints:**
1. Use `@README.md` in your prompt to give Claude context
2. Ask: "Based on @README.md, create a hello.py file with a greeting function"
3. Claude can read the README and create code that matches your project style

**What You'll Learn:** How to provide file context to Claude for better, context-aware code generation

---

## 📅 Day 3: Running Commands with `!`
**Feature:** Executing shell commands directly with `!`

**Task:** Test your Python file from Day 2 by running it, then ask Claude to check if Python is properly installed on your system.

**Hints:**
1. Try: `!python hello.py` to run your script
2. Ask: "Check what version of Python I have installed"
3. The `!` prefix runs commands without Claude's interpretation layer (faster, fewer tokens)

**What You'll Learn:** How to execute system commands within Claude sessions

---

## 📅 Day 4: The `/help` Command
**Feature:** Discovering available slash commands

**Task:** Explore all available Claude Code commands and create a personal cheat sheet file listing the 5 commands you think will be most useful for your work.

**Hints:**
1. Type `/help` to see all slash commands
2. Ask Claude: "Create a cheat-sheet.md file with my top 5 most useful slash commands and what they do"
3. Look for commands like `/commit`, `/pr`, `/diff`, etc.

**What You'll Learn:** Self-discovery of Claude Code's capabilities

---

## 📅 Day 5: Initializing Project Context with `/init`
**Feature:** Creating a CLAUDE.md file

**Task:** Initialize your project with a CLAUDE.md file that describes your coding preferences, project architecture, and any conventions you want Claude to follow.

**Hints:**
1. Run `/init` to create the file
2. Ask Claude: "Update CLAUDE.md to include: Python 3.10+, use type hints, follow PEP 8, prefer composition over inheritance"
3. This file is loaded automatically in every new session!

**What You'll Learn:** How to give Claude persistent project memory

---

## 📅 Day 6: Git Workflow - Commits
**Feature:** Automatic commit message generation

**Task:** Make some changes to your hello.py file (add error handling), then ask Claude to commit these changes with an appropriate message.

**Hints:**
1. First initialize git: `!git init` (if not done already)
2. Ask: "Review my changes and create a commit"
3. Claude will examine the diff and write a meaningful commit message

**What You'll Learn:** How Claude automates git workflows

---

## 📅 Day 7: Understanding Your Codebase
**Feature:** Codebase exploration and explanation

**Task:** Ask Claude to explain the structure of your project so far, including all files and their relationships. Then ask it to suggest what you should build next.

**Hints:**
1. Try: "Explain the current project structure and what each file does"
2. Follow up with: "What would be a good next feature to add?"
3. Claude reads your entire project directory automatically

**What You'll Learn:** How Claude maintains awareness of your full project context

---

## 📅 Day 8: Multi-file Edits
**Feature:** Simultaneous editing across files

**Task:** Refactor your project to separate concerns: move the greeting logic to a utils.py module, and update hello.py to import from it. Update tests accordingly.

**Hints:**
1. Ask: "Refactor the greeting function into a new utils.py module and update hello.py to use it"
2. Claude will create/edit multiple files at once
3. Watch how it maintains consistency across files

**What You'll Learn:** Claude's ability to make coherent multi-file changes

---

## 📅 Day 9: Clearing Context with `/clear`
**Feature:** Resetting conversation history

**Task:** After your refactoring work, use `/clear` to start fresh, then ask Claude to add a new feature: command-line argument parsing for custom greetings.

**Hints:**
1. Type `/clear` to reset
2. Notice that CLAUDE.md context is still available
3. Ask: "Add argparse to hello.py so users can pass their name as a command-line argument"

**What You'll Learn:** How to manage context window and start new sub-tasks

---

## 📅 Day 10: Plan Mode (Extended Thinking)
**Feature:** Using Plan Mode for complex problems

**Task:** Plan a complete mini web API using Flask that exposes your greeting functionality. Don't implement yet—just get Claude to create a detailed plan.

**Hints:**
1. Press `Shift + Tab + Tab` to enter Plan Mode
2. Ask: "Plan a Flask REST API that provides greeting endpoints"
3. Review the plan, save it to a file if you like it

**What You'll Learn:** How to get strategic planning before implementation

---

## 📅 Day 11: Implementing from Plans
**Feature:** Executing planned solutions

**Task:** Take yesterday's plan and ask Claude to implement the Flask API. Reference the plan document if you saved it.

**Hints:**
1. If you have a plan file: "Implement the API based on @plan.md"
2. Otherwise: "Now implement the Flask API we planned yesterday"
3. Ask Claude to also create a requirements.txt

**What You'll Learn:** The research → plan → implement workflow

---

## 📅 Day 12: Testing & Validation
**Feature:** Automated test generation

**Task:** Ask Claude to create comprehensive unit tests for your Flask API using pytest. Then run the tests and fix any failures.

**Hints:**
1. Ask: "Create pytest unit tests for all API endpoints"
2. Run tests: `!pytest`
3. If tests fail: "Fix the failing tests"

**What You'll Learn:** How Claude generates and fixes tests

---

## 📅 Day 13: Switching Models with `/model`
**Feature:** Choosing the right model for the task

**Task:** Switch to Claude 4 Opus (if available) and ask it to review your entire codebase for potential security vulnerabilities and performance improvements.

**Hints:**
1. Type `/model` and select Opus (or the most capable model available)
2. Ask: "Perform a security and performance audit of the entire codebase"
3. Compare the depth of analysis with Sonnet

**What You'll Learn:** When to use different models for different tasks

---

## 📅 Day 14: Custom Slash Commands
**Feature:** Creating reusable command shortcuts

**Task:** Create a custom `/review` command that checks code quality, style compliance, and test coverage.

**Hints:**
1. Create `.claude/commands/` directory
2. Ask Claude: "Create a custom /review command that checks: PEP 8 compliance, type hints, docstrings, and test coverage"
3. Test it: `/review`

**What You'll Learn:** How to automate repetitive workflows

---

## 📅 Day 15: Git Branching & PRs
**Feature:** Branch management and pull requests

**Task:** Create a new feature branch, implement a new endpoint (e.g., /goodbye), commit it, and have Claude create a pull request with a detailed description.

**Hints:**
1. Ask: "Create a new branch called feature/goodbye-endpoint"
2. Implement the feature
3. Ask: "Create a PR for this feature with a detailed description"

**What You'll Learn:** Complete git workflow automation

---

## 📅 Day 16: Documentation Generation
**Feature:** Automatic documentation

**Task:** Ask Claude to generate comprehensive documentation for your API, including docstrings for all functions, a complete API.md guide, and inline comments where needed.

**Hints:**
1. "Add comprehensive docstrings to all functions in the project"
2. "Create an API.md documenting all endpoints with examples"
3. Check that it follows your CLAUDE.md style guidelines

**What You'll Learn:** Automated documentation generation

---

## 📅 Day 17: Debugging & Error Analysis
**Feature:** Error diagnosis and fixing

**Task:** Intentionally break something in your code (remove an import, introduce a syntax error), run it to get an error, then paste the error to Claude and ask it to fix it.

**Hints:**
1. Break your code deliberately
2. Copy the error output
3. Ask: "Here's the error I'm getting: [paste error]. Please diagnose and fix it."

**What You'll Learn:** Claude's debugging capabilities

---

## 📅 Day 18: Code Review & Refactoring
**Feature:** Quality improvement suggestions

**Task:** Ask Claude to perform a comprehensive code review of your entire project and implement its suggested improvements.

**Hints:**
1. Ask: "Review all code for improvements: readability, performance, and best practices"
2. "Implement the top 3 suggestions"
3. Use Plan Mode for complex refactorings

**What You'll Learn:** How Claude identifies and fixes code smells

---

## 📅 Day 19: Working with External APIs
**Feature:** Integrating third-party services

**Task:** Add a new endpoint that fetches data from a public API (like JSONPlaceholder or a weather API) and processes it.

**Hints:**
1. Ask: "Add an endpoint that fetches and displays weather data from wttr.in"
2. Claude will handle requests library, error handling, and response formatting
3. Test the endpoint with `!curl`

**What You'll Learn:** How Claude handles external integrations

---

## 📅 Day 20: Environment Configuration
**Feature:** Managing configs and secrets

**Task:** Refactor your app to use environment variables for configuration. Create a .env.example file and update CLAUDE.md to note this pattern.

**Hints:**
1. Ask: "Refactor to use environment variables for API keys and config"
2. "Create .env.example and add instructions to CLAUDE.md"
3. Claude should add .env to .gitignore automatically

**What You'll Learn:** Best practices for configuration management

---

## 📅 Day 21: Sub-Agents for Specialized Tasks
**Feature:** Creating specialized helper agents

**Task:** Create a specialized sub-agent focused on security reviews. Use it to audit your API for security best practices.

**Hints:**
1. Type `/agents` to create a sub-agent
2. Ask: "Create a security specialist agent"
3. The sub-agent will be saved in .claude/agents/
4. Use it: "Have the security agent review the entire codebase"

**What You'll Learn:** How to delegate specialized work to focused agents

---

## 📅 Day 22: Headless Mode & Automation
**Feature:** Running Claude without interactive mode

**Task:** Create a script that uses Claude in headless mode to automatically generate a weekly changelog from git history.

**Hints:**
1. Learn the syntax: `claude -p "prompt" > output.md`
2. Try: `git log --since="7 days ago" --pretty=format:"%h %s" | claude -p "Create a user-friendly changelog from these commits" > CHANGELOG.md`
3. This is great for CI/CD pipelines!

**What You'll Learn:** Non-interactive Claude usage for automation

---

## 📅 Day 23: Hooks for Automatic Actions
**Feature:** Post-action automation with hooks

**Task:** Set up a hook that automatically runs your linter (e.g., black for Python) every time Claude writes a Python file.

**Hints:**
1. Edit `.claude/settings.json`
2. Add a PostToolUse hook with matcher `Write(*.py)` and command `black $file`
3. Ask Claude to help set this up
4. Test by having Claude edit a .py file

**What You'll Learn:** How to automate quality checks

---

## 📅 Day 24: Status Line Customization
**Feature:** Custom status information display

**Task:** Create a custom status line that shows your current model, token usage, git branch, and project name.

**Hints:**
1. Use `/statusline` command
2. Try: `/statusline add Model | Git Branch | Tokens | Directory`
3. Ask Claude to create a bash script that runs on startup

**What You'll Learn:** How to monitor your session at a glance

---

## 📅 Day 25: Complete Project Integration
**Feature:** Bringing it all together

**Task:** Start a completely new project from scratch using everything you've learned. Build a todo CLI application with full test coverage, documentation, CI/CD ready configs, and proper git workflow.

**Hints:**
1. Use `/init` first with comprehensive guidelines
2. Use Plan Mode to design the architecture
3. Create custom commands for your workflow
4. Set up sub-agents for testing and docs
5. Use hooks for automatic formatting
6. Generate complete documentation
7. Create a PR-ready final branch

**What You'll Learn:** How to orchestrate all Claude Code features in a real-world workflow

---

## 🎯 Bonus Challenges

Once you complete all 25 days, try these advanced challenges:

1. **MCP Integration:** Set up Model Context Protocol to connect Claude to external data sources
2. **Team Workflows:** Share your .claude/ configs with teammates and standardize your team's Claude usage
3. **CI/CD Integration:** Set up GitHub Actions that use Claude Code for automated PR reviews
4. **Custom Agents:** Create a full team of specialized agents (tester, documenter, security auditor, performance optimizer)
5. **Template Project:** Create a project template with all your learned best practices baked in

---

## 📚 Additional Resources

- Official Docs: https://docs.claude.com/en/docs/claude-code/overview
- Best Practices: https://www.anthropic.com/engineering/claude-code-best-practices
- GitHub Repo: https://github.com/anthropics/claude-code
- Community: Claude Developers Discord

---

## 🎓 Completion Certificate

Once you finish all 25 days, you'll have mastered:
- ✅ Basic to advanced Claude Code operations
- ✅ Git workflow automation
- ✅ Multi-file codebase management
- ✅ Testing and debugging with AI
- ✅ Custom commands and automation
- ✅ Sub-agent orchestration
- ✅ Production-ready configuration
- ✅ Team collaboration patterns

**Congratulations on becoming a Claude Code power user! 🎉**

---

*Remember: The best way to learn is by doing. Don't just read these challenges—actually implement them. Each day should take 15-30 minutes.*
