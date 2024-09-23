"""Helper functions for handling the tensorflow neural network model."""
import tensorflow as tf
from tensorflow import keras


def create_model():
    """
    Create model for AI.
    """
    model = tf.keras.Sequential()
    model.add(keras.layers.Input(shape=(13,)))  # Input tensor
    model.add(keras.layers.Dense(units=64, activation="relu"))  # Hidden layer 1
    model.add(keras.layers.Dense(units=64, activation="relu"))  # Hidden layer 1
    model.add(keras.layers.Dense(units=4))  # Output layer
    model.compile(loss="mse", optimizer=tf.keras.optimizers.legacy.Adam())

    return model


def load_model(path):
    """Load trained neural network model."""
    model = create_model()
    model.load_weights(path)

    return model
