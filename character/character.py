class Character:
    def __init__(self, name, skills, char_class, race, body=0, mind=0, social=0, discipline=0, level=1, inventory=None):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.body = body
        self.mind = mind
        self.social = social
        self.discipline = discipline
        self.level = level
        self.skills = skills
        self.inventory = inventory


    def __str__(self):
        return (
            "===== Character Info =====\n"
            f"Name: {self.name.capitalize()}\n"
            f"Level: {self.level}\n"
            f"Class: {self.char_class.capitalize()}\n"
            f"Race: {self.race.capitalize()}\n"
            f"Body: {self.body}\n"
            f"Mind: {self.mind}\n"
            f"Social: {self.social}\n"
            f"Discipline: {self.discipline}"
        )
