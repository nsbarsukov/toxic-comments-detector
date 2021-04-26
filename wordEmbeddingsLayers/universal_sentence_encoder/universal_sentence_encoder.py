import tensorflow as tf
import tensorflow_text as tf_text # dont remove it: need for downloading from hub
import tensorflow_hub as hub

# universal-sentence-encoder-multilingual
USE_HUB_MODEL = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'
USE_SENTENCE_EMBEDDING_DIMENSION = 512

universal_sentence_encoder_layer = hub.KerasLayer(
    handle=USE_HUB_MODEL,
    input_shape=[],
    dtype=tf.string,
    trainable=True,
)