from collections import deque

bullet_price, barrel_size = int(input()), int(input())
current_barrel = barrel_size
bullets = deque(int(n) for n in input().split())
locks = deque(int(n) for n in input().split())
intelligence_price = int(input())
while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        exit()

    bullet = bullets.pop()
    intelligence_price -= bullet_price
    current_barrel -= 1
    if bullet <= locks[0]:
        print(f"Bang!")
        locks.popleft()
    else:
        print(f"Ping!")

    if current_barrel == 0 and bullets:
        print(f"Reloading!")
        current_barrel = barrel_size

print(f"{len(bullets)} bullets left. Earned ${intelligence_price}")
