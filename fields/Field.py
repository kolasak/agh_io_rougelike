class Field:
    def __init__(self, colour, character, passable):
        self.colour = colour
        self.token = None
        self.item = None
        self.passable = passable
        self.character = character

    def interact(self, character_info=None):
        if self.token is not None:
            self.token.interact(character_info)

    def put_item(self, item):
        self.item = item

    def get_item(self):
        picked_item = self.item
        self.item = None
        return picked_item

    def put_token(self, token):
        self.token = token

    def get_token(self):
        picked_token = self.token
        self.token = None
        return picked_token

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character
