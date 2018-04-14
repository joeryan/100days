# calc.py  
# simple calculator that will also roll dice

from random import randint
from numbers import Number
from operator import xor

def add(num1, num2):
  return dice_num(num1) + dice_num(num2)

def sub(num1, num2):
  return dice_num(num1) - dice_num(num2)

def mult(num1, num2):
  accum = 0
  if isinstance(num1, Number) and isinstance(num2, Number):
    accum = num1 * num2
  if type(num1) == str and type(num2) == str:
    accum = dice_num(num1) * dice_num(num2)
  if type(num1) == str:
    for _ in range(1,abs(num2)+1):
      accum += dice_num(num1)
    if num2 < 0:
      accum = -accum
  else:
    for _ in range(1,abs(num1)+1):
      accum += dice_num(num2)
    if num1 < 0:
      accum = -accum
  return accum

def div(num1, num2):
  if not (isinstance(num1, Number) and isinstance(num2, Number)):
    raise ValueError("cannot use dice in divion")
  return num1 / num2

def dice_num(num):
  if type(num) == str:
    if len(num) > 1 and num[0] == 'd':
      dice = int(num[1:])
      num = randint(1, dice)
  else:
    num = int(num)
  return num

