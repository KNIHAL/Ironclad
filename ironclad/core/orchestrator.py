from ironclad.schemas.plan import ExecutionPlan

class Orchestrator:
    def __init__(self, planner, registry, guard, logger, audit):
        self.planner = planner
        self.registry = registry
        self.guard = guard
        self.logger = logger
        self.audit = audit

    def run(self, user_input: str):
        self.audit.add("REQUEST", {"input": user_input})

        raw_plan = self.planner.generate_plan(user_input)
        self.audit.add("PLAN_RAW", raw_plan)

        plan = ExecutionPlan.model_validate(raw_plan)
        self.guard.validate(plan, self.registry)
        self.audit.add("PLAN_OK", plan.model_dump())

        results = []
        for step in plan.actions:
            self.audit.add("STEP_START", {"action": step.action, "params": step.params})
            out = self.registry.get(step.action).execute(step.params)
            self.audit.add("STEP_END", {"action": step.action, "output": out})
            results.append({"action": step.action, "output": out})

        self.audit.add("RUN_COMPLETE", {"results": results})
        return results
