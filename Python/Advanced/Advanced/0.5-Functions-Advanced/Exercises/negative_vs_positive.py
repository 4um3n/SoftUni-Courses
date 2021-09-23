def negatives_vs_positives(nums, negative_r=0, positive_r=0):
    if not nums:
        return negative_r, positive_r

    if nums[0] < 0:
        res = negatives_vs_positives(nums[1:], negative_r+nums[0], positive_r)
    else:
        res = negatives_vs_positives(nums[1:], negative_r, positive_r+nums[0])

    return res


data = list(map(int, input().split()))
negative, positive = negatives_vs_positives(data, negative_r=0, positive_r=0)
print(f"{negative}\n{positive}")
if abs(negative) > positive:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
