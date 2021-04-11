import re


def remove_extra_space(text: str) -> str:
    """Убирает излишние пробелы (два и более пробела подряд)"""
    return re.sub('\s\s+', " ", text)
