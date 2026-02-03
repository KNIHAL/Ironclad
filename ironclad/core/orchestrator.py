from ironclad.schemas.plan import ExecutionPlan

class Orchestrator:
    def __init__(self, planner, registry, guard, logger):
        self.planner = planner
        self.registry = registry
        self.guard = guard
        self.logger = logger

    def run(self, user_input: str):
        self.logger.log("PLAN_START")
        raw_plan = self.planner.generate_plan(user_input)
        plan = ExecutionPlan.model_validate(raw_plan)
        self.guard.validate(plan, self.registry)

        results = []
        for step in plan.actions:
            self.logger.log(f"EXECUTE {step.action}")
            executor = self.registry.get(step.action)
            output = executor.execute(step.params)
            results.append({"action": step.action, "output": output})

        self.logger.log("RUN_COMPLETE")
        return results
