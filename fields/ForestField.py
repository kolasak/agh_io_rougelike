from fields.Field import Field


class ForestField(Field):
    def __init__(self):
        Field.__init__(self, (0, 153, 0), 'F', True)
