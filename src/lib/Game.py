"""Snake game class."""

import pygame

from src import constants
from src.lib.Screen import Screen

# State imports
from src.states.TitleScreenState import TitleScreenState
from src.states.PlayState import PlayState
from src.states.GameOverState import GameOverState


class Game:
    def __init__(self, initial_state) -> None:
        """Initialize game class."""
        pygame.init()
        self.states = {"TitleScreenState": TitleScreenState, "PlayState": PlayState, "GameOverState": GameOverState}
        self.screen = Screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.state = self.states[initial_state](self, None)

    def change_state(self, new_state, *ignore, params: dict) -> None:
        """
        Change game state.

        params:
        new_state - new game state
        params - parameters to pass into new_state
        """
        if params is not None:
            exit_params = self.state.exit()
            if exit_params is not None:
                params = params | self.state.exit()
        self.state = self.states[new_state](self, params)

    def update(self) -> None:
        """Update game."""
        while True:
            # Update game state
            self.state.update()
            # Update screen
            pygame.display.update()