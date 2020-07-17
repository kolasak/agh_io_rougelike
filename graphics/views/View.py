import time
from abc import ABC

import pygame

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

    def display_game_ending(self, exp, is_won):
        Screen.display_surface.fill(black)

        if is_won:
            text = 'CONGRATULATIONS! You WON the game!'
        else:
            text = 'GAME OVER. Thanks for playing. You can try again in a year! ;)'

        self.render_line_center(text, 1)
        self.render_line_center(f'You got {exp} EXP.', 2)
        time.sleep(5)
        Screen.exit_pressed = True
