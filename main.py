import pygame
from character.CharacterInfo import CharacterInfo
from character.items.Key import Key
from configuration import load_map, load_questions, load_multi_room_map
from fixtures.dimens import initial_character_display_coord_x, initial_character_display_coord_y
from graphics.Screen import Screen
from graphics.views.CharacterInfoView import CharacterInfoView
from graphics.views.BattleView import BattleView
from tokens.BossToken import BossToken


def get_example_character_info_view():
    character_info = CharacterInfo(100, 0, 2, initial_character_display_coord_x, initial_character_display_coord_y)

    # laptop = Laptop()
    # backpack = Backpack()
    # sword = Sword()
    #
    # character_info.add_item(backpack)
    # character_info.add_item(laptop)
    # character_info.add_item(sword)

    return CharacterInfoView(character_info)


if __name__ == "__main__":
    game_map = load_multi_room_map('map_generator/generated_map.json')
    load_questions()
    fields = game_map[0][0]

    screen = Screen(fields, game_map)

    character_info_view = get_example_character_info_view()
    Screen.display_character_info(character_info_view)
    Screen.animate(character_info_view)  # todo: add threads??

