import numpy as np


def get_3d_quartile_words_count(sentences_array):
    """
    Получает массив строк/предложений.
    Отдает число N.
    75% всех предложений данного массива не превышают N слов в длину.
    """

    def count_words(sentence):
        return len(sentence.split(' '))

    return int(round(
        np.percentile(
            list(map(count_words, sentences_array)),
            75
        )
    ))
