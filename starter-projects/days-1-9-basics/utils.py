"""
Utility functions for the greeting application.

This module contains helper functions used throughout the project.
"""


def create_greeting(name: str) -> str:
    """
    Create a personalized greeting message.

    Args:
        name: The name of the person to greet.

    Returns:
        A formatted greeting string.

    Examples:
        >>> create_greeting("Alice")
        'Hello, Alice! Welcome to Advent of Claude Code!'
    """
    if not name or not name.strip():
        name = "World"
    return f"Hello, {name.strip()}! Welcome to Advent of Claude Code!"


def validate_name(name: str) -> bool:
    """
    Validate that a name is appropriate for greeting.

    Args:
        name: The name to validate.

    Returns:
        True if the name is valid, False otherwise.
    """
    if not name or not isinstance(name, str):
        return False
    if len(name.strip()) == 0:
        return False
    if len(name) > 100:
        return False
    return True
