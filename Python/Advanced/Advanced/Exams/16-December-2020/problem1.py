from collections import deque


def calculate_total_matches(females, males, matches=0):
    if not females or not males:
        return f"Matches: {matches}\n" \
               f"Males left: {'none' if not males else ', '.join([str(n) for n in list(males)[::-1]])}\n" \
               f"Females left: {'none' if not females else ', '.join([str(n) for n in females])}"

    if females[0] <= 0 or males[-1] <= 0:
        if females[0] <= 0:
            females.popleft()
        if males[-1] <= 0:
            males.pop()

        return calculate_total_matches(females, males, matches)

    if females[0] % 25 == 0 or males[-1] % 25 == 0:
        if females[0] % 25 == 0:
            for _ in range(2):
                if females:
                    females.popleft()

        if males[-1] % 25 == 0:
            for _ in range(2):
                if males:
                    males.pop()

        return calculate_total_matches(females, males, matches)

    if females[0] == males[-1]:
        matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

    return calculate_total_matches(females, males, matches)


males_data = deque([int(n) for n in input().split()])
females_data = deque([int(n) for n in input().split()])
print(calculate_total_matches(females_data, males_data))


'''
from collections import deque

males = deque([int(n) for n in input().split()])
females = deque([int(n) for n in input().split()])
total_matches = 0
while males and females:
    if females[0] <= 0 or males[-1] <= 0:
        if females[0] <= 0:
            females.popleft()
        if males[-1] <= 0:
            males.pop()
        continue

    if females[0] % 25 == 0 or males[-1] % 25 == 0:
        if females[0] % 25 == 0:
            for _ in range(2):
                if females:
                    females.popleft()

        if males[-1] % 25 == 0:
            for _ in range(2):
                if males:
                    males.pop()

        continue

    if females[0] == males[-1]:
        total_matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {total_matches}")
print(f"Males left: {'none' if not males else ', '.join([str(n) for n in list(males)[::-1]])}")
print(f"Females left: {'none' if not females else ', '.join([str(n) for n in females])}")
'''
