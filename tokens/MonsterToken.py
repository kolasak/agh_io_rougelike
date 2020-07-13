from tokens.Token import Token
from controllers.BattleController import BattleController


class MonsterToken(Token):
    def __init__(self, hp, strength, image, xp):
        self._hp = hp
        self._strength = strength
        self._image = image
        self._xp = xp

    @property
    def image(self):
        return self._image

#TODO: set rewards

    def interact(self, character_info=None):
        controller = BattleController(character_info, None)
        return controller.start_battle()
