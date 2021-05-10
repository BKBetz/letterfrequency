import tensorflow as tf
from tensorflow.keras import layers

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.Input(shape=(28, 28)),
        layers.Conv2D(kernel_size=(3, 3), filters=32, activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.Conv2D(kernel_size=(3, 3), filters=32, activation='relu'),
        layers.BatchNormalization(axis=-1),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(2)])

    return model