"""
Tests for the Task Manager.

These tests will fail until the bugs are fixed!
"""

import pytest


class TestTask:
    """Tests for the Task class."""

    def test_task_creation(self):
        """Test that tasks can be created."""
        # This import will fail due to Bug 1
        from task_manager import Task

        task = Task("Test task")
        assert task.title == "Test task"
        assert task.completed is False

    def test_task_completion(self):
        """Test that tasks can be marked complete."""
        from task_manager import Task

        task = Task("Test task")
        task.mark_complete()
        assert task.completed is True


class TestTaskManager:
    """Tests for the TaskManager class."""

    def test_add_task(self):
        """Test adding tasks to the manager."""
        from task_manager import TaskManager

        manager = TaskManager()
        manager.add_task("Task 1")
        assert len(manager.tasks) == 1

    def test_get_task_by_index(self):
        """Test getting a task by 1-based index."""
        from task_manager import TaskManager

        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")

        # User expects 1-based indexing
        task = manager.get_task(1)
        assert task.title == "Task 1"  # Will fail due to Bug 2

    def test_get_pending_count(self):
        """Test counting pending tasks."""
        from task_manager import TaskManager

        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")

        # Complete one task
        manager.tasks[0].mark_complete()

        count = manager.get_pending_count()
        assert count == 2  # Will fail due to Bug 4

    def test_remove_completed(self):
        """Test removing completed tasks."""
        from task_manager import TaskManager

        manager = TaskManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")

        # Complete two tasks
        manager.tasks[0].mark_complete()
        manager.tasks[2].mark_complete()

        removed = manager.remove_completed()
        assert removed == 2  # Will fail due to Bug 6
        assert len(manager.tasks) == 1
