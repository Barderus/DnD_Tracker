from character.character import Character
from character.creation import get_name, get_race, get_class, allocate_attributes, allocate_skills

def create_character():

    print("Let's create your character first...")

    char_name = get_name()
    char_race = get_race()
    char_class = get_class()
    char_body, char_mind, char_social = allocate_attributes(5)
    skills = allocate_skills(level=1, mind = char_mind)


    player = Character(
        name=char_name,
        char_class= char_class,
        race=char_race,
        body=char_body,
        mind=char_mind,
        social=char_social,
        discipline=0,
        skills=skills,
    )
    print(player.skills)
    return player

def main():
    print("===== Welcome to the DnD Habit Tracker ======")

    character = create_character()
    print(character)

if __name__ == '__main__':
    main()
