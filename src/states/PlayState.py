"""Play state class for snake game."""
import pygame

# Get intellisense for Game and AI class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game
<<<<<<< HEAD

from src.lib.AI.AIPlayer import AIPlayer
# Constants
from src.constants import BOARD_SIZE, TILE_SIZE, SCREEN_WIDTH
=======
    from src.lib.AI import AI
# Constants
from src.constants import BOARD_SIZE, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
>>>>>>> refs/remotes/origin/main
# State imports
from src.states.BaseState import BaseState
# Class imports
from src.classes.Snake import Snake
from src.classes.Apple import Apple

# Function imports
from src.lib.functions import assign_distance

<<<<<<< HEAD

class PlayState(BaseState):
    def __init__(self, game, params: dict) -> None:
        """
        :params:
        game - Game object that runs the state
        params - dictionary containing parameter values. Required field is "player" (str). if "player" is "AI" then
        "spedUp" (bool), "modelPath" (str) and "train" (bool) must also be specified
        Initialize PlayState class.
        """
        super().__init__()
        pygame.init()
        self.game: Game = game
        self.params = params

        self.score = 0
        self.paused = False

        self.sped_up = False

        self.player = params["player"]
        if self.player == "AI" and not params["train"]:
            self.AI: AIPlayer = AIPlayer(game, params["modelPath"])
            self.sped_up = params["spedUp"]

        self.snake = Snake(self.game, BOARD_SIZE // 2, BOARD_SIZE // 2)
        self.direction = self.current_direction = self.last_direction = "E"

        self.clock = pygame.time.Clock()
        self.move_speed = 2.4  # How many tiles to move per second
        self.cur_time = 0
        self.counter = 0
        self.moves_survived = 0

        self.game_ended = False
=======
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
>>>>>>> refs/remotes/origin/main

        self.apple = self.create_apple()

    def update(self) -> float:
        """Update play state."""
        # Get direction to move in
        opposites = {"S": "N", "N": "S", "W": "E", "E": "W"}
<<<<<<< HEAD
        events = pygame.event.get()
        if self.player != "AI":
            self.direction = self.get_keyboard_input(events)
=======
        if self.player != "AI":
            self.direction = self.get_keyboard_input()
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD

            if not self.sped_up and self.cur_time >= 1 / self.move_speed:
                self.move_snake()
            elif self.sped_up:
                self.move_snake()  # Do not wait for the delay if game is sped up

            self.detect_collisions()

            if self.game_ended:
                if self.player == "AI":
                    self.game.change_state("PlayState", params=self.params)  # Start new game if AI is playing
                else:
                    self.game.change_state("GameOverState")

        self.game.screen.clear()
        self.render()

=======
            # Move the snake
            self.move_snake()
            # Detect collisions
            self.detect_collisions()
        # Render screen
        self.game.screen.clear()
        self.render()
        # Time operations
>>>>>>> refs/remotes/origin/main
        dt = self.clock.tick() / 1000
        self.cur_time += dt

        return dt

    def render(self):
        """Render objects in play state."""
        # Draw game area box
        self.game.screen.graphics["color"] = "white"
        self.game.screen.graphics["border-width"] = 2
<<<<<<< HEAD
        self.game.screen.draw_box(BOARD_SIZE * TILE_SIZE, BOARD_SIZE * TILE_SIZE,
                                  2 * TILE_SIZE, 2 * TILE_SIZE, fill=False)
        # Draw apple
        apple_size = TILE_SIZE - 6
        self.game.screen.draw_box(apple_size, apple_size, (self.apple.x + 2) * TILE_SIZE + 3,
                                  (self.apple.y + 2) * TILE_SIZE + 3)
=======
        self.game.screen.draw_box(BOARD_SIZE * TILE_SIZE, BOARD_SIZE * TILE_SIZE, 2 * TILE_SIZE, 2 * TILE_SIZE, fill=False)
        # Draw apple
        apple_size = TILE_SIZE - 6
        self.game.screen.draw_box(apple_size, apple_size, (self.apple.x + 2) * TILE_SIZE + 3, (self.apple.y + 2) * TILE_SIZE + 3)
>>>>>>> refs/remotes/origin/main
        # Draw snake
        self.snake.render()
        # Draw score
        self.game.screen.graphics["color"] = "white"
        self.game.screen.graphics["font"] = "largeFont"
<<<<<<< HEAD
        self.game.screen.draw_text(f"SCORE    {self.score}", (BOARD_SIZE + 2) * TILE_SIZE
                                   + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, 4 * TILE_SIZE)
=======
        self.game.screen.draw_text(f"SCORE    {self.score}", (BOARD_SIZE + 2) * TILE_SIZE + (SCREEN_WIDTH - (BOARD_SIZE + 2) * TILE_SIZE) / 2, 4 * TILE_SIZE)
>>>>>>> refs/remotes/origin/main
        # If paused, draw PAUSED text
        if self.paused:
            self.game.screen.graphics["color"] = "orange"
            self.game.screen.graphics["font"] = "largeFont"
            self.game.screen.draw_text("PAUSED", (BOARD_SIZE + 4) * TILE_SIZE / 2, TILE_SIZE * 4)

<<<<<<< HEAD
    def get_keyboard_input(self, events) -> str:
        """Get keyboard input in frame."""
        for event in events:
=======
    def get_keyboard_input(self) -> str:
        """Get keyboard input in frame."""
        for event in pygame.event.get():
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
        self.snake.move_snake(self.direction)
        self.cur_time = 0
        self.current_direction = self.direction
        self.moves_survived += 1

    def game_over(self):
        """Event handler for when game ends."""
        self.game_ended = True
=======
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
>>>>>>> refs/remotes/origin/main

    def get_state(self) -> list:
        """
        Get current state of the game.

        :return:
<<<<<<< HEAD
        list of state attributes
        """
        left_distance = assign_distance(self.snake.head.x - 1, -1, self.snake, direction="horizontal")
        right_distance = assign_distance(self.snake.head.x + 1, BOARD_SIZE, self.snake, direction="horizontal")
        up_distance = assign_distance(self.snake.head.y, -1, self.snake, direction="vertical")
        down_distance = assign_distance(self.snake.head.y, BOARD_SIZE, self.snake, direction="vertical")

        going_to_die_left = left_distance == 0
        going_to_die_right = right_distance == 0
        going_to_die_down = down_distance == 0
        going_to_die_up = up_distance == 0

        apple_on_left = 1 if self.apple.x < self.snake.head.x else 0
        apple_on_right = 1 if self.snake.head.x < self.apple.x else 0
        apple_above = 1 if self.apple.y < self.snake.head.y else 0
        apple_below = 1 if self.snake.head.y < self.apple.y else 0

        moving_left = self.current_direction == 'W'
        moving_right = self.current_direction == 'E'
        moving_up = self.current_direction == 'N'
        moving_down = self.current_direction == 'S'

        moving_toward_apple = ((apple_on_left and moving_left) or (apple_on_right and moving_right) or
                               (apple_below and moving_down) or (apple_above and moving_up))

        return [moving_up, moving_right, moving_down, moving_left, apple_on_left, apple_on_right,
                apple_above, apple_below, moving_toward_apple, going_to_die_left, going_to_die_right,
                going_to_die_up, going_to_die_down]
=======
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

                    

>>>>>>> refs/remotes/origin/main
