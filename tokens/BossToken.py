from tokens.MonsterToken import MonsterToken


class BosToken(MonsterToken):
    def __init__(self):
        MonsterToken.__init__(self)
        # additional properties


    def interact(self):
        # additional rules
        MonsterToken.interact(self)