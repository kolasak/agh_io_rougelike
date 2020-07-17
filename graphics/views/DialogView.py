import pygame
import time
from fixtures.constants import font_name, font_size
from fixtures.constants import green, dark_blue, black
from fixtures.dimens import item_display_offset
from graphics.views.View import View
from utils import keyboard_control
from graphics.Screen import Screen
from graphics.TextUtil import TextUtil
import fixtures.constants as fc


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
        self.text_util = TextUtil(0, 100)

    def display(self):
        self.display_dialog()

    def display_dialog(self):
        while(True):
            self.clearDialogView()
            if (not self.displayNpcLine()):
                break
            if (not self.displayPlayerLines()):
                break
            self.pollPlayersResponse()
            time.sleep(0.3)
        pygame.event.wait()
        # pygame.event.wait()

    def clearDialogView(self):
        self.text_util.clear()

    def displayPlayerLines(self):
        playerLines = self.controller.getPlayerLines()
        if not playerLines:
            return False
        for lineId, line in enumerate(playerLines):
            self.text_util.print_multiline(str(lineId+1) + '. ' + line)
        return True

    def displayNpcLine(self):
        npcLine = self.controller.getNpcNextLine()
        if not npcLine:
            return False
        npcLine = self.controller.npc.name + ': ' + npcLine
        self.text_util.print_multiline(npcLine, font_color=fc.white)
        return True

    def pollPlayersResponse(self):
        self.controller.awaitResponse()
        while (not self.controller.receivedResponse()):
            keyboard_control(self.response_actions)