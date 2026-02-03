from abc import ABC, abstractmethod

class Planner(ABC):
    @abstractmethod
    def generate_plan(self, user_input: str) -> dict:
        """Return JSON ONLY (ExecutionPlan-compatible)"""
        raise NotImplementedError
