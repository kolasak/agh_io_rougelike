from character.items.Item import Item


class Sword(Item):
    def __init__(self):
        img_name = 'sword.png'
        super(Sword, self).__init__(img_name)
