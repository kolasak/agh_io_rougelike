from abc import abstractmethod


class Token:
    @abstractmethod
    def interact(self, character_info=None):
        pass
