import numpy as np

from ..utils.pad_words_arr import pad_words_arr
from ..constants.aliases import PAD_WORD


def vectorize_sentence(sentence: str, vectorizer, pad_word=PAD_WORD, pad_sentence_to_n_words=30) -> np.array:
    words_arr = sentence.split(' ')
    padded_word_arr = pad_words_arr(words_arr, maxlen=pad_sentence_to_n_words, pad_word=pad_word)

    return np.array(list(map(vectorizer, padded_word_arr)))


def make_sentence_vectorizer(vectorizer, pad_word=PAD_WORD, pad_sentence_to_n_words=30):
    return lambda sentence: vectorize_sentence(sentence, vectorizer, pad_word, pad_sentence_to_n_words)
