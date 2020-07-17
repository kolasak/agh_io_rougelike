from graphics.Screen import Screen
from graphics.ScreenUtil import ScreenUtil
import fixtures.constants as fc
import pygame
from itertools import chain


class TextUtil:
    def __init__(self, left_top, right_bottom, left_margin=50, font_name=fc.font_name, font_size=fc.font_size):
        self.left_top = left_top
        self.right_bottom = right_bottom
        self.left_margin = left_margin
        self.font = pygame.font.Font(font_name, font_size)
        self.current_line = 5

    def print_multiline(self, text, font_color=fc.green, background_color=fc.black):
        for line in self.wrapline(text, Screen.screen_width - 100):
            self.print_line(line, font_color=font_color, background_color=background_color)
            print(line)

    def print_line(self, text, font_color=fc.green, background_color=fc.black):
        text_render = self.font.render(
            text, True, font_color, background_color)
        text_rect = text_render.get_rect()
        text_rect.topleft = (50, self.current_line * 25)
        Screen.display_surface.blit(text_render, text_rect)
        pygame.display.flip()
        self.current_line = self.current_line + 1

    def rewind(self):
        self.current_line = 5

    def clear(self, background_color=fc.black):
        Screen.display_surface.fill(background_color)
        self.rewind()


# https://www.pygame.org/wiki/TextWrapping?parent=CookBook

    def truncline(self, text, maxwidth):
        real = len(text)
        stext = text
        l = self.font.size(text)[0]
        cut = 0
        a = 0
        done = 1
        old = None
        while l > maxwidth:
            a = a+1
            n = text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext = n[:-cut]
            else:
                stext = n
            l = self.font.size(stext)[0]
            real = len(stext)
            done = 0
        return real, done, stext

    def wrapline(self, text, maxwidth):
        done = 0
        wrapped = []

        while not done:
            nl, done, stext = self.truncline(text, maxwidth)
            wrapped.append(stext.strip())
            text = text[nl:]
        return wrapped

    def wrap_multi_line(self, text, font, maxwidth):
        """ returns text taking new lines into account.
        """
        lines = chain(*(self.wrapline(line, maxwidth)
                        for line in text.splitlines()))
        return list(lines)
