class Romanization2023:
  def __init__(self):
    self.cyrillic = [
      'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'ё', 'ж', 'з', 'і', 'й', 'к', 'л',
      'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ў', 'ф', 'х', 'ц', 'ч', 'ш',
      'ы', 'ь', 'э', 'ю', 'я', '’', ' '
    ]
    self.alphabet = [
      'a', 'b', 'v', 'h', 'g', 'd', '', '', 'zh', 'z', 'i', 'j', 'k', '',
      'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'f', 'h', 'c', 'ch', 'sh',
      'y', '', 'e', '', '', '', ' '
    ]
    self.cyrillic_vowels = ['я', 'е', 'ё', 'ю', 'і']
    self.latin_vowels_j = ['ja', 'je', 'jo', 'ju', 'ji']
    self.latin_vowels_i = ['ia', 'ie', 'io', 'iu', 'i']


  def soft_vowels(self, i, text, new_text):
    vowels = "аэоуыяеёюійўьАЭОУЫЯЕЁЮІЙЎЬ’'"
    consonants = 'цкнгґшзхфвпрлджчсмтбЦКНГҐШЗХФВПРЛДЖЧСМТБ'
    try:
      if text[i-1] in consonants and i != 0: # Перад зычнымі (I)
        for j in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[j]:
            new_text += self.latin_vowels_i[j]
            return new_text
      else: # Ва ўсіх астатніх выпадках (J)
        for j in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[j]:
            new_text += self.latin_vowels_j[j]
            return new_text
    except: # На выпадак памылкі (J)
      for j in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[j]:
          new_text += self.latin_vowels_j[j]
          return new_text


    return new_text


  def soft_vowels_top(self, i, text, new_text):
    vowels = "аэоуыяеёюійўьАЭОУЫЯЕЁЮІЙЎЬ’'"
    consonants = 'цкнгґшзхфвпрлджчсмтбЦКНГҐШЗХФВПРЛДЖЧСМТБ'
    try:
      if text[i-1] in consonants and i != 0: # Перад зычнымі (I)
        for j in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[j].upper():
            new_text += self.latin_vowels_i[j].upper()
            return new_text
      else: # Ва ўсіх астатніх выпадках (J)
        for j in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[j].upper():
            try:
              if (text[i+1].isupper() == False and text[i+2].isupper() == False) or text[i+2].isupper() == False:
                new_text += f'{self.latin_vowels_j[j][0].upper()}{self.latin_vowels_j[j][1]}'
                return new_text
              else:
                new_text += self.latin_vowels_j[j].upper()
                return new_text
            except:
              new_text += self.latin_vowels_j[j].upper()
              return new_text
    except: # На выпадак памылкі (J)
      for j in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[j].upper():
          new_text += self.latin_vowels_j[j].upper()
          return new_text


  def other_letters(self, i, text, new_text):
    j = 0
    while j != len(self.cyrillic) + 1:
      if j == len(self.cyrillic): # калі ў масыве няма гэтага сымбаля, то ставіцца сымбаль з арыгінальнага тэксту
        new_text += text[i]
        return new_text
      if self.cyrillic[j].upper() == text[i]:
        if self.cyrillic[j].upper() == 'Ж':
          try:
            if text[i+1].isupper() == True:
              new_text += self.alphabet[j].upper()
              return new_text
            else:
              new_text += f'{self.alphabet[j][0].upper()}{self.alphabet[j][1]}'
              return new_text
          except:
            new_text += self.latin_vowels_j[j].upper()
            return new_text
        elif self.cyrillic[j].upper() == 'Ч':
          try:
            if text[i+1].isupper() == True:
              new_text += self.alphabet[j].upper()
              return new_text
            else:
              new_text += f'{self.alphabet[j][0].upper()}{self.alphabet[j][1]}'
              return new_text
          except:
            new_text += self.latin_vowels_j[j].upper()
            return new_text
        elif self.cyrillic[j].upper() == 'Ш':
          try:
            if text[i+1].isupper() == True:
              new_text += self.alphabet[j].upper()
              return new_text
            else:
              new_text += f'{self.alphabet[j][0].upper()}{self.alphabet[j][1]}'
              return new_text
          except:
            new_text += self.latin_vowels_j[j].upper()
            return new_text
        else:
          new_text += self.alphabet[j].upper()
          return new_text
      elif self.cyrillic[j] == text[i]: # літара ў ніжэйшым рэгістры
          new_text += self.alphabet[j]
          return new_text
      j += 1

    return new_text


  def get(self, text):
    new_text = ''
    for i in range(len(text)):
      # работа з ётаванымі 
      if text[i] in 'яеёюі': 
        new_text = self.soft_vowels(i, text, new_text)
      # работа з ётаванымі (верхні рэгістр)
      elif text[i] in 'ЯЕЁЮІ': 
        new_text = self.soft_vowels_top(i, text, new_text)
      # работа зь іншымі літарамі
      else:
        new_text = self.other_letters(i, text, new_text)

    return f'{new_text}'
