def recursive_power(n, p, result=1):
    if p <= 0:
        return result

    return recursive_power(n, p-1, result * n)
