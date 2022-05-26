"""Class for edible apple"""
import random
from src.constants import BOARD_SIZE, TILE_SIZE

from src.classes.GameElement import GameElement

class Apple(GameElement):
    def __init__(self) -> None:
        """
        Initialize apple class.

        params:
        x - X coordinate of apple
        y - Y coordinate of apple
        """
        x = random.randrange(0, BOARD_SIZE)
        y = random.randrange(0, BOARD_SIZE)
        super().__init__(x, y)
    
    def __eq__(self, other):
        """Check if equal."""
        return self.x == other.x and self.y == other.y

