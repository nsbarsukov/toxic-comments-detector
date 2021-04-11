# Russian text preprocessing
В данном директории собран весь код, относящий к предварительной предобработке русскоязычного текста.
Посмотреть принцип работы всех утилит можно в файле [sandbox.ipynb](./sandbox.ipynb).

## Lemmatization
Для лемматизации русских слов есть два основных инструмента: [**Pymorphy2**](https://github.com/kmike/pymorphy2) и [**MyStem**](https://yandex.ru/dev/mystem/).
В [данной статье](https://newtechaudit.ru/normalizaciya-slov/) сравнили качество и скорость их работы —
Pymorphy2 выиграл по показателям скорости работы и времени. Поэтому используем его.

## Используемая литература
- [Анализ инструментов для нормализации слов (2020)](https://newtechaudit.ru/normalizaciya-slov/)