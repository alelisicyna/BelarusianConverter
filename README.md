# BelarusianConverter
Library for convertation Belarusian texts from Cyrillic to other Belarusian alphabets
## Quick Start
```py
$ pip install belarusianconverter
```
## Code Example
```py
# test.py
from BelarusianConverter import BelarusianConverter



if __name__ == '__main__':
  text = BelarusianConverter().convert(0, 'А хто там ідзе?') # example
  print(text) # Return: "A chto tam idzie?"

'''
  BelarusianConverter().convert(alphabet: int, text: str, plosive_g: bool, assimilation: bool, iotation: bool)
  alphabet:
    0 - LatinMuzyckajaPrauda (K. Kalinoŭski)
    1 - Latin1929 (B. Taraškievič)
    2 - Latin1962 (Ja. Stankievič)
    3 - LatinUnitedNations
    4 - Romanization2023
    5 - Arabic (Belarusian Tatars)
  plosive_g:
    True: H -> G in some words
    False: keep the original text
  assimilation:
    True: add a soft assimilation
    False: keep the original text
  iotation:
    True: I -> Ji/J after vowels
    False: keep the original text
'''

```    

## Links
About Belarusian Latin: [Wikipedia](https://en.wikipedia.org/wiki/Belarusian_Latin_alphabet)      
About Belarusian Arabic: [Wikipedia](https://en.wikipedia.org/wiki/Belarusian_Arabic_alphabet)
