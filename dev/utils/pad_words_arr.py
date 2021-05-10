from ..constants.aliases import PAD_WORD


def pad_words_arr(words_arr, maxlen=3, pad_word=PAD_WORD):
    """
    Приводит массив слов к нужной длине

    :param words_arr: массив слов
    :param maxlen: какой длины должен стать массив
    :param pad_word: какое слово добавлять в массив, если длина массива < maxlen
    :return: массив слов длины maxlen
    """
    if len(words_arr) > maxlen:
        return words_arr[:maxlen]
    elif len(words_arr) < maxlen:
        padded_words_arr = [pad_word] * (maxlen - len(words_arr))

        return [*words_arr, *padded_words_arr]

    return words_arr
