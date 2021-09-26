from collections import deque


customers = deque([int(n) for n in input().split(", ")])
taxis = deque([int(n) for n in input().split(", ")])
total_passed_time = 0
while taxis:
    if customers[0] <= taxis[-1]:
        total_passed_time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

    if not customers:
        print(f"All customers were driven to their destinations\n"
              f"Total time: {total_passed_time} minutes")
        break
else:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join([str(n) for n in customers])}")
