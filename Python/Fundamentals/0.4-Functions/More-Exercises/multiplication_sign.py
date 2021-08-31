def multiplacation_sign(a, b ,c):
    if a < 0 and b > 0 < c:
        return "negative"
    elif b < 0 and a > 0 < c:
        return "negative"
    elif c < 0 and a > 0 < b:
        return "negative"
    elif a < 0 and b < 0 and c < 0:
        return "negative"
    elif a == 0 or b == 0 or c == 0:
        return "zero"
    return "positive"

print(multiplacation_sign(int(input()), int(input()), int(input())))
