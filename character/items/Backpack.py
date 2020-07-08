from character.items.Item import Item


class Backpack(Item):
    def __init__(self):
        img_name = 'backpack.png'
        super(Backpack, self).__init__(img_name)
