from collections import deque

pumps = [input().split() for _ in range(int(input()))]
pumps = deque([int(data[0]), int(data[1])] for data in pumps)
counter, tank, i, is_found, min_i  = 0, 0, 0, 0, 0
while counter < len(pumps):
    petrol, distance = pumps[0]
    pumps.append(pumps.popleft())
    tank += petrol
    if tank >= distance:
        if not is_found:
            min_i = i
            is_found = 1

        tank -= distance
        counter += 1 

    else:
        min_i, is_found, tank, counter  = 0, 0, 0, 0

    i += 1
    if i == len(pumps):
        i = 0

print(min_i)
