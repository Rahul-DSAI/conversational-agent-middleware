from uuid import uuid4
from app.services.router import classify
from app.services.agents import AGENTS
from app.services.session_store import SessionStore

class ConversationOrchestrator:
    def __init__(self):
        self.sessions = SessionStore()

    def handle(self, session_id: str, message: str) -> dict:
        route = classify(message)
        answer = AGENTS[route.intent](message)
        self.sessions.append(session_id, "user", message)
        self.sessions.append(session_id, "assistant", answer)
        return {
            "response_id": str(uuid4()),
            "session_id": session_id,
            "intent": route.intent,
            "confidence": route.confidence,
            "reply": answer,
            "history": self.sessions.get(session_id),
            "provider": "mock-agent",
        }

    def clear(self, session_id: str) -> None:
        self.sessions.clear(session_id)

orchestrator = ConversationOrchestrator()
