lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toys_count = 0
birthday_moneys = 0
birthday_moneys_sum = 0

for birthday in range(1, lily_age + 1):

    if birthday % 2 == 0:
        birthday_moneys += 10
        birthday_moneys_sum += birthday_moneys
        birthday_moneys_sum -= 1

    else:
        toys_count += 1

toys_moneys = toys_count * toy_price
birthday_moneys_sum += toys_moneys

diff = abs(birthday_moneys_sum - washing_machine_price)

if birthday_moneys_sum >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
