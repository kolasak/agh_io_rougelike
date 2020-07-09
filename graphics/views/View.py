from abc import ABC

from graphics.Screen import Screen


class View(ABC):
    def __init__(self):
        self.screen = Screen(None)

    def display(self):
        pass
