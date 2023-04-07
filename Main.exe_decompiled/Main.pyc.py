# Source Generated with Decompyle++
# File: Main.pyc (Python 3.8)

from DATA.Modules.Player.player import Player
from DATA.Modules.base.screen import Screen
from DATA.Modules.base import file as game
from DATA.Modules.variables import *
import pygame
import numpy
pygame.init()
settings = game.start()
clock = pygame.time.Clock()
(world, x, y) = game.Level.load(settings['level'], block_group, **('level', 'block_group'))
player = Player(x, y, **('x', 'y'))
screen = Screen(world, blocks, player, settings, **('world', 'blocks', 'player', 'settings'))
play = True
if play:
    fps_count += 1
    screen.draw()
    if screen.menu == 'game':
        player.animation(fps_count, **('fps',))
        player.fall(player, block_group, **('player', 'block_group'))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.run(player, block_group, 'right', **('player', 'block_group', 'route'))
    if keys[pygame.K_a]:
        player.run(player, block_group, 'left', **('player', 'block_group', 'route'))
    if keys[pygame.K_SPACE]:
        player.jump_start(player, block_group, **('player', 'block_group'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f'''\xd0\xbc\xd0\xb8\xd0\xbd. - {round(fps.min())}\n\xd0\xbc\xd0\xb0\xd0\xba\xd1\x81. - {round(fps.max())}\n\xd1\x81\xd1\x80. - {round(fps.sum() / len(fps))}''')
            game.exit(screen.settings, **('player',))
            continue
            if round(clock.get_fps()) != 0:
                fps = numpy.append(fps, round(clock.get_fps()))
    clock.tick(FPS)
    continue
