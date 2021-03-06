from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type DarkWizard has level {self.level}"