from fixtures.constants import black
from graphics.Screen import Screen
from graphics.views.View import View
from utils import keyboard_control
from pygame import K_a, K_d
import time


class ChestView(View):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.line_no = 1

    def display(self):
        Screen.display_surface.fill(black)
        self.render_line_center('Use \'A\' and \'D\' to break the code', self.line_no)
        self.line_no += 1
        while True:
            keyboard_control({K_a: lambda: self.controller.pressed_key('a'),
                              K_d: lambda: self.controller.pressed_key('d')})
            if self.controller.is_code_correct():
                self.render_line_center('CORRECT', self.line_no)
                self.line_no += 1
                if self.controller.code_ended():
                    self.render_line_center('You opened the chest', self.line_no)
                    time.sleep(1)
                    self.line_no += 1
                    break
            else:
                self.render_line_center('WRONG', self.line_no)
                self.line_no += 1
                self.render_line_center('Try again', self.line_no)
                time.sleep(1)
                self.line_no += 1
                break
