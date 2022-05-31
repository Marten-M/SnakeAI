"""Game over state."""
import pygame
import sys

from src.constants import TILE_SIZE, BOARD_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
# Get intellisense for Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game

from src.states.BaseState import BaseState

class GameOverState(BaseState):
    def __init__(self, game, params: dict):
        """Initialize game over state."""
        super().__init__()
        self.game: Game = game
        self.clock = pygame.time.Clock()
        self.render_play_state = params["render"]

    def render(self):
        """Render game screen."""
        self.game.screen.clear()
        # Render playstate state
        self.render_play_state()
        # Draw GAME OVER text
        self.game.screen.graphics["font"] = "largeFont"
        self.game.screen.graphics["color"] = "red"
        self.game.screen.draw_text("GAME OVER", (BOARD_SIZE + 2) * TILE_SIZE + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, SCREEN_HEIGHT / 2)
        self.game.screen.graphics["color"] = "orange"
        self.game.screen.draw_text("ENTER", (BOARD_SIZE + 2) * TILE_SIZE + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, SCREEN_HEIGHT / 4 * 3 + 25)
        # Draw play again text
        self.game.screen.graphics["color"] = "white"
        self.game.screen.graphics["font"] = "mediumFont"
        self.game.screen.draw_text("Press", (BOARD_SIZE + 2) * TILE_SIZE + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, SCREEN_HEIGHT / 4 * 3)
        self.game.screen.draw_text("to  return  to  Title  Screen", (BOARD_SIZE + 2) * TILE_SIZE + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, SCREEN_HEIGHT / 4 * 3 + 85)

    def update(self) -> float:
        """Update game over state."""
        # Get keyboard input
        self.get_keyboard_input()
        # Render screen
        self.render()

        dt = self.clock.tick() / 1000
        return dt

    def get_keyboard_input(self):
        """Get keyboard input."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state("TitleScreenState")
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)