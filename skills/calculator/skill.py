class CalculatorSkill:

    name = "calculator"

    description = "Performs mathematical calculations."

    triggers = [
        "calculate",
        "math",
    ]

    def can_handle(self, user_input):
        user_input = user_input.lower().strip()

        # Explicit commands
        if any(user_input.startswith(trigger) for trigger in self.triggers):
            return True

        # Plain mathematical expression
        allowed = set("0123456789+-*/().% ")

        return bool(user_input) and all(
            char in allowed for char in user_input
        )

    def execute(self, user_input):
        user_input = user_input.strip()

        # Remove command if present
        for trigger in self.triggers:
            if user_input.lower().startswith(trigger):
                user_input = user_input[len(trigger):].strip()
                break

        try:
            return eval(
                user_input,
                {"__builtins__": {}},
                {}
            )
        except Exception:
            return "I couldn't calculate that."