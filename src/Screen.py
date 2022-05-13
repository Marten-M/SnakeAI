"""Screen class for Snake."""

import pygame

class Screen:
    def __init__(self, width: int, height: int) -> None:
        """
        Initialize screen.

        params:
        width - width of the screen in pixels
        height - height of the screen in pixels
        """
        self.font: pygame.font = None
        self.font_size = None
        self.color = (0, 0, 0)
        self.display = self.create_display(width, height)

    def clear(self) -> None:
        """Clear the screen."""
        self.color = (0, 0, 0)
        self.display.fill((self.color))
        pygame.display.update()

    def draw_text(self, text: str, x: int, y: int) -> None:
        """
        Draw text to specified coordinates.

        params:
        text - text to be drawn
        x - horizontal coordinate of text
        y - vertical coordinate of text
        """
        self.display.blit(self.font.Font.render(text, True, (self.color)), (x, y))
        self.display.update()

    def draw_box(self, width: int, height: int, x: int, y: int, fill: bool=False) -> None:
        """
        Draw a box with given dimensions on the screen.

        params:
        width - width of the box
        height - height of the box
        x - X coordinate of top left corner of the box
        y - Y coordinate of top left corner of the box
        fill - whether to fill the box or not
        """
        # TODO
        pass

    def create_display(self, width: int, height: int):
        """
        Create display screen.

        params:
        width - width of the screen in pixels
        height - height of the screen in pixels
        """
        screen_dimensions = (width, height)
        screen = pygame.display.set_mode(size=screen_dimensions)

        pygame.display.set_caption("Snake")
        # Fill screen with black
        black = (0, 0, 0)
        screen.fill((black))
        pygame.display.update()
        return screen