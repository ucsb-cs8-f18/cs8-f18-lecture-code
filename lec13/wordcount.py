def word_count (s):
  '''Return the number of words in s.
  s might have multiple spaces between words,
  but will have no leading or trailing spaces.'''  
  
  if not s:
    return 0
  
  counter = 0
  words = 1
  while counter < len(s):
    if s[counter] == ' ':
      while s[counter] == ' ':
        counter += 1
      words += 1
    counter += 1
  return words
  