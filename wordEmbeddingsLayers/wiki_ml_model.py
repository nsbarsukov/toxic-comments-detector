import tensorflow as tf
import tensorflow_text as tf_text # dont remove it: need for downloading from hub
import tensorflow_hub as hub

RUSSIAN = 'ru'
RUSSIAN_WORDS_EMBEDDING_HUB_MODEL = 'https://tfhub.dev/google/wiki40b-lm-{}/1'.format(RUSSIAN)

wiki40_russian_embedding_layer = hub.KerasLayer(
    handle=RUSSIAN_WORDS_EMBEDDING_HUB_MODEL,
    signature='word_embeddings', # модель умеет многое, но нас интересует только векторизация слов
    output_key='word_embeddings',
    dtype=tf.string,
    trainable=False, # Denotes whether we want to finetune model or not. We set it to True, the embeddings present in model are finetuned based on our downstream task
)
