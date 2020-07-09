import pygame

from graphics.settings import *


class Screen:
    pygame = None
    exit_pressed = False
    display_surface = None

    class __Screen:
        def __init__(self, fields):
            Screen.pygame = pygame.init()
            width, height = fields.shape

            Screen.display_surface = pygame.display.set_mode(
                (width * PIXEL_SIZE + SCREEN_PADDING_X, height * PIXEL_SIZE + SCREEN_PADDING_Y))
            for x in range(0, width):
                for y in range(0, height):
                    pygame.draw.rect(Screen.display_surface, fields[x][y].colour,
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
