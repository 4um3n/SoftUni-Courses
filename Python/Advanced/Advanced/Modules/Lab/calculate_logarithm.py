import math


a = int(input())
b = input()
try:
    print(f"{math.log(a, int(b)):.2f}")
except ValueError:
    print(f"{math.log(a):.2f}")
