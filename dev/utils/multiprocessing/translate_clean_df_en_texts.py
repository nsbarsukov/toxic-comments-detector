import multiprocessing
import pandas as pd
from tqdm import tqdm

from textPreprocessing import preprocess_text
from dev import DIRECTORY_WITH_DATA, ORIGINAL_ENGLISH_DF_NAME, TRANSLATED_CLEANED_ENGLISH_DF_NAME
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
    STREAMS_COUNT = min(multiprocessing.cpu_count(), 5)
    print('Запущен скрипт в', STREAMS_COUNT, 'потоков')

    orig_en_toxic_comments_df = pd.read_csv(f"../../../{DIRECTORY_WITH_DATA}/{ORIGINAL_ENGLISH_DF_NAME}").loc[:100, :]

    pool = multiprocessing.Pool(STREAMS_COUNT)

    orig_en_toxic_comments_df['translated_cleaned_comment'] = tqdm(
        pool.imap(translate_clean, orig_en_toxic_comments_df['comment_text']),
        total=len(orig_en_toxic_comments_df)
    )

    TOXIC_CATEGORY_COLUMNS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    orig_en_toxic_comments_df['is_toxic'] = orig_en_toxic_comments_df[TOXIC_CATEGORY_COLUMNS].any(axis='columns') * 1
    orig_en_toxic_comments_df = orig_en_toxic_comments_df.drop(columns=[*TOXIC_CATEGORY_COLUMNS, 'id', 'comment_text'])

    orig_en_toxic_comments_df.to_csv(f"../../../{DIRECTORY_WITH_DATA}/{TRANSLATED_CLEANED_ENGLISH_DF_NAME}", index=False)

    pool.close()
    pool.join()
