from fixtures.constants import black
from graphics.views.View import View
from utils import keyboard_control

import time
class QuestionView(View):
    def __init__(self, question, controller):
        """correct answer has to be pygame keyboard constant"""
        super().__init__()
        self.question_text = question.question_text
        self.answers = question.answers
        self.controller = controller
        self.line = 1
        self.question_actions = {a: self.success if a == question.correct_answer else self.failure for a in
                                 self.answers.keys()}

    def display(self):
        self.screen.display_surface.fill(black)
        self.render_line_center("If you answer this question correctly you will get boost.", self.line)
        self.line += 1
        self.render_line_center(self.question_text, self.line)
        self.line += 1
        for answer_text in self.answers.values():
            self.render_line_center(answer_text, self.line)
            self.line += 1
        keyboard_control(self.question_actions)
        time.sleep(2)

    def success(self):
        self.controller.accept_answer()
        self.render_line_center("Correct answer. Attack increased.", self.line)

    def failure(self):
        self.controller.reject_answer()
        self.render_line_center("Wrong answer.", self.line)
