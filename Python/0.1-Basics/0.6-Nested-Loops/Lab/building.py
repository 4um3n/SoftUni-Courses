floors_count = int(input())
rooms_per_floor_count = int(input())

for floor in range(floors_count, 0, -1):
    for room in range(rooms_per_floor_count):
        if floor == floors_count:
            print(f"L{floor}{room}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")
        else:
            print(f"A{floor}{room}", end=" ")
    print()
