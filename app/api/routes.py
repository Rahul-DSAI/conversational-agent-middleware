from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.orchestrator import orchestrator

router = APIRouter()

@router.post("/chat")
def chat(payload: ChatRequest):
    return orchestrator.handle(payload.session_id, payload.message)

@router.get("/capabilities")
def capabilities():
    return {"capabilities": ["recipe", "pantry", "shopping", "general"]}

@router.delete("/sessions/{session_id}")
def clear_session(session_id: str):
    orchestrator.clear(session_id)
    return {"session_id": session_id, "cleared": True}
