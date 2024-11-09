from BelarusianConverter.alphabets.latin1929 import Latin1929
from BelarusianConverter.alphabets.latin1962 import Latin1962
# from alphabets.latinMP import LatinMP
# from alphabets.latinUN import LatinUN
# from alphabets.romanization2023 import Romanization2023



class BelarusianConverter:
  def __init__(self):
    self.spellings = [Latin1929(), Latin1962()]


  def assimilation(self, text):
    return text


  def plosive_g(self, text):
    '''
    dictionary_h = ['haza', 'hambija', 'hient', 'hibraltar', 'hitlin', 'ahra', 'arlinhtan', 'redynh']
    dictionary_g = ['Gaza', 'Gambija', 'Gient', 'Gibraltar', 'Gitlin', 'Agra', 'Arlingtan', 'Redyng']
    for i in range(len(dictionary_h)):
      if dictionary_h[i].lower() in text.lower():
        text = text.replace(dictionary_h[i], dictionary_g[i])
    '''
    return text


  def convert(self, alphabet: int, plosive_g: bool, assimilation: bool, text: str):
    try:
      text = self.spellings[alphabet].get(text)
      if plosive_g: text = self.plosive_g(text)
      if assimilation: text = self.assimilation(text)
      return text
    except Exception as e:
      return f'{e}'
    