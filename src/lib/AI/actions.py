import numpy as np


def get_legal_actions(env_state) -> list:
    opposites = {0: 2, 1: 3, 2: 0, 3: 1}  # 0 is North, 1 is East, 2 is South and 3 is West

    moving_direction = list(env_state).index(1)  # Moving direction is the 1st value that is 0
    # Get only actions that don't force the snake to move back the direction it came from
    legal_actions = [action for action in opposites if action != opposites[moving_direction]]

    return legal_actions


def get_best_legal_action(Qs, env_state) -> int:
    legal_actions = get_legal_actions(env_state)

    sorted_idx = np.argsort(Qs)
    if sorted_idx[-1] in legal_actions:  # The action with the biggest value is the last element in argsort
        return sorted_idx[-1]
    else:
        return sorted_idx[-2]  # Second-largest element if first not legal
