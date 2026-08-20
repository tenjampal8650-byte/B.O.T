class CalculatorSkill:

    name = "calculator"

    description = "Performs basic mathematical calculations."

    def execute(self, expression):
        try:
            return eval(
                expression,
                {"__builtins__": {}},
                {}
            )
        except Exception:
            return "I couldn't calculate that."