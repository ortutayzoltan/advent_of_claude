"""
Integration tests for the Greeting API.

Tests the Flask application endpoints.
"""

import pytest
from app import create_app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHealthCheck:
    """Tests for the root endpoint."""

    def test_index_returns_200(self, client):
        """Test that the root endpoint returns 200 OK."""
        response = client.get("/")
        assert response.status_code == 200

    def test_index_returns_json(self, client):
        """Test that the root endpoint returns JSON."""
        response = client.get("/")
        assert response.content_type == "application/json"

    def test_index_contains_status(self, client):
        """Test that the response includes status field."""
        response = client.get("/")
        data = response.get_json()
        assert data["status"] == "healthy"


class TestGreetEndpoints:
    """Tests for greeting endpoints."""

    def test_greet_default(self, client):
        """Test default greeting endpoint."""
        response = client.get("/greet")
        assert response.status_code == 200
        data = response.get_json()
        assert "greeting" in data

    def test_greet_with_name(self, client):
        """Test personalized greeting endpoint."""
        response = client.get("/greet/Alice")
        assert response.status_code == 200
        data = response.get_json()
        assert "Alice" in data["greeting"]
        assert data["name"] == "Alice"

    def test_greet_post_casual(self, client):
        """Test custom greeting with casual style."""
        response = client.post(
            "/greet",
            json={"name": "Bob", "style": "casual"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["style"] == "casual"

    def test_greet_post_formal(self, client):
        """Test custom greeting with formal style."""
        response = client.post(
            "/greet",
            json={"name": "Dr. Smith", "style": "formal"}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["style"] == "formal"
        assert "Good day" in data["greeting"]


class TestGoodbyeEndpoint:
    """Tests for the goodbye endpoint (Day 15)."""

    def test_goodbye_returns_farewell(self, client):
        """Test that goodbye endpoint returns a farewell."""
        response = client.get("/goodbye/Charlie")
        assert response.status_code == 200
        data = response.get_json()
        assert "farewell" in data
        assert data["name"] == "Charlie"
