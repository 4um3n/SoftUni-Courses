nums = tuple(float(n) for n in input().split())
nums_counts = {n: nums.count(n) for n in nums}
[print(f"{n:.1f} - {c} times") for n, c in nums_counts.items()]
