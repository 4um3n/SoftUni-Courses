def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    result = subtract(result, c)
    return result


sum_numbers = lambda a, b: a + b
subtract = lambda a, b: a - b
print(add_and_subtract(int(input()), int(input()), int(input())))
