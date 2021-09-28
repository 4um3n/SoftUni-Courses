from collections import deque

pumps = deque([[int(n) for n in input().split()] for _ in range(int(input()))])
counter, tank, i, min_i = 0, 0, 0, None
while counter < len(pumps):
    petrol, distance = pumps[0]
    pumps.append(pumps.popleft())
    tank += petrol
    if tank >= distance:
        if min_i is None:
            min_i = i

        tank -= distance
        counter += 1

    else:
        min_i, tank, counter = None, 0, 0

    i = 0 if i+1 == len(pumps) else i+1

print(min_i)
