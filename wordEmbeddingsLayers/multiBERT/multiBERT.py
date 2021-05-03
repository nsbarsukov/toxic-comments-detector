import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_text as tf_text # dont remove it: need for downloading from hub
import tensorflow_hub as hub
from typing import List


multiBERT_PREPROCESS_HUB_MODEL = 'https://tfhub.dev/tensorflow/bert_multi_cased_preprocess/3'
multiBERT_ENCODER_HUB_MODEL = 'https://tfhub.dev/tensorflow/bert_multi_cased_L-12_H-768_A-12/4'


def create_multiBERT_preprocess_layer():
    return hub.KerasLayer(multiBERT_PREPROCESS_HUB_MODEL)


def create_multiBERT_encoder_layer():
    return hub.KerasLayer(
        multiBERT_ENCODER_HUB_MODEL,
        input_shape=[],
        dtype=tf.string,
        trainable=True,
    )


class BERTLayer(layers.Layer):
    def __init__(self, to_sequence=True):
        super(BERTLayer, self).__init__()
        self.to_sequence = to_sequence
        self.preprocessor = create_multiBERT_preprocess_layer()
        self.encoder = create_multiBERT_encoder_layer()

    def call(self, texts_arr: List[str]) -> tf.Tensor:
        preprocessed_texts = self.preprocessor(texts_arr)
        encoded_output = self.encoder(preprocessed_texts)

        return encoded_output['sequence_output'] if self.to_sequence else encoded_output['pooled_output']

