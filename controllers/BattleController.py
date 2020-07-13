from graphics.views.BattleView import BattleView
from graphics.views.QuestionView import QuestionView
from utils import load_random_question


class BattleController:
    def __init__(self, character, monster, has_question=False):
        self.character = character
        self.monster = monster
        self.won = False
        self.hp_lost = 0
        self.boost = 0
        if has_question:
            self.question_view = QuestionView(load_random_question(), self)
            self.battle_view = BattleView(self, self.question_view)
        else:
            self.battle_view = BattleView(self)

    def start_battle_view(self):
        self.battle_view.display()
        return self.won

    def start_battle(self):
        while self.character.hp > 0 and self.monster.hp > 0:
            self.battle_player_strike()
            if self.monster.hp > 0:
                self.battle_monster_strike()

    def battle_won_result(self):
        self.won = True
        self.character.exp += self.monster.xp
        return ['You win!', f'You lost {self.hp_lost} hp and gained {self.monster.xp} xp.']

    def battle_lost_result(self):
        self.won = False
        # self.character._exp += self.monster.xp
        return ['You lost!']

    def battle_player_strike(self):
        strike_amount = self.character.strength + self.boost
        self.monster.hp -= strike_amount
        self.battle_view.display_round(f'You hit monster with {strike_amount} damage.')
        if self.monster.hp <= 0:
            self.battle_view.invoke_battle_won()

    def battle_monster_strike(self):
        strike_amount = self.monster.strength
        self.character.hp -= strike_amount
        self.hp_lost += strike_amount
        self.battle_view.display_round(f'Monster hit you with {strike_amount} damage.')
        if self.character.hp <= 0:
            self.battle_view.invoke_battle_lost()

    def accept_answer(self):
        self.boost = 3

    def reject_answer(self):
        self.boost = 0
