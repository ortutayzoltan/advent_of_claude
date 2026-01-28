#!/usr/bin/env python3
"""
Task Manager - A buggy application for debugging practice.

WARNING: This file contains INTENTIONAL BUGS for learning purposes!
Your goal is to find and fix them using Claude Code.
"""

import json
from datatime import datetime  # Bug 1: Typo in module name


class Task:
    """Represents a single task."""

    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.title}"


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self):
        self.tasks = []
        print("Task Manager initialized!")

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to the manager."""
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Added task: {title}")
        return task

    def get_task(self, index: int) -> Task:
        """Get a task by its index (1-based for user friendliness)."""
        # Bug 2: Off-by-one error - should be index - 1
        return self.tasks[index]

    def complete_task(self, index: int) -> None:
        """Mark a task as complete by its index."""
        task = self.get_task(index)
        task.mark_complete()
        print(f"Completed: {task.title}")

    def list_tasks(self) -> None:
        """Print all tasks."""
        print("All tasks:")
        for i, task in enumerate(self.tasks):
            # Bug 3: Should be i + 1 for 1-based display
            print(f"  {i}. {task}")

    def get_pending_count(self) -> int:
        """Get the count of pending (incomplete) tasks."""
        count = 0
        for task in self.tasks:
            if not task.completed:
                count += 1
        # Bug 4: Missing return statement
        print(f"Pending tasks: {count}")

    def save_to_file(self, filename: str) -> None:
        """Save tasks to a JSON file."""
        data = []
        for task in self.tasks:
            data.append({
                "title": taks.title,  # Bug 5: Typo in variable name
                "description": task.description,
                "completed": task.completed
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def remove_completed(self) -> int:
        """Remove all completed tasks and return count removed."""
        # Bug 6: Modifying list while iterating
        removed = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed += 1
        return removed


def main():
    """Main function to demonstrate the task manager."""
    manager = TaskManager()

    # Add some tasks
    manager.add_task("Buy groceries")
    manager.add_task("Write report")
    manager.add_task("Call mom")

    # List all tasks
    manager.list_tasks()

    # Complete the first task (should be index 1 for user)
    manager.complete_task(1)

    # List again
    manager.list_tasks()

    # Show pending count
    pending = manager.get_pending_count()


if __name__ == "__main__":
    main()
