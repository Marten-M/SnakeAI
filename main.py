"""Main code to execute"""
import sys
import pygame

from src.lib.Game import Game
from src.lib.AI import AIPlayer
from src.lib.AI.Trainer import AITRainer

def main():
    # if len(sys.argv) < 2: # Normal game
    #     game = Game("TitleScreenState", {})
    #     game.update()
    # elif sys.argv[1] == "TRAIN":
    # params = {"player": "AI", "modelPath": "Models/1400.h5", "spedUp": True}
    # game = Game("PlayState", params)
    # game.update()

    params = {"player": "AI", "train": True, }
    game = Game("TrainState", params)
    trainer = AITRainer(game, params)
    trainer.train_neural_network(300, True, 50, "Models")


if __name__ == "__main__":
    main()