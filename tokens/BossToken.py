from tokens.MonsterToken import MonsterToken
from controllers.BattleController import BattleController


class BossToken(MonsterToken):
    def __init__(self):
        MonsterToken.__init__(self)
        # additional properties

    def interact(self, character_info=None):
        controller = BattleController(character_info, self, True)
        return controller.start_battle_view()
