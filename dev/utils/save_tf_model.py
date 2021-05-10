import os
import tensorflow as tf

from ..constants.repo_paths import DIRECTORY_WITH_SAVED_MODELS


def save_tf_model(model: tf.keras.models.Model):
    if not os.path.exists(DIRECTORY_WITH_SAVED_MODELS):
        os.makedirs(DIRECTORY_WITH_SAVED_MODELS)

    model.save(f'{DIRECTORY_WITH_SAVED_MODELS}/{model.name}')
