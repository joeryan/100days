# repeater.py
# simple script for linux academy functions exercise
# asks for a text phrase and number of times to repeat
# outputs the entered phrase the specified number of times
from sys import exit

def repeater(phrase, count):
  for num in range(count):
    print(f"Line {num}: {phrase}")

if __name__ == '__main__':
  phrase = input("Type a phrase you want to repeat: ")
  count = input("How many times should it be repeated? ")
  try:
    count = int(count)
  except ValueError:
    exit("You entered an invalid count.  This needs to be an integer.")

  repeater(phrase, count)

