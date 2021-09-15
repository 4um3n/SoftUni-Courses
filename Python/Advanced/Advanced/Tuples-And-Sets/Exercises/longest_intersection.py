longest_intersection = set()
for _ in range(int(input())):
    r1, r2 = input().split("-")
    r1 = tuple(int(n) for n in r1.split(","))
    r2 = tuple(int(n) for n in r2.split(","))
    set1 = set(range(r1[0], r1[1] + 1))
    set2 = set(range(r2[0], r2[1] + 1))
    intersection = set1 & set2
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection.copy()

print(f"Longest intersection is [{', '.join([str(n) for n in longest_intersection])}]"
      f" with length {len(longest_intersection)}")
