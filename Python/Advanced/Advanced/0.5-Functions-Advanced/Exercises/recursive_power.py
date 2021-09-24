def recursive_power(n, p):
    if p == 1:
        return n
    return n * recursive_power(n, p-1)
