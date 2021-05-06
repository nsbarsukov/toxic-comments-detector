import multiprocessing
import pandas as pd
from tqdm import tqdm

from textPreprocessing import preprocess_text
from dev import (
    DIRECTORY_WITH_DATA,
    ORIGINAL_ENGLISH_DF_NAME,
    TRANSLATED_CLEANED_ENGLISH_DF_NAME,
    TRANSLATED_CLEANED_TEXTS_COLUMN,
    ORIGINAL_ENGLISH_TEXTS_COLUMN,
    ENGLISH_TEXTS_TOXIC_LABEL_COLUMN
)
from dev.utils.multiprocessing.translate_en_rus import translate_en_rus


def translate_clean(text):
    return preprocess_text(translate_en_rus(text))


if __name__ == "__main__":
    """
    Запускает перевод текста комментариев внутри датасета {DIRECTORY_WITH_DATA}/{ORIGINAL_ENGLISH_DF_NAME}
    с английского языка на русский,
    а также применяет к каждой комментарию функцию from textPreprocessing import preprocess_text
    (чистка и нормализация русского текста)
    """
    TOXIC_CATEGORY_COLUMNS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    orig_en_toxic_comments_df = pd.read_csv(f"../../../{DIRECTORY_WITH_DATA}/{ORIGINAL_ENGLISH_DF_NAME}")

    # create new dependent variable
    orig_en_toxic_comments_df[ENGLISH_TEXTS_TOXIC_LABEL_COLUMN] = orig_en_toxic_comments_df[TOXIC_CATEGORY_COLUMNS].any(axis='columns') * 1
    orig_en_toxic_comments_df = orig_en_toxic_comments_df.drop(columns=TOXIC_CATEGORY_COLUMNS)

    # slice certain category
    def slice_certain_label_df_part(origin_df, label):
        filtered_by_label_df = origin_df[origin_df[ENGLISH_TEXTS_TOXIC_LABEL_COLUMN] == label].reset_index(drop=True)
        return filtered_by_label_df.loc[1:5000, :]

    toxic_comments_df = slice_certain_label_df_part(orig_en_toxic_comments_df, 1)
    non_toxic_comments_df = slice_certain_label_df_part(orig_en_toxic_comments_df, 0)
    sliced_df = pd.concat([toxic_comments_df, non_toxic_comments_df]).sample(frac=1)

    STREAMS_COUNT = min(multiprocessing.cpu_count(), 5)
    print('Запущен скрипт в', STREAMS_COUNT, 'потоков')
    pool = multiprocessing.Pool(STREAMS_COUNT)

    sliced_df[TRANSLATED_CLEANED_TEXTS_COLUMN] = tqdm(
        pool.imap(translate_clean, sliced_df[ORIGINAL_ENGLISH_TEXTS_COLUMN]),
        total=len(sliced_df)
    )

    sliced_df = sliced_df.drop(columns=[ORIGINAL_ENGLISH_TEXTS_COLUMN])

    sliced_df.to_csv(
        f"../../../{DIRECTORY_WITH_DATA}/{TRANSLATED_CLEANED_ENGLISH_DF_NAME}",
        index=False
    )

    pool.close()
    pool.join()
