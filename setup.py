from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='belarusianconverter',
  version='0.0.6',
  author='alelisicyna',
  author_email='alelisicyna@gmail.com',
  description='Library for convertation Belarusian texts from Cyrillic to other Belarusian alphabets',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/alelisicyna/BelarusianConverter',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)'
  ],
  keywords='files speedfiles spellings spelling Belarusian Belarus convert converter alphabets',
  project_urls={
    'GitHub': 'https://github.com/alelisicyna'
  },
  python_requires='>=3.6'
)