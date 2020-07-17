import pygame

from fixtures.constants import black
from graphics.Screen import Screen
from graphics.views.View import View
from utils import keyboard_control


class IntroView(View):
    def __init__(self):
        super().__init__()
        self.intro_actions = {
            pygame.K_SPACE: self.close_intro
        }

    def close_intro(self):
        pass

    def display(self):
        import time

        Screen.display_surface.fill(black)

        img = pygame.image.load("images/items/character.png")
        Screen.display_surface.blit(img, (Screen.screen_width // 2 - 16, 10))

        story = [
            "Hello",
            "I am Computer Science student",
            "I need to go through all this university mazes",
            "And find the room of my final exam",
            "But it can be dangerous...",
            "And it will take a lot of wisdom to accomplish",
            "Please join me!",
            "Maybe someone or something there could help us",
            "But be careful of the scary monster",
            "Let's go!",
            "Use 'h' button for help during game"
            "(PRESS SPACE TO START)"
        ]

        for i in range(len(story)):
            self.render_line_center(story[i], i+3)
            time.sleep(1)

        keyboard_control(self.intro_actions)
