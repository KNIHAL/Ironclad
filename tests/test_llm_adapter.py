import pytest
from ironclad.core.llm_adapter import LocalLLMAdapter

class FlakyModel:
    def __init__(self):
        self.calls = 0
    def complete(self, _):
        self.calls += 1
        if self.calls < 2:
            return "not json"
        return '{"intent":"ok","actions":[]}'

def test_llm_adapter_retry_success():
    adapter = LocalLLMAdapter(FlakyModel(), max_retries=3, backoff_sec=0)
    plan = adapter.generate_plan("hi")
    assert plan["intent"] == "ok"
