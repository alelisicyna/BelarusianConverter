class Latin1962:
  def __init__(self):
    self.cyrillic = [
      'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'ё', 'ж', 'з', 'і', 'й', 'к', 'л',
      'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ў', 'ф', 'х', 'ц', 'ч', 'ш',
      'ы', 'ь', 'э', 'ю', 'я', '’', ' '
    ]
    self.alphabet = [
      'a', 'b', 'v', 'h', 'g', 'd', '', '', 'ž', 'z', 'i', 'j', 'k', '',
      'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'ŭ', 'f', 'ch', 'c', 'č', 'š',
      'y', '', 'e', '', '', '', ' '
    ]
    self.cyrillic_vowels = ['я', 'е', 'ё', 'ю']
    self.latin_vowels_j = ['ja', 'je', 'jo', 'ju']
    self.latin_vowels_i = ['ia', 'ie', 'io', 'iu']


  def soft_vowels(self, i, text, new_text):
    vowels = 'аэоуыяеёюіАЭОУЫЯЕЁЮІ'
    consonants = 'цкнгґшзхфвпрлджчсмтб'
    # j на пачатку тэксту
    if i == 0:
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v]:
          new_text += self.latin_vowels_j[v]
    # j пасьля галоснай
    for j in range(len(vowels)):
      if text[i-1] == vowels[j]:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v]:
            new_text += self.latin_vowels_j[v]
    # пачатак новага слова
    if text[i-1] == ' ':
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v]:
          new_text += self.latin_vowels_j[v]
    # і
    for j in range(len(consonants)):
      if text[i-1] == consonants[j].upper() or text[i-1] == consonants[j]:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v]:
            if text[i-1] == 'л':
              new_text += self.latin_vowels_i[v][1]
            elif text[i-1] == 'Л':
              new_text += self.latin_vowels_i[v][1]
            else:
              new_text += self.latin_vowels_i[v]

    return new_text


  def soft_vowels_top(self, i, text, new_text):
    vowels = 'аэоуыяеёюійўАЭОУЫЯЕЁЮІЎЙ'
    consonants = 'цкнгґшзхфвпрлджчсмтб'
    # j на пачатку тэксту
    if i == 0:
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v].upper():
          new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
    # j пасьля галоснай
    for j in range(len(vowels)):
      if text[i-1] == vowels[j]:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v].upper():
            new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
    # пачатак новага слова
    if text[i-1] == ' ':
      if text[i-2] == '.' or text[i-2] == '?' or text[i-2] == '!' or text[i-2] == ';':
        if text[i+1].isupper() == True or text[i+2].isupper() == True or text[i-1].isupper() == True:
          for v in range(len(self.cyrillic_vowels)):
            if text[i] == self.cyrillic_vowels[v].upper():
              new_text += self.latin_vowels_j[v].upper()
              break
        else:
          for v in range(len(self.cyrillic_vowels)):
            if text[i] == self.cyrillic_vowels[v].upper():
              new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
              break
      else:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v].upper():
            new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
            break
    # і
    for j in range(len(consonants)):
      if text[i-1] == consonants[j].upper() or text[i-1] == consonants[j]:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v].upper():
            if text[i-1] == 'л':
              new_text += self.latin_vowels_i[v][1].upper()
            elif text[i-1] == 'Л':
              new_text += self.latin_vowels_i[v][1].upper()
            else:
              new_text += self.latin_vowels_i[v].upper()

    return new_text


  def letter_l(self, i, text, new_text):
    if text[i+1] == 'а' or text[i+1] == 'э' or text[i+1] == 'о' or text[i+1] == 'у' or text[i+1] == 'ы':
      new_text += 'ł'
    elif text[i+1] == 'я' or text[i+1] == 'е' or text[i+1] == 'ё' or text[i+1] == 'ю' or text[i+1] == 'і' or text[i+1] == 'ь':
      new_text += 'l'

    return new_text


  def letter_l_top(self, i, text, new_text):
    if text[i+1] == 'А' or text[i+1] == 'Э' or text[i+1] == 'О' or text[i+1] == 'У' or text[i+1] == 'Ы':
      new_text += 'Ł'
    elif text[i+1] == 'Я' or text[i+1] == 'Е' or text[i+1] == 'Ё' or text[i+1] == 'Ю' or text[i+1] == 'І' or text[i+1] == 'Ь':
      new_text += 'L'

    return new_text


  def other_letters(self, i, text, new_text):
    j = 0
    while j != len(self.cyrillic) + 1:
      if j == len(self.cyrillic): # калі ў масыве няма гэтага сымбаля, то ставіцца сымбаль з арыгінальнага тэксту
        new_text += text[i]
        break
      if self.cyrillic[j].upper() == text[i]: # літара ў вялікім рэгістры
        if text[i] == 'С' and text[i+1] == 'ь':
          new_text += 'Ś'
          break
        elif text[i] == 'С' and text[i+1] == 'Ь':
          new_text += 'Ś'
          break
        elif text[i] == 'З' and text[i+1] == 'ь':
          new_text += 'Ź'
          break
        elif text[i] == 'З' and text[i+1] == 'Ь':
          new_text += 'Ź'
          break
        elif text[i] == 'Ц' and text[i+1] == 'ь':
          new_text += 'Ć'
          break
        elif text[i] == 'Ц' and text[i+1] == 'Ь':
          new_text += 'Ć'
          break
        elif self.cyrillic[j].upper() == 'Х':
          if i == 0 or text[i-2] == '.' or text[i-2] == '?' or text[i-2] == '!' or text[i-2] == ';':
            new_text += self.alphabet[j][0].upper() + self.alphabet[j][1]
            break
          else:
            new_text += self.alphabet[j].upper()
            break
        else:
          new_text += self.alphabet[j].upper()
          break
      elif self.cyrillic[j] == text[i]: # літара ў ніжэйшым рэгістры
        if text[i] == 'с' and text[i+1] == 'ь':
          new_text += 'ś'
          break
        elif text[i] == 'з' and text[i+1] == 'ь':
          new_text += 'ź'
          break
        elif text[i] == 'ц' and text[i+1] == 'ь':
          new_text += 'ć'
          break
        else:
          new_text += self.alphabet[j]
          break
      j += 1

    return new_text


  def get(self, text):
    new_text = ''
    for i in range(len(text)):

      # работа з ётаванымі 
      if text[i] == 'я' or text[i] == 'е' or text[i] == 'ё' or text[i] == 'ю': 
        new_text = self.soft_vowels(i, text, new_text)

      # работа з ётаванымі (верхні рэгістр)
      elif text[i] == 'Я' or text[i] == 'Е' or text[i] == 'Ё' or text[i] == 'Ю': 
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
