from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_chat_response():
    response = client.post("/chat", json={"session_id": "test-session", "message": "Suggest dinner"})
    assert response.status_code == 200
    assert response.json()["intent"] == "recipe"
    assert response.headers.get("x-request-id")
