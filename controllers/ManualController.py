from graphics.views.ManualView import ManualView


class ManualController:
    def __init__(self):
        self.manual_view = ManualView(self)

    def display_manual(self):
        self.manual_view.display()
