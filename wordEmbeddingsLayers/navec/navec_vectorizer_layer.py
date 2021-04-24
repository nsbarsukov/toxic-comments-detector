import tensorflow as tf
from tensorflow.keras import layers
from navec import Navec
from typing import List

from dev import PAD_WORD
from wordEmbeddingsLayers import CustomVectorizerLayer


navec_embeddings = Navec.load('wordEmbeddingsLayers/navec/navecWeights.tar')

NAVEC_UNKNOWN_TOKEN = '<unk>'
NAVEC_EMBEDDING_DIMENSION = navec_embeddings.get(NAVEC_UNKNOWN_TOKEN).shape[0]


def navec_word_vectorizer(word):
    try:
        return navec_embeddings[word]
    except:
        return navec_embeddings[NAVEC_UNKNOWN_TOKEN]


class NavecVectorizerLayer(layers.Layer):
    def __init__(self, pad_word=PAD_WORD, pad_sentence_to_n_words=30):
        super(NavecVectorizerLayer, self).__init__()

        self.vectorizer = CustomVectorizerLayer(
            vectorizer=navec_word_vectorizer,
            pad_sentence_to_n_words=pad_sentence_to_n_words,
            pad_word=pad_word
        )

    def call(self, texts_arr: List[str]) -> tf.Tensor:
        return self.vectorizer(texts_arr)
