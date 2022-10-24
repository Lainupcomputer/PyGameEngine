from Engine import engine
from Engine.lib.storage import Swap
from urllib import request
import logging


# setup logger
logger = logging.getLogger()
logging.basicConfig(filename="log.log", level=logging.DEBUG, format="%(asctime)s %(message)s")
logger.info("application started")

logger.info("creating Swap")
swap = Swap()
logger.info("try getting version information")


def get_external_version():
    req = request.urlopen("https://github.com/Lainupcomputer/PyGameEngine/blob/master/version.txt")
    data = req.read().decode('UTF-8')
    s = data.find('_version==')
    logger.info(f"remote version = {data[s + 10:s + 17]}")
    return data[s + 10:s + 17]


remote_version = get_external_version()


def start_game(swap):
    game = engine.Engine(swap, logger)
    game.main_loop()


if swap.local_version == remote_version:
    logger.info(f"Game is Up to date! current version = {swap.local_version}")
    # Game is Up to date // start game
    start_game(swap)

else:
    logger.warning(f"Game needs update! current version = {swap.local_version}, remote is {remote_version}")
    print("Update Available\n"
          "Update the Game to play.")


