import time

import pygame
from pygame.locals import KEYDOWN

from character.CharacterController import CharacterController
from fixtures.constants import *
from graphics.settings import *
from graphics.settings import CHARACTER_IMAGE_PATH


class Screen:
    pygame = None
    exit_pressed = False
    display_surface = None
    game_map = None
    screen_width = None
    screen_height = None
    instance = None

    class __Screen:
        def __init__(self, fields):
            Screen.pygame = pygame.init()
            self.width, self.height = fields.shape
            self.fields = fields

            Screen.screen_width = self.width * PIXEL_SIZE + SCREEN_PADDING_X
            Screen.screen_height = self.height * PIXEL_SIZE + SCREEN_PADDING_Y
            Screen.display_surface = pygame.display.set_mode((Screen.screen_width, Screen.screen_height))
            self.display_map()

        def display_map(self):
            Screen.display_surface.fill(dark_blue)
            for x in range(0, self.width):
                for y in range(0, self.height):
                    Screen.draw_field(x, y, self.fields)
            pygame.display.flip()

    def __new__(cls, fields, game_map):
        if not Screen.instance:
            Screen.instance = Screen.__Screen(fields)
            Screen.game_map = game_map
        return Screen.instance

    @staticmethod
    def animate(character_info_view):
        while not Screen.exit_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Screen.exit_pressed = True
                elif event.type == KEYDOWN:
                    CharacterController.execute_character_movement(event.key, character_info_view,
                                                                   Screen.instance.fields)
        pygame.quit()

    @staticmethod
    def display_character_info(character_info_view):
        character_info_view.display()

    @staticmethod
    def render_character(old_x, old_y, x, y, img, direction):
        Screen.draw_field(old_x, old_y, Screen.instance.fields)
        img = pygame.transform.rotate(img, direction.value * 90)
        Screen.display_surface.blit(img, (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y))
        pygame.display.update()

    @staticmethod
    def display_character(character_info, direction):
        x = character_info.x
        y = character_info.y
        img = pygame.image.load(CHARACTER_IMAGE_PATH)
        # img = pygame.transform.rotate(img, direction.value * 90)
        Screen.display_surface.blit(img, (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y))
        pygame.display.update()

    @staticmethod
    def display_map():
        Screen.instance.display_map()

    @staticmethod
    def repaint_screen():
        fields = Screen.instance.fields
        Screen.instance = None
        Screen.instance = Screen(fields, Screen.game_map)

    @staticmethod
    def render_text_values_for_n_seconds(character_info_view, text_value, x, x_offset, y, y_offset, font_color=green,
                                         background_color=dark_blue, nsec=1):
        Screen.render_text_values(text_value, x, x_offset, y, y_offset, font_color, background_color)
        pygame.display.flip()
        time.sleep(nsec)
        Screen.display_surface.fill(dark_blue)  # erases the entire screen surface
        Screen.repaint_screen()
        Screen.display_character_info(character_info_view)

    @staticmethod
    def render_text_values(text_value, x, x_offset, y, y_offset, font_color=green, background_color=dark_blue):
        font = pygame.font.Font(font_name, font_size)
        text = font.render(text_value, True, font_color, background_color)

        text_rect = Screen.__get_positioned_text(text, x, x_offset, y, y_offset)

        Screen.display_surface.blit(text, text_rect)

    @staticmethod
    def __get_positioned_text(text, x, x_offset, y, y_offset):
        X, Y = Screen.__calculate_text_coordinates_with_offset(x, x_offset, y, y_offset)

        text_rect = text.get_rect()
        text_rect.center = (X // 2, Y // 2)

        return text_rect

    @staticmethod
    def draw_field(x, y, fields):
        pygame.draw.rect(Screen.display_surface, fields[x][y].colour,
                         (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y,
                          PIXEL_SIZE, PIXEL_SIZE))
        if fields[x][y].item is not None:
            img = pygame.image.load(fields[x][y].item.img_path)
            Screen.display_surface.blit(img, (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y))

        if fields[x][y].token is not None:
            img = pygame.image.load(fields[x][y].token.image)
            Screen.display_surface.blit(img, (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y))

    @staticmethod
    def __calculate_text_coordinates_with_offset(x, x_offset, y, y_offset):
        return x - x_offset, y + y_offset
