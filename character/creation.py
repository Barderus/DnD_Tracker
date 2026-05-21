CLASSES = ["warrior", "archer", "mage", "druid", "paladin", "dragoon"]
RACES = ["human", "elf", "dwarf", "gnome", "halfling", "owling"]
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

yes = ["yes", "y"]

# Normalize typed skill names back to the canonical display keys.
SKILL_NAME_LOOKUP = {skill_name.lower(): skill_name for skill_name in SKILL_NAMES}

# Confirm options function
def confirm():
    confirm = input("\tAre you sure of your choice? (y/n) ").lower()
    if confirm in yes:
        return True
    else:
        print()
        return False

# Get the character name
def get_name():
    while True:
        name = input("What is your character's name? ").capitalize()
        val = confirm()
        if val:
            return name

# Get the character class
def get_class():
    while True:
        print("\n== Classes Available ===")
        print(*CLASSES, sep=", ")
        char_class = input("What is your character's class? ").lower()
        if char_class in CLASSES:
            val = confirm()
            if val:
                return char_class
        else:
            print(f"\n {char_class} not available. Please selected one of the available classes.")

# Get the character race
def get_race():
    while True:
        print("\n== Races Available ===")
        print(*RACES, sep=", ")
        char_race = input("What is your character's class? ").lower()
        if char_race in RACES:
            val = confirm()
            if val:
                return char_race
        else:
            print(f"\n {char_race} not available. Please selected one of the available races.")

def get_points(atr, max_points):
    while True:
        attribute = input(f"\nEnter how many points you would like to add to {atr}. You have {max_points} points available ")
        try:
            points = int(attribute)

            # Reject negative allocations so remaining points cannot increase.
            if points < 0:
                print("\nPoints cannot be negative.")
                continue

            # Check if too many points were allocated, > max_points
            if points > max_points:
                print(f"\nYou cannot allocate more than {max_points} points.")
                continue

            points_left = max_points - points
            return points, points_left
        except ValueError:
            print("Must enter a valid number")


# Distribute attributes
def allocate_attributes(points):
    body_points, mind_points, social_points = 0, 0, 0

    print(f"""\n
    === Welcome to Attributes Point Allocation ===
    \nYou have {points} to distribute.
    1. Body
    \t Represents your physical strength
    2. Mind
    \t Represents your willpower and cleverness 
    3. Social
    \t Represents how social your character is
            """)

    # Allocate the points to each attribute
    while points != 0:
        # Accumulate each pass
        new_points, points_left = get_points("body", points)
        body_points += new_points
        points = points_left
        if points == 0:
            break

        new_points, points_left = get_points("mind", points)
        mind_points += new_points
        points = points_left
        if points == 0:
            break

        new_points, points_left = get_points("social", points)
        social_points += new_points
        points = points_left

    body = body_points
    mind = mind_points
    social = social_points
    return body, mind, social

# Each character starts with the same skill list at zero.
def build_default_skills():
    return {skill_name: 0 for skill_name in SKILL_NAMES}

# Distribute skills (depends on the attribute "Mind")
def allocate_skills(level, mind):
    skill_dict = build_default_skills()

    if level == 1:
        points = 5
    else:
        if mind / 2 < 1:
            points = 1
        else:
            points = mind // 2

    print("\n === Welcome to Skill Allocation ===")
    print("\t\tPossible skills list:")
    print(*SKILL_NAMES, sep=", ")

    while points != 0:
        # Accept case-insensitive input while storing the original skill name.
        skill_input = input("\nWhich skill would you like to add points to? ").strip().lower()
        skill_name = SKILL_NAME_LOOKUP.get(skill_input)
        if skill_name:
            while True:
                try:
                    skill_point = int(input(f"\nHow many points would you like to add to {skill_name}? "))
                except ValueError:
                    print("Must enter a valid number")
                    continue

                # Reject negative skill allocations for the same reason as attributes.
                if skill_point < 0:
                    print("\nPoints cannot be negative.")
                    continue

                if skill_point <= points:
                    skill_dict[skill_name] += skill_point
                    points -= skill_point
                    print(f"\nYou allocated {skill_point} point to {skill_name}.")
                    break

                print(f"\nYou don't have enough points to allocate to {skill_name}. Try again.")
        else:
            print(f"\n{skill_input} doesn't exist. Try again.")

    return skill_dict



