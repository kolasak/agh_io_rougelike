from fields.Field import Field


class PassageField(Field):
    def __init__(self):
        Field.__init__(self, (0, 255, 255), 'P', True)