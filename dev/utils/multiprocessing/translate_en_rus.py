from dev import make_en_rus_translator


def translate_en_rus(text):
    translate = make_en_rus_translator()

    return translate(text)
