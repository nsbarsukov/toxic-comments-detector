import os

os.system('cd tempPublishFolder && python setup.py sdist && twine upload dist/*')
