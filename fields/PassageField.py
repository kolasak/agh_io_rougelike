from fields.Field import Field
from graphics.Screen import Screen
from graphics.views.CharacterInfoView import CharacterInfoView


class PassageField(Field):
    def __init__(self):
        Field.__init__(self, (0, 255, 255), 'P', True)
        self.bound = False
        self.room = None
        self.next_x = None
        self.next_y = None

    def bind(self, room, coordinates):
        self.room = room
        self.next_x, self.next_y = coordinates

    def interact(self, character_info=None):
        print("Interact")
        if not character_info:
            print("No character info")
        else:
            character_info._x = self.next_x
            character_info._y = self.next_y
            screen = Screen(None, None)
            screen.fields = self.room
            character_info_view = CharacterInfoView(character_info)
            # screen.display_character_info(character_info_view)
            Screen.animate(character_info_view)
            Screen.display_map()
            Screen.instance.display_map()
            print("Done")