import re

racers = {r: 0 for r in input().split(", ")}
pattern = r"([A-Za-z])|(\d)"
data = input()
while data != "end of race":
    data = [g.group() for g in re.finditer(pattern, data)]
    name = ''.join(ch for ch in data if not ch.isdigit())
    score = sum(int(d) for d in data if d.isdigit())
    if name in racers:
        racers[name] += score

    data = input()

racers = {r: s for r, s in sorted(racers.items(), key=lambda x: -x[1])}
for i, n in zip(["1st", "2nd", "3rd"], racers.keys()):
    print(f"{i} place: {n}")
