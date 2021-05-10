# toxic-comments-detector

## Структура проекта
```
├── data # Используемые данные
│
├── dev # Набор констант и утилит для разработки
│   ├── constants
|   └── utils
│
├── models # различные модели для решения главной задачи классификации  
│    
├── textPreprocessing # набор утилит для предобработки русскоязычных текстов
│   ├── text_utils # набор маленьких утилит по очистке текста
│   └── preprocess_text.py # собирает все утилиты из text_utils в одну функцию
│
└── wordEmbeddingsLayers # различные способы векторизации слов
```

## Навигация по проекту
- [Используемые данные](/data)
- [Предварительная очистка текстовых данных](/textPreprocessing)<br>
Как обрабатывались сырые текстовые данные перед их дальнейшим использованием в построении моделей машинного обучения.
- [Какие способы векторизации слов применялись](/wordEmbeddingsLayers)
- [Какие модели ML были опробованы для решения поставленной главной задачи классификации](/models)


## Python package release
Публикация происходит согласно данному [tutorial](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

0. Установи нужные пакеты
```shell
pip3 install twine
```
1. Находясь в корне проект исполни
```shell
python prepare-python-package.py
```
2. Увеличь версию пакета в `toxic-comments-detector/setup.py`
3. First, go to github.com and navigate to your repository.
   Next, click on the tab “releases” and then on “Create a new release”.
   Now, define a Tag verion (it is best to use the same number as you used in your setup.py version-field: v_01.
   Add a release title and a description (not that important), then click on “publish release”.
   Now you see a new release and under Assets, there is a link to Source Code (tar.gz).
   Right-click on this link and chose Copy Link Address.
   Paste this link-address into the download_url field in the setup.py file.
4. Находясь в корне репозитория
```shell
python publishPackageUtils/publish-python-package.py
```