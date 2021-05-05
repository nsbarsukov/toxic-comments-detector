import time
from dev import make_en_rus_translator

translate = make_en_rus_translator()


def translate_en_rus(text):
    try:
        return translate(text)
    except:
        time.sleep(1)
        translate_en_rus(text)
