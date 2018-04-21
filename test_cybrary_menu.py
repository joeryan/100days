# tests for cybrary beginner menu

import cybrary_menu

def test_menu_generation():
  expected_menu = \
"""Please select from the following options:

1. Determine if an input value is odd or even
2. Return the sum of a list of input vaules
3. Return how many of an input list of integers are even
4. Return an input string reversed
5. Determine if an input string is a palindrome
Q. Quit program

Enter choice: """
  assert(cybrary_menu.menu_generator() == expected_menu)
