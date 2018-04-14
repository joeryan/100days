# cybrary1.py
# exercise 1: practical applications in python
# adapted and expanded from cybrary.it video course 
# Python for Security Professionals at www.cybrary.it/course/python
# used to improve pytest understanding and overall python knowledge
import platform

# display a menu of options to choose from
def menu_generator():
    menu = \
"""Please select from the following options:

1. Determine if an input value is odd or even
2. Return the sum of two input vaules
3. Return how many of an input list of integers are even
4. Return an input string reversed
5. Determine if an input string is a palindrome
Q. Quit program

Enter choice: """
    return menu

# 1. determine if the input is odd or even
def check_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

def check_odd_or_even_input():
  num = input("Enter a number to check: ")
  result = "The entered number is "
  try:
    num = int(num)
    if check_even(num):
      result += "Even"
    else:
      result += "Odd"
  except ValueError:
    result = "You must enter an number that can be converted to an integer."
  print(result)


# 2. return the sum of two input values
def sum_numbers():
  pass

# 3. given a list of integers, determine how many are even
def count_even_numbers():
  pass

# 4. answer the input string backwards
def reverse_string():
  pass

# 5. determine if input string is a palindrome
def check_input_for_palindrome():
  pass

# utility functions
def prompt_to_clear_screen():
  running_os = platform.system
  input("Press any key to continue.....")
  if running_os == 'Linux' or running_os == 'Darwin':
    _ = os.system('clear')
  elif running_os == 'Windows':
    _ = os.system('cls')
  else:
    print("\n" * 100)

def noop():
  pass

def invalid_selection():
  print("Invalid selection")


choices = {
  '1': check_odd_or_even_input,
  '2': sum_numbers,
  '3': count_even_numbers,
  '4': reverse_string,
  '5': check_input_for_palindrome,
  'q': noop
}

if __name__ == '__main__':
  choice = ''
  while choice != 'q':
    choice = input(menu_generator()).lower()
    action = choices.get(choice, invalid_selection)
    action()
    if choice != 'q':
      prompt_to_clear_screen()   
