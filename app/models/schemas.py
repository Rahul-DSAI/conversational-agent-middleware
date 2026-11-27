from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    session_id: str = Field(default="demo-session", min_length=1, max_length=80)
    message: str = Field(min_length=1, max_length=2000)
