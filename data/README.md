# Размеченные данные на токсичность контента

## toxicRUCommentsOriginalDF.csv
Это оригинальный датасет (без примененных каких либо трансформаций) c Kaggle
[«Russian Language Toxic Comments»](https://www.kaggle.com/blackmoon/russian-language-toxic-comments).

## toxicRUCommentsCleanedDF.csv
Это датасет c Kaggle
[«Russian Language Toxic Comments»](https://www.kaggle.com/blackmoon/russian-language-toxic-comments),
к которому применены NLP-техники по очистке текста (смотри файл [clean_df_ru_texts.py](/dev/utils/multiprocessing/clean_df_ru_texts.py)).

## toxicENcommentsOriginalDF.csv
Это англоязычный датасет с Kaggle [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge).

## toxicRUCommentsTranslatedCleanedDF.csv
Это англоязычный датасет с Kaggle [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge),
над текстами которого сделали машинный перевод на русский язык с помощью библиотеки [TextBlob](https://github.com/sloria/TextBlob) и [googletrans](https://github.com/ssut/py-googletrans),
а после над переведенным вариантом текстов сделали чистку и нормализацию слов.
Весь описанный алгоритм представлен в файле [translate_clean_df_en_texts.py](dev/utils/multiprocessing/translate_clean_df_en_texts.py).