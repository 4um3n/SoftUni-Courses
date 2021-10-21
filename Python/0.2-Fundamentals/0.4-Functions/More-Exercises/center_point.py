from math import floor


def center_point(a, a1, b, b1):
    a_result = abs(a) + abs(a1)
    b_result = abs(b) + abs(b1)
    if b_result < a_result:
        return b, b1
    return a, a1


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x, y = center_point(x1, y1, x2, y2)
print(f"({floor(x)}, {floor(y)})")