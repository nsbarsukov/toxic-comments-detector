import numpy as np


def get_class_weights(pos_count, neg_count):
    """
    For binary classification
    https://www.tensorflow.org/tutorials/structured_data/imbalanced_data#calculate_class_weights
    """
    total = pos_count + neg_count

    return {
        0: (1 / neg_count) * total / 2.0,
        1: (1 / pos_count) * total / 2.0
    }


def get_initial_output_bias(pos_count, neg_count):
    """
    For binary classification
    https://www.tensorflow.org/tutorials/structured_data/imbalanced_data#optional_set_the_correct_initial_bias
    """
    return np.log([pos_count/neg_count])