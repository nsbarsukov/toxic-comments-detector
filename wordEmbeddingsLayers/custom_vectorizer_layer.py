import tensorflow as tf
from tensorflow.keras import layers
from typing import List

from dev import pad_words_arr, PAD_WORD


def decode_byte_string_to_russian_text(string_tensor):
    try:
        return string_tensor[0].numpy().decode('utf-8')
    except:
        return ''

# def custom_standardization(texts_tensor):
#         result = tf.map_fn(fn=lambda x: preprocess_text(decode_byte_string_to_russian_text(x)), elems=texts_tensor)
#         return result

class CustomVectorizerLayer(layers.Layer):
    def __init__(self, vectorizer, pad_word=PAD_WORD, pad_sentence_to_n_words=30):
        super(CustomVectorizerLayer, self).__init__()
        self.vectorizer = vectorizer
        self.pad_word = pad_word
        self.pad_sentence_to_n_words = pad_sentence_to_n_words

    def call(self, texts_arr: List[str]) -> tf.Tensor:
        def sentence_to_embedding_arrs(sentence):
            words_arr = decode_byte_string_to_russian_text(sentence).split(' ')
            padded_word_arr = pad_words_arr(words_arr, maxlen=self.pad_sentence_to_n_words, pad_word=self.pad_word)

            return list(map(self.vectorizer, padded_word_arr))

        return tf.convert_to_tensor(
            list(map(sentence_to_embedding_arrs, texts_arr))
        )
