from fastapi import FastAPI
from app.api.routes import router
from app.middleware.request_context import RequestContextMiddleware

app = FastAPI(title="Conversational Agent Middleware Demo", version="1.0.0")
app.add_middleware(RequestContextMiddleware)
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "environment": "local-demo"}
