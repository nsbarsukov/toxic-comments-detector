from distutils.core import setup
setup(
  name = 'toxic-comments-detector',
  packages = ['toxic-comments-detector'],
  version = '0.2',
  license='MIT',
  description = 'Deep learning classifier of russian toxic comments',
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
)