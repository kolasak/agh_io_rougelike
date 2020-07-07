from fields.Field import Field


class MountainField(Field):
    def __init__(self):
        Field.__init__(self, (96, 96, 96), 'M', True)