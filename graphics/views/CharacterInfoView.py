import pygame

from enums.Direction import Direction
from fixtures.dimens import item_display_offset
from graphics.settings import CHARACTER_IMAGE_PATH
from graphics.views.ItemView import ItemView
from graphics.views.View import View
from graphics.Screen import Screen


class CharacterInfoView(View):
    def __init__(self, character_info):
        super().__init__()
        self.character_info = character_info
        self.general_text_info = 'HP: ' + str(self.character_info.hp) + ', EXP: ' + str(
            self.character_info.exp) + ', STRENGTH: ' + str(self.character_info.strength)
        self.items_text_info = 'ITEMS: '
        self.character_img = pygame.image.load(CHARACTER_IMAGE_PATH)

    @property
    def get_general_text_info(self):
        return 'HP: ' + str(self.character_info.hp) + ', EXP: ' + str(
            self.character_info.exp) + ', STRENGTH: ' + str(self.character_info.strength)


    def display(self):
        self.__display_general_character_info()
        self.__display_items_info()
        self.__display_character()

        pygame.display.update()

    def __display_general_character_info(self):
        Screen.render_text_values(self.get_general_text_info, 320, 0, 50, 0)

    def __display_items_info(self):
        Screen.render_text_values(self.items_text_info, 320, 220, 50, 70)

        for i, item in enumerate(self.character_info.items):
            item_view = ItemView(item.img_path)
            item_view.display(self.screen.display_surface, i * item_display_offset)

    def __display_character(self):
        Screen.render_character(self.character_info.x, self.character_info.y, self.character_info.x, self.character_info.y, self.character_img, Direction.SOUTH)
