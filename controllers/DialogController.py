from graphics.views.DialogView import DialogView
import random


class DialogController:
    def __init__(self, character, npc):
        self.character = character
        self.npc = npc
        self.npcLineId = -1
        self.playerLineId = 0
        self.npcLines = self.npc.dialog['npc_lines']
        self.playerLines = self.npc.dialog['player_lines']
        self.hasResponse = False
        self.dialog_view = DialogView(self)

    def start_dialog(self):
        self.dialog_view.display()
        return self.npc.attributes['finishedQuest']

    def getNpcStartLine(self):
        self.npcLineId = random.choice(self.npc.dialog['npc_starting_lines'])
        return self.npcLines[self.npcLineId]['text']

    def getNpcNextLine(self):
        if (self.npcLineId == -1):
            return self.getNpcStartLine()
        npcResponseIds = self.playerLines[self.playerLineId]['response']
        if not npcResponseIds:
            return None
        self.npcLineId = random.choice(npcResponseIds)
        return self.npcLines[self.npcLineId]['text']

    def getPlayerLines(self):
        playerResponseIds = self.npcLines[self.npcLineId]['responses']
        if not playerResponseIds:
            return None
        lines = list()
        for responseId in playerResponseIds:
            if (self.meetsResponseRequirements(responseId)):
                lines.append(self.playerLines[responseId]['text'])
        return lines

    def meetsResponseRequirements(self, responseId):
        if ('requirements' not in self.playerLines[responseId]):
            return True
        for key, value in self.playerLines[responseId]['requirements'].items():
            if (value != self.npc.attributes[key]):
                return False
        # if dialog option requires questItem check if player has it
        if ('questItem' not in self.playerLines[responseId]):
            return True
        for item in self.character._items:
            if (item.name == self.playerLines[responseId]['questItem']['name']):
                # and remove it from players inventory in the round :) 
                self.character.remove_item(item)
                return True
        return False

    def playerRespond(self, responseId):
        if (responseId < len(self.npcLines[self.npcLineId]['responses'])):
            self.playerLineId = self.npcLines[self.npcLineId]['responses'][responseId]
            self.hasResponse = True
            # performa asociated action
            if ('action' in self.playerLines[self.playerLineId]):
                for key, value in self.playerLines[self.playerLineId]['action'].items():
                    self.npc.attributes[key] = value
            return True
        else:
            return False

    def respond0(self):
        return self.playerRespond(0)

    def respond1(self):
        return self.playerRespond(1)

    def respond2(self):
        return self.playerRespond(2)

    def respond3(self):
        return self.playerRespond(3)

    def respond4(self):
        return self.playerRespond(4)

    def awaitResponse(self):
        self.hasResponse = False

    def receivedResponse(self):
        return self.hasResponse

    def dialog_result(self):
        return None
