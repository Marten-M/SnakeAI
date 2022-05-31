"""Play state class for snake game."""
import pygame

# Get intellisense for Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game
# Constants
from src.constants import BOARD_SIZE, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
# State imports
from src.states.BaseState import BaseState
# Class imports
from src.classes.Snake import Snake
from src.classes.Apple import Apple

class PlayState(BaseState):
    def __init__(self, game, params: dict) -> None:
        """Initialize PlayState class."""
        super().__init__()
        pygame.init()
        self.game: Game = game
        self.score = 0
        self.paused = False

        self.snake = Snake(self.game, BOARD_SIZE // 2, BOARD_SIZE // 2)
        self.direction = self.current_direction = self.last_direction = "E"

        self.clock = pygame.time.Clock()
        self.move_speed = 2.4 # How many tiles to move per second
        self.cur_time = 0
        self.counter = 0

        self.apple = self.create_apple()

    def update(self) -> float:
        """Update play state."""
        # Get direction to move in
        opposites = {"S": "N", "N": "S", "W": "E", "E": "W"}
        self.direction = self.get_keyboard_input()
        if self.direction == "PAUSED":
            self.paused = not self.paused
        if not self.paused and self.direction != "PAUSED":
            if self.direction is None or self.direction == opposites[self.current_direction]:
                self.direction = self.last_direction
            else:
                self.last_direction = self.direction
            # Move the snake
            if self.cur_time >= 1 / self.move_speed:
                self.snake.move_snake(self.direction)
                self.cur_time = 0
                self.current_direction = self.direction
            # Check wall collision
            if self.snake.collides_with_wall():
                self.game.change_state("GameOverState")
            # Check body collision
            if self.snake.collides(self.snake):
                self.game.change_state("GameOverState")            
            # Check if we collide with apple
            if self.snake.collides(self.apple):
                self.snake.increase_length(1)
                self.apple = self.create_apple()
                self.score += 1
                self.move_speed += 0.1
        # Render screen
        self.game.screen.clear()
        self.render()
        # Time operations
        dt = self.clock.tick() / 1000
        self.cur_time += dt

        return dt

    def render(self):
        """Render objects in play state."""
        # Draw game area box
        self.game.screen.graphics["color"] = "white"
        self.game.screen.graphics["border-width"] = 2
        self.game.screen.draw_box(BOARD_SIZE * TILE_SIZE, BOARD_SIZE * TILE_SIZE, 2 * TILE_SIZE, 2 * TILE_SIZE, fill=False)
        # Draw apple
        apple_size = TILE_SIZE - 6
        self.game.screen.draw_box(apple_size, apple_size, (self.apple.x + 2) * TILE_SIZE + 3, (self.apple.y + 2) * TILE_SIZE + 3)
        # Draw snake
        self.snake.render()
        # Draw score
        self.game.screen.graphics["color"] = "white"
        self.game.screen.graphics["font"] = "largeFont"
        self.game.screen.draw_text(f"SCORE    {self.score}", (BOARD_SIZE + 2) * TILE_SIZE + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, 4 * TILE_SIZE)
        # If paused, draw PAUSED text
        if self.paused:
            self.game.screen.graphics["color"] = "orange"
            self.game.screen.graphics["font"] = "largeFont"
            self.game.screen.draw_text("PAUSED", (BOARD_SIZE + 4) * TILE_SIZE / 2, TILE_SIZE * 4)
    
    def get_keyboard_input(self) -> str:
        """Get keyboard input in frame."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    return "S"
                elif event.key == pygame.K_UP:
                    return "N"
                elif event.key == pygame.K_RIGHT:
                    return "E"
                elif event.key == pygame.K_LEFT:
                    return "W"
                elif event.key == pygame.K_ESCAPE:
                    return "PAUSED"

    def create_apple(self) -> Apple:
        """Create an Apple."""
        tmp = Apple()
        while tmp in self.snake.body:
            tmp = Apple()
        return tmp

    def exit(self) -> dict:
        return {"render": self.render}