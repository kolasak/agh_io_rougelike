from tokens.Token import Token


class MonsterToken(Token):
    def __init__(self, hp, strength, image):
        self._hp = hp
        self._strength = strength
        self._image = image

    @property
    def image(self):
        return self._image

#TODO: set rewards

    def interact(self):
        # fight
        pass
