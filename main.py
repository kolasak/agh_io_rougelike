from character.CharacterInfo import CharacterInfo
from character.items.Backpack import Backpack
from character.items.Laptop import Laptop
from character.items.Sword import Sword
from configuration import load_configuration
from graphics.Screen import Screen
from graphics.views.CharacterInfoView import CharacterInfoView


def get_example_character_info_view():
    character_info = CharacterInfo(100, 0, 2)

    laptop = Laptop()
    backpack = Backpack()
    sword = Sword()

    character_info.add_item(backpack)
    character_info.add_item(laptop)
    character_info.add_item(sword)

    return CharacterInfoView(character_info)


if __name__ == "__main__":
    game_map = load_configuration()
    first_stage = game_map[0]

    screen = Screen(first_stage)

    character_info_view = get_example_character_info_view()
    screen.display_character_info(character_info_view)
    screen.animate()  # todo: add threads??

    for row in game_map:
        print(row)

    screen.create_and_show_example_character_info()
