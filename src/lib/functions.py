"""Helper functions for the game."""

# Get intellisense for Snake class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.classes.Snake import Snake


def get_distance(wall_distance: int, part: tuple, pos: int, snake: Snake) -> int:
    """
    Get wall/body distance from the head.

    :params:
    part - part to check
    pos - variable coordinate of the part
    snake - snake in the game

    :return:
    distance from the wall/head.
    """
    if part in snake.body:
        # Distance from head
        distance = snake.head.x - pos
        # How many body parts are left
        body_parts_left = snake.size - snake.body.index(part) - 1
        if distance <= body_parts_left: # If the snake will collide with its body
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
    distance = snake.head.x if direction == "horizontal" else snake.head.y
    for i in range(start, end, step):
        if direction == "horizontal":
            part = (i, snake.head.y)
        else:
            part = (snake.head.x, i)

        tmp = get_distance(distance, part, i, snake)
        if tmp != -1:
            distance = tmp
            break
    return distance