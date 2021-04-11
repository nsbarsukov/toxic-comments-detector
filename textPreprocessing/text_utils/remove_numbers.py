import re


def remove_numbers(text: str) -> str:
    pattern = r'[0-9]'

    return re.sub(pattern, '', text)

