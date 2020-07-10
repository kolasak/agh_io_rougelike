import pygame

from fixtures.dimens import initial_item_display_y_coord, initial_item_display_x_coord


class ItemView:
    def __init__(self, img_path):
        self.x = initial_item_display_x_coord
        self.y = initial_item_display_y_coord
        self.img_path = img_path

    def get_img_name(self):
        return self.img_path

    def display(self, game_display_surface, offset):
        img = pygame.image.load(self.img_path)
        game_display_surface.blit(img, (self.x + offset, self.y))
