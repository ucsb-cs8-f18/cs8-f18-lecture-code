def equal_indices(s1, s2):
  '''(str, str) -> tuple of (int, int)
  Return the number of indices where s1 and s2 are exactly equal,
  and the number of indices where there is a match ignoring case.  
  
  >>> equal_indices('aBcd', 'abce')
  (2, 1)
  '''
  
  exact = 0
  case_insensitive = 0
  for count in range(len(s1)):
    if s1[count] == s2[count]:
      exact += 1
    elif s1[count].lower() == s2[count].lower():
      case_insensitive += 1
  return (exact, case_insensitive)
  