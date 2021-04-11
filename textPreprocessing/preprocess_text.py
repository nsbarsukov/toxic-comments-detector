from text_utils import lemmatize_word, remove_numbers


def preprocess_text(text: str) -> str:
    """
    Принимает на вход текст/предложение (слова разделенные пробелом). Отдает обработанный вариант этого же текста.

    * Каждое слово в этом предложение приводится к начальной форме
    * Убираются цифры
    """
    preprocessed_text = remove_numbers(text)

    def preprocess_word(word: str) -> str:
        return lemmatize_word(word)

    words = preprocessed_text.split(' ')

    # TODO: закончить утилиту
    return ' '.join([preprocess_word(word) for word in words])
