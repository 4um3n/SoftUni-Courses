def negatives_vs_positives(nums, positives=0, negatives=0):
    if not nums:
        if abs(negatives) > positives:
            return f"{negatives}", f"{positives}", f"The negatives are stronger than the positives"
        return f"{negatives}", f"{positives}", f"The positives are stronger than the negatives"

    if nums[0] < 0:
        return negatives_vs_positives(nums[1:], positives, negatives+nums[0])
    return negatives_vs_positives(nums[1:], positives+nums[0], negatives)


print('\n'.join(negatives_vs_positives(list(map(int, input().split())))))
