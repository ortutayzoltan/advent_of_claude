"""
Greeting Service - Business logic for greetings.

This module contains the core business logic for creating greetings.
"""


class GreetingService:
    """Service class for handling greeting operations."""

    FORMAL_TEMPLATES = {
        "greeting": "Good day, {name}. It is a pleasure to make your acquaintance.",
        "farewell": "Farewell, {name}. Until we meet again."
    }

    CASUAL_TEMPLATES = {
        "greeting": "Hey {name}! Welcome to the Greeting API!",
        "farewell": "See ya later, {name}! Take care!"
    }

    def create_greeting(self, name: str, style: str = "casual") -> str:
        """
        Create a greeting message.

        Args:
            name: The name to include in the greeting.
            style: The greeting style ('formal' or 'casual').

        Returns:
            A formatted greeting string.

        Examples:
            >>> service = GreetingService()
            >>> service.create_greeting("Alice")
            'Hey Alice! Welcome to the Greeting API!'
            >>> service.create_greeting("Bob", style="formal")
            'Good day, Bob. It is a pleasure to make your acquaintance.'
        """
        name = self._sanitize_name(name)
        templates = self.FORMAL_TEMPLATES if style == "formal" else self.CASUAL_TEMPLATES
        return templates["greeting"].format(name=name)

    def create_farewell(self, name: str, style: str = "casual") -> str:
        """
        Create a farewell message.

        Args:
            name: The name to include in the farewell.
            style: The farewell style ('formal' or 'casual').

        Returns:
            A formatted farewell string.
        """
        name = self._sanitize_name(name)
        templates = self.FORMAL_TEMPLATES if style == "formal" else self.CASUAL_TEMPLATES
        return templates["farewell"].format(name=name)

    def _sanitize_name(self, name: str) -> str:
        """
        Sanitize and validate a name input.

        Args:
            name: The raw name input.

        Returns:
            Cleaned name string, defaulting to 'Friend' if invalid.
        """
        if not name or not isinstance(name, str):
            return "Friend"
        cleaned = name.strip()
        if not cleaned or len(cleaned) > 100:
            return "Friend"
        return cleaned
