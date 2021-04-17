import re
from .text_utils import lemmatize_word, remove_numbers, remove_extra_space, remove_punctuation

SPACE = ' '

def preprocess_text(text: str) -> str:
    """
    Принимает на вход текст/предложение (слова разделенные пробелом). Отдает обработанный вариант этого же текста.

    * Приведение всего к нижнему регистру
    * Убирает цифры
    * Убирает излишние пробелы (два и более пробела подряд)
    * Убирает пунктуацию
    * Каждое слово в этом предложение приводится к начальной форме (лемматизация)
    """
    def preprocess_whole_sentence(sentence):
        corrected_sentence = sentence.lower()
        corrected_sentence = remove_numbers(corrected_sentence)
        corrected_sentence = remove_punctuation(text=corrected_sentence, replace_by_string=SPACE)
        corrected_sentence = re.sub(r'\n', '', corrected_sentence)

        return remove_extra_space(corrected_sentence)

    preprocessed_text = preprocess_whole_sentence(text)

    def preprocess_word(word: str) -> str:
        return lemmatize_word(word)

    words = preprocessed_text.split(' ')

    return ' '.join([preprocess_word(word) for word in words])
