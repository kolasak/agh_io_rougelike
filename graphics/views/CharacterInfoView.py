import pygame

from fixtures.constants import font_name, font_size
from fixtures.constants import green, dark_blue
from fixtures.dimens import item_display_offset
from graphics.views.View import View


class CharacterInfoView(View):
    def __init__(self, character_info):
        super().__init__()
        self.character_info = character_info
        self.general_text_info = 'HP: ' + str(self.character_info.hp) + ', EXP: ' + str(
            self.character_info.exp) + ', STRENGTH: ' + str(self.character_info.strength)
        self.items_text_info = 'ITEMS: '

    def display(self):
        self.__display_general_character_info()
        self.__display_items_info()

        pygame.display.update()

    def __display_general_character_info(self):
        self.__render_text_values(self.general_text_info, 0, 0)

    def __render_text_values(self, text_value, x_offset, y_offset):
        font = pygame.font.Font(font_name, font_size)
        text = font.render(text_value, True, green, dark_blue)

        text_rect = self.get_positioned_text(text, x_offset, y_offset)

        self.screen.display_surface.blit(text, text_rect)

    def get_positioned_text(self, text, x_offset, y_offset):
        X, Y = self.calculate_text_coordinates_with_offset(x_offset, y_offset)

        text_rect = text.get_rect()
        text_rect.center = (X // 2, Y // 2)

        return text_rect

    def calculate_text_coordinates_with_offset(self, x_offset, y_offset):
        return 320 - x_offset, 50 + y_offset

    def __display_items_info(self):
        self.__render_text_values(self.items_text_info, 220, 70)

        for i, item in enumerate(self.character_info.items):
            item.display(self.screen.display_surface, i * item_display_offset)
