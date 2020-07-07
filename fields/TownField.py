from fields.Field import Field


class TownField(Field):
    def __init__(self):
        Field.__init__(self, (255, 128, 0), 'T', True)