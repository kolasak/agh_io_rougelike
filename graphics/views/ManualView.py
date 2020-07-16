import pygame

from fixtures.constants import black
from graphics.Screen import Screen
from graphics.views.View import View
from utils import keyboard_control


class ManualView(View):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.manual_actions = {
            pygame.K_h: self.close_manual
        }

    def close_manual(self):
        pass

    def display(self):
        Screen.display_surface.fill(black)

        self.render_line_center('GAME CONTROLS INFO', 1)

        number_of_lines = 10
        line_height = Screen.screen_height // number_of_lines

        i = 1

        img = pygame.image.load("images/manual/keyboard_key_w.png")
        Screen.display_surface.blit(img, (Screen.screen_width // 8, i * line_height))

        img = pygame.image.load("images/manual/keyboard_key_a.png")
        Screen.display_surface.blit(img, (Screen.screen_width // 8 - 32, i * line_height + 32))

        img = pygame.image.load("images/manual/keyboard_key_s.png")
        Screen.display_surface.blit(img, (Screen.screen_width // 8, i * line_height + 32))

        img = pygame.image.load("images/manual/keyboard_key_d.png")
        Screen.display_surface.blit(img, (Screen.screen_width // 8 + 32, i * line_height + 32))

        Screen.render_text_values("Use wasd to move your character", Screen.screen_width + 150, 0, 0,
                                  i * Screen.screen_height * 2 // 10 + 48, background_color=black)

        images_paths = ["manual/keyboard_key_e.png", "items/sword.png", "items/key.png",
                        "items/hp_potion.png", "manual/keyboard_key_r.png",
                        "manual/keyboard_key_m.png", "manual/keyboard_key_h.png"]

        descriptions = ["Pick items from the map", "Some items can boost your strength",
                        "Some items can help you explore the map", "And some items can restore your HP",
                        "Interact with surroundings", "Use magic potions", "Open/Close Info"]

        for path, description in zip(images_paths, descriptions):
            i += 1
            img = pygame.image.load("images/" + path)
            if path.startswith("manual"):
                Screen.display_surface.blit(img, (Screen.screen_width // 8, i * line_height))
            else:
                Screen.display_surface.blit(img, (Screen.screen_width // 6, i * line_height))
            Screen.render_text_values(description, Screen.screen_width + 100, 0, 0,
                                      i * Screen.screen_height * 2 // 10 + 32, background_color=black)

        pygame.display.flip()

        keyboard_control(self.manual_actions)
