"""Base state that all other states inherit from."""

class BaseState:
    """BaseState class with empty default functions."""
    def update(self) -> None:
        """Update game state."""
        pass
    
    def render(self) -> None:
        """Render objects onto the screen."""
        pass

    def exit(self) -> dict:
        """Function that gets called when exiting game state."""
        pass
