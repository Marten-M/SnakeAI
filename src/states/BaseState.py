"""Base state that all other states inherit from."""

class BaseState:
    """BaseState class with empty default functions."""
    def __init__(self) -> None:
        """Initialize base state class."""
        self.drawFPS = True # Draw FPS by default

    def update(self) -> None:
        """Update game state."""
        pass
    
    def render(self) -> None:
        """Render objects onto the screen."""
        pass

    def exit(self) -> dict:
        """Function that gets called when exiting game state."""
        pass
