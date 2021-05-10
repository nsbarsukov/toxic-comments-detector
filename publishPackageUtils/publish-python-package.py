import os

os.system('cd toxic-comments-detector && python setup.py sdist && twine upload dist/*')