from character.CharacterInfo import CharacterInfo
from configuration import load_questions, load_multi_room_map
from enums.Direction import Direction
from fixtures.constants import max_hp
from fixtures.dimens import initial_character_display_coord_x, initial_character_display_coord_y
from graphics.Screen import Screen
from graphics.views.CharacterInfoView import CharacterInfoView


def get_example_character_info_view():
    character_info = CharacterInfo(max_hp, 0, 2, initial_character_display_coord_x, initial_character_display_coord_y,
                                   Direction.SOUTH)

    return CharacterInfoView(character_info)


if __name__ == "__main__":
    game_map = load_multi_room_map('config.json')
    fields = game_map[1][1]
    load_questions()

    screen = Screen(fields, game_map)

    character_info_view = get_example_character_info_view()
    Screen.display_character_info(character_info_view)
    Screen.animate(character_info_view)  # todo: add threads??
