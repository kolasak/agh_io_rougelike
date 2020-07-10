from character.CharacterInfo import CharacterInfo
from character.CharacterInfoView import CharacterInfoView
from character.items.Backpack import Backpack
from character.items.Laptop import Laptop
from character.items.Sword import Sword
from configuration import load_configuration


def create_and_show_example_character_info():
    character_info = CharacterInfo(100, 0, 2)

    laptop = Laptop()
    backpack = Backpack()
    sword = Sword()

    character_info.add_item(backpack)
    character_info.add_item(laptop)
    character_info.add_item(sword)

    character_info_view = CharacterInfoView(character_info)
    character_info_view.display_character_info()


if __name__ == "__main__":
    game_map = load_configuration()
    for row in game_map:
        print(row)

    create_and_show_example_character_info()
