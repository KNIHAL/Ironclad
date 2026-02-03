from ironclad.core.registry import ActionRegistry
from ironclad.executors.run_sql import ReadOnlySQLExecutor
from ironclad.core.planner_local import LocalPlanner


registry = ActionRegistry()

registry.register(
    "RUN_SQL",
    ReadOnlySQLExecutor(db_url="sqlite:///example.db")
)
