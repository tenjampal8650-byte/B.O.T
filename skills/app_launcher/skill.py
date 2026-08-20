import os


class AppLauncherSkill:

    name = "app_launcher"

    description = "Launches approved applications on Windows."

    triggers = [
        "open ",
        "launch ",
        "start "
    ]

    applications = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vscode": r"code",
        "vs code": r"code",
        "powershell": "powershell.exe",
        "explorer": "explorer.exe",
        "file explorer": "explorer.exe"
    }

    def can_handle(self, user_input):

        text = user_input.lower().strip()

        for trigger in self.triggers:

            if text.startswith(trigger):

                app_name = text[len(trigger):].strip()

                return app_name in self.applications

        return False

    def execute(self, user_input):

        text = user_input.lower().strip()

        app_name = None

        for trigger in self.triggers:

            if text.startswith(trigger):

                app_name = text[len(trigger):].strip()
                break

        if app_name not in self.applications:
            return f"I don't know how to open '{app_name}'."

        command = self.applications[app_name]

        try:

            os.startfile(command)

            return f"Opening {app_name}."

        except Exception as e:

            return f"I couldn't open {app_name}: {e}"