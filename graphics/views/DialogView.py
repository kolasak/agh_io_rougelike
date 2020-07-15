import pygame
import time
from fixtures.constants import font_name, font_size
from fixtures.constants import green, dark_blue, black
from fixtures.dimens import item_display_offset
from graphics.views.View import View
from utils import keyboard_control
from graphics.Screen import Screen


class DialogView(View):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.response_actions = {
            pygame.K_1: self.controller.respond0,
            pygame.K_2: self.controller.respond1,
            pygame.K_3: self.controller.respond2,
            pygame.K_4: self.controller.respond3,
            pygame.K_5: self.controller.respond4,
        }

    def display(self):
        Screen.display_surface.fill(black)
        self.display_dialog()

    def display_dialog(self):
        self.render_line_center(self.controller.npc.name(), 2)
        time.sleep(1)
        self.render_line_center(self.controller.getNpcStartLine(), 4)


        while(True):
            playerLines = self.controller.getPlayerLines()
            if not playerLines:
                break
            for lineId, line in enumerate(playerLines):
                self.render_line_center(str(lineId+1) + ". " + line, 6 + 2*lineId)
            
            self.controller.awaitResponse()
            while (not self.controller.receivedResponse()):
                keyboard_control(self.response_actions)

            Screen.display_surface.fill(black)
            self.render_line_center(self.controller.npc.name(), 2)

            npcLine = self.controller.getNpcNextLine()
            if not npcLine:
                break
            self.render_line_center(npcLine, 4)
        
        time.sleep(1)