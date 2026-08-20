from core.skill_manager import SkillManager


class Jarvis:

    def __init__(self):
        print("Loading JARVIS...")

        self.skill_manager = SkillManager()
        self.skill_manager.load_skills()

        print("Skills loaded:", list(self.skill_manager.skills.keys()))

    def process(self, user_input):
        user_input = user_input.strip()

        if user_input.lower().startswith("calculate "):

            expression = user_input[10:].strip()

            calculator = self.skill_manager.get_skill("calculator")

            if calculator:
                return calculator.execute(expression)

            return "Calculator skill is not available."

        if user_input.lower().startswith("search "):

            query = user_input[7:].strip()

            web_search = self.skill_manager.get_skill("web_search")

            if web_search:
                return web_search.execute(query)

            return "Web search skill is not available."

        return f"You said: {user_input}"