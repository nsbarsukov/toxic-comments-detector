from .text_utils import lemmatize_word, remove_numbers, remove_redundant_whitespace_chars, remove_punctuation

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

        return remove_redundant_whitespace_chars(corrected_sentence)

    preprocessed_text = preprocess_whole_sentence(text)

    def preprocess_word(word: str) -> str:
        return lemmatize_word(word)

    words = preprocessed_text.split(' ')

    return ' '.join([preprocess_word(word) for word in words])
