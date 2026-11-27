from collections import defaultdict, deque

class SessionStore:
    def __init__(self, max_turns: int = 12):
        self._history = defaultdict(lambda: deque(maxlen=max_turns))

    def append(self, session_id: str, role: str, content: str) -> None:
        self._history[session_id].append({"role": role, "content": content})

    def get(self, session_id: str) -> list[dict[str, str]]:
        return list(self._history[session_id])

    def clear(self, session_id: str) -> None:
        self._history.pop(session_id, None)
