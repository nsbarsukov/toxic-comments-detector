import numpy as np
import fasttext.util

PATH_TO_FASTTEXT_WEIGHTS = 'wordEmbeddingsLayers/fastText/cc.ru.300.bin'

try:
    ft = fasttext.load_model(PATH_TO_FASTTEXT_WEIGHTS)
except:
    fasttext.util.download_model('ru', if_exists='ignore')
    ft = fasttext.load_model(PATH_TO_FASTTEXT_WEIGHTS)

FASTTEXT_EMBEDDING_DIMENSION = ft.get_dimension()


def fasttext_word_vectorizer(word: str):
    try:
        return ft.get_word_vector(word)
    except:
        return np.zeros(FASTTEXT_EMBEDDING_DIMENSION)
