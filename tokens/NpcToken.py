from tokens.Token import Token
from controllers.DialogController import DialogController

class NpcToken(Token):
    def __init__(self, name, image, attributes, dialog):
        self._name = name
        self._image = image
        self._attributes = attributes
        self._dialog = dialog

    @property
    def image(self):
        return self._image

    def interact(self, character_info=None):
        controller = DialogController(character_info, self)
        return controller.start_dialog()

    def name(self):
        return self._name

    def attributes(self):
        return self._attributes
    
    def dialog(self):
        return self._dialog

