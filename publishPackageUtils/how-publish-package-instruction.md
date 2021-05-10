## Python package release
Публикация происходит согласно данному [tutorial](https://realpython.com/pypi-publish-python-package/).

0. Установи нужные пакеты
```shell
pip3 install twine
```
1. Находясь в корне проект исполни
```shell
python publishPackageUtils/prepare-python-package.py
```
2. Увеличь версию пакета в `toxic-comments-detector/setup.py`
3. (Опциональный шаг) First, go to github.com and navigate to your repository.
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