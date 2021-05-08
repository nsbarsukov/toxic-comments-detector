# Word Embeddings Layers
Варианты получения векторных представлений слов/предложений (word/sentence embeddings).<br>
На вход подается tensor из строк и возвращает тензор с числами, которые уже можно дальше
"скормить" внутрь нейронной сети.

## wiki_lm
Collection of wiki40b-lm language models trained on Wiki40B dataset in different languages.<br>
Для текущий задачи был взят именно русскоязычный вариант.

Модель берется с [tensorflow hub](https://tfhub.dev/google/collections/wiki40b-lm/1).

Описана в [статье](https://research.google/pubs/pub49029/):
> Mandy Guo, Zihang Dao, Denny Vrandecic, Rami Al-Rfou. Wiki-40B: Multilingual Language Model Dataset. To appear, LREC, May 2020.

## Navec
Navec is a library of pretrained word embeddings for Russian language.
It shows competitive or better results than RusVectores, loads ~10 times faster (~1 sec), takes ~10 times less space (~50 MB).

Модель внедряется через библиотеку [navec](https://github.com/natasha/navec#installation) с подгрузкой [весов](https://github.com/natasha/navec#downloads).

Описана в [статье](https://natasha.github.io/navec/).

## Universal Sentence Encoder (multilingual)
16 languages (Arabic, Chinese-simplified, Chinese-traditional, English, French, German, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Spanish, Thai, Turkish, **Russian**) text encoder.

Модель берется с [tensorflow hub](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3).
> Yinfei Yang, Daniel Cer, Amin Ahmad, Mandy Guo, Jax Law, Noah Constant, Gustavo Hernandez Abrego , Steve Yuan, Chris Tar, Yun-hsuan Sung, Ray Kurzweil. Multilingual Universal Sentence Encoder for Semantic Retrieval. July 2019

## FastText
Русскоязычный вариант модели берется с [официального сайта модели FastText](https://fasttext.cc/docs/en/crawl-vectors.html).