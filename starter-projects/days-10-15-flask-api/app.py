#!/usr/bin/env python3
"""
Greeting API - Flask REST Application

A simple REST API demonstrating Flask development with Claude Code.
"""

import os
from flask import Flask, jsonify

from routes.greetings import greetings_bp


def create_app():
    """
    Application factory for creating Flask app instances.

    Returns:
        Flask: Configured Flask application.
    """
    app = Flask(__name__)

    # Configuration
    app.config["DEBUG"] = os.getenv("DEBUG", "True").lower() == "true"

    # Register blueprints
    app.register_blueprint(greetings_bp)

    # Root endpoint
    @app.route("/")
    def index():
        """Health check and welcome endpoint."""
        return jsonify({
            "status": "healthy",
            "message": "Welcome to the Greeting API!",
            "version": "1.0.0",
            "endpoints": [
                "GET /greet",
                "GET /greet/<name>",
                "POST /greet",
                "GET /goodbye/<name>"
            ]
        })

    return app


# Create the application instance
app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
