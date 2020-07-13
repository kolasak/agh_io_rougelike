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

    def start_battle_view(self):
        self.battle_view.display()
        return self.character

    def start_battle(self):
        while self.character.hp > 0 and self.monster.hp > 0:
            self.battle_player_strike()
            if self.monster.hp > 0:
                self.battle_monster_strike()

    def battle_won_result(self):
        self.character._exp += self.monster.xp
        return ['You win!', 'You lost 1 hp and gained 5 exp.']

    def battle_lost_result(self):
        # self.character._exp += self.monster.xp
        return ['You lost!']

    def accept_answer(self):
        self.boost = 3

    def battle_player_strike(self):
        self.monster.hp -= self.character.strength
        if self.monster.hp <= 0:
            self.battle_view.invoke_battle_won()

    def battle_monster_strike(self):
        self.character.hp -= self.monster.strength
        if self.character.hp <= 0:
            self.battle_view.invoke_battle_lost()

    def reject_answer(self):
        self.boost = 0
