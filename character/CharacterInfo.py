# Define character's fields (hp, strength, ...). Create character class. Display fields values in GUI.

class CharacterInfo():
    def __init__(self, hp, exp, strength, items):
        self._hp = hp
        self._exp = exp
        self._strength = strength
        self._items = items

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

# todo: add and remove specific item from items
