from collections import deque


def pop_element(i: int, nums: deque):
    if nums[i] <= 0 and i == 0:
        nums.popleft()
    elif nums[i] <= 0 and i == -1:
        nums.pop()
    return nums


fireworks = deque([int(n) for n in input().split(', ')])
explosive_powers = deque([int(n) for n in input().split(', ')])

bombs = {
    "P": {"name": "Palm Fireworks", "count": 0},
    "W": {"name": "Willow Fireworks", "count": 0},
    "C": {"name": "Crossette Fireworks", "count": 0}
}

while fireworks and explosive_powers:
    if fireworks[0] <= 0 or explosive_powers[-1] <= 0:
        fireworks = pop_element(0, fireworks)
        explosive_powers = pop_element(-1, explosive_powers)
        continue

    result = fireworks[0] + explosive_powers[-1]

    if result % 3 == 0 and result % 5 == 0:
        bombs["C"]["count"] += 1

    elif result % 3 == 0:
        bombs["P"]["count"] += 1

    elif result % 5 == 0:
        bombs["W"]["count"] += 1

    else:
        fireworks.append(fireworks.popleft() - 1)
        continue

    fireworks.popleft()
    explosive_powers.pop()

    if all([3 <= v["count"] for k, v in bombs.items()]):
        print(f"Congrats! You made the perfect firework show!")
        break
else:
    print(f"Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(n) for n in fireworks])}")

if explosive_powers:
    print(f"Explosive Power left: {', '.join([str(n) for n in explosive_powers])}")

for v in bombs.values():
    print(f"{v['name']}: {v['count']}")
