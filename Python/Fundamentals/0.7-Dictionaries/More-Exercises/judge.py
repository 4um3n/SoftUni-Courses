command, contests = input(), {}
while command != "no more time":
    name, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in contests:
        contests[contest] = {}
    
    if name not in contests[contest] or contests[contest][name] < points:
        contests[contest][name] = points
    
    command = input()

individual_standing = {}
for c, i in contests.items():
    for u, p in i.items():
        if u not in individual_standing:
            individual_standing[u] = 0
        
        individual_standing[u] += p

for c, users in contests.items():
    print(f"{c}: {len(users)} participants")
    position = 0
    for u, p in sorted(users.items(), key=lambda x: (-x[1], x[0])):
        position += 1
        print(f"{position}. {u} <::> {p}")

print(f"Individual standings:")
position = 0
for u, p in sorted(individual_standing.items(), key=lambda x: (-x[1], x[0])):
    position += 1
    print(f"{position}. {u} -> {p}")
