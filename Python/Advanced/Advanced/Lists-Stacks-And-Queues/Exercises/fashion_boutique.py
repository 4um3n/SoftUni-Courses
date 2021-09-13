from collections import deque

clothes = deque(int(n) for n in input().split())
rack_capacity = int(input())
racks_count = 0 if len(clothes) == 0 else 1
current_rack = []
while len(clothes) > 0:
    if sum(current_rack) + clothes[-1] > rack_capacity:
        racks_count += 1
        current_rack.clear()
        continue

    current_rack.append(clothes.pop())

print(racks_count)
