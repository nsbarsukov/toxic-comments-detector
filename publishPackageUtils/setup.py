from os import path
from setuptools import setup, find_packages

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md')) as f:
  long_description = f.read()

setup(
  name = 'toxicity',
  version = '0.30',
  packages = find_packages(),
  license='MIT',
  description = 'Deep learning classifier of russian toxic comments',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Barsukov Nikita',
  author_email = 'nikita.s.barsukov@gmail.com',
  url = 'https://github.com/nsbarsukov/toxic-comments-detector',
  download_url = 'https://github.com/nsbarsukov/toxic-comments-detector/archive/refs/tags/0.1.tar.gz',
  keywords = ['toxic', 'comments', 'tensorflow', 'classifier'],
  install_requires=[
      'tensorflow',
      'numpy',
      'navec',
      'pymorphy2',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
  include_package_data=True,
)