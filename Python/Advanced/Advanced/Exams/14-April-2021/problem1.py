from collections import deque

pizza_orders = deque([int(n) for n in input().split(", ")])
employees_possibilities = deque([int(n) for n in input().split(", ")])
total_pizzas_made = 0

while pizza_orders:
    if pizza_orders[0] not in range(1, 11):
        pizza_orders.popleft()
        continue

    if pizza_orders[0] > employees_possibilities[-1]:
        total_pizzas_made += employees_possibilities[-1]
        pizza_orders[0] -= employees_possibilities[-1]
        employees_possibilities.pop()
    else:
        total_pizzas_made += pizza_orders[0]
        pizza_orders.popleft()
        employees_possibilities.pop()

    if pizza_orders and not employees_possibilities:
        print(f"Not all orders are completed.\n"
              f"Orders left: {', '.join([str(n) for n in pizza_orders])}")
        break
else:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizzas_made}\n"
          f"Employees: {', '.join([str(n) for n in employees_possibilities])}")
