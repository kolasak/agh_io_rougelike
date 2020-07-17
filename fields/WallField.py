from fields.Field import Field


class WallField(Field):
    def __init__(self):
        Field.__init__(self, (0, 0, 0), 'V', False)