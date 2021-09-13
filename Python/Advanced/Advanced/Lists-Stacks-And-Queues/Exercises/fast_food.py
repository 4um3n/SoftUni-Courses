from collections import deque

quantity = int(input())
orders = deque(int(n) for n in input().split())
print(max(orders))
while orders:
    if orders[0] > quantity:
        print(f"Orders left: {' '.join(str(n) for n in orders)}")
        exit()
    
    quantity -= orders[0]
    orders.popleft()

print(f"Orders complete")
