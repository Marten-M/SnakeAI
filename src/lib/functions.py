"""Helper functions for the game."""
<<<<<<< HEAD
from src.classes.Snake import Snake

from src.constants import BOARD_SIZE


def get_distance(part: tuple, pos: int, snake: Snake, *ignore, direction: str) -> int:
=======

# Get intellisense for Snake class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.classes.Snake import Snake


def get_distance(wall_distance: int, part: tuple, pos: int, snake: Snake) -> int:
>>>>>>> refs/remotes/origin/main
    """
    Get wall/body distance from the head.

    :params:
    part - part to check
    pos - variable coordinate of the part
    snake - snake in the game
<<<<<<< HEAD
    direction - direction in which to compare the distance. "horizontal" or "vertical"
=======
>>>>>>> refs/remotes/origin/main

    :return:
    distance from the wall/head.
    """
    if part in snake.body:
        # Distance from head
<<<<<<< HEAD
        if direction == "horizontal":
            distance = abs(snake.head.x - pos)
        else:
            distance = abs(snake.head.y - pos)

        body_parts_left = snake.size - snake.body.index(part) - 1
        # Check if the snake will collide with the body part or will the body part move away before the snake head reaches it
        if distance <= body_parts_left:
=======
        distance = snake.head.x - pos
        # How many body parts are left
        body_parts_left = snake.size - snake.body.index(part) - 1
        if distance <= body_parts_left: # If the snake will collide with its body
>>>>>>> refs/remotes/origin/main
            return distance - 1

    return -1


def assign_distance(start: int, end: int, snake: Snake, *ignore, direction: str) -> int:
    """
    Assign distance from body/wall to variable.

    :params:
    start - number to start counting from (included)
    end - number to end counting on (excluded)
    snake - snake in the game
    direction - direction to start counting in
    """
    step = 1 if start <= end else -1
<<<<<<< HEAD
    # Assign distance to wall at first
    if direction == "horizontal":
        distance = BOARD_SIZE - snake.head.x - 1 if step == 1 else snake.head.x
    else:
        distance = BOARD_SIZE - snake.head.y - 1 if step == 1 else snake.head.y

    # Assign distance to body part if it should be collided with before the wall
=======
    distance = snake.head.x if direction == "horizontal" else snake.head.y
>>>>>>> refs/remotes/origin/main
    for i in range(start, end, step):
        if direction == "horizontal":
            part = (i, snake.head.y)
        else:
            part = (snake.head.x, i)

<<<<<<< HEAD
        tmp = get_distance(part, i, snake, direction=direction)
        if tmp != -1:
            distance = tmp
            break

    return distance
=======
        tmp = get_distance(distance, part, i, snake)
        if tmp != -1:
            distance = tmp
            break
    return distance
>>>>>>> refs/remotes/origin/main
