"""Snake game class."""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import pygame
import constants
from Screen import Screen

class Game:
    def __init__(self) -> None:
        """Initialize game class."""
        pygame.init()
        self.state = "start"
        self.states = {}
        self.screen = Screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)


    def change_state(self, new_state, params: dict) -> None:
        """
        Change game state.

        params:
        new_state - new state to change to
        params - parameter to pass into new_state
        """
        pass