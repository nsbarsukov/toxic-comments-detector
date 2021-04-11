import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def lemmatize_word(word: str) -> str:
    """Приводит русскоязычное слово к начальной форме"""
    try:
        p = morph.parse(word)[0] # содержит кучу различных вариантов инфинитивов

        return p.normal_form  # забираем инфинитив
    except:
        return word
