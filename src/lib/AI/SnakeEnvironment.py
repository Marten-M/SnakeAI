"""Python environment to help train neural network with."""
from tf_agents.environments import py_environment, utils
from tf_agents.specs import array_spec
import numpy as np
from tf_agents.trajectories import time_step as ts
from tf_agents.typing import types

from src.lib.AI.AI_training_playstate import AIPlayState


class SnakeEnvironment(py_environment.PyEnvironment):
    def __init__(self, game, params):
        # 4 possible actions
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int64, minimum=0, maximum=3, name="action"
        )

        self._observation_spec = array_spec.BoundedArraySpec(
            shape=tuple((1 for _ in range(13))), dtype=np.int32, name="observation"
        )
        self.episode_ended = False

        self._cur_state = []
        self.play_state: AIPlayState = None

        self.game = game
        self.params = params

        self.create_new_play_state()

    def action_spec(self) -> types.NestedArraySpec:
        return self._action_spec

    def observation_spec(self) -> types.NestedArraySpec:
        return self._observation_spec

    def _reset(self) -> ts.TimeStep:
        self.create_new_play_state()
        self.episode_ended = False
        return ts.restart(np.array(self._cur_state, dtype=np.int32))

    def _step(self, action):
        if self.episode_ended:
            return self.reset()
        if self.play_state.game_ended:
            self.episode_ended = True

        if self.play_state.take_step(action):
            # game ended
            self.episode_ended = True

        self._cur_state = self.play_state.get_state()
        reward = self.play_state.evaluate_state()
        if self.episode_ended or self.play_state.game_ended:
            return ts.termination(np.array(self._cur_state, dtype=np.int32), reward)
        else:
            return ts.transition(np.array(self._cur_state, dtype=np.int32), reward=reward, discount=0.95)

    def create_new_play_state(self):
        """Creates a new snake game for AI to play."""
        self.play_state = AIPlayState(self.game, self.params)
        self._cur_state = self.play_state.get_state()
