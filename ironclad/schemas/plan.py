from pydantic import BaseModel, Field
from typing import List, Literal

ActionType = Literal[
    "RUN_SQL",
    "CLEAN_DATA",
    "BUILD_CHART",
    "EXPLAIN_RESULT",
]

class Action(BaseModel):
    action: ActionType
    params: dict = Field(default_factory=dict)

class ExecutionPlan(BaseModel):
    intent: str
    actions: List[Action]
