number = int(input())
special_numbers = [5, 7, 11]

for n in range(1, number + 1):
    sum_of_digits = sum(int(d) for d in str(n))
    is_special = False
    if sum_of_digits in special_numbers:
        is_special = True

    print(f"{n} -> {is_special}")
    