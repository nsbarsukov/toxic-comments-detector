# Russian text preprocessing
В данном документе демонстрируется принцип работы утилит для обработки текста,
которыми обрабатываются текста перед их дальнейшим использованием в построении моделей машинного обучения.
<br>
<br>

## Утилита preprocess_text
Вся предобратка текста полученных утилит собрана в одной функции [preprocess_text](./preprocess_text.py):
принимает на вход строку (может содержать несколько слов, разделенных пробелом) и возращает обработанный вариант этой же строки.

```python
from textPreprocessing import preprocess_text

preprocess_text('Дети бежали скорее со ШКОЛЫ в 6 вечера.')
```
> ребёнок бежать скорее с школа в вечер

<br>
<br>

## Состав утилиты preprocess_text
Эта утилита включает в себе обработку следующих функций:
### lemmatize_word
Лемматизация слова (приведение его к начальной форме).

Для лемматизации русских слов есть два основных инструмента: [**Pymorphy2**](https://github.com/kmike/pymorphy2) и [**MyStem**](https://yandex.ru/dev/mystem/).
В [данной статье](https://newtechaudit.ru/normalizaciya-slov/) сравнили качество и скорость их работы —
Pymorphy2 выиграл по показателям скорости работы и времени. Поэтому используем его.
```python
from text_utils import lemmatize_word 

words = ['бежала', 'пятого', 'любимая', 'дети']

for not_initial_form_word in words:
    print(not_initial_form_word, '===>', lemmatize_word(not_initial_form_word))
```
> бежала ===> бежать <br>
> пятого ===> пятый <br>
> любимая ===> любимый <br>
> дети ===> ребёнок <br>

---
### remove_punctuation
```python
from text_utils import remove_punctuation

remove_punctuation('string.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ With. Punctuation?')
```
> string With Punctuation

---
### remove_numbers
```python
from text_utils import remove_numbers

remove_numbers('Дети бежали скорее со школы в 6 вечера')
```
> Дети бежали скорее со школы в  вечера

---
### remove_redundant_whitespace_chars
```python
from text_utils import remove_redundant_whitespace_chars

remove_redundant_whitespace_chars('   Тут  сейчас 2 места с лишними       \n       пробелами\n')
```
> Тут сейчас 2 места с лишними пробелами

<br>
<br>

## Используемая литература
- [Анализ инструментов для нормализации слов (2020)](https://newtechaudit.ru/normalizaciya-slov/)