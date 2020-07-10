import pygame
import time
from fixtures.constants import font_name, font_size
from fixtures.constants import green, dark_blue, black
from fixtures.dimens import item_display_offset
from graphics.views.View import View
from utils import keyboard_control


class BattleView(View):
    def __init__(self, controller, question_view=None):
        super().__init__()
        self.controller = controller
        self.question_view = question_view
        self.battle_init_actions = {
            pygame.K_y: self.display_battle,
            pygame.K_n: self.withdraw_from_battle,
        }

    def display(self):
        self.screen.display_surface.fill(black)
        self.render_line_center('Do you want to fight? (Y - yes, N - no)', 1)
        keyboard_control(self.battle_init_actions)

    def withdraw_from_battle(self):
        self.render_line_center("Go back when you're prepared", 2)
        time.sleep(1)

    def display_battle(self):
        self.render_line_center("Battle starts", 2)
        time.sleep(1)
        if self.question_view:
            self.question_view.display()
        end_messages = self.controller.battle_result()
        self.screen.display_surface.fill(black)
        for line, message in enumerate(end_messages, 1):
            self.render_line_center(message, line)
            time.sleep(1)
        time.sleep(1)

