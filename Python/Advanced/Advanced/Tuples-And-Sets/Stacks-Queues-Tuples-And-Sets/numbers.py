from collections import deque

set1 = set([int(n) for n in input().split()])
set2 = set([int(n) for n in input().split()])
for _ in range(int(input())):
    data = deque(input().split())
    command = data.popleft()
    set_n = data.popleft()
    data = [int(n) for n in data]
    if command == "Add":
        if set_n == "First":
            set1.update(data)
        elif set_n == "Second":
            set2.update(data)

    elif command == "Remove":
        for n in data:
            if set_n == "First" and n in set1:
                set1.remove(n)
            elif set_n == "Second" and n in set2:
                set2.remove(n)

    elif command == "Check":
        equals = set1 & set2
        if equals == set1 or equals == set2:
            print(True)
        else:
            print(False)

set1 = list(str(n) for n in sorted(set1))
set2 = list(str(n) for n in sorted(set2))
print(', '.join(set1))
print(', '.join(set2))