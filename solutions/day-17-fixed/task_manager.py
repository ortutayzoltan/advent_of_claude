#!/usr/bin/env python3
"""
Task Manager - FIXED VERSION

This is the corrected version of the buggy task manager.
Compare with starter-projects/day-17-debugging/task_manager.py to see all fixes.
"""

import json
from datetime import datetime  # FIX 1: Corrected typo (was 'datatime')


class Task:
    """Represents a single task."""

    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at = None

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
        # FIX 2: Corrected off-by-one error (was 'self.tasks[index]')
        return self.tasks[index - 1]

    def complete_task(self, index: int) -> None:
        """Mark a task as complete by its index."""
        task = self.get_task(index)
        task.mark_complete()
        print(f"Completed: {task.title}")

    def list_tasks(self) -> None:
        """Print all tasks."""
        print("All tasks:")
        for i, task in enumerate(self.tasks):
            # FIX 3: Corrected to show 1-based index (was 'i')
            print(f"  {i + 1}. {task}")

    def get_pending_count(self) -> int:
        """Get the count of pending (incomplete) tasks."""
        count = 0
        for task in self.tasks:
            if not task.completed:
                count += 1
        print(f"Pending tasks: {count}")
        # FIX 4: Added missing return statement
        return count

    def save_to_file(self, filename: str) -> None:
        """Save tasks to a JSON file."""
        data = []
        for task in self.tasks:
            data.append({
                # FIX 5: Corrected typo (was 'taks.title')
                "title": task.title,
                "description": task.description,
                "completed": task.completed
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def remove_completed(self) -> int:
        """Remove all completed tasks and return count removed."""
        # FIX 6: Don't modify list while iterating
        # Old code:
        #   for task in self.tasks:
        #       if task.completed:
        #           self.tasks.remove(task)
        # This fails because removing items shifts indices

        # Correct approach: filter to create new list
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = original_count - len(self.tasks)
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

    # Complete the first task (index 1 for user)
    manager.complete_task(1)

    # List again
    manager.list_tasks()

    # Show pending count
    pending = manager.get_pending_count()
    print(f"Returned pending count: {pending}")


if __name__ == "__main__":
    main()
