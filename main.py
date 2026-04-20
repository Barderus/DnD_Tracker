from character import Character
from character_creation import distribute_attributes, distribute_skills, get_bio


def main():
    print("===== Welcome to the DnD Habit Tracker ======")
    print("Let's create your character first...")

    name, player_race, player_class = get_bio()
    body, mind, social = distribute_attributes(5)
    skills = distribute_skills(mind)

    player = Character(
        name=name,
        char_class=player_class,
        race=player_race,
        body=body,
        mind=mind,
        social=social,
        discipline=0,
        skills=skills,
    )

    print(player)

if __name__ == '__main__':
    main()
