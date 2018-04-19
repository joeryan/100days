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
2. Return the sum of a list of input vaules
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

def test_check_sum_of_one_numbers():
  assert(cybrary.sum_numbers([4]) == 4)

def test_check_sum_of_two_numbers():
  assert(cybrary.sum_numbers([3,4]) == 7)

def test_check_sum_of_three_numbers():
  assert(cybrary.sum_numbers([3,5.0,4.2]) == 12.2)

def test_count_even_numbers_in_empty_list():
  assert(cybrary.count_even_numbers([]) == 0)

def test_count_even_numbers_in_one_item_input_list():
  assert(cybrary.count_even_numbers([3]) == 0)
  assert(cybrary.count_even_numbers([2]) == 1)

def test_count_even_numbers_in_multiple_item_input_list():
  assert(cybrary.count_even_numbers([3,4,8,7,230,233]) == 3)

