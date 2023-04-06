from DATA.Modules.ultilius.button import Button

from DATA.Modules.base import file

from PIL import ImageFont


def settings(screen, width, height):
    ttf = ImageFont.truetype("DATA/Arial.ttf", 30)

    text = "Settings"
    width_button = 250
    height_button = 85

    x = width / 2 - width_button / 2
    y = height / 2 - height_button / 2

    button_game = Button(screen=screen, width=width_button, height=height_button,
                         inactive_color="#868D8E", active_color="#6F7172", rama_color="#525252")

    button_game.draw(x=x, y=y, message=text, action=None,
                     text_x=x + (button_game.width - ttf.getsize(text)[0]) / 2,
                     text_y=y + (button_game.height - ttf.getsize(text)[1]) / 2)


def exit(screen, width, height, player):
    ttf = ImageFont.truetype("DATA/Arial.ttf", 30)

    text = "Exit"
    width_button = 250
    height_button = 85

    x = width / 2 - width_button / 2
    y = height / 2 - height_button / 2 + 100

    button_game = Button(screen=screen, width=width_button, height=height_button,
                         inactive_color="#868D8E", active_color="#6F7172", rama_color="#525252")

    button_game.draw(x=x, y=y, message=text, action=lambda: file.exit(player=player),
                     text_x=x + (button_game.width - ttf.getsize(text)[0]) / 2,
                     text_y=y + (button_game.height - ttf.getsize(text)[1]) / 2)


def play(screen, width, height, function):
    ttf = ImageFont.truetype("DATA/Arial.ttf", 30)

    text = "Play"
    width_button = 250
    height_button = 85

    x = width / 2 - width_button / 2
    y = height / 2 - height_button / 2 - 100

    button_game = Button(screen=screen, width=width_button, height=height_button,
                         inactive_color="#868D8E", active_color="#6F7172", rama_color="#525252")

    button_game.draw(x=x, y=y, message=text, action=function,
                     text_x=x + (button_game.width - ttf.getsize(text)[0]) / 2,
                     text_y=y + (button_game.height - ttf.getsize(text)[1]) / 2)
