import re

SPACE = ' '


def remove_redundant_whitespace_chars(text: str) -> str:
    """
    Чистим пробельные символы

    * Заменяет все пробельные символы (например, табуляцию или перенос строки) на пробел
    * Убирает излишние пробелы (два и более пробела подряд)
    * Удаляет пробел в конце/начале строки
    """
    without_whitespace_characters = re.sub(r'\s', SPACE, text)

    return re.sub('\s\s+', SPACE, without_whitespace_characters).strip()
