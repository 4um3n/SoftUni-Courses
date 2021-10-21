import math

figure = input()
figure = figure.lower()

area = 0

if figure == "square":
    a = float(input())
    area = a**2
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = math.pi * r * r
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = (a * h) / 2

print(f"{area:.3f}")
