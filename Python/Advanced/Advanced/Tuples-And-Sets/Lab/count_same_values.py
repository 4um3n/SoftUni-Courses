from collections import defaultdict

nums = tuple(float(n) for n in input().split())
nums_counts = defaultdict(int)
for n in nums:
    nums_counts[n] += 1

[print(f"{n:.1f} - {c} times") for n, c in nums_counts.items()]
