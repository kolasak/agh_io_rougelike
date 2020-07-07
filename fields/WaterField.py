from fields.Field import Field


class WaterField(Field):
    def __init__(self):
        Field.__init__(self, (0, 128, 255), 'W', True)