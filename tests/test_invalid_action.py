import pytest
from pydantic import ValidationError
from ironclad.schemas.plan import ExecutionPlan

def test_invalid_action_fails():
    with pytest.raises(ValidationError):
        ExecutionPlan(
            intent="bad",
            actions=[{"action": "HACK", "params": {}}]
        )
