import pygame
from graphics.settings import *


class Screen:
    def __init__(self, fields):
        pygame.init()
        width, height = fields.shape
        self.screen = pygame.display.set_mode((width*PIXEL_SIZE, height*PIXEL_SIZE))
        for x in range(width):
            for y in range(height):
                pygame.draw.rect(self.screen, fields[x][y].colour,
                                 (x*PIXEL_SIZE, y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
        pygame.display.flip()
        self.exit_pressed = False

    def animate(self):
        while not self.exit_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_pressed = True
        pygame.quit()

