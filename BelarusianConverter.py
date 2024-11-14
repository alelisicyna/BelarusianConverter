from BelarusianConverter.converters.latinMP import LatinMP
from BelarusianConverter.converters.latin1929 import Latin1929
from BelarusianConverter.converters.latin1962 import Latin1962
from BelarusianConverter.converters.latinUN import LatinUN
from BelarusianConverter.converters.romanization2023 import Romanization2023



class BelarusianConverter:
  def __init__(self):
    self.spellings = [LatinMP(), Latin1929(), Latin1962(), LatinUN(), Romanization2023()]


  def plosive_g(self, text):
    G_List = [
      ['švahier', 'švagier'],
      ['šwahier', 'šwagier'],
      ['hanak', 'ganak'],
      ['hvałt', 'gvałt'],
      ['hwałt', 'gwałt'],
      ['huzik', 'guzik'],
      ['honta', 'gonta'],
      ['niahiehły', 'niagiegły'],
      ['hirsa', 'girsa'],
      ['haza', 'gaza'],
      ['lazh', 'lazg'],
      ['rezhiny', 'rezginy'],
      ['mazhi', 'mazgi'],
      ['rozhi', 'rozgi'],
      ['hrošy', 'grošy'],
      ['hieraičny', 'gieraičny'],
      ['hazeta', 'gazeta'],
      ['intelihiencyja', 'inteligiencyja'],
      ['hrabli', 'grabli'],
      ['hranica', 'granica'],
      ['hust', 'gust'],
      ['hrafa', 'grafa'],
      ['brazhat', 'brazgat'],
      ['vedzhać', 'vedzgać'],
      ['wedzhać', 'wedzgać'],
      ['vozhry', 'vozgry'],
      ['wozhry', 'wozgry'],
      ['abryzhły', 'abryzgły'],
      ['plavuzhać', 'plavuzgać'],
      ['plawuzhać', 'plawuzgać'],
      ['ahrest', 'agrest'],
      ['hierhietać', 'giergietać'],
      ['cuhli', 'cugli'],
      ['hłuzd', 'głuzd'],
      ['džhać', 'džgać'],
      ['zhrabny', 'zgrabny'],
      ['zhraja', 'zgraja'],
      ['hruca', 'gruca'],
      ['huzy', 'guzy'],
      ['habruś', 'gabruś'],
      ['cehła', 'cegła'],
      ['ahata', 'agata'],
      ['izhoj', 'izgoj'],
      ['ciahli', 'ciagli'],
      ['lezhinka', 'lezginka'],
      ['harniec', 'garniec'],
      ['ekshumacyja', 'eksgumacyja']
    ]
    new_text = text
    for i in range(len(G_List)):
      if G_List[i][0] in text.lower():
        new_text = new_text.replace(G_List[i][0], G_List[i][1])
      if G_List[i][0].upper() in text:
        new_text = new_text.replace(G_List[i][0].upper(), G_List[i][1].upper())
      if f'{G_List[i][0][0].upper()}{G_List[i][0][1:]}' in text:
        new_text = new_text.replace(f'{G_List[i][0][0].upper()}{G_List[i][0][1:]}', f'{G_List[i][1][0].upper()}{G_List[i][1][1:]}')
      else:
        pass
    return new_text


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
      if plosive_g and (alphabet == 1 or alphabet == 2):
        text = self.plosive_g(text)
      if assimilation and (alphabet == 0 or alphabet == 1 or alphabet == 2 or alphabet == 3):
        text = self.assimilation(text)
      if iotation and (alphabet == 1 or alphabet == 2):
        text = self.iotation(text)
      return text
    except Exception as e:
      return f'{e}'
    