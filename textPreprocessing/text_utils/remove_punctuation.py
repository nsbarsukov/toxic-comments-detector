import re
import string


def remove_punctuation(text: str, replace_by_string: str = '') -> str:
    punctuation_pattern = f"[{re.escape(string.punctuation)}]"

    return re.sub(punctuation_pattern, replace_by_string, text)
