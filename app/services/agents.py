"""Deterministic specialist agents with synthetic content."""

def recipe_agent(message: str) -> str:
    return "Demo suggestion: try a chickpea tomato bowl. Ingredients: chickpeas, tomato, onion, and lemon."

def pantry_agent(message: str) -> str:
    return "Demo pantry: rice (500 g), tomatoes (3), and olive oil (150 ml)."

def shopping_agent(message: str) -> str:
    return "Sample shopping list: chickpeas, tomatoes, onions, and lemons."

def general_agent(message: str) -> str:
    return "I am a local demo assistant. Ask about recipes, pantry contents, or a shopping list."

AGENTS = {
    "recipe": recipe_agent,
    "pantry": pantry_agent,
    "shopping": shopping_agent,
    "general": general_agent,
}
