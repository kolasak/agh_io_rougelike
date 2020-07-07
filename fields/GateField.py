from fields.Field import Field


class GateField(Field):
    def __init__(self):
        Field.__init__(self, (127, 0, 255), 'G', False)