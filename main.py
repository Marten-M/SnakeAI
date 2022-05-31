"""Main code to execute"""
from src.lib.Game import Game

def main():
    game = Game("TitleScreenState")
    game.update()


if __name__ == "__main__":
    main()