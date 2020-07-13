import pygame
from pygame.locals import KEYDOWN, K_w, K_a, K_s, K_d, K_e, K_r

from enums.Direction import Direction
from graphics import Screen


class CharacterControl:
    def __init__(self):
        pass

    @staticmethod
    def execute_character_movement(event_key, character_info_view, fields):
        old_x = character_info_view.character_info.x
        old_y = character_info_view.character_info.y

        move_keys = {
            K_w: (0, -1, Direction.NORTH),
            K_a: (-1, 0, Direction.WEST),
            K_d: (1, 0, Direction.EAST),
            K_s: (0, 1, Direction.SOUTH)
        }

        if event_key in move_keys.keys():
            x = character_info_view.character_info.x + move_keys[event_key][0]
            y = character_info_view.character_info.y + move_keys[event_key][1]
            token = fields[x][y].get_token()
            if token is not None:
                token.interact(character_info_view.character_info)
                Screen.Screen.display_map()
                character_info_view.display()
            elif CharacterControl.check_if_passable(fields[x][y]):
                character_info_view.character_info.x = x
                character_info_view.character_info.y = y
                Screen.Screen.render_character(old_x, old_y, x, y, character_info_view.character_img, move_keys[event_key][2])
        elif event_key == K_e:
            field = fields[character_info_view.character_info.x][character_info_view.character_info.y]
            if field.item is not None:
                character_info_view.character_info.add_item(field.get_item())
                Screen.Screen.render_character(character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.SOUTH)
                Screen.Screen.display_character_info(character_info_view)
        elif event_key == K_r:
            fields[character_info_view.character_info.x][character_info_view.character_info.y].interact()

    @staticmethod
    def check_if_passable(field):
        return field.passable
