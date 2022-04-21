from collections import deque

found_colors = []
substrings = input().split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"], "purple": ["red", "blue"], "green": ["yellow", "blue"]}
left_half = deque(substrings[:len(substrings) // 2])
right_half = deque(substrings[len(substrings) // 2:])
while left_half or right_half:
    try:
        left = left_half.popleft()
    except IndexError:
        left = ""

    try:
        right = right_half.pop()
    except IndexError:
        right = ""

    if left + right in main_colors or left + right in secondary_colors:
        found_colors.append(left + right)
    elif right + left in main_colors or right + left in secondary_colors:
        found_colors.append(right + left)
    else:
        left = left[:-1]
        right = right[:-1]
        if left:
            left_half.append(left)
        if right:
            right_half.appendleft(right)
        if len(right_half) - len(left_half) == 2:
            left_half.append(right_half.popleft())

for secondary_c, main_c in secondary_colors.items():
    if secondary_c in found_colors:
        first_main, second_main = main_c
        if first_main not in found_colors or second_main not in found_colors:
            found_colors.remove(secondary_c)

print(found_colors)
