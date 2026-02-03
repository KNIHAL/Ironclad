class LocalPlanner:
    def generate_plan(self, user_input: str) -> dict:
        return {
            "intent": "run_read_query",
            "actions": [
                {
                    "action": "RUN_SQL",
                    "params": {"query": "SELECT 1 AS ok"}
                }
            ]
        }
