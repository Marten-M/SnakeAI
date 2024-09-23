"""Main code to execute"""
import sys
import pygame

import os
# Keep using keras-2 (tf-keras) rather than keras-3 (keras).
# This must be before other imports or it doesn't work
os.environ['TF_USE_LEGACY_KERAS'] = '1'

from src.lib.Game import Game
from src.lib.AI import AIPlayer
from src.lib.AI.Trainer import AITRainer

def main():
    # if len(sys.argv) < 2: # Normal game
    #     game = Game("TitleScreenState", {})
    #     game.update()
    # elif sys.argv[1] == "TRAIN":

    # params = {"player": "AI", "modelPath": "Models/100.weights.h5", "spedUp": True, "train": False}
    # game = Game("PlayState", params)
    # game.update()

    params = {"player": "AI", "train": True}
    game = Game("TrainState", params)
    trainer = AITRainer(game, params)
    trainer.train_neural_network(300, False, 50, "Models")


if __name__ == "__main__":
    main()