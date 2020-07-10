from character.items.Item import Item


class Laptop(Item):
    def __init__(self):
        self.img_name = 'laptop.png'
        super(Laptop, self).__init__(self.img_name)
