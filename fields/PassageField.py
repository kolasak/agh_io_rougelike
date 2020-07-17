import pygame

from enums.Direction import Direction
from fields.Field import Field
from graphics.Screen import Screen
from graphics.views.CharacterInfoView import CharacterInfoView


class PassageField(Field):
    def __init__(self):
        Field.__init__(self, (0, 255, 255), 'P', True)
        self.bound = False
        self.room = None
        self.next_x = None
        self.next_y = None

    def bind(self, room, coordinates):
        self.room = room
        self.next_x, self.next_y = coordinates

    def interact(self, character_info=None):
        if not character_info:
            pass
        else:
            character_info._x = self.next_x
            character_info._y = self.next_y
            Screen.instance.fields = self.room
            Screen.display_map()
            Screen.display_character(character_info, Direction.SOUTH)
            pygame.display.update()
