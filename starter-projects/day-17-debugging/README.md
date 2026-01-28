# Day 17: Debugging Practice

This project contains **intentionally buggy code** for practicing debugging skills with Claude Code.

## The Challenge

This is a simple task management application that has several bugs. Your mission:

1. Try to run the application
2. Observe the errors
3. Use Claude Code to diagnose and fix each bug
4. Verify your fixes work

## How to Use

```bash
# Try running the app (it will fail!)
python task_manager.py

# Run the tests (they will fail!)
pytest test_task_manager.py -v
```

## Known Issues

The code contains the following types of bugs (no spoilers on which lines!):

- Import errors
- Syntax errors
- Logic errors
- Type errors
- Off-by-one errors
- Undefined variable references

## Learning Objectives

After completing this exercise, you'll know how to:

1. Copy error messages to Claude for diagnosis
2. Ask Claude to explain what went wrong
3. Have Claude suggest and implement fixes
4. Verify fixes by re-running the code

## Tips

- Don't look at the solutions until you've tried debugging with Claude!
- Copy the full error traceback when asking for help
- Ask Claude to explain *why* the bug occurred, not just how to fix it

## Expected Behavior (When Fixed)

```bash
$ python task_manager.py
Task Manager initialized!
Added task: Buy groceries
Added task: Write report
Added task: Call mom
All tasks:
  1. [ ] Buy groceries
  2. [ ] Write report
  3. [ ] Call mom
Completed: Buy groceries
All tasks:
  1. [x] Buy groceries
  2. [ ] Write report
  3. [ ] Call mom
Pending tasks: 2
```
