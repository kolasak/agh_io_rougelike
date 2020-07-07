from fields.Field import Field


class RoadField(Field):
    def __init__(self):
        Field.__init__(self, (153, 76, 0), 'R', True)