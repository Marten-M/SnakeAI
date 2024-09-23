"""AITrainer class file"""
import random
from collections import deque

import numpy as np

from src.lib.AI.actions import get_legal_actions, get_best_legal_action
from src.lib.AI.modelfunctions import load_model, create_model
from src.lib.AI.SnakeEnvironment import SnakeEnvironment


class AITRainer:
    def __init__(self, game, params, saved_weights_path: str = None):
        if saved_weights_path is not None:
            self.model = load_model(saved_weights_path)
        else:
            self.model = create_model()

        self.game = game
        self.env = SnakeEnvironment(self.game, params)
        self.env.play_state.update()

        self.gamma = 0.9  # How much impact future actions have. High as the future plays a significant role
        self.epsilon = 1  # How often to make random moves
        self.epsilon_decay = 0.9 # We learn pretty often so keep it fairly low
        self.min_epsilon_value = 0.08

        self.batch_size = 64

    def train_neural_network(self, iterations: int, save: bool = False, save_increment_generations: int = 0,
                             save_folder_path: str = ""):
        """
        Train neural network on specified number of games.
        """
        memory = deque(maxlen=self.batch_size * 4)

        for episode in range(iterations):
            state = self.env.reset().observation

            while not self.env.episode_ended:
                # TODO have a max number of steps so we don't ever get stuck in infinite loop
                Qs = self.model.predict(np.array([state]))[0]

                if np.random.rand() < self.epsilon:
                    # Don't accidentally pick an illegal action by taking a sample from action_space
                    legal_actions = get_legal_actions(state)
                    action = random.choice(legal_actions)
                else:
                    action = get_best_legal_action(Qs, state)
                print(Qs)
                step_result = self.env.step(action)
                new_state, reward = step_result.observation, step_result.reward

                memory.append([state, action, new_state, reward])
                if len(memory) > self.batch_size:
                    sample = random.sample(memory, self.batch_size)

                    x = np.array([e[0] for e in sample])
                    y = self.model.predict(x)
                    x2 = np.array([e[2] for e in sample])
                    Q2 = self.gamma * np.max(self.model.predict(x2), axis=1)

                    for idx, (s, a, n, r) in enumerate(sample):
                        y[idx][a] = r

                        if r > 0:  # If reward is negative then we lost
                            y[idx][a] += Q2[idx]
                    # TODO have a memory and take a random sample
                    self.model.fit(x, y, batch_size=self.batch_size, epochs=1, verbose=0)

                    # Decrease randomness every time we learn
                    self.epsilon = max(self.min_epsilon_value, self.epsilon * self.epsilon_decay)

                state = new_state


                self.env.play_state.update()  # Update screen



            if save and episode % save_increment_generations == 0:
                self.model.save_weights(f"{save_folder_path}/{episode}.weights.h5")
