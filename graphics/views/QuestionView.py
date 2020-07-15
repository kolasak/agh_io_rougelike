import pygame
from numpy.core.defchararray import isnumeric

from fixtures.constants import black
from graphics.views.View import View

import time

class QuestionView(View):
    def __init__(self, question, controller):
        """correct answer has to be pygame keyboard constant"""
        super().__init__()
        self.question = question
        self.question_text = question.question_text
        self.answers = question.answers
        self.controller = controller
        self.line = 1

    def display(self):
        self.screen.display_surface.fill(black)
        self.render_line_center(self.question_text, self.line)
        self.line += 1
        for answer_text in self.answers:
            self.render_line_center(answer_text, self.line)
            self.line += 1
        self.answer_question(self.get_answer_key())
        time.sleep(2)

    def get_answer_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if isnumeric(pygame.key.name(event.key)) and int(pygame.key.name(event.key)) in range(1, len(self.answers)+1):
                        return pygame.key.name(event.key)

    def answer_question(self, answer):
        if answer is None:
            pass
        elif self.question.answers[int(answer) - 1] == self.question.correct_answer:
            self.success()
        elif self.question.answers[int(answer) - 1] in self.question.answers:
            self.failure()

    def success(self):
        self.controller.accept_answer()
        self.render_line_center("Correct answer.", self.line)
        self.screen.display_surface.fill(black)

    def failure(self):
        self.controller.reject_answer()
        self.render_line_center("Wrong answer.", self.line)
        self.screen.display_surface.fill(black)
