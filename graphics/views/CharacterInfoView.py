import pygame
from graphics.views.ItemView import ItemView

from fixtures.dimens import item_display_offset
from graphics.views.View import View


class CharacterInfoView(View):
    def __init__(self, character_info):
        super().__init__()
        self.character_info = character_info
        self.general_text_info = 'HP: ' + str(self.character_info.hp) + ', EXP: ' + str(
            self.character_info.exp) + ', STRENGTH: ' + str(self.character_info.strength)
        self.items_text_info = 'ITEMS: '

    def display(self, screen):
        self.__display_general_character_info(screen)
        self.__display_items_info(screen)

        pygame.display.update()

    def __display_general_character_info(self, screen):
        screen.render_text_values(self.general_text_info, 320, 0, 50, 0)

    def __display_items_info(self, screen):
        screen.render_text_values(self.items_text_info, 320, 220, 50, 70)

        for i, item in enumerate(self.character_info.items):
            item_view = ItemView(item.img_path)
            item_view.display(screen.display_surface, i * item_display_offset)
