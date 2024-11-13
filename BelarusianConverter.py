from BelarusianConverter.converters.latinMP import LatinMP
from BelarusianConverter.converters.latin1929 import Latin1929
from BelarusianConverter.converters.latin1962 import Latin1962
from BelarusianConverter.converters.latinUN import LatinUN
from BelarusianConverter.converters.romanization2023 import Romanization2023



class BelarusianConverter:
  def __init__(self):
    self.spellings = [LatinMP(), Latin1929(), Latin1962(), LatinUN(), Romanization2023()]


  def plosive_g(self, text):
    return text


  def assimilation(self, text):
    return text


  def iotation(self, text: str):
    new_text = ''
    vowels = "aeouiAEOUI"
    for i in range(len(text)):
      if text[i] in 'iI' and text[i-1] == ' ' and text[i+1] == ' ':
        if text[i+1].isupper() == True:
          new_text += 'J'
        elif text[i+1].isupper() == False:
          new_text += 'j'
      elif text[i] in 'iI' and (text[i-1] in vowels or (text[i-2] in vowels and text[i-1] == ' ')):
        if text[i+1].isupper() == True:
          new_text += 'JI'
        elif text[i+1].isupper() == False:
          new_text += 'ji'
      else:
        new_text += text[i]

    return new_text


  def convert(self, alphabet: int, text: str, plosive_g = False, assimilation = False, iotation = False):
    try:
      text = self.spellings[alphabet].get(text)
      if plosive_g:
        text = self.plosive_g(text=text)
      if assimilation:
        text = self.assimilation(text=text)
      if iotation and (alphabet == 1 or alphabet == 2):
        text = self.iotation(text)
      return text
    except Exception as e:
      return f'{e}'
    