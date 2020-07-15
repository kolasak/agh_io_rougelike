from graphics.Screen import Screen


class ScreenInstance(object):
    instance = None
    game_map = None

    def __new__(cls, fields, game_map):
        if not ScreenInstance.instance:
            ScreenInstance.instance = Screen(fields)
            ScreenInstance.game_map = game_map
        return ScreenInstance.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

