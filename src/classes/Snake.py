"""Snake class"""

# Get intellisense for Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.lib.Game import Game

from src.constants import TILE_SIZE, BOARD_SIZE

from src.classes.GameElement import GameElement

<<<<<<< HEAD

class BodyPart(GameElement):
    def __init__(self, x: int, y: int, nr: int) -> None:
        """
        Initialize body part class.
=======
class Bodypart(GameElement):
    def __init__(self, x: int, y: int, nr: int) -> None:
        """
        Initialze body part class.
>>>>>>> refs/remotes/origin/main
        
        params:
        x - X coordinate of body part
        y - Y coordinate of body part
        nr - the number of the body part
        """
        super().__init__(x, y)

    def __eq__(self, other) -> bool:
        """Check if two body parts or a tuple formatted as (x, y) are equal."""
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]

        return self.x == other.x and self.y == other.y
<<<<<<< HEAD
=======
        
>>>>>>> refs/remotes/origin/main

    def __str__(self) -> str:
        """Convert to string."""
        return f"{[self.x, self.y]}"


class Snake:
    def __init__(self, game, x: int, y: int) -> None:
        """
        Initialize snake class.

        params:
        x - starting X coordinate of snake
        y - starting Y coordinate of snake
        """
        self.game: Game = game
<<<<<<< HEAD
        self.head = BodyPart(x, y, 0)
        self.body = [self.head]
        self.size = 1

    def increase_length(self, size_increase: int = 1) -> None:
=======
        self.head = Bodypart(x, y, 0)
        self.body = [self.head]
        self.size = 1

    def increase_length(self, size_increase: int=1) -> None:
>>>>>>> refs/remotes/origin/main
        """
        Increase length of the snake.

        params:
        size_increase - extra size to increase the snake by, default is 1
        """
        for i in range(size_increase):
            x, y = self.body[-1].x, self.body[-1].y
<<<<<<< HEAD
            self.body.insert(self.size - 1, BodyPart(x, y, self.size))
=======
            self.body.insert(self.size - 1, Bodypart(x, y, self.size))
>>>>>>> refs/remotes/origin/main
            self.size += 1

    def move_snake(self, head_direction: str) -> None:
        """
        Move snake one step.

        params:
        head_direction - direction of the head
        """
        directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
        for i in range(self.size - 1):
            x, y = self.body[i + 1].x, self.body[i + 1].y
            self.body[i].x, self.body[i].y = x, y

        dx, dy = directions[head_direction]
        self.head.x += dx 
        self.head.y += dy

    def collides(self, other) -> bool:
        """
        Check if snake is colliding with other snake.

        params:
        other - snake to check collision with.

        return:
        True if snake is colliding with other snake, False otherwise
        """
        if isinstance(other, Snake):
            if other is self:
<<<<<<< HEAD
                # Second part is necessary to not count the snake eating an apple and extending as it colliding with itself,
                # since the body part is spawned right after the head, so it will be "inside" of the snake for 1 turn
=======
>>>>>>> refs/remotes/origin/main
                return self.head in other.body[:self.size - 1] and other.body[-1] != other.body[-2]
            else:
                return self.head in other.body
        else:
            # If it is not a snake it is an apple
            return other in self.body

    def collides_with_wall(self) -> bool:
        """
        Check snake's collision with wall.

        return:
        True if snake is colliding with a wall, False otherwise
        """
        # Ceiling collision
        if self.head.y < 0:
            return True
        # Floor collision
        if self.head.y >= BOARD_SIZE:
            return True
        # Left wall collision
        if self.head.x < 0:
            return True
        # Right wall collision
        if self.head.x >= BOARD_SIZE:
            return True

        return False

    def render(self) -> None:
        """Render snake."""
        self.game.screen.graphics["color"] = "white"
        for body_part in self.body[:-1]:
            self.draw_body_part(body_part)
        # Draw the head a different color
        self.game.screen.graphics["color"] = "gray"
        self.draw_body_part(self.head)
    
<<<<<<< HEAD
    def draw_body_part(self, body_part:BodyPart) -> None:
=======
    def draw_body_part(self, body_part:Bodypart) -> None:
>>>>>>> refs/remotes/origin/main
        """
        Draw body part onto the screen.

        params:
        body_part - Body part to be drawn onto the screen
        """
        body_size = TILE_SIZE - 2
        self.game.screen.draw_box(body_size, body_size, (body_part.x + 2) * TILE_SIZE + 1, (body_part.y + 2) * TILE_SIZE + 1)