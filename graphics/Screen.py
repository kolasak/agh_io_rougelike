import pygame

from character.CharacterControl import CharacterControl
from fixtures.constants import font_name, font_size, green, dark_blue
from graphics.settings import *
from pygame.locals import KEYDOWN

class Screen:
    pygame = None
    exit_pressed = False
    display_surface = None

    class __Screen:
        def __init__(self, fields):
            Screen.pygame = pygame.init()
            width, height = fields.shape
            self.fields = fields

            Screen.display_surface = pygame.display.set_mode(
                (width * PIXEL_SIZE + SCREEN_PADDING_X, height * PIXEL_SIZE + SCREEN_PADDING_Y))
            for x in range(0, width):
                for y in range(0, height):
                    Screen.draw_field(x, y, fields)

            pygame.display.flip()

    instance = None

    def __init__(self, fields):
        if not Screen.instance:
            Screen.instance = Screen.__Screen(fields)
            # self.exit_pressed = False
        # else: todo: ???
        #     Screen.instance.fields = fields

    def animate(self, character_info_view):
        while not self.exit_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_pressed = True
                elif event.type == KEYDOWN:
                    CharacterControl.execute_character_movement(event.key, character_info_view, Screen.instance.fields)

        pygame.quit()

    @staticmethod
    def display_character_info(character_info_view):
        character_info_view.display()

    @staticmethod
    def render_character(old_x, old_y, x, y, img, direction):
        Screen.draw_field(old_x, old_y, Screen.instance.fields)
        img = pygame.transform.rotate(img, direction.value * 90)
        print("render character: x: " + str(x))
        print("render character: y: " + str(y))
        Screen.display_surface.blit(img, (x * PIXEL_SIZE + SCREEN_PADDING_X / 2, y * PIXEL_SIZE + SCREEN_PADDING_Y))
        pygame.display.update()

    def render_text_values(self, text_value, x, x_offset, y, y_offset):
        font = pygame.font.Font(font_name, font_size)
        text = font.render(text_value, True, green, dark_blue)

        text_rect = self.__get_positioned_text(text, x, x_offset, y, y_offset)

        self.display_surface.blit(text, text_rect)

    def __get_positioned_text(self, text, x, x_offset, y, y_offset):
        X, Y = self.__calculate_text_coordinates_with_offset(x, x_offset, y, y_offset)

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

    @staticmethod
    def __calculate_text_coordinates_with_offset(x, x_offset, y, y_offset):
        return x - x_offset, y + y_offset
