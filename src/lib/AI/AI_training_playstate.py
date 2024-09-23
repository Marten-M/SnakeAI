"""PlayState adapted to train the AI."""

from src.states.PlayState import PlayState
import pygame


class AIPlayState(PlayState):
    def __init__(self, game, params):
        super().__init__(game, params)
        self.game_ended = False
        self.was_moving_toward_apple = False
        self.last_score = 0
        self.previous_heading = 'N'

    def update(self) -> float:
        pygame.event.get()  # Needed or nothing about pygame will work
        self.game.screen.clear()
        self.render()
        pygame.display.update()

        dt = self.clock.tick() / 1000
        self.cur_time += dt

        return dt

    def take_step(self, action: int) -> bool:
        """
        Take a singe action step.

        :params:
        action - whether to move north, east, south or west indicated by 0, 1, 2, 3 respectively.

        :return:
        boolean indicating whether the taken move caused the game to be over
        """
        directions = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
        opposites = {'S': 'N', 'N': 'S', 'W': 'E', 'E': 'W'}

        self.direction = directions[action]
        if self.direction == opposites[self.current_direction]:
            self.direction = self.last_direction
            return True  # Illegal move which would end the game if it were legal
        else:
            self.last_direction = self.direction

        self.move_snake()
        self.detect_collisions()

        if self.game_ended:
            return True
        return False

    def move_snake(self):
        self.snake.move_snake(self.direction)
        self.current_direction = self.direction
        self.moves_survived += 1

    def game_over(self):
        self.game_ended = True

    def evaluate_state(self) -> int:
        """
        Evaluate the current state of the game and convert it to a numerical score.
        Score is calculated based on survival time, score, and how close the snake head is to the apple.

        :return:
        current state's evaluation as a numerical score
        """
        apple_on_left = 1 if self.apple.x < self.snake.head.x else 0
        apple_on_right = 1 if self.snake.head.x < self.apple.x else 0
        apple_above = 1 if self.apple.y < self.snake.head.y else 0
        apple_below = 1 if self.snake.head.y < self.apple.y else 0

        moving_toward_apple = False
        if apple_on_left and self.current_direction == 'W':
            moving_toward_apple = True
        elif apple_on_right and self.current_direction == 'E':
            moving_toward_apple = True
        elif apple_above and self.current_direction == 'N':
            moving_toward_apple = True
        elif apple_below and self.current_direction == 'S':
            moving_toward_apple = 6

        reward = -2
        if self.was_moving_toward_apple and not moving_toward_apple and not (self.last_score < self.score):
            reward -= 3
        if self.last_score < self.score:  # Apple was eaten
            reward += 20
        if not self.was_moving_toward_apple and self.direction != self.previous_heading:  # Direction was changed after moving away from apple
            reward += 2
        if not self.was_moving_toward_apple and moving_toward_apple:
            reward += 5
        if self.game_ended:
            reward -= 15

        self.was_moving_toward_apple = moving_toward_apple
        self.last_score = self.score
        self.previous_heading = self.direction

        return reward
