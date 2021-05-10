import os

os.system('cd tempPublishFolder && python setup.py sdist bdist_wheel && twine upload dist/*')
