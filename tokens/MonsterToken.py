from tokens.Token import Token
from controllers.BattleController import BattleController


class MonsterToken(Token):
    def __init__(self):
        # set atributes
        pass

    def interact(self, character_info=None):
        controller = BattleController(character_info, None)
        return controller.start_battle()
