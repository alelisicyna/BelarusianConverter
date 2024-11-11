class LatinUN:
  def __init__(self):
    self.cyrillic = [
      'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'ё', 'ж', 'з', 'і', 'й', 'к', 'л',
      'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ў', 'ф', 'х', 'ц', 'ч', 'ш',
      'ы', 'ь', 'э', 'ю', 'я', '’', ' '
    ]
    self.alphabet = [
      'a', 'b', 'v', 'h', 'g', 'd', '', '', 'ž', 'z', 'i', 'j', 'k', 'l',
      'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'ŭ', 'f', 'ch', 'c', 'č', 'š',
      'y', '', 'e', '', '', '’', ' '
    ]
    self.cyrillic_vowels = ['я', 'е', 'ё', 'ю']
    self.latin_vowels_j = ['ja', 'je', 'jo', 'ju']
    self.latin_vowels_i = ['ia', 'ie', 'io', 'iu']


  def soft_vowels(self, i, text, new_text):
    vowels = 'аэоуыяеёюійўАЭОУЫЯЕЁЮІЙЎ’'
    consonants = 'цкнгґшзхфвпрлджчсмтбЦКНГҐШЗХФВПРЛДЖЧСМТБ'
    # j на пачатку тэксту
    if i == 0:
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v]:
          new_text += self.latin_vowels_j[v]
          break
    # j пасьля галоснай
    for j in range(len(vowels)):
      if text[i-1] == vowels[j] and i != 0:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v]:
            new_text += self.latin_vowels_j[v]
            break
    if text[i-1] == 'ь' and text[i-2] == 'л' and i != 0:
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v]:
          new_text += self.latin_vowels_j[v]
    # пачатак новага слова
    k = 0
    letters = 'йцукенгшўзхфывапролджэячсмітьбюЙЦУКЕНГШЎЗХФЫВАПРОЛДЖЭЯЧСМІТЬБЮ'
    while k != 61:
      for h in range(len(letters)):
        if k == 60:
          for v in range(len(self.cyrillic_vowels)):
            if text[i] == self.cyrillic_vowels[v] and i != 0:
              new_text += self.latin_vowels_j[v]
              break
          break
        if text[i-1] == letters[h]:
          break
        elif text[i-1] != letters[h]:
          k += 1
      break
    # і
    for j in range(len(consonants)):
      if text[i-1] == consonants[j] and i != 0:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v]:
            new_text += self.latin_vowels_i[v]
            break

    return new_text


  def soft_vowels_top(self, i, text, new_text):
    vowels = 'аэоуыяеёюійАЭОУЫЯЕЁЮІЙ’'
    consonants = 'цкнгґшзхфвпрлджчсмтбЦКНГҐШЗХФВПРЛДЖЧСМТБ'
    # j на пачатку тэксту
    if i == 0 and (text[i+1].isupper() == False and text[i+2].isupper() == False):
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v].upper():
          new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
    try:
      if text[i+1].isupper() == True and text[i+2].isupper() == True:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v].upper():
            new_text += self.latin_vowels_j[v].upper()
    except:
      pass
    # j пасьля галоснай
    for j in range(len(vowels)):
      if text[i-1] == vowels[j] and i != 0:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v].upper():
            new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
    if text[i-1] == 'Ь' and text[i-2] == 'Л' and i != 0:
      for v in range(len(self.cyrillic_vowels)):
        if text[i] == self.cyrillic_vowels[v].upper():
          new_text += self.latin_vowels_j[v].upper()
    # пачатак новага слова
    k = 0
    letters = 'йцукенгшўзхфывапролджэячсмітьбюЙЦУКЕНГШЎЗХФЫВАПРОЛДЖЭЯЧСМІТЬБЮ'
    while k != 61:
      for h in range(len(letters)):
        if k == 60:
          for v in range(len(self.cyrillic_vowels)):
            if text[i] == self.cyrillic_vowels[v].upper() and i != 0:
              new_text += f'{self.latin_vowels_j[v][0].upper() + self.latin_vowels_j[v][1]}'
              break
          break
        if text[i-1] == letters[h]:
          break
        elif text[i-1] != letters[h]:
          k += 1
      break
    # і
    for j in range(len(consonants)):
      if text[i-1] == consonants[j]:
        for v in range(len(self.cyrillic_vowels)):
          if text[i] == self.cyrillic_vowels[v].upper():
            new_text += self.latin_vowels_i[v].upper()
            break

    return new_text


  def other_letters(self, i, text, new_text):
    j = 0
    while j != len(self.cyrillic) + 1:
      if j == len(self.cyrillic): # калі ў масыве няма гэтага сымбаля, то ставіцца сымбаль з арыгінальнага тэксту
        new_text += text[i]
        break
      if self.cyrillic[j].upper() == text[i]: # літара ў вялікім рэгістры
        if text[i] == 'С' and (text[i+1] == 'ь' or text[i+1] == 'Ь'):
          new_text += 'Ś'
          break
        elif text[i] == 'З' and (text[i+1] == 'ь' or text[i+1] == 'Ь'):
          new_text += 'Ź'
          break
        elif text[i] == 'Ц' and (text[i+1] == 'ь' or text[i+1] == 'Ь'):
          new_text += 'Ć'
          break
        elif text[i] == 'Н' and (text[i+1] == 'ь' or text[i+1] == 'Ь'):
          new_text += 'Ń'
          break
        elif self.cyrillic[j].upper() == 'Х':
          # пачатак новага слова
          k = 0
          letters = 'йцукенгшўзхфывапролджэячсмітьбюЙЦУКЕНГШЎЗХФЫВАПРОЛДЖЭЯЧСМІТЬБЮ'
          while k != 61:
            for h in range(len(letters)):
              if k == 60 and text[i+1].isupper() == False and text[i+2].isupper() == False:
                new_text += f'{self.alphabet[j][0].upper() + self.alphabet[j][1]}'
                break
              if text[i-1] == letters[h]:
                break
              elif text[i-1] != letters[h]:
                k += 1
            break
          if i == 0 and (text[i+1].isupper() == False and text[i+2].isupper() == False):
            new_text += f'{self.alphabet[j][0].upper() + self.alphabet[j][1]}'
            break
          elif text[i+1].isupper() == True and text[i+2].isupper() == True:
            new_text += self.alphabet[j].upper()
            break
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
        elif text[i] == 'л' and text[i+1] == 'ь':
          new_text += 'ĺ'
          break
        elif text[i] == 'н' and text[i+1] == 'ь':
          new_text += 'ń'
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

      # работа зь іншымі літарамі
      else:
        new_text = self.other_letters(i, text, new_text)

    return f'{new_text}'
