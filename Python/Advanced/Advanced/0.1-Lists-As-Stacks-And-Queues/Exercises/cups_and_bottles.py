from collections import deque

cups = deque(int(n) for n in input().split())
bottles = deque(int(n) for n in input().split())
wasted_water = 0
while cups:
    if not bottles:
        print(f"Cups: {' '.join(str(n) for n in cups)}")
        break

    bottle = bottles.pop()
    if bottle < cups[0]:
        cups[0] -= bottle
    else:
        wasted_water += bottle - cups[0]
        cups.popleft()
else:
    bottles = [str(bottles[i]) for i in range(len(bottles) -1, -1, -1)]
    print(f"Bottles: {' '.join(bottles)}")

print(f"Wasted litters of water: {wasted_water}")
