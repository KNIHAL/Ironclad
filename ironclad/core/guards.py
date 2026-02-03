class PlanGuard:
    MAX_STEPS = 5

    def validate(self, plan, registry):
        if len(plan.actions) > self.MAX_STEPS:
            raise ValueError("Plan too long")

        for step in plan.actions:
            if registry.get(step.action) is None:
                raise ValueError(f"Unregistered action: {step.action}")
