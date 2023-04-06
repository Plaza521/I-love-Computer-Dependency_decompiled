from DATA.Modules.variables import *

import json
import sys
import os


class Level(object):
    @classmethod
    def load(cls, level, block_group):
        player_x = None
        player_y = None

        block_group.empty()

        with open(f"DATA/Levels/{level}.json", "r") as file:
            world = json.load(file)

        for x in range(cols):
            for y in range(rows):
                if not world[x][y] in nons["block"]:
                    block = Group(x=x, y=y)
                    block_group.add(block)

                if world[x][y] == 25:
                    player_x = x * cellsize
                    player_y = y * cellsize

        return world, player_x, player_y


def start():
    settings = {
        "level": 1
    }

    if not os.path.exists("DATA/Player/player.json"):
        with open("DATA/Player/player.json", "w") as file:
            file.write(json.dumps(settings))
    else:
        with open("DATA/Player/player.json", "r") as file:
            try:
                settings = json.load(file)
            except:
                with open("DATA/Player/player.json", "w") as file:
                    file.write(json.dumps(settings))

    return settings


def exit(player):
    with open("DATA/Player/player.json", "w+") as file:
        file.write(json.dumps(player, indent=4))

    sys.exit()
