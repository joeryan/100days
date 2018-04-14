# cybrary1.py
# exercise 1: practical applications in python
# adapted and expanded from cybrary.it video course 
# Python for Security Professionals at www.cybrary.it/course/python
# used to improve pytest understanding and overall python knowledge

# display a menu of options to choose from

# 1. determine if the input is odd or even

# 2. return the sum of two input values

# 3. given a list of integers, determine how many are even

# 4. answer the input string backwards

# 5. determine if input string is a palindrome

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

if __name__ == '__main__':
  choice = ''
  while choice.lower() != 'q':
    choice = input(menu_generator())
  
