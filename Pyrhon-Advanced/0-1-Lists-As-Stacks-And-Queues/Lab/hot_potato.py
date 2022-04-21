from collections import deque

people = deque(input().split())
toss= int(input())
while len(people) > 1:
    for _ in range(toss - 1):
        people.append(people.popleft())

    name = people.popleft()
    print(f"Removed {name}")

print(f"Last is {people[0]}")
