import os
NAVEC_UNKNOWN_TOKEN = '<unk>'


def load_navec_embeddings():
    from navec import Navec

    try:
        return Navec.load(f'{os.path.dirname(__file__)}/navecWeights.tar')
    except:
        return Navec.load('wordEmbeddingsLayers/navec/navecWeights.tar')


def get_navec_word_vectorizer():
    navec_embeddings = load_navec_embeddings()
    NAVEC_EMBEDDING_DIMENSION = navec_embeddings.get(NAVEC_UNKNOWN_TOKEN).shape[0]

    def navec_word_vectorizer(word):
        try:
            return navec_embeddings[word]
        except:
            return navec_embeddings[NAVEC_UNKNOWN_TOKEN]

    return navec_word_vectorizer, NAVEC_EMBEDDING_DIMENSION


# class NavecVectorizerLayer(layers.Layer):
#     def __init__(self, pad_word=PAD_WORD, pad_sentence_to_n_words=30):
#         super(NavecVectorizerLayer, self).__init__()
#
#         self.vectorizer = CustomVectorizerLayer(
#             vectorizer=get_navec_word_vectorizer(),
#             pad_sentence_to_n_words=pad_sentence_to_n_words,
#             pad_word=pad_word
#         )
#
#     def call(self, texts_arr: List[str]) -> tf.Tensor:
#         return self.vectorizer(texts_arr)
