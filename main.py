from character.CharacterInfo import CharacterInfo
from character.items.Key import Key
from configuration import load_configuration
from graphics.Screen import Screen


def get_example_character_info():
    character_info = CharacterInfo(100, 0, 2)

    # laptop = Laptop()
    # backpack = Backpack()
    # sword = Sword()
    #
    # character_info.add_item(backpack)
    # character_info.add_item(laptop)
    # character_info.add_item(sword)

    character_info.add_item(Key())

    return character_info


if __name__ == "__main__":
    game_map = load_configuration()
    fields = game_map[0]

    screen = Screen(fields, get_example_character_info())

    for row in game_map:
        print(row)
