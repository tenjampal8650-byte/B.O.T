import importlib
import pkgutil
import skills


class SkillManager:

    def __init__(self):
        self.skills = {}

    def register(self, skill):
        self.skills[skill.name] = skill

    def get_skill(self, name):
        return self.skills.get(name)

    def load_skills(self):

        for module_info in pkgutil.iter_modules(skills.__path__):

            skill_name = module_info.name

            print(f"Loading skill: {skill_name}")

            try:
                module = importlib.import_module(
                    f"skills.{skill_name}.skill"
                )

                print(f"  Imported: {module}")

                for item in dir(module):

                    obj = getattr(module, item)

                    if (
                        isinstance(obj, type)
                        and hasattr(obj, "name")
                        and hasattr(obj, "execute")
                    ):
                        self.register(obj())
                        print(f"  Registered: {obj.name}")

            except Exception as e:

                print(
                    f"  ERROR loading '{skill_name}': "
                    f"{type(e).__name__}: {e}"
                )