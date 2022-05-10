"""Snake class"""

class Snake:
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize snake class.
        
        params:
        x - starting X coordinate of snake
        y - starting Y coordinate of snake
        """
        self.x = x
        self.y = y
    
    def render(self) -> None:
        """Render snake."""
        # TODO