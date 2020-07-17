from graphics.views.ChestView import ChestView
from graphics.views.QuestionView import QuestionView
from utils import load_random_question


class ChestController:
    def __init__(self, chest):
        self.chest = chest
        self.chest_view = ChestView(self)
        self.opened = False
        self.code = []
        if self.chest.shortened:
            self.code_length = int(len(chest.code) / 2)
        else:
            self.code_length = len(chest.code)

    def start_chest_view(self):
        if not self.chest.already_interacted:
            question_view = QuestionView(load_random_question(), self)
            question_view.display()
        self.chest_view.display()
        return self.opened

    def pressed_key(self, code_character):
        self.code.append(code_character)

    def is_code_correct(self):
        if self.chest.code[len(self.code) - 1] == self.code[len(self.code) - 1]:
            if self.code_length == len(self.code):
                self.opened = True
            return True
        return False

    def code_ended(self):
        return self.code_length == len(self.code)

    def accept_answer(self):
        self.code_length = int(self.code_length / 2)
        self.chest.shortened = True

    def reject_answer(self):
        pass
