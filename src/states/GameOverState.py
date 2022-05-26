"""Game over state."""
import pygame

# Get intellisense for Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game

from src.states.BaseState import BaseState

class GameOverState(BaseState):
    def __init__(self, game, params: dict):
        """Initialize game over state."""
        self.game: Game = game