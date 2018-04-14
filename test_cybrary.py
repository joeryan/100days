# Tests for the cybrary.it journeyman level project
# extended exercises, but based on the video course:
# Python for Security Professionals found at
# www.cybrary.it/courses/python

import pytest
import cybrary

def test_menu_generation():
  expected_menu = \
"""Please select from the following options:

1. Determine if an input value is odd or even
2. Return the sum of two input vaules
3. Return how many of an input list of integers are even
4. Return an input string reversed
5. Determine if an input string is a palindrome
Q. Quit program

Enter choice: """
  assert(cybrary.menu_generator() == expected_menu)

def test_check_even_with_an_odd_number_returns_false():
  assert(cybrary.check_even(3) == False)

def test_check_even_with_an_even_number_returns_true():
  assert(cybrary.check_even(12) == True)


