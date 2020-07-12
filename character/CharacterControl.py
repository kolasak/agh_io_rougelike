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

        if event_key == K_w:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x][character_info_view.character_info.y-1]):
                character_info_view.character_info.y = character_info_view.character_info.y-1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.NORTH)
        if event_key == K_a:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x-1][character_info_view.character_info.y]):
                character_info_view.character_info.x = character_info_view.character_info.x-1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.WEST)
        if event_key == K_d:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x+1][character_info_view.character_info.y]):
                character_info_view.character_info.x = character_info_view.character_info.x+1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.EAST)
        if event_key == K_s:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x][character_info_view.character_info.y+1]):
                character_info_view.character_info.y = character_info_view.character_info.y+1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.SOUTH)
        if event_key == K_e:
            field = fields[character_info_view.character_info.x][character_info_view.character_info.y]
            if field.item is not None:
                character_info_view.character_info.add_item(field.get_item())
                Screen.Screen.render_character(character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.SOUTH)
                Screen.Screen.display_character_info(character_info_view)
        if event_key == K_r:
            fields[character_info_view.character_info.x][character_info_view.character_info.y].interact()

    @staticmethod
    def check_if_passable(field):
        return field.passable
