from Engine import engine
from Engine.lib.storage import Swap
from urllib import request

# create Swap
swap = Swap()


def get_external_version():
    req = request.urlopen("https://github.com/Lainupcomputer/PyGameEngine/blob/master/version.txt")
    data = req.read().decode('UTF-8')
    s = data.find('_version==')
    return data[s + 10:s + 17]


def start_game(swap):
    Game = engine.Engine(swap)
    Game.main_loop()


if swap.local_version == get_external_version():
    # Game is Up to date // start game
    start_game(swap)

else:
    print("Update Available\n"
          "Update the Game to play.")


