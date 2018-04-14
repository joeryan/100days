# test_calc.py 
# tests for the simple calculator
import pytest
import calc

def test_addition_of_simple_numbers():
  assert(calc.add(1,1) == 2)
  assert(calc.add(3,5) == 8)

def test_addition_of_dice_and_numbers():
  assert(calc.add(1,'d4') in range(1,5))
  assert(calc.add(3,'d8') in range(3,25))

def test_subtraction_of_simple_numbers():
  assert(calc.sub(1,5) == -4)
  assert(calc.sub(8,4) == 4)

def test_subtraction_of_dice_and_numbers():
  assert(calc.sub(1,'d6') in range(-5,1))
  assert(calc.sub('d8',4) in range(-3,5))

def test_multiplication_of_simple_numbers():
  assert(calc.mult(1,1) == 1)
  assert(calc.mult(2,4) == 8)
  assert(calc.mult(4,-3) == -12)

def test_multiplication_of_simple_numbers():
  assert(calc.mult(1,'d4') in range(1,5))
  assert(calc.mult(2,'d4') in range(2,9))
  assert(calc.mult('d8',-3) in range(-24,-2))

def test_division_of_simple_numbers():
  assert(round(calc.div(2,4), 5) == .50000)
  assert(round(calc.div(6,3),1) == 2.0)


