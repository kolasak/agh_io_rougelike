from character.items.BoostItem import BoostItem
from character.items.Key import Key
from fixtures.constants import max_items_count, hp_potion_item_name, max_hp


class CharacterInfo:
    def __init__(self, hp, exp, strength, x, y, direction):
        self._hp = hp
        self._exp = exp
        self._strength = strength
        self._items = []
        self._x = x
        self._y = y
        self._direction = direction

    @property
    def hp(self):
        return self._hp

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def exp(self):
        return self._exp

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

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
        if len(self._items) < max_items_count:
            self._items.append(item)
            if isinstance(item, BoostItem):
                self.strength += item.strength
            return True
        return False

    def remove_item(self, item):
        self._items.remove(item)
        if isinstance(item, BoostItem):
            self.strength -= item.strength

    def remove_key(self, key_id):
        for item in self._items:
            if isinstance(item, Key) and item.id == key_id:
                self.remove_item(item)

    def find_healing_item(self):
        for item in self._items:
            if item.name == hp_potion_item_name:
                return item

    def heal_with_item(self, item):
        result_hp = self._hp + item.healing
        if result_hp > max_hp:
            return False
        self._hp = result_hp
        self.remove_item(item)
        return True
