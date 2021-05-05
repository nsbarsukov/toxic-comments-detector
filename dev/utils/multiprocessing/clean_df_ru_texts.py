import multiprocessing
import pandas as pd
from tqdm import tqdm

from textPreprocessing import preprocess_text
from dev import DIRECTORY_WITH_DATA, ORIGINAL_RUSSIAN_DF_NAME, CLEANED_RUSSIAN_DF_NAME

if __name__ == "__main__":
    """
    Запускает очистку текста комментариев внутри датасета {DIRECTORY_WITH_DATA}/{ORIGINAL_RUSSIAN_DF_NAME},
    применяя к каждой комментарию функцию from textPreprocessing import preprocess_text
    """
    STREAMS_COUNT = multiprocessing.cpu_count()
    print('Запущен скрипт в', STREAMS_COUNT, 'потоков')

    orig_toxic_comments_df = pd.read_csv(f"../../../{DIRECTORY_WITH_DATA}/{ORIGINAL_RUSSIAN_DF_NAME}")

    pool = multiprocessing.Pool(STREAMS_COUNT)

    orig_toxic_comments_df['norm_comment'] = tqdm(
        pool.imap(preprocess_text, orig_toxic_comments_df['comment']),
        total=len(orig_toxic_comments_df)
    )

    orig_toxic_comments_df.to_csv(f"../../{DIRECTORY_WITH_DATA}/{CLEANED_RUSSIAN_DF_NAME}", index=False)

    pool.close()
    pool.join()
