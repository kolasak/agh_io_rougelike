from abc import abstractmethod


class Token:
    @abstractmethod
    def interact(self):
        pass
