import pytest
from ironclad.schemas.plan import ExecutionPlan
from ironclad.core.registry import ActionRegistry
from ironclad.core.guards import PlanGuard


def test_valid_plan_passes():
    registry = ActionRegistry()
    registry.register("RUN_SQL", object())
    guard = PlanGuard()

    plan = ExecutionPlan(
        intent="test",
        actions=[{"action": "RUN_SQL", "params": {}}]
    )
    guard.validate(plan, registry)
