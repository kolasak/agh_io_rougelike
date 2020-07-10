import pygame
from pygame.locals import KEYDOWN, K_w, K_a, K_s, K_d, K_e

from enums.Direction import Direction
from graphics import Screen


class CharacterControl:
    def __init__(self):
        pass

    @staticmethod
    def execute_character_movement(event_key, character_info_view, fields):
        if event_key == K_w:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x][character_info_view.character_info.y-1]):
                old_x = character_info_view.character_info.x
                old_y = character_info_view.character_info.y
                character_info_view.character_info.y = character_info_view.character_info.y-1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.NORTH)
            else:
                print("not passable")
        if event_key == K_a:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x-1][character_info_view.character_info.y]):
                old_x = character_info_view.character_info.x
                old_y = character_info_view.character_info.y
                character_info_view.character_info.x = character_info_view.character_info.x-1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.WEST)
            else:
                print("not passable")
        if event_key == K_d:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x+1][character_info_view.character_info.y]):
                old_x = character_info_view.character_info.x
                old_y = character_info_view.character_info.y
                character_info_view.character_info.x = character_info_view.character_info.x+1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.EAST)
            else:
                print("not passable")
        if event_key == K_s:
            if CharacterControl.check_if_passable(fields[character_info_view.character_info.x][character_info_view.character_info.y+1]):
                old_x = character_info_view.character_info.x
                old_y = character_info_view.character_info.y
                character_info_view.character_info.y = character_info_view.character_info.y+1
                Screen.Screen.render_character(old_x, old_y, character_info_view.character_info.x, character_info_view.character_info.y, character_info_view.character_img, Direction.SOUTH)
            else:
                print("not passable")

    @staticmethod
    def check_if_passable(field):
        print(field.colour)
        return field.passable
