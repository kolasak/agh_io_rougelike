class CharacterInfo():
    def __init__(self, hp, exp, strength):
        self._hp = hp
        self._exp = exp
        self._strength = strength
        self._items = []

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

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)
