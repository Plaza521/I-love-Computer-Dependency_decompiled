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
world, x, y = game.Level.load(
    level=settings['level'],
    block_group=block_group
)
player = Player(x=x, y=y)
screen = Screen(world=world, blocks=blocks, player=player, settings=settings)
play = True
while play:
    fps_count += 1
    screen.draw()
    if screen.menu == 'game':
        player.animation(fps=fps_count)
        player.fall(player=player, block_group=block_group)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.run(player=player, block_group=block_group, route='right')
    if keys[pygame.K_a]:
        player.run(player=player, block_group=block_group, route='left')
    if keys[pygame.K_SPACE]:
        player.jump_start(player=player, block_group=block_group)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f'''мин. - {round(fps.min())}
макс. - {round(fps.max())}
ср. - {round(fps.sum() / len(fps))}''')
            game.exit(player=screen.settings)
        if round(clock.get_fps()) != 0:
            fps = numpy.append(fps, round(clock.get_fps()))
    clock.tick(FPS)
