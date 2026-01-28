"""
Greeting route handlers.

This module contains all endpoints related to greeting functionality.
"""

from flask import Blueprint, jsonify, request

from services.greeting_service import GreetingService


greetings_bp = Blueprint("greetings", __name__)
greeting_service = GreetingService()


@greetings_bp.route("/greet", methods=["GET"])
def greet_default():
    """
    Get the default greeting.

    Returns:
        JSON response with default greeting message.
    """
    greeting = greeting_service.create_greeting("World")
    return jsonify({"greeting": greeting})


@greetings_bp.route("/greet/<name>", methods=["GET"])
def greet_name(name: str):
    """
    Get a personalized greeting.

    Args:
        name: The name to include in the greeting.

    Returns:
        JSON response with personalized greeting.
    """
    greeting = greeting_service.create_greeting(name)
    return jsonify({"greeting": greeting, "name": name})


@greetings_bp.route("/greet", methods=["POST"])
def greet_custom():
    """
    Create a custom greeting with options.

    Expected JSON body:
        - name (str): Name to greet
        - style (str, optional): 'formal' or 'casual' (default: casual)

    Returns:
        JSON response with customized greeting.
    """
    data = request.get_json() or {}
    name = data.get("name", "World")
    style = data.get("style", "casual")

    greeting = greeting_service.create_greeting(name, style=style)
    return jsonify({
        "greeting": greeting,
        "name": name,
        "style": style
    })


@greetings_bp.route("/goodbye/<name>", methods=["GET"])
def goodbye(name: str):
    """
    Get a farewell message.

    This endpoint is for Day 15 exercise (feature branch practice).

    Args:
        name: The name to include in the farewell.

    Returns:
        JSON response with farewell message.
    """
    farewell = greeting_service.create_farewell(name)
    return jsonify({"farewell": farewell, "name": name})
