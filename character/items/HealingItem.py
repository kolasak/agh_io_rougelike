from character.items.Item import Item


class HealingItem(Item):
    def __init__(self, name, healing, img_path):
        self.healing = healing
        super().__init__(name, img_path)
