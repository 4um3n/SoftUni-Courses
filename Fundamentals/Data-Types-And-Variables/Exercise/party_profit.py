companions_count = int(input())
days_count = int(input())
earned_coins = 0

for day in range(1, days_count + 1):

    if day % 10 == 0:
        companions_count -= 2

    if day % 15 == 0:
        companions_count += 5

    earned_coins += 50
    earned_coins -= companions_count * 2

    if day % 3 == 0:
        earned_coins -= companions_count * 3

    if day % 5 == 0:
        earned_coins += companions_count * 20
        if day % 3 == 0:
            earned_coins -= companions_count * 2

companion_money = earned_coins / companions_count
print(f"{companions_count} companions received {int(companion_money)} coins each.")