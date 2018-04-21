# Tests for the cybrary.it journeyman level project
# extended exercises, but based on the video course:
# Python for Security Professionals found at
# www.cybrary.it/courses/python

import pytest
import cybrary


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

def test_reverse_string_zero_length():
  assert(cybrary.reverse_string('') == '')

def test_reverse_string_fixed_length():
  assert(cybrary.reverse_string('Test') == 'tseT')

def test_ispalindrome_on_known_palindrome():
  assert(cybrary.is_palindrome("toot")) == True

def test_ispalindrome_on_palindrome_with_caps():
  assert(cybrary.is_palindrome("Dud")) == True

def test_is_palindrome_on_non_palindrome():
  assert(cybrary.is_palindrome("Beer")) == False

