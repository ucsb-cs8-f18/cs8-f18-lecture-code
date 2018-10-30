import pytest

def printElementsOfCollection(col):
  ''' print the elements of a collection
      traverse the collection'''
  for c in col:
    print(c)

def concept_test_1():
  for x in range(100):
    return ('Hello'*x)


def containsOddNumber(lst):
  ''' return True if any element in lst is odd, otherwise
      return False'''
  for item in lst:
    if item % 2 == 1: # item is odd
      return True

  return False

def isListOfNumbers(lst):
  '''`return True if all the elements in the list are integers, otherwise return False'''
  for item in lst:
    if type(item) != int:
      return False

  return True


def test_isListOfNumbers_1():
  assert isListOfNumbers([1, 5, 6, "oops"]) == False

def test_isListOfNumbers_2():
  assert isListOfNumbers([1, 5, 6, 400]) == True
  
  


def test_containsOddNumber_1():
  assert containsOddNumber([2, 4, 6, 8]) == False

def test_containsOddNumber_2():
  assert containsOddNumber([1, 3, 5, 7]) == True


def test_containsOddNumber_3():
  assert containsOddNumber([10, 20, 3]) == True

def test_containsOddNumber_4():
  assert containsOddNumber([10, 5, 3]) == True



  
