from collections import deque

effects = deque([int(n) for n in input().split(", ")])
casings = deque([int(n) for n in input().split(", ")])
bombs_types = {40: {"name": "Datura Bombs", "quantity": 0},
               60: {"name": "Cherry Bombs", "quantity": 0},
               120: {"name": "Smoke Decoy Bombs", "quantity": 0}
               }

while effects and casings:
    res = effects[0] + casings[-1]
    if res in bombs_types:
        bombs_types[res]["quantity"] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5

    bombs_count = [data["quantity"] for _, data in bombs_types.items()]
    if bombs_count[0] >= 3 and bombs_count[1] >= 3 and bombs_count[2] >= 3:
        print(f"Bene! You have successfully filled the bomb pouch!")
        break
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {'empty' if not effects else ', '.join([str(n) for n in effects])}")
print(f"Bomb Casings: {'empty' if not casings else ', '.join([str(n) for n in casings])}")
bombs_types = {data["name"]: data["quantity"] for _, data in sorted(bombs_types.items(), key=lambda x: x[1]["name"])}
[print(f"{n}: {q}") for n, q in bombs_types.items()]
