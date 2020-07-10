from character.items.Item import Item
import random
import string


class Key(Item):
    def __init__(self):
        self.id = ''.join(random.choice(string.ascii_letters) for i in range(10))
        super().__init__('Key', 'images/items/key.png')
