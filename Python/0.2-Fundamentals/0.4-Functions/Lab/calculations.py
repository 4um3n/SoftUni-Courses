def calculator(operation: str, a: int, b: int):
    result = None
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a // b
    return result

div, c, d = input(), int(input()), int(input())
print(calculator(div, c, d))
