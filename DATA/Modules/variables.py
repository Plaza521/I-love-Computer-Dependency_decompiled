import pygame
import numpy


class Group(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.rect = pygame.Rect(x * cellsize, y * cellsize, cellsize, cellsize)


fps = numpy.array([])
fps_count = 0
fps_count_max = 60

width = 840
height = 640
FPS = 120

cellsize = 40

cols = width // cellsize
rows = height // cellsize

bg = pygame.image.load("DATA/Sprites/bg.png")

blocks = [
    {"image": pygame.image.load("DATA/Sprites/blocks/air.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-right.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-down.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-left.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-right-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-right-down.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-left-down.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-left-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-right-up-full.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-right-down-full.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-left-down-full.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-left-up-full.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-up-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-right-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-down-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-left-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-sides-right.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-sides-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-popfull-right-left-up.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-popfull-up-down-right.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-popfull-right-left-down.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-popfull-up-down-left.png")},
    {"image": pygame.image.load("DATA/Sprites/blocks/brick-wall-full.png")},
    {"image": pygame.image.load("DATA/Sprites/place/start.png")},
    {"image": pygame.image.load("DATA/Sprites/place/finish.png")}
]

editor = [
    [0, 24],
    [25, 26]
]

nons = {
    "block": (
        0,
        25,
        26
    ),

    "print": (
        25,
        26
    )
}

player_images = {
    "idle": [pygame.transform.scale(pygame.image.load("DATA/Sprites/player/player_idle.png"), (40, 55))],
    "run": [
        pygame.transform.scale(pygame.image.load("DATA/Sprites/player/player_run_1.png"), (40, 55)),
        pygame.transform.scale(pygame.image.load("DATA/Sprites/player/player_run_2.png"), (40, 55))
    ],
    "fall": [pygame.transform.scale(pygame.image.load("DATA/Sprites/player/player_fall.png"), (40, 55))],
    "jump": [pygame.transform.scale(pygame.image.load("DATA/Sprites/player/player_jump.png"), (40, 55))]
}

names = [
    "blocks",
    "place"
]

block_group = pygame.sprite.Group()
