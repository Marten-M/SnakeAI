"""AI class for snake game."""
import numpy as np
# Get intellisense for Snake, Apple and Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game

from src.lib.AI.modelfunctions import load_model
from src.lib.AI.actions import get_best_legal_action


class AIPlayer:
    def __init__(self, game, model_path: str):
        """Initialize AI class."""
        self.game: Game = game
        self.model = load_model(model_path)

    def get_move(self, state: list) -> str:
        """
        Get the move the AI will make.

        params:
        state - state of the game

        :return:
        Direction in which the snake will move.
        """
        actions = self.model.predict(np.array([state]))[0]
        actual_action = get_best_legal_action(actions, state)

        return "NESW"[actual_action]
