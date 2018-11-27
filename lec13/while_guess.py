import random

def guess():
  answer = random.randint(1, 10)
  guess = raw_input("Guess a number between 1 and 10: ")
  while int(guess) != answer:
    guess = raw_input("Sorry, guess again: ")
