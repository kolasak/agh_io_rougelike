from fields.Field import Field
from graphics.views.View import View


class EndStageField(Field):
    def __init__(self):
        Field.__init__(self, (255, 0, 127), 'E', True)

    def interact(self, character_info=None):
        View().display_game_ending(character_info.exp, True)
