import pygame

from fixtures.dimens import initial_item_display_y_coord, initial_item_display_x_coord


class Item:
    def __init__(self, img_name):
        self.x = initial_item_display_x_coord
        self.y = initial_item_display_y_coord
        self.img_name = img_name

    def get_img_name(self):
        return self.img_name

    def display(self, game_display_surface, offset):
        img = pygame.image.load('images/items/' + self.img_name)
        game_display_surface.blit(img, (self.x + offset, self.y))
