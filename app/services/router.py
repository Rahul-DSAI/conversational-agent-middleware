from dataclasses import dataclass

@dataclass(frozen=True)
class Route:
    intent: str
    confidence: float

RULES = {
    "recipe": ("recipe", "cook", "dinner", "meal", "ingredient"),
    "pantry": ("pantry", "stock", "what do i have"),
    "shopping": ("shopping list", "grocery", "buy", "shopping"),
}

def classify(message: str) -> Route:
    text = message.casefold()
    for intent, keywords in RULES.items():
        if any(keyword in text for keyword in keywords):
            return Route(intent=intent, confidence=0.85)
    return Route(intent="general", confidence=0.55)
