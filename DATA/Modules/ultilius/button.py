from DATA.Modules.ultilius.print_text import print_text
import pygame


class Button(object):
    def __init__(self, screen, width, height, inactive_color, active_color, rama_color, sound_click=None):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_clr = inactive_color
        self.active_clr = active_color
        self.rama_clr = rama_color
        self.sound = sound_click

    def draw(self, x, y, message, text_x=None, text_y=None, action=None, font_size=30):
        if text_x is None:
            text_x = x

        if text_y is None:
            text_y = y

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(self.screen, self.active_clr, (x, y, self.width, self.height))

                if click[0] == 1:
                    if self.sound is not None:
                        try:
                            pygame.mixer.Sound.play(self.sound)
                            pygame.time.delay(200)
                        except:
                            print('Not found file')

                    if action is not None:
                        action()

            else:
                pygame.draw.rect(self.screen, self.inactive_clr, (x, y, self.width, self.height))

        else:
            pygame.draw.rect(self.screen, self.inactive_clr, (x, y, self.width, self.height))

        pygame.draw.rect(self.screen, self.rama_clr, (x, y, self.width, self.height), 3)
        print_text(self.screen, text_x, text_y, message, font_size)
