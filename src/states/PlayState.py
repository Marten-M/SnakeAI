"""Play state class for snake game."""
import pygame

# Get intellisense for Game and AI class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game
    from src.lib.AI import AI
# Constants
from src.constants import BOARD_SIZE, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
# State imports
from src.states.BaseState import BaseState
# Class imports
from src.classes.Snake import Snake
from src.classes.Apple import Apple

# Function imports
from src.lib.functions import assign_distance

class PlayState(BaseState):
    def __init__(self, game, params: dict) -> None:
        """Initialize PlayState class."""
        super().__init__()
        pygame.init()
        self.game: Game = game
        self.score = 0
        self.paused = False

        self.player = '' if not params["player"] else params["player"]
        if self.player == "AI":
            self.AI: AI = params["AI"]

        self.snake = Snake(self.game, BOARD_SIZE // 2, BOARD_SIZE // 2)
        print(self.snake.body.index((BOARD_SIZE // 2, BOARD_SIZE // 2)))
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
        if self.player != "AI":
            self.direction = self.get_keyboard_input()
        else:
            state = self.get_state()
            self.direction = self.AI.get_move(state)

        if self.direction == "PAUSED":
            self.paused = not self.paused

        if not self.paused and self.direction != "PAUSED":
            if self.direction is None or self.direction == opposites[self.current_direction]:
                self.direction = self.last_direction
            else:
                self.last_direction = self.direction
            # Move the snake
            self.move_snake()
            # Detect collisions
            self.detect_collisions()
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
                if event.key in {pygame.K_DOWN, pygame.K_s}:
                    return "S"
                elif event.key in {pygame.K_UP, pygame.K_w}:
                    return "N"
                elif event.key in {pygame.K_RIGHT, pygame.K_d}:
                    return "E"
                elif event.key in {pygame.K_LEFT, pygame.K_a}:
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

    def detect_collisions(self):
        """Detect collisions in game."""
        # Check wall collision
        if self.snake.collides_with_wall():
            self.game_over()

        # Check body collision
        if self.snake.collides(self.snake):
            self.game_over()

        # Check if we collide with apple
        if self.snake.collides(self.apple):
            self.snake.increase_length(1)
            self.apple = self.create_apple()
            self.score += 1
            self.move_speed += 0.1

    def move_snake(self):
        """Move the snake."""
        if self.player != "AI":
            if self.cur_time >= 1 / self.move_speed:
                self.snake.move_snake(self.direction)
                self.cur_time = 0
                self.current_direction = self.direction
        else:
            self.snake.move_snake(self.direction)
            self.current_direction = self.direction

    def game_over(self):
        """Event handler for when game ends."""
        if self.player != "AI":
            self.game.change_state("GameOverState")
        else:
            self.AI.new_game()

    def get_state(self) -> list:
        """
        Get current state of the game.

        :return:
        list of state attributes in the form
        [LEFT_DISTANCE, RIGHT_DISTANCE, UP_DISTANCE, DOWN_DISTANCE, HEAD_X, HEAD_Y, APPLE_X, APPLE_Y],
        where distances are distances from the wall or body, whichever is closer, if the snake were to move in that direction
        """
        # Get horizontal distances
        left_distance = assign_distance(self.snake.head.x - 1, -1, self.snake, direction="horizontal")
        right_distance = assign_distance(self.snake.head.x + 1, BOARD_SIZE, self.snake, direction="horizontal")
        # Get vertical distances
        up_distance = assign_distance(self.snake.head.y, -1, self.snake, direction="vertical")
        down_distance = assign_distance(self.snake.head.y, BOARD_SIZE, self.snake, direction="vertical")

        return [left_distance, right_distance, up_distance, down_distance, self.snake.head.x, self.snake.head.y, self.apple.x, self.apple.y]

                    

