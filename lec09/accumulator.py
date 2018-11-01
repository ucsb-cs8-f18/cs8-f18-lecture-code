# accumulator.py :
# Solving problems that involve collections (strings, lists, tuples, namedtuples)
# Patterns of programming using loops, nested loops
# Nov 1, 2018

def countElements(lst):
  '''returns the number of elements in lst'''
  count = 0
  for item in lst:
    count = count+1
  return count


def countOddNumbers(lst):
  '''returns the number of odd numbers in lst'''
  count = 0
  for item in lst:
    if(item % 2 == 1):
      count = count+1
  return count


def countWords(sentence):
  '''returns the number of words in the sentence'''
  count = 0
  for item in sentence:
    if(item == ' '):
      count = count+1
  return count+1

def countWords_2(sentence):
  '''returns the number of words in the sentence'''

  lst = sentence.split()
  count = 0
  for item in lst:
      count = count+1
  return count



def countWords_3(sentence, len):
  '''returns the number of words in the sentence with length greater than len'''
  return "stub"


def createOddList(lst):
  '''returns a new list that contains all the odd numbers in lst'''
  newlist = []
  for item in lst:
    if(item%2 == 1):
      # item is odd
      #append item to newlist
      newlist.append(item)  # add item to newlist
  #    newlist  = newlist+ [item] (also works)
  
  return newlist


def drawRectangle(width, height):
  '''print a rectangle with given width and height using the character *
    (instead of turtle)'''
  rect =''
  for i in range(height):
    #Write code that creates a string of width '*'s  and one '\n'
    rect = rect + '*'*width + '\n'

  print(rect)
  return

def drawRectangle_2(width, height):
  '''print a rectangle with given width and height using the character *
    (instead of turtle)'''
  rect =''
  for i in range(height):
    #Write code that creates a string of width '*'s  and one '\n'
    line =''
    for j in range(width):
      line= line+ '*'
    print(line)
  return

def drawTriangle(height):
  '''print a right triagle with given height using stars(*).
     Assume the size of the base and height are equal'''
  for i in range(1, height+1):
    # print ith row, print i '*'s
    print('*'*i)
    


def countVowels(strList):
  """ Count vowels in list of strings """
  ''' [ 'This' , 'is', 'an', 'apple'] ->return 5'''
  vowels = 'AEIOUaeiou'
  count = 0
  for item in strList:
    for c in item:
      if c in vowels:
        count = count +1
        
  return count        
    
  
 
    





