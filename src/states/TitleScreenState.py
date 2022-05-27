"""Title screen state class."""
import pygame

# Get intellisense for Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, gColors
from src.states.BaseState import BaseState

class TitleScreenState(BaseState):
    def __init__(self, game, params: dict) -> None:
        """Initialize title screen"""
        self.game: Game = game
        pygame.init()
        self.create_boxes()
        self.current_selection = 0
        self.input_ticker = 0
        self.clock = pygame.time.Clock()

    def render(self) -> None:
        """Draw the title screen."""
        # Set graphics settings
        self.game.screen.graphics["color"] = gColors["white"]
        self.game.screen.graphics["border-width"] = 2
        # Draw large title
        self.game.screen.graphics["font"] = "veryLargeFont"
        self.game.screen.draw_text("SNAKE GAME", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

        self.game.screen.graphics["font"] = "largeFont"
        # Draw play box
        self.set_selection_color(1)
        self.game.screen.draw_box(rect=self.play_box, fill=False)
        self.game.screen.draw_text("PLAY", rect=self.play_box)
        # Draw exit box
        self.set_selection_color(2)
        self.game.screen.draw_box(rect=self.exit_box, fill=False)
        self.game.screen.draw_text("EXIT", rect=self.exit_box)

    def update(self) -> None:
        """Update screen."""
        # Allow input only after 5 frames have passed
        if self.input_ticker > 0:
            self.input_ticker -= 1
        # Handle keyboard input
        self.handle_keyboard_input()

        # Render the screen
        self.game.screen.clear()
        self.render()

        dt = self.clock.tick() / 1000

        return dt

    def create_boxes(self) -> None:
        """Create PlAY and EXIT boxes."""
        box_width = SCREEN_WIDTH * 0.4
        box_height = 60

        center_pos_horizontal = SCREEN_WIDTH / 2 - box_width / 2
        play_box_pos_vertical = SCREEN_HEIGHT / 2
        exit_box_pos_vertical = play_box_pos_vertical + (box_height + 20)

        self.play_box = pygame.Rect(center_pos_horizontal, play_box_pos_vertical, box_width, box_height)
        self.exit_box = pygame.Rect(center_pos_horizontal, exit_box_pos_vertical, box_width, box_height)

    def set_selection_color(self, target_value: int) -> None:
        """
        Set color of selection box.

        params:
        target_value - target value of self.current_selection in which case the box should be orange
        """
        if target_value == self.current_selection:
            self.game.screen.graphics["color"] = "orange"
        else:
            self.game.screen.graphics["color"] = "white"

    def handle_keyboard_input(self) -> None:
        """
        Get change of selected box.
        """
        # Only allow input if at least 5 frames have passed since last input
        if self.input_ticker == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.current_selection == 1:
                            self.game.change_state("PlayState", params=None)
                        elif self.current_selection == 2:
                            pygame.quit()
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.current_selection = 1 if self.current_selection != 1 else 2
                    elif event.key == pygame.K_ESCAPE:
                        self.current_selection = 0
                    self.input_ticker = 5
            
