from graphics.Screen import Screen


class ScreenInstance(object):
    instance = None

    def __new__(cls, fields):
        if not ScreenInstance.instance:
            ScreenInstance.instance = Screen(fields)
        return ScreenInstance.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

