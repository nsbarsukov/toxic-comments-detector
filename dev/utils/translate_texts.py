def find_in_array(array, cb):
    for item in array:
        if cb(item):
            return item

    return None


def download_file_from_url(url, dest_path):
    import requests

    myfile = requests.get(url, allow_redirects=True)

    open(dest_path, 'wb').write(myfile.content)


def make_en_rus_argos_translator():
    from argostranslate import package, translate
    import os

    if not os.path.exists('en_rus.argosmodel'):
        download_file_from_url(
            'https://storage.googleapis.com/argospm/translate-en_ru-1_1.argosmodel',
            'en_rus.argosmodel'
        )
        package.install_from_path('en_rus.argosmodel')

    installed_languages = translate.get_installed_languages()

    russian = find_in_array(installed_languages, lambda lang: str(lang) == 'Russian')
    english = find_in_array(installed_languages, lambda lang: str(lang) == 'English')

    translation_en_rus = english.get_translation(russian)

    return lambda text: translation_en_rus.translate(text)


def make_en_rus_googletrans_translator():
    from googletrans import Translator

    googletrans_translator = Translator()

    def translate(text):
        googletrans_res = googletrans_translator.translate(text, src='en', dest='ru').text

        if googletrans_res == text:
            raise ValueError('googletrans is out of order!')
        return googletrans_res

    return translate


def make_en_rus_textblob_translator():
    """
    https://stackabuse.com/translating-strings-in-python-with-textblob/
    """
    from textblob import TextBlob

    return lambda text: str(TextBlob(text).translate(from_lang='en', to='ru'))


def make_en_rus_translator():
    googletrans_translator = make_en_rus_googletrans_translator()
    argos_translator = make_en_rus_argos_translator()
    textblob_translator = make_en_rus_textblob_translator()

    translators = [argos_translator, googletrans_translator, textblob_translator]

    def translate(text):
        return translators[0](text)

    return translate