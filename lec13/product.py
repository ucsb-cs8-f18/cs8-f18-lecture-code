def do_something():
  total = 1
  response = int(input("Please enter an integer: "))
  while response != 0:
    if response % 2 == 0:
      total = total * response
    response = int(input("Please enter an integer: "))
  return total
  