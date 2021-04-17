# Word Embeddings Layers
Варианты получения векторных представлений слов (word embeddings).
На вход подается tensor из строк и возвращает тензор с числами, которые уже можно дальше
"скормить" внутрь нейронной сети.

## wiki40b-lm
Collection of wiki40b-lm language models trained on Wiki40B dataset in different languages.
Для текущий задачи был взят именно русскоязычный вариант.

Модель берется с [tensorflow hub](https://tfhub.dev/google/collections/wiki40b-lm/1).

Описана в [статье](https://research.google/pubs/pub49029/):
> Mandy Guo, Zihang Dao, Denny Vrandecic, Rami Al-Rfou. Wiki-40B: Multilingual Language Model Dataset. To appear, LREC, May 2020.