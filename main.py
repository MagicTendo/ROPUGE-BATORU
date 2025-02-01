import os
import error_handler

from game import Game

os.system("")

if __name__ == "__main__":
    try:
        game = Game()
        game.main_screen()
    except KeyboardInterrupt as error:
        error_handler.catch_error(KeyboardInterrupt)
    except Exception as error:
        error_handler.catch_error(Exception, error)
