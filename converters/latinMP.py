class LatinMP:
  def __init__(self):
    self.cyrillic = [
      'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'ё', 'ж', 'з', 'і', 'й', 'к', 'л',
      'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ў', 'ф', 'х', 'ц', 'ч', 'ш',
      'ы', 'ь', 'э', 'ю', 'я', '’', "'", ' '
    ]
    self.alphabet = [
      'a', 'b', 'w', 'h', 'g', 'd', '', '', 'ż', 'z', 'i', 'j', 'k', '',
      'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'u', 'f', 'ch', 'c', 'cz', 'sz',
      'y', '', 'e', '', '', '', "", ' '
    ]
    self.cyrillic_vowels = ['я', 'е', 'ё', 'ю']
    self.latin_vowels_j = ['ja', 'je', 'jo', 'ju']
    self.latin_vowels_i = ['ia', 'ie', 'io', 'iu']


  def soft_vowels(self, i, text, new_text):
    vowels = "аэоуыяеёюійўьАЭОУЫЯЕЁЮІЙЎЬ’'"
    consonants = 'цкнгґшзхфвпрлджчсмтбЦКНГҐШЗХФВПРЛДЖЧСМТБ'
    try:
      if text[i-1] in consonants and i != 0: # Перад зычнымі (I)
        for j in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[j]:
            if text[i-1] in 'лЛ':
                new_text += self.latin_vowels_i[j][1]
                return new_text
            else:
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
            if text[i-1] in 'лЛ':
                new_text += self.latin_vowels_i[j][1].upper()
                return new_text
            else:
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


  def letter_l(self, i, text, new_text):
    vowels_lj = 'яеёюіьЯЕЁЮІЬ'
    if text[i+1] in vowels_lj:
      new_text += 'l'
    else:
      new_text += 'ł'

    return new_text


  def letter_l_top(self, i, text, new_text):
    vowels_lj = 'яеёюіьЯЕЁЮІЬ'
    if text[i+1] in vowels_lj:
      new_text += 'L'
    else:
      new_text += 'Ł'


    return new_text


  def other_letters(self, i, text, new_text):
    j = 0
    while j != len(self.cyrillic) + 1:
      if j == len(self.cyrillic): # калі ў масыве няма гэтага сымбаля, то ставіцца сымбаль з арыгінальнага тэксту
        new_text += text[i]
        break
      if self.cyrillic[j].upper() == text[i]: # літара ў вялікім рэгістры
        if text[i] == 'С' and text[i+1] in 'ьЬ':
          new_text += 'Ś'
          return new_text
        elif text[i] == 'З' and text[i+1] in 'ьЬ':
          new_text += 'Ź'
          return new_text
        elif text[i] == 'Ц' and text[i+1] in 'ьЬ':
          new_text += 'Ć'
          return new_text
        elif text[i] == 'Н' and text[i+1] in 'ьЬ':
          new_text += 'Ń'
          return new_text
        elif text[i] == 'І' and text[i-1] in "'’":
          new_text += 'JI'
          return new_text
        elif text[i] == 'І':
          new_text += 'I'
          return new_text
        elif self.cyrillic[j].upper() == 'Х':
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
        try:
          if text[i] == 'с' and text[i+1] == 'ь':
            new_text += 'ś'
            return new_text
          elif text[i] == 'з' and text[i+1] == 'ь':
            new_text += 'ź'
            return new_text
          elif text[i] == 'ц' and text[i+1] == 'ь':
            new_text += 'ć'
            return new_text
          elif text[i] == 'н' and text[i+1] == 'ь':
            new_text += 'ń'
            return new_text
          elif text[i] == 'і' and text[i-1] in "'’":
            new_text += 'ji'
            return new_text
          elif text[i] == 'і':
            new_text += 'i'
            return new_text
          else:
            new_text += self.alphabet[j]
            return new_text
        except:
          new_text += self.alphabet[j]
          return new_text
      j += 1

    return new_text


  def get(self, text):
    new_text = ''
    for i in range(len(text)):
      # работа з ётаванымі 
      if text[i] in 'яеёю': 
        new_text = self.soft_vowels(i, text, new_text)
      # работа з ётаванымі (верхні рэгістр)
      elif text[i] in 'ЯЕЁЮ': 
        new_text = self.soft_vowels_top(i, text, new_text)
      # L і Ł
      elif text[i] == 'л':
        new_text = self.letter_l(i, text, new_text)
      # L і Ł (верхні рэгістр)
      elif text[i] == 'Л':
        new_text = self.letter_l_top(i, text, new_text)
      # работа зь іншымі літарамі
      else:
        new_text = self.other_letters(i, text, new_text)

    return f'{new_text}'
