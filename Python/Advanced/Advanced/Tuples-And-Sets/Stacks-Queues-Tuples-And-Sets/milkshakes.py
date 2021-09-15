from collections import deque

chocolates = deque([int(n) for n in input().split(", ")])
milks = deque([int(n) for n in input().split(", ")])
milkshakes_count = 0
while chocolates and milks:
    if chocolates[-1] <= 0 or milks[0] <= 0:
        if chocolates[-1] <= 0:
            chocolates.pop()
        if milks[0] <= 0:
            milks.popleft()
        continue

    choco, milk = chocolates.pop(), milks.popleft()
    if choco == milk:
        milkshakes_count += 1
    else:
        milks.append(milk)
        chocolates.append(choco - 5)

    if milkshakes_count == 5:
        print(f"Great! You made all the chocolate milkshakes needed!")
        break
else:
    print(f"Not enough milkshakes.")


if chocolates:
    print(f"Chocolate: {', '.join([str(n) for n in chocolates])}")
else:
    print(f"Chocolate: empty")

if milks:
    print(f"Milk: {', '.join([str(n) for n in milks])}")
else:
    print(f"Milk: empty")
