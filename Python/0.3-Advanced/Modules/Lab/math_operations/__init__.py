def calculate(a, b, sign):
    if sign == "*":
        return a * b

    elif sign == "/":
        if a == 0 or b == 0:
            return 0
        return a / b

    elif sign == "+":
        return a + b

    elif sign == "-":
        return a - b

    elif sign == "^":
        return a ** b
