from tokens.Token import Token
from controllers.DialogController import DialogController

class NpcToken(Token):
    def __init__(self, name, image, attributes, quest, quest_item, dialog):
        self.name = name
        self._image = image
        self.attributes = attributes
        self.quest = quest
        self.item = quest_item
        self.dialog = dialog

    @property
    def image(self):
        return self._image

    def interact(self, character_info=None):
        controller = DialogController(character_info, self)
        return controller.start_dialog()
