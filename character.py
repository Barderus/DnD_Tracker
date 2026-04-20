SKILL_NAMES = (
    "Athletics",
    "Arcana",
    "Persuasion",
    "Knowledge",
    "Insight",
    "Investigation",
    "Medicine",
    "Perception",
    "Performance",
    "Agility",
    "Survival",
)


def build_default_skills():
    # Each character starts with the same skill list at zero.
    return {skill_name: 0 for skill_name in SKILL_NAMES}


class Character:
    def __init__(self, name, char_class, race, body=0, mind=0, social=0, discipline=0, level=1, skills=None, inventory=None):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.level = self._validate_level(level)
        self.body = self._validate_stat("body", body)
        self.mind = self._validate_stat("mind", mind)
        self.social = self._validate_stat("social", social)
        self.discipline = self._validate_stat("discipline", discipline)
        self.skills = self._build_skills(skills)
        self.inventory = list(inventory) if inventory is not None else []

    def _validate_level(self, level):
        if not isinstance(level, int):
            raise TypeError("level must be an integer")
        if level < 1:
            raise ValueError("level must be at least 1")
        return level

    def _validate_stat(self, stat_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{stat_name} must be an integer")
        if value < 0:
            raise ValueError(f"{stat_name} cannot be negative")
        return value

    def _build_skills(self, skills):
        # Merge any provided skill values into the default skill template.
        default_skills = build_default_skills()
        if skills is None:
            return default_skills

        for skill_name, value in skills.items():
            if skill_name not in default_skills:
                raise ValueError(f"Unknown skill: {skill_name}")
            default_skills[skill_name] = self._validate_stat(skill_name, value)

        return default_skills

    def allocate_attributes(self, body, mind, social, discipline=None):
        self.body = self._validate_stat("body", body)
        self.mind = self._validate_stat("mind", mind)
        self.social = self._validate_stat("social", social)
        if discipline is not None:
            self.discipline = self._validate_stat("discipline", discipline)

    def level_up(self, levels=1):
        if not isinstance(levels, int):
            raise TypeError("levels must be an integer")
        if levels < 1:
            raise ValueError("levels must be at least 1")
        self.level += levels

    def reset_skills(self):
        self.skills = build_default_skills()

    def set_skill(self, skill_name, value):
        if skill_name not in self.skills:
            raise ValueError(f"Unknown skill: {skill_name}")
        self.skills[skill_name] = self._validate_stat(skill_name, value)

    def increase_skill(self, skill_name, amount=1):
        if skill_name not in self.skills:
            raise ValueError(f"Unknown skill: {skill_name}")
        amount = self._validate_stat("amount", amount)
        self.skills[skill_name] += amount

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def __str__(self):
        return (
            "===== Character Info =====\n"
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Class: {self.char_class}\n"
            f"Race: {self.race}\n"
            f"Body: {self.body}\n"
            f"Mind: {self.mind}\n"
            f"Social: {self.social}\n"
            f"Discipline: {self.discipline}"
        )
