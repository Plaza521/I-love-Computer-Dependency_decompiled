from DATA.Modules.ultilius.print_text import print_text
from DATA.Modules.draw import button
from DATA.Modules.variables import *
from PIL import ImageFont

import pygame
import numpy


class Screen(object):
    def __init__(self, world, blocks, player, settings):
        object.__init__(self)

        self.screen = pygame.display.set_mode((width, height))

        self.__game_over = False
        self.__version = "beta 0.1"
        self.__name = "I love Computer Dependency"  # I love Computer Dependency

        self.level = 0
        self.menu = "menu"

        self.world = world
        self.blocks = blocks
        self.player = player
        self.settings = settings

        pygame.display.set_caption(self.__name)
        pygame.display.set_icon(pygame.image.load("DATA/Sprites/icon.png"))

    def version(self):
        return self.__version

    """Рисование окна"""
    def draw(self):
        for sprite in block_group:
            pygame.draw.rect(self.screen, pygame.color.Color("white"), (sprite.x * cellsize, sprite.y * cellsize, cellsize, cellsize), 1)

        if self.menu == "menu":
            self.screen.blit(bg, (0, 0))

            button.play(screen=self.screen, width=width, height=height, function=lambda: self.menu_set("game"))
            button.exit(screen=self.screen, width=width, height=height, player=self.player)
            button.settings(screen=self.screen, width=width, height=height)

            ttf = ImageFont.truetype("DATA/arial.ttf", 50)

            print_text(self.screen, 10, 610, f'Версия: {self.__version}', 20)
            print_text(self.screen, width / 2 - ttf.getsize(self.__name)[0] / 2, 35, f'{self.__name}', 50, font_color=(255, 255, 255))

        elif self.menu == "game":
            self.screen.fill("#606060")

            for x in numpy.arange(cols):
                for y in numpy.arange(rows):
                    pygame.draw.rect(self.screen, (255, 255, 255), (x * cellsize, y * cellsize, cellsize, cellsize), 1)
                    if not self.world[x][y] in nons["print"]:
                        self.screen.blit(blocks[self.world[x][y]].get("image"), (x * cellsize, y * cellsize))

            self.screen.blit(self.player.image, (self.player.x, self.player.y))

        else:
            print("ERROR: Not found menu to draw.")

        pygame.display.update()

    def menu_set(self, type):
        self.menu = type
