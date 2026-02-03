from ironclad.core.orchestrator import Orchestrator
from ironclad.core.registry import ActionRegistry
from ironclad.core.guards import PlanGuard
from ironclad.core.logger import AuditLogger
from ironclad.executors.run_sql import ReadOnlySQLExecutor
from ironclad.core.planner_local import LocalPlanner
from ironclad.core.audit import AuditTrail


def test_planner_flow():
    registry = ActionRegistry()
    registry.register("RUN_SQL", ReadOnlySQLExecutor("sqlite:///:memory:"))

    orch = Orchestrator(             
        LocalPlanner(),
        registry,
        PlanGuard(),
        AuditLogger(),
        AuditTrail(),
    )

    result = orch.run("anything")
    assert result[0]["action"] == "RUN_SQL"
