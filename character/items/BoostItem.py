from character.items.Item import Item


class BoostItem(Item):
    def __init__(self, name, strength, img_path):
        self.strength = strength
        super().__init__(name, img_path)
