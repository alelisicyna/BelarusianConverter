from BelarusianConverter.alphabets.latin1929 import Latin1929
from BelarusianConverter.alphabets.latin1962 import Latin1962
# from alphabets.latinMP import LatinMP
# from alphabets.latinUN import LatinUN
# from alphabets.romanization2023 import Romanization2023



class BelarusianConverter:
  def __init__(self):
    self.spellings = [Latin1929(), Latin1962()]


  def assimilation(self):
    pass


  def plosive_g(self):
    pass


  def convert(self, alphabet: int, text: str):
    try:
      return self.spellings[alphabet].get(text)
    except Exception as e:
      return f'{e}'
    