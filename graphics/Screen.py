import pygame

from fixtures.constants import font_name, font_size, green, dark_blue
from graphics.ScreenUtil import ScreenUtil
from graphics.settings import *
from graphics.views.CharacterInfoView import CharacterInfoView


class Screen:
    class __Screen:
        def __init__(self, fields, character_info_view):
            self.__pygame = pygame.init()
            self.__exit_pressed = False
            self.__fields = fields
            self.__character_info_view = character_info_view

            self.__width, self.__height = fields.shape

            self.__display_surface = pygame.display.set_mode(
                (self.__width * PIXEL_SIZE + SCREEN_PADDING_X, self.__height * PIXEL_SIZE + SCREEN_PADDING_Y))

            self.__display()
            self.__display_character_info()
            self.__animate()

        def __display(self):
            for x in range(0, self.__width):
                for y in range(0, self.__height):
                    pygame.draw.rect(self.__display_surface, self.__fields[x][y].colour,
                                     (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y,
                                      PIXEL_SIZE, PIXEL_SIZE))
                    if fields[x][y].item is not None:
                        img = pygame.image.load(fields[x][y].item.img_path)
                        Screen.display_surface.blit(img, (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y))

            pygame.display.flip()

        def __display_character_info(self):
            self.__character_info_view.display(self)

        def __animate(self):
            while not self.__exit_pressed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__exit_pressed = True
            pygame.quit()

        def render_text_values(self, text_value, x, x_offset, y, y_offset):
            font = pygame.font.Font(font_name, font_size)
            text = font.render(text_value, True, green, dark_blue)

            text_rect = ScreenUtil.get_positioned_text(text, x, x_offset, y, y_offset)

            self.__display_surface.blit(text, text_rect)

        @property
        def display_surface(self):
            return self.__display_surface

        @display_surface.setter
        def display_surface(self, value):
            self.__display_surface = value

    instance = None

    def __init__(self, fields, character_info):
        self.character_info = character_info
        if not Screen.instance:
            Screen.instance = Screen.__Screen(fields, CharacterInfoView(character_info))
