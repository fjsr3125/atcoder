import decimal
import math
n = int(input())

def count_digit(number):
  number_str = str(number)
  return len(number_str)

decimal_n =n / (10 ** (count_digit(n)-3))

decimal_n = math.floor(decimal_n)
n = decimal_n * (10 ** (count_digit(n)-3))

print(int(n))
