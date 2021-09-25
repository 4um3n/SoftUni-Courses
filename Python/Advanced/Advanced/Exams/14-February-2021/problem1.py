from collections import deque

fireworks_effects = deque([int(n) for n in input().split(", ")])
explosive_powers = deque([int(n) for n in input().split(", ")])
palm_count, willow_count, crossette_count = 0, 0, 0
while fireworks_effects and explosive_powers:
    if fireworks_effects[0] <= 0 or explosive_powers[-1] <= 0:
        if fireworks_effects[0] <= 0:
            fireworks_effects.popleft()
        if explosive_powers[-1] <= 0:
            explosive_powers.pop()
        continue

    res = fireworks_effects[0] + explosive_powers[-1]
    if res % 3 == 0 and res % 5 == 0:
        crossette_count += 1
    elif res % 5 == 0:
        willow_count += 1
    elif res % 3 == 0:
        palm_count += 1
    else:
        fireworks_effects.append(fireworks_effects.popleft() - 1)
        continue

    fireworks_effects.popleft()
    explosive_powers.pop()
    if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
        print(f"Congrats! You made the perfect firework show!")
        break
else:
    print(f"Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(n) for n in fireworks_effects])}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join([str(n) for n in explosive_powers])}")

print(f"Palm Fireworks: {palm_count}\n"
      f"Willow Fireworks: {willow_count}\n"
      f"Crossette Fireworks: {crossette_count}")
