import pygame


def print_text(screen, x, y, message, font_size, font_type='DATA/arial.ttf', font_color=(0, 0, 0)):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, font_color)
    screen.blit(text, (x, y))
