from fields.Field import Field


class EndStageField(Field):
    def __init__(self):
        Field.__init__(self, (255, 0, 127), 'E', True)