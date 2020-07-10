class Field:
    def __init__(self, colour, character, passable):
        self.colour = colour
        self.token = None
        self.passable = passable
        self.character = character

    def interact(self, character_info=None):
        if self.token is not None:
            self.token.interact(character_info)

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character
