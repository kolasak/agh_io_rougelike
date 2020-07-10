from graphics.views.BattleView import BattleView
from graphics.views.QuestionView import QuestionView
from utils import load_random_question


class BattleController:
    def __init__(self, character, monster, has_question=False):
        self.character = character
        self.monster = monster
        self.boost = 0
        if has_question:
            self.question_view = QuestionView(load_random_question(), self)
            self.battle_view = BattleView(self, self.question_view)
        else:
            self.battle_view = BattleView(self)

    def start_battle(self):
        self.battle_view.display()
        return self.character

    def battle_result(self):
        self.character._hp -= 1
        self.character._exp += 5
        return ['You win!', 'You lost 1 hp and gained 5 exp.']

    def accept_answer(self):
        self.boost = 3

    def reject_answer(self):
        self.boost = 0
