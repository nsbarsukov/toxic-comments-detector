import re

SPACE = ' '


def remove_extra_whitespace_characters(text: str) -> str:
    """
    Чистим пробельные символы

    * Заменяет все пробельные символы (например, табуляцию или перенос строки) на пробел
    * Убирает излишние пробелы (два и более пробела подряд)
    """
    withoutWhitespaceCharacters = re.sub(r'\s', SPACE, text)

    return re.sub('\s\s+', SPACE, withoutWhitespaceCharacters)
