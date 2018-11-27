def get_yn ():
  response = ''
  while response != 'y' and response != 'n':
    response = input('Type y or n to continue: ')
  return response
    