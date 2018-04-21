# cybrary1.py
# exercise 1: practical applications in python
# adapted and expanded from cybrary.it video course 
# Python for Security Professionals at www.cybrary.it/course/python
# used to improve pytest understanding and overall python knowledge
import platform
import numbers


# 1. determine if the input is odd or even
def check_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

# 2. return the sum of two input values
def sum_numbers(nums):
  accum = 0
  for num in nums:
    accum += num
  return accum

# 3. given a list of integers, determine how many are even
def count_even_numbers(nums):
  count = 0
  for num in nums:
    if num % 2 ==0:
      count += 1
  return count

# 4. answer the input string backwards
def reverse_string(input_string):
  if len(input_string) > 0:
    input_string =  ''.join(reversed(input_string))
  return input_string

# 5. determine if input string is a palindrome
def is_palindrome(input_string):
  return input_string.lower() == reverse_string(input_string.lower())


if __name__ == '__main__':
  print("designed to be run with cybrary_menu.py")
