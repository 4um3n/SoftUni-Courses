from math_operations import *


a, sign, b = input().split()
a, b = float(a), float(b)
print(f"{calculate(a, b, sign):.2f}")
