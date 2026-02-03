import json
import time
from ironclad.schemas.plan import ExecutionPlan

class LocalLLMAdapter:
    def __init__(self, model, max_retries: int = 3, backoff_sec: float = 0.5):
        self.model = model
        self.max_retries = max_retries
        self.backoff_sec = backoff_sec

    def generate_plan(self, user_input: str) -> dict:
        last_err = None

        for attempt in range(1, self.max_retries + 1):
            raw = self.model.complete(user_input)
            try:
                data = json.loads(raw)
                ExecutionPlan.model_validate(data)
                return data
            except Exception as e:
                last_err = e
                if attempt < self.max_retries:
                    time.sleep(self.backoff_sec * attempt)

        raise ValueError(f"Invalid LLM output after retries: {last_err}")
