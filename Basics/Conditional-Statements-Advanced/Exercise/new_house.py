flowers_kind = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers_kind == "Roses":
    price = flowers_count * 5
    if flowers_count > 80:
        price -= price * 0.10
elif flowers_kind == "Dahlias":
    price = flowers_count * 3.80
    if flowers_count > 90:
        price -= price * 0.15
elif flowers_kind == "Tulips":
    price = flowers_count * 2.80
    if flowers_count > 80:
        price -= price * 0.15
elif flowers_kind == "Narcissus":
    price = flowers_count * 3
    if flowers_count < 120:
        price += price * 0.15
elif flowers_kind == "Gladiolus":
    price = flowers_count * 2.50
    if flowers_count < 80:
        price += price * 0.20

left_needed_sum = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_kind} and {left_needed_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_needed_sum:.2f} leva more.")
