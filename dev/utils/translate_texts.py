def make_en_rus_translator():
    """
    https://stackabuse.com/translating-strings-in-python-with-textblob/
    """
    from textblob import TextBlob
    from googletrans import Translator

    googletrans_translator = Translator()

    def translate(text):
        try:
            # first service attempt
            return str(TextBlob(text).translate(from_lang='en', to='ru'))
        except:
            pass

        # second service attempt
        googletrans_res = googletrans_translator.translate(text, src='en', dest='ru').text
        if googletrans_res == text:
            raise ValueError('googletrans is out of order!')
        return googletrans_res

    return translate
