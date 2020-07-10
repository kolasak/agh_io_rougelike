import pygame

from fixtures.constants import font_name, font_size, green, dark_blue
from fixtures.constants import font_name, font_size
from fixtures.constants import *
from graphics.settings import *


class Screen:
    pygame = None
    exit_pressed = False
    display_surface = None

    class __Screen:
        def __init__(self, fields):
            Screen.pygame = pygame.init()
            self.fields = fields
            self.width, self.height = fields.shape
            Screen.screen_width = self.width * PIXEL_SIZE + SCREEN_PADDING_X
            Screen.screen_height = self.height * PIXEL_SIZE + SCREEN_PADDING_Y

            Screen.display_surface = pygame.display.set_mode((Screen.screen_width, Screen.screen_height))

        def display_map(self):
            Screen.display_surface.fill(dark_blue)
            for x in range(0, self.width):
                for y in range(0, self.height):
                    pygame.draw.rect(Screen.display_surface, self.fields[x][y].colour,
                                     (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y,
                                      PIXEL_SIZE, PIXEL_SIZE))
            pygame.display.flip()

    instance = None

    def __init__(self, fields):
        if not Screen.instance:
            Screen.instance = Screen.__Screen(fields)
            # self.exit_pressed = False
        # else: todo: ???
        #     Screen.instance.fields = fields

    def animate(self):
        while not self.exit_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_pressed = True
        pygame.quit()

    @staticmethod
    def display_character_info(character_info_view):
        character_info_view.display()

    @staticmethod
    def display_map():
        Screen.instance.display_map()

    def render_text_values(self, text_value, x, x_offset, y, y_offset, font_color=green, background_color=dark_blue):
        font = pygame.font.Font(font_name, font_size)
        text = font.render(text_value, True, font_color, background_color)

        text_rect = self.__get_positioned_text(text, x, x_offset, y, y_offset)

        self.display_surface.blit(text, text_rect)

    def __get_positioned_text(self, text, x, x_offset, y, y_offset):
        X, Y = self.__calculate_text_coordinates_with_offset(x, x_offset, y, y_offset)

        text_rect = text.get_rect()
        text_rect.center = (X, Y)

        return text_rect

    @staticmethod
    def __calculate_text_coordinates_with_offset(x, x_offset, y, y_offset):
        return x - x_offset, y + y_offset
