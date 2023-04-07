# Source Generated with Decompyle++
# File: Editor.pyc (Python 3.8)

from DATA.Modules.ultilius.print_text import print_text
from DATA.Modules.base import file as game
from DATA.Modules.variables import *
from PIL import ImageFont
import pygame
import numpy
import json
import os

def Name():
    '''Name'''
    
    def __init__(self, x, y, name, group):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.name = name
        self.add(group)

    
    def update(self):
        self.y -= 1.5
        if self.y < -40:
            self.kill()

    
    def draw(self):
        print_text(screen, self.x, self.y, self.name, 40, (0, 0, 255), **('font_color',))


Name = <NODE:27>(Name, 'Name', pygame.sprite.Sprite)
level = input('\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5 \xd1\x83\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c: ')
names_group = pygame.sprite.Group()
ttf = ImageFont.truetype('DATA/Arial.ttf', 40)
world = []
for x in numpy.arange(cols):
    l = []
    for y in numpy.arange(rows):
        l.append(0)
    world.append(l)

def draw(screen, world, square_x, square_y, plus):
    screen.fill((0, 0, 0))
    for x in numpy.arange(cols):
        for y in numpy.arange(rows):
            pygame.draw.rect(screen, (255, 255, 255), (x * cellsize, y * cellsize, cellsize, cellsize), 1)
            
            try:
                screen.blit(blocks[world[x][y]].get('image'), (x * cellsize, y * cellsize))
            finally:
                continue
                except IndexError:
                    world = []
                    for x in numpy.arange(cols):
                        l = []
                        for y in numpy.arange(rows):
                            l.append(0)
                        world.append(l)
                    continue
                    continue
                
                continue
                screen.blit(blocks[plus].get('image'), (square_x * cellsize, square_y * cellsize))
                for name in names_group:
                    name.update()
                    name.draw()
                pygame.display.update()
                return None


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('\xd0\xa0\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xbe\xd1\x80 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82')
clock = pygame.time.Clock()
player = game.start()
plus = 1
rotation = 1
copy = -1
now = 0
square_x = -1
square_y = -1
print(f'''\xd0\xa1\xd0\x9a\xd0\x9c = {plus}''')
play = True
# WARNING: Decompyle incomplete
