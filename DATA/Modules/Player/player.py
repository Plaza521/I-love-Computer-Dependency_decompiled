from DATA.Modules.variables import *
import pygame
import numpy


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.last_x = x
        self.last_y = y

        self.images = player_images
        self.image = self.images["idle"][0]

        self.rect = self.image.get_rect()

        self.speed = 1.5
        self.canJump = True
        self.jump = False
        self.gravity = 0

        self.anim = ""
        self.last = ""

    """Анимация"""
    def animation(self, fps):
        var = False

        # print(f"now X - {round(self.x, 0)}, last X - {round(self.last_x, 0)}")
        # print(f"now Y - {round(self.y, 0)}, last Y - {round(self.last_y, 0)}")

        # print(self.anim)

        if self.gravity > 0:
            self.anim = "jump"

        else:
            if self.gravity < 0:
                self.anim = "fall"

            else:
                self.anim = "idle"

                for sprite in block_group:
                    rect = pygame.Rect(sprite.x * cellsize, sprite.y * cellsize, cellsize, cellsize)

                    for i in numpy.arange(0, self.rect.width, 5):
                        if rect.collidepoint(self.x + i, self.y + self.rect.height):
                            var = True

                if var:
                    if round(self.last_x, 0) == round(self.x, 0) and round(self.last_y, 0) == round(self.y, 0):
                        self.anim = "idle"

                    else:
                        self.anim = "run"

                else:
                    self.anim = "run"

        if self.anim == "idle":
            self.image = self.images["idle"][0]

        elif self.anim == "jump":
            self.image = self.images["jump"][0]

        elif self.anim == "fall":
            self.image = self.images["fall"][0]

        elif self.anim == "run":
            self.image = self.images["run"][(fps // 20) % 2]

        else:
            self.image = self.images["idle"][0]

        self.last_x = int(round(self.x))
        self.last_y = int(round(self.y))

    """Управление вправо и влево"""
    def run(self, player, block_group, route=None):
        move = True

        if route == "right" and pygame.sprite.spritecollide(self, block_group, False):
            if self.last != "right" and self.last != "":
                for element in self.images:
                    for i in range(len(self.images[element])):
                        self.images[element][i] = pygame.transform.flip(self.images[element][i], True, False)

                self.image = self.images["idle"][0]

            for sprite in block_group:
                rect = pygame.Rect(sprite.x * cellsize, sprite.y * cellsize, cellsize, cellsize)

                for i in numpy.arange(0, self.rect.height, 5):
                    if rect.collidepoint(self.x + self.rect.width, self.y + i):
                        move = False

            self.last = "right"

            if move:
                self.x += self.speed

        if route == "left" and pygame.sprite.spritecollide(self, block_group, False):
            if self.last != "left":
                for element in self.images:
                    for i in range(len(self.images[element])):
                        self.images[element][i] = pygame.transform.flip(self.images[element][i], True, False)

                self.image = self.images["idle"][0]

            for sprite in block_group:
                rect = pygame.Rect(sprite.x * cellsize, sprite.y * cellsize, cellsize, cellsize)

                for i in numpy.arange(0, self.rect.height, 5):
                    if rect.collidepoint(self.x, self.y + i):
                        move = False

            self.last = "left"

            if move:
                self.x -= self.speed

    """Прыжок"""
    def jump_start(self, player, block_group):
        if self.canJump:
            self.canJump = False
            self.gravity = 6

    """Падение"""
    def fall(self, player, block_group):
        self.y -= self.gravity

        if self.jump:
            for sprite in block_group:
                rect = pygame.Rect(sprite.x * cellsize, sprite.y * cellsize, cellsize - 2, cellsize - 2)

                for i in numpy.arange(0, self.rect.width, 5):
                    if rect.collidepoint(self.x + i, self.y):
                        self.gravity = 0
                        break

        self.gravity -= 0.2

        if self.gravity > 0:
            self.jump = True
        else:
            self.jump = False

        fall = True
        for sprite in block_group:
            rect = pygame.Rect(sprite.x * cellsize, sprite.y * cellsize, cellsize, cellsize)

            if rect.collidepoint(self.x + 3, self.y + self.rect.height):
                fall = False
                break

            if rect.collidepoint(self.x + self.rect.width - 3, self.y + self.rect.height):
                fall = False
                break

        if fall:
            self.canJump = False
        else:
            self.canJump = True
            self.gravity = 0

        for i in numpy.arange(0, self.rect.width, 5):
            while rect.collidepoint(self.x + i, self.y + self.rect.height - 1):
                self.y -= 1
