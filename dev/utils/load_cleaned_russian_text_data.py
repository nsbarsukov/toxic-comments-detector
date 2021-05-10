import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from ..constants.default_hyperparameters import SEED
from ..constants.repo_paths import (
    DIRECTORY_WITH_DATA,
    CLEANED_RUSSIAN_DF_NAME,
    TRANSLATED_CLEANED_ENGLISH_DF_NAME,
)
from ..constants.aliases import ENGLISH_TEXTS_TOXIC_LABEL_COLUMN


def load_cleaned_russian_text_data():
    cleaned_toxic_comments_df = pd.read_csv(f"{DIRECTORY_WITH_DATA}/{CLEANED_RUSSIAN_DF_NAME}", )

    df = cleaned_toxic_comments_df.copy()
    df = df.drop(columns=['comment'])
    df = df.astype({'toxic': 'int64'})

    y = df.pop('toxic')
    X = np.array(df)

    return train_test_split(X, y, test_size=0.2, random_state=SEED)


def load_translated_from_english_cleaned_russian_text_data():
    translated_cleaned_toxic_comments_df = pd.read_csv(f"{DIRECTORY_WITH_DATA}/{TRANSLATED_CLEANED_ENGLISH_DF_NAME}")

    df = translated_cleaned_toxic_comments_df.copy().dropna()
    df = df.drop(columns=['id'])
    df = df.astype({ENGLISH_TEXTS_TOXIC_LABEL_COLUMN: 'int64'})

    y = df.pop(ENGLISH_TEXTS_TOXIC_LABEL_COLUMN)
    X = np.array(df)

    return X, y
