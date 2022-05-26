"""Base class for a game element."""

class GameElement:
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize game element.

        params:
        x - X coordinate of game element
        y - Y coordinate of game element
        """
        self.x = x
        self.y = y
