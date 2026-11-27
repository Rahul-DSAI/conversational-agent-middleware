from app.services.router import classify

def test_recipe_route():
    assert classify("Can you suggest dinner?").intent == "recipe"

def test_pantry_route():
    assert classify("What is in my pantry?").intent == "pantry"

def test_shopping_route():
    assert classify("Make a shopping list").intent == "shopping"

def test_general_route():
    assert classify("Hello there").intent == "general"
