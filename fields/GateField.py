from fields.Field import Field


class GateField(Field):
    def __init__(self):
        self.key_id = None
        Field.__init__(self, (127, 0, 255), 'G', False)

    def set_key_id(self, key_id):
        self.key_id = key_id
