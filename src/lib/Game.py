"""Snake game class."""
import pygame

from src import constants
from src.lib.Screen import Screen

# State imports
from src.states.TitleScreenState import TitleScreenState
from src.states.PlayState import PlayState
from src.states.GameOverState import GameOverState


class Game:
<<<<<<< HEAD
    def __init__(self, initial_state, params=None) -> None:
=======
    def __init__(self, initial_state) -> None:
>>>>>>> refs/remotes/origin/main
        """Initialize game class."""
        pygame.init()
        self.states = {"TitleScreenState": TitleScreenState, "PlayState": PlayState, "GameOverState": GameOverState}
        self.screen = Screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
<<<<<<< HEAD
        if params["player"] == "AI" and not params["train"]:  # Don't set the state if we are training a model
            self.state = self.states[initial_state](self, params)
=======
        self.state = self.states[initial_state](self, None)
>>>>>>> refs/remotes/origin/main

        self.time = 0
        self.frame_count = 0
        self.fps = None

<<<<<<< HEAD
    def change_state(self, new_state, *ignore, params=None) -> None:
=======
    def change_state(self, new_state, *ignore, params: dict=dict()) -> None:
>>>>>>> refs/remotes/origin/main
        """
        Change game state.

        params:
        new_state - new game state
        params - parameters to pass into new_state
        """
<<<<<<< HEAD
        if params is None:
            params = dict()

=======
>>>>>>> refs/remotes/origin/main
        exit_params = self.state.exit()
        if exit_params is not None:
            params = params | self.state.exit()
        self.state = self.states[new_state](self, params)

    def update(self) -> None:
        """Update game."""
        while True:
            # Update game state
            self.time += self.state.update()
            self.frame_count += 1
<<<<<<< HEAD

=======
    
>>>>>>> refs/remotes/origin/main
            if self.time >= 1:
                self.fps = round(self.frame_count / self.time)
                self.time = 0
                self.frame_count = 0

            # Draw FPS if state allows it
            if self.state.drawFPS and self.fps is not None:
                self.screen.graphics["color"] = "white"
                self.screen.graphics["font"] = "mediumFont"
                self.screen.draw_text(f"{self.fps} FPS", 5, 0, text_align="left")
            # Update screen
            pygame.display.update()
