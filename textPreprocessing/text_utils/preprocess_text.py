from . import lemmatize_word, remove_numbers, remove_extra_space


def preprocess_text(text: str) -> str:
    """
    Принимает на вход текст/предложение (слова разделенные пробелом). Отдает обработанный вариант этого же текста.

    * Каждое слово в этом предложение приводится к начальной форме
    * Убираются цифры
    * Убирает излишние пробелы (два и более пробела подряд)
    """
    def preprocess_whole_sentence(sentence):
        new_sentence = remove_numbers(sentence)

        return remove_extra_space(new_sentence)

    preprocessed_text = preprocess_whole_sentence(text)

    def preprocess_word(word: str) -> str:
        return lemmatize_word(word)

    words = preprocessed_text.split(' ')

    # TODO: закончить утилиту
    return ' '.join([preprocess_word(word) for word in words])
