longest_intersection = set()
for _ in range(int(input())):
    range1, range2 = [[int(n) for n in r.split(",")] for r in input().split("-")]
    set1 = set(range(range1[0], range1[1] + 1))
    set2 = set(range(range2[0], range2[1] + 1))
    intersection = set1 & set2
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection.copy()

print(f"Longest intersection is [{', '.join([str(n) for n in longest_intersection])}]"
      f" with length {len(longest_intersection)}")
