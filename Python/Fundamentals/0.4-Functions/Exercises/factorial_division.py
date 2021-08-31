# 5! = 5 * 4 * 3 * 2 *1 or 5 * 4!
def factorial(n):
    if n == 1:
        return 1
    
    n_factorial = n * factorial(n - 1)
    return n_factorial


a = factorial(int(input()))
b = factorial(int(input()))
c = a / b
print(f"{c:.2f}")
