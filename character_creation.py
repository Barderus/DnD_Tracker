from character import SKILL_NAMES, build_default_skills


CLASSES = ["warrior", "archer", "mage", "druid", "paladin", "dragoon"]
RACES = ["human", "elf", "dwarf", "gnome", "halfling", "owling"]


def _prompt_confirmation(message):
    while True:
        response = input(message).strip().lower()
        if response in {"y", "n"}:
            return response == "y"
        print("Invalid input. Enter 'y' or 'n'.")


def _prompt_non_negative_int(message, maximum=None):
    while True:
        try:
            value = int(input(message).strip())
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue

        if value < 0:
            print("Invalid input. You must use a non-negative integer.")
            continue
        if maximum is not None and value > maximum:
            print("Not enough points. Try again.")
            continue
        return value


def _prompt_choice(message, options):
    while True:
        print(message)
        for option in options:
            print(f"\t{option.capitalize()}")

        choice = input(" Pick one: ").strip().lower()
        if choice not in options:
            print("Invalid input. Enter one of the listed options.")
            continue

        if _prompt_confirmation(f"Is {choice.capitalize()} correct? (y/n): "):
            return choice


def get_bio():
    while True:
        name = input(" Pick your character name: ").strip()
        if not name:
            print("Invalid input. Name cannot be empty.")
            continue
        if _prompt_confirmation(f"Is your character name {name} correct? (y/n): "):
            break

    player_class = _prompt_choice(
        f"\n{name.capitalize()} pick your class from the following options:",
        CLASSES,
    )
    player_race = _prompt_choice(
        f"\n{name.capitalize()} pick your race from the following options:",
        RACES,
    )

    print(
        f"\nName: {name.capitalize()}"
        f"\nRace: {player_race.capitalize()}"
        f"\nClass: {player_class.capitalize()}"
    )
    return name, player_race, player_class


def distribute_attributes(points):
    print(
        f"\nLet's distribute your points now."
        f"\nYou have {points} points to distribute between Body, Mind, and Social."
    )

    remaining_points = points
    body = _prompt_non_negative_int(
        f"\nHow many points would you like to add to Body? ({remaining_points} available): ",
        maximum=remaining_points,
    )
    remaining_points -= body

    mind = _prompt_non_negative_int(
        f"How many points would you like to add to Mind? ({remaining_points} available): ",
        maximum=remaining_points,
    )
    remaining_points -= mind

    # Social gets whatever is left so the full pool is always spent.
    social = remaining_points
    remaining_points -= social

    print(
        f"\nPoint Distribution:"
        f"\nBody: {body}"
        f"\nMind: {mind}"
        f"\nSocial: {social}"
        f"\nUnspent Points: {remaining_points}"
    )
    return body, mind, social


def distribute_skills(mind):
    # Mind determines how many total skill points the player can assign.
    available_points = mind // 2 + 1
    selected_skills = build_default_skills()

    print(
        f"\nThis is great!"
        f"\nLet's now set up your skills. You have {available_points} skill points to assign."
    )
    print(display_skills())
    print("Enter 0 at any time to show the skill list again.")

    spent_points = 0
    while spent_points < available_points:
        remaining_points = available_points - spent_points
        choice = _prompt_non_negative_int(
            f"Choose a skill number to gain 1 point ({remaining_points} remaining): "
        )

        if choice == 0:
            print(display_skills())
            continue

        if choice > len(SKILL_NAMES):
            print("Invalid input. Enter one of the listed skill numbers.")
            continue

        # Repeated picks stack, so players can specialize in one skill.
        skill_name = SKILL_NAMES[choice - 1]
        selected_skills[skill_name] += 1
        spent_points += 1
        print(f"{skill_name} increased to {selected_skills[skill_name]}.")

    print("\nFinal skill allocation:")
    for skill_name, value in selected_skills.items():
        if value > 0:
            print(f"{skill_name}: {value}")

    return selected_skills


def display_skills():
    lines = ["Options:"]
    for index, skill_name in enumerate(SKILL_NAMES, start=1):
        lines.append(f"{index}. {skill_name}")
    return "\n".join(lines)
