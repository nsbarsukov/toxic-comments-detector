import tensorflow as tf
from tensorflow.keras import layers
from navec import Navec
from typing import List

from dev import PAD_WORD
from wordEmbeddingsLayers import CustomVectorizerLayer


class NavecVectorizerLayer(layers.Layer):
    def __init__(self, pad_word=PAD_WORD, pad_sentence_to_n_words=30):
        super(NavecVectorizerLayer, self).__init__()
        self.navec_embeddings = Navec.load('wordEmbeddingsLayers/navec/navecWeights.tar')

        def vectorizer(word):
            try:
                return self.navec_embeddings[word]
            except:
                return self.navec_embeddings['<unk>']

        self.vectorizer = CustomVectorizerLayer(
            vectorizer=vectorizer,
            pad_sentence_to_n_words=pad_sentence_to_n_words,
            pad_word=pad_word
        )

    def call(self, texts_arr: List[str]) -> tf.Tensor:
        return self.vectorizer(texts_arr)
