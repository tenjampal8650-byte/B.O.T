from skills.calculater.skill import CalculatorSkill


class SkillManager:

    def __init__(self):
        self.skills = [
            CalculatorSkill()
        ]

    def find_skill(self, user_input):
        text = user_input.lower()

        if "calculate" in text or "calc" in text:
            return self.skills[0]

        return None