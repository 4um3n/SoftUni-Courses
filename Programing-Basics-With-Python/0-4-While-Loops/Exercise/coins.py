balance = float(input())
coins_counter = 0
balance = int(balance * 100)

while balance > 0:
    if balance >= 200:
        balance -= 200
        coins_counter += 1
    elif balance >= 100:
        balance -= 100
        coins_counter += 1
    elif balance >= 50:
        balance -= 50
        coins_counter += 1
    elif balance >= 20:
        balance -= 20
        coins_counter += 1
    elif balance >= 10:
        balance -= 10
        coins_counter += 1
    elif balance >= 5:
        balance -= 5
        coins_counter += 1
    elif balance >= 2:
        balance -= 2
        coins_counter += 1
    elif balance >= 1:
        balance -= 1
        coins_counter += 1

print(coins_counter)

