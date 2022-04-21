command, colors = input(), {}
while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)

    if color not in colors:
        colors[color] = {}
    
    if name not in colors[color] or colors[color][name] < physics:
        colors[color][name] = physics

    command = input()

dwarfs = [(c, n, p, len(items)) for c, items in colors.items() for n, p in items.items()]
for items in sorted(dwarfs, key=lambda x: (-x[2], -x[3])):
    c, n, p, _ = items
    print(f"({c}) {n} <-> {p}")
