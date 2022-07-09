def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


num = int(input())
print(factorial(num))
