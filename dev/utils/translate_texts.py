def find_in_array(array, cb):
    for item in array:
        if cb(item):
            return item

    return None


def make_en_rus_translator():
    from textblob import TextBlob

    return lambda text: str(TextBlob(text).translate(from_lang='en', to='ru'))

