import numpy as np

PATH_TO_FASTTEXT_WEIGHTS = 'wordEmbeddingsLayers/fastText/cc.ru.300.bin'


def load_russian_fasttext_model():
    import fasttext.util

    try:
        ft = fasttext.load_model(PATH_TO_FASTTEXT_WEIGHTS)
    except:
        fasttext.util.download_model('ru', if_exists='ignore')
        ft = fasttext.load_model(PATH_TO_FASTTEXT_WEIGHTS)

    return ft


def get_russian_fasttext_word_vectorizer():
    ft = load_russian_fasttext_model()

    FASTTEXT_EMBEDDING_DIMENSION = ft.get_dimension()

    def fasttext_word_vectorizer(word: str):
        try:
            return ft.get_word_vector(word)
        except:
            return np.zeros(FASTTEXT_EMBEDDING_DIMENSION)

    return fasttext_word_vectorizer, FASTTEXT_EMBEDDING_DIMENSION
