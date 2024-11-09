# BelarusianConverter
Script who convert some Belarusian texts from Cyrillic to other Belarusian alphabets       
Programming Language: Python 3
## How to use it?
1. Download the repository
2. Add it to your project
3. Code example:
```py
# test.py
from BelarusianConverter.main import BelarusianConverter



if __name__ == '__main__':
  BelarusianConverter = BelarusianConverter()
  text = BelarusianConverter.convert(0, 'А хто там ідзе?') # example
  print(text)

'''
  Console: A chto tam idzie?

  BelarusianConverter.convert(alphabet: int, text: str)
  Alphabets:
    0 - Latin1929 (B. Taraskievic)
    1 - Latin1962 (Ja. Stankievic)
    2 - LatinMuzyckajaPrauda (K. Kalinouski) [not working]
    3 - LatinUnitedNations [not working]
    4 - Romanization2023 [not working]
    5 - Arabic (Belarusian Tatars) [not working]
'''

```
4. ???
5. Profit.     

## Other
About Belarusian Latin: [Wikipedia](https://en.wikipedia.org/wiki/Belarusian_Latin_alphabet)      
About Belarusian Arabic: [Wikipedia](https://en.wikipedia.org/wiki/Belarusian_Arabic_alphabet)
