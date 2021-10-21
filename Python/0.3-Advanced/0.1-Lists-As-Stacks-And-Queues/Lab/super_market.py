from collections import deque

queue = deque()
name = input()
while name != "End":
    if name == "Paid":
        while queue:
            print(queue[0])
            queue.popleft()
    else:
        queue.append(name)

    name = input()

print(f"{len(queue)} people remaining.")
