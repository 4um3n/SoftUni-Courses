from collections import deque

working_bees = deque([int(n) for n in input().split()])
nectar = deque([int(n) for n in input().split()])
process_symbols = deque(input().split())
total_honey = 0
while working_bees and nectar:
    bee = working_bees.popleft()
    while nectar:
        current_load = nectar.pop()
        if current_load >= bee:
            break
    else:
        working_bees.appendleft(bee)
        break

    symbol = process_symbols.popleft()
    if symbol == "+":
        total_honey += abs(bee + current_load)
    elif symbol == "-":
        total_honey += abs(bee - current_load)
    elif symbol == "*":
        total_honey += abs(bee * current_load)
    elif symbol == "/":
        if bee != 0 and current_load != 0:
            total_honey += abs(bee / current_load)

print(f"Total honey made: {total_honey}")
if working_bees:
    working_bees = [str(n) for n in working_bees]
    print(f"Bees left: {', '.join(working_bees)}")
if nectar:
    nectar = [str(n) for n in nectar]
    print(f"Nectar left: {', '.join(nectar)}")
