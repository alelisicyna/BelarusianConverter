from .latinMP import LatinMP
from .latin1929 import Latin1929
from .latin1962 import Latin1962
from .latinUN import LatinUN
from .romanization2023 import Romanization2023



class BelarusianConverter:
  def __init__(self):
    self.spellings = [LatinMP(), Latin1929(), Latin1962(), LatinUN(), Romanization2023()]


  def plosive_g(self, text):
    G_List: str = [
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
    new_text: str = text
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
    new_text: str = ''
    letters: str = 'szcSZC'
    letters_with_diacritics: str = 'śźćŚŹĆ'
    for i in range(len(text)):
      try:
        if text[i] in letters and (text[i+1] in 'śźćńŚŹĆŃ' or text[i+1] in 'jlJL' or text[i+2] in 'iI'):
          for j in range(len(letters)):
            if text[i] == letters[j]:
              new_text += letters_with_diacritics[j]
        elif text[i] in 'nN' and text[i+2] in 'iI':
          if text[i].isupper() == True:
            new_text += 'Ń'
          elif text[i].isupper() == False:
            new_text += 'ń'
        else:
          new_text += text[i]
      except:
        new_text += text[i]

    return new_text


  def iotation(self, text: str):
    new_text: str = ''
    vowels: str = "aeouiAEOUI"
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
      text: str = self.spellings[alphabet].get(text)
      if plosive_g and (str(alphabet) in '012'):
        text = self.plosive_g(text)
      if assimilation and (str(alphabet) in '012'):
        text = self.assimilation(text)
      if iotation and (str(alphabet) in '012'):
        text = self.iotation(text)
      return text
    except Exception as e:
      return f'{e}'
    