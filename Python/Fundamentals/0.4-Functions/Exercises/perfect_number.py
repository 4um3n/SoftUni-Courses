def is_num_perfect(n: int):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    
    if sum(divisors) == n:
        return f"We have a perfect number!"
    return f"It's not so perfect."


print(is_num_perfect(int(input())))
