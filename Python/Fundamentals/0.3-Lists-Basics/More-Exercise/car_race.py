numbers = [int(n) for n in input().split()]
middle = len(numbers) // 2
left_racer_score = numbers[:middle]
right_racer_score = reversed(numbers[middle + 1:])
left_racer_time = 0
right_racer_time = 0

for left, right in zip(left_racer_score, right_racer_score):

    if left != 0:
        left_racer_time += left
    else:
        left_racer_time *= 0.8

    if right != 0:
        right_racer_time += right
    else:
        right_racer_time *= 0.8

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
elif right_racer_time < left_racer_time:
    print(f"The winner is right with total time: {right_racer_time:.1f}")

