import re
import string


def remove_punctuation(text: str) -> str:
    punctuation_pattern = f"[{re.escape(string.punctuation)}]"

    return re.sub(punctuation_pattern, '', text)
