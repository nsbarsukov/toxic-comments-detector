def find_in_array(array, cb):
    for item in array:
        if cb(item):
            return item

    return None


def make_en_rus_translator():
    from argostranslate import package, translate
    # package.install_from_path('dev/utils/en_rus.argosmodel')
    installed_languages = translate.get_installed_languages()

    russian = find_in_array(installed_languages, lambda lang: str(lang) == 'Russian')
    english = find_in_array(installed_languages, lambda lang: str(lang) == 'English')

    translation_en_rus = english.get_translation(russian)

    return lambda text: translation_en_rus.translate(text)

