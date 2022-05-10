"""Snake game class."""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import pygame
import constants

class Game:
    def __init__(self) -> None:
        """Initialize game class."""
        pygame.init()
        self.state = "start"
        self.states = {}
        self.screen = self.initialize_screen()

    def initialize_screen(self) -> pygame.display:
        """Initialize game window."""
        # Create screen
        window = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        pygame.display.set_caption("Snake")
        screen = pygame.display.set_mode(size=window)
        # Fill screen with black
        black = (0, 0, 0)
        screen.fill((black))
        pygame.display.update()

        return screen

    def change_state(self, new_state, params: dict) -> None:
        """
        Change game state.

        params:
        new_state - new state to change to
        params - parameter to pass into new_state
        """
        pass