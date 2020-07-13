from tokens.Token import Token
from controllers.BattleController import BattleController


class MonsterToken(Token):
    def __init__(self, hp, strength, image, xp):
        self._hp = hp
        self._strength = strength
        self._image = image
        self._xp = xp
        self._item = None

    @property
    def image(self):
        return self._image

    @property
    def strength(self):
        return self._strength

    @property
    def xp(self):
        return self._xp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @strength.setter
    def strength(self, value):
        self._hp = value

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

#TODO: set rewards

    def interact(self, character_info=None):
        controller = BattleController(character_info, self, None)
        return controller.start_battle_view()
