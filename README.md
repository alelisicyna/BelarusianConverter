# BelarusianConverter
Script who convert some Belarusian texts from Cyrillic to other Belarusian alphabets       
Programming Language: Python 3
## How to use it?
1. Download the repository
2. Add the directory to your project
3. Code example:
```py
# test.py
from BelarusianConverter.BelarusianConverter import BelarusianConverter



if __name__ == '__main__':
  BelarusianConverter = BelarusianConverter()
  text = BelarusianConverter.convert(0, True, True, 'А хто там ідзе?') # example
  print(text) # Return: "A chto tam idzie?"

'''
  BelarusianConverter.convert(alphabet: int, text: str, plosive_g = False, assimilation = False, iotation = False)
  alphabet:
    0 - LatinMuzyckajaPrauda (K. Kalinoŭski)
    1 - Latin1929 (B. Taraškievič)
    2 - Latin1962 (Ja. Stankievič)
    3 - LatinUnitedNations
    4 - Romanization2023
    5 - Arabic (Belarusian Tatars)
  plosive_g:
    True - H -> G in some words
    False - keep the original text
  assimilation:
    True: add a soft assimilation
    False: keep the original text
  iotation:
    True: I -> Ji/J after vowels
    False: keep the original text
'''

```
4. ???
5. Profit.     

## Other
About Belarusian Latin: [Wikipedia](https://en.wikipedia.org/wiki/Belarusian_Latin_alphabet)      
About Belarusian Arabic: [Wikipedia](https://en.wikipedia.org/wiki/Belarusian_Arabic_alphabet)
