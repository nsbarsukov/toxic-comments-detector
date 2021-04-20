import tensorflow as tf
from tensorflow.keras import layers
from typing import List

from dev import pad_words_arr, PAD_WORD


class CustomVectorizerLayer(layers.Layer):
    def __init__(self, vectorizer, pad_word=PAD_WORD, pad_sentence_to_n_words=30):
        super(CustomVectorizerLayer, self).__init__()
        self.vectorizer = vectorizer
        self.pad_word = pad_word
        self.pad_sentence_to_n_words = pad_sentence_to_n_words

    def call(self, texts_arr: List[str]) -> tf.Tensor:
        def sentence_to_embedding_arrs(sentence):
            words_arr = sentence.split(' ')
            padded_word_arr = pad_words_arr(words_arr, maxlen=self.pad_sentence_to_n_words, pad_word=self.pad_word)

            return list(map(self.vectorizer, padded_word_arr))

        return tf.convert_to_tensor(
            list(map(sentence_to_embedding_arrs, texts_arr))
        )
