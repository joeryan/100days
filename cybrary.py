# cybrary1.py
# exercise 1: practical applications in python
# adapted and expanded from cybrary.it video course 
# Python for Security Professionals at www.cybrary.it/course/python
# used to improve pytest understanding and overall python knowledge
import platform
import numbers

# display a menu of options to choose from
def menu_generator():
    menu = \
"""Please select from the following options:

1. Determine if an input value is odd or even
2. Return the sum of a list of input vaules
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
def sum_numbers(nums):
  accum = 0
  for num in nums:
    accum += num
  return accum

def get_sum_of_input_numbers():
  nums = input("Type a list of numbers separated by a space, end the list with Enter: ")
  num_list = []  
  nums = nums.split(' ')
  for num in nums:
    try:
      num_list.append(int(num))
    except ValueError:
      try:
        num_list.append(float(num))
      except ValueError:
        print("Error: input {0} is not a valid number".format(num))
  print("The sum of the numbers is {0}".format(sum_numbers(num_list)))

# 3. given a list of integers, determine how many are even
def count_even_numbers(nums):
  count = 0
  for num in nums:
    if num % 2 ==0:
      count += 1
  return count

def count_even_numbers_in_list():
  nums = []
  num_list = input("Type a list of inegers separated by a space.  Press Enter when done\n> ")
  num_list = list(num_list.split(' '))
  for num in num_list:
    if len(num) > 0:
      nums.append(int(num.strip()))
  print(count_even_numbers(nums))

# 4. answer the input string backwards
def reverse_string(input_string):
  if len(input_string) > 0:
    input_string =  ''.join(reversed(input_string))
  return input_string

def print_input_string_reversed():
  input_string = input("Type a string to reverse.  Press Enter when finished. ")
  output_string = reverse_string(input_string)
  print(output_string)

# 5. determine if input string is a palindrome
def check_input_for_palindrome():
  word = input("Type a word to check if it is a palindrome: ")
  if is_palindrome(word):
    print("It is definitely a palindrome!")
  else:
    print("Sorry, that word is not a palindrome.")

def is_palindrome(input_string):
  return input_string.lower() == reverse_string(input_string.lower())

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
  '2': get_sum_of_input_numbers,
  '3': count_even_numbers_in_list,
  '4': print_input_string_reversed,
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
