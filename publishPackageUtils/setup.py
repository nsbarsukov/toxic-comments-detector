from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
  long_description = readme.read()

setup(
  name = 'toxicity',
  version = '0.25',
  packages = find_packages(),
  license='MIT',
  description = 'Deep learning classifier of russian toxic comments',
  # long_description = long_description,
  author = 'Barsukov Nikita',
  author_email = 'nikita.s.barsukov@gmail.com',
  url = 'https://github.com/nsbarsukov/toxic-comments-detector',
  download_url = 'https://github.com/nsbarsukov/toxic-comments-detector/archive/refs/tags/0.1.tar.gz',
  keywords = ['toxic', 'comments', 'tensorflow', 'classifier'],
  install_requires=[
      'tensorflow',
      'numpy',
      'navec'
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