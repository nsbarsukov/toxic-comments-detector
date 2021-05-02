import tensorflow as tf
import tensorflow_text as tf_text # dont remove it: need for downloading from hub
import tensorflow_hub as hub


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
