def operate(sign, result=None, *args):
    numbers = list(map(int, args))
    if result is None and numbers:
        result = numbers.pop(0)

    if not numbers:
        return result

    n = numbers.pop(0)
    if sign == "*":
        result *= n
    elif sign == "/":
        result /= n
    elif sign == "+":
        result += n
    elif sign == "-":
        result -= n

    return operate(sign, result, *numbers)
