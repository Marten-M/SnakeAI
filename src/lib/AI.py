"""AI class for snake game."""
import tensorflow as tf
from tensorflow import keras

# Get intellisense for Snake, Apple and Game class
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.classes.Snake import Snake
    from src.classes.Apple import Apple
    from src.lib.Game import Game


class AI:
    def __init__(self, game, create_new=False):
        """Initialize AI class."""
        self.game: Game = game
        if create_new:
            self.model = self.create_model()
            self.train_model()
        else:
            self.model = self.load_model()

    def load_model(self):
        """Load trained neural network model."""
        model = tf.keras.models.load_model('../../AIModel/trainedAI.h5')
        return model

    def get_move(self, state: dict):
        """
        Get the move the AI will make.

        params:
        state - a dictionary mapping keys "snake", "apple" and "direction" to the class instances of the snake and apple found in the game and the direction the snake is currently moving in

        :return:
        Direction in which the snake will move.
        """
        direction: str = state["direction"]
        snake: Snake = state["snake"]
        apple: Apple = state["apple"]

        # Decide which direction to move in
        # TODO

    def create_model(self):
        """
        Create model for AI.
        """
        model = tf.keras.Sequential()
        model.add(keras.layers.Input(shape=(8,))) # Input tensor
        model.add(keras.layers.Dense(units=16)) # Hidden layer 1
        model.add(keras.layers.Dense(units=4, activation='softmax')) # Output layer

        return model

    def train_model(self):
        """Train the AI to play Snake."""
        # TODO
        pass

    def new_game(self):
        """Create a new game."""
        # TODO
        pass