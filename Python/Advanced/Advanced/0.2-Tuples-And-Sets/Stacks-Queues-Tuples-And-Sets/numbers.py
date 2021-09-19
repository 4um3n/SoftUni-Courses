from collections import deque

set1 = set([int(n) for n in input().split()])
set2 = set([int(n) for n in input().split()])
sets = {"First": set1, "Second": set2}
for _ in range(int(input())):
    data = deque(input().split())
    command = data.popleft()
    set_n = data.popleft()
    data = [int(n) for n in data]
    if command == "Add":
        sets[set_n].update(data)

    elif command == "Remove":
        for n in data:
            if n in sets[set_n]:
                sets[set_n].remove(n)

    elif command == "Check":
        equals = sets["First"] & sets["Second"]
        if equals == sets["First"] or equals == sets["Second"]:
            print(True)
        else:
            print(False)

print(', '.join(list(str(n) for n in sorted(sets["First"]))))
print(', '.join(list(str(n) for n in sorted(sets["Second"]))))
