"""
Unit tests for the GreetingService.

Tests the business logic independently from Flask.
"""

import pytest
from services.greeting_service import GreetingService


@pytest.fixture
def service():
    """Create a GreetingService instance for testing."""
    return GreetingService()


class TestCreateGreeting:
    """Tests for the create_greeting method."""

    def test_casual_greeting(self, service):
        """Test casual greeting format."""
        result = service.create_greeting("Alice")
        assert "Alice" in result
        assert "Hey" in result

    def test_formal_greeting(self, service):
        """Test formal greeting format."""
        result = service.create_greeting("Bob", style="formal")
        assert "Bob" in result
        assert "Good day" in result

    def test_empty_name_defaults_to_friend(self, service):
        """Test that empty name defaults to Friend."""
        result = service.create_greeting("")
        assert "Friend" in result

    def test_whitespace_name_defaults_to_friend(self, service):
        """Test that whitespace-only name defaults to Friend."""
        result = service.create_greeting("   ")
        assert "Friend" in result

    def test_name_is_trimmed(self, service):
        """Test that name whitespace is trimmed."""
        result = service.create_greeting("  Alice  ")
        assert "Alice" in result
        assert "  Alice  " not in result


class TestCreateFarewell:
    """Tests for the create_farewell method."""

    def test_casual_farewell(self, service):
        """Test casual farewell format."""
        result = service.create_farewell("Charlie")
        assert "Charlie" in result
        assert "See ya" in result

    def test_formal_farewell(self, service):
        """Test formal farewell format."""
        result = service.create_farewell("Diana", style="formal")
        assert "Diana" in result
        assert "Farewell" in result


class TestSanitizeName:
    """Tests for the _sanitize_name method."""

    def test_valid_name_unchanged(self, service):
        """Test that valid names pass through."""
        result = service._sanitize_name("Alice")
        assert result == "Alice"

    def test_none_returns_friend(self, service):
        """Test that None returns Friend."""
        result = service._sanitize_name(None)
        assert result == "Friend"

    def test_long_name_returns_friend(self, service):
        """Test that overly long names return Friend."""
        long_name = "A" * 101
        result = service._sanitize_name(long_name)
        assert result == "Friend"
