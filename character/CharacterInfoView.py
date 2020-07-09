import pygame

from fixtures.constants import font_name, font_size
from fixtures.constants import green, dark_blue
from fixtures.dimens import character_info_display_width, item_display_offset


class CharacterInfoView():
    def __init__(self, character_info):
        self.character_info = character_info
        self.game_display_surface = None

        self.display_character_info()

    def display_character_info(self):
        self.init_display_screen()

        self.display_general_character_info()
        self.display_items_info()

        self.listen_for_quit()

    def init_display_screen(self):
        pygame.init()
        pygame.display.set_caption("Character's info")

        self.game_display_surface = pygame.display.set_mode(
            (character_info_display_width, character_info_display_width))
        self.game_display_surface.fill(dark_blue)

    def display_general_character_info(self):
        text_values = 'HP: ' + str(self.character_info.hp) + ', EXP: ' + str(
            self.character_info.exp) + ', STRENGTH: ' + str(self.character_info.strength)
        self.render_text_values(text_values, 0, 0)

    def render_text_values(self, text_value, x_offset, y_offset):
        font = pygame.font.Font(font_name, font_size)
        X = 320 - x_offset
        Y = 50 + y_offset

        text = font.render(text_value, True, green, dark_blue)
        text_rect = text.get_rect()
        text_rect.center = (X // 2, Y // 2)

        self.game_display_surface.blit(text, text_rect)

    def display_items_info(self):
        text_values = 'ITEMS: '
        self.render_text_values(text_values, 220, 70)

        for i, item in enumerate(self.character_info.items):
            item.display(self.game_display_surface, i * item_display_offset)

    def listen_for_quit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
