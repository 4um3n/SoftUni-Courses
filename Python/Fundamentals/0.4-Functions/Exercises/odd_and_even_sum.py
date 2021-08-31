def odd_and_even_sum(number: str):
    even_sum, odd_sum = 0, 0
    for n in number:
        if int(n) % 2 == 0:
            even_sum += int(n)
        else:
            odd_sum += int(n)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(odd_and_even_sum(input()))