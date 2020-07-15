import pygame
from abc import ABC

from fixtures.constants import black
from graphics.Screen import Screen


class View(ABC):
    def __init__(self):
        self.screen = Screen(None, None)
        self.x_center = Screen.screen_width // 2

    def display(self):
        pass

    def render_line_center(self, text, line_no):
        Screen.render_text_values(text, self.x_center * 2, 0, line_no * 50, 0, background_color=black)
        pygame.display.flip()
