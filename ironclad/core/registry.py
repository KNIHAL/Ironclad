class ActionRegistry:
    ALLOWED_ACTIONS = {
        "RUN_SQL",
        "CLEAN_DATA",
        "BUILD_CHART",
        "EXPLAIN_RESULT",
    }

    def __init__(self):
        self._actions = {}

    def register(self, name: str, executor):
        if name not in self.ALLOWED_ACTIONS:
            raise ValueError(f"Action not allowed: {name}")
        self._actions[name] = executor

    def get(self, name: str):
        return self._actions.get(name)
