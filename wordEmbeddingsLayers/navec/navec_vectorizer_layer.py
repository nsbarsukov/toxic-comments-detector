from navec import Navec

from dev import PAD_WORD
from wordEmbeddingsLayers import CustomVectorizerLayer

navec_embeddings = Navec.load('navecWeights.tar')


def navec_vectorizer(word):
    return navec_embeddings[word]


navec_vectorizer_layer = CustomVectorizerLayer(navec_vectorizer, pad_sentence_to_n_words=3, pad_word=PAD_WORD)

