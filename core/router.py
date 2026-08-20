class Router:

    def __init__(self, skill_manager):
        self.skill_manager = skill_manager

    def route(self, user_input):

        skill = self.skill_manager.find_skill(user_input)

        if skill:
            return skill.execute(user_input)

        return None