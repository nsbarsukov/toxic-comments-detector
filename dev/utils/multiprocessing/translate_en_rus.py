import time
from random import randint
from dev import make_en_rus_translator

translate = make_en_rus_translator()


def translate_en_rus(text):
    try:
        return translate(text)
    except:
        time.sleep(randint(5, 30))
        return translate_en_rus(text)
