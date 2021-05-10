import tensorflow as tf
import numpy as np
from textPreprocessing import preprocess_text
from navec_vectorizer_layer import get_navec_word_vectorizer
from dev import make_sentence_vectorizer


class ToxicCommentsDetector:
    def __init__(self):
        self.model = tf.keras.models.load_model('weightedCNN_NavecWordEmbeddings')
        self.sentenceVectorizer = make_sentence_vectorizer(
            vectorizer=get_navec_word_vectorizer()[0],
            pad_sentence_to_n_words=31
        )

    def predict(self, raw_texts):
        preprocessed_texts = np.array(
            list(map(lambda text: self.sentenceVectorizer(preprocess_text(text)), raw_texts))
        )

        return self.model.predict(preprocessed_texts)


test_raw_texts = ['ты чего берега попутал?', 'это правый берег реки, не путай с левым']

toxicDetector = ToxicCommentsDetector()
print(toxicDetector.predict(test_raw_texts))