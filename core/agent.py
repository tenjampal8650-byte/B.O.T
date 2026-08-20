from core.skill_manager import SkillManager


class Jarvis:

    def __init__(self):
        print("Loading JARVIS...")
        self.skill_manager = SkillManager()

    def process(self, user_input):

        skill = self.skill_manager.find_skill(user_input)

        if skill:
            expression = user_input

            expression = expression.replace("calculate", "")
            expression = expression.replace("calc", "")
            expression = expression.strip()

            return skill.execute(expression)

        return f"You said: {user_input}"