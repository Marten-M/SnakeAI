"""Main code to execute"""
import sys

from src.lib.Game import Game
from src.lib.AI import AI

def main():
    if len(sys.argv) < 2:
        game = Game("TitleScreenState")
        game.update()
    else:
        computer = AI(Game("PlayState"), create_new=False)



if __name__ == "__main__":
    main()