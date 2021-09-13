from collections import deque

water_quantity = int(input())
queue = deque()
name = input()
while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    if command.isdigit():
        liters = int(command)
        if water_quantity < liters:
            print(f"{queue[0]} must wait")
            queue.popleft()
        else:
            print(f"{queue[0]} got water")
            water_quantity -= liters
            queue.popleft()
    
    elif "refill" in command:
        liters = int(command.split()[1])
        water_quantity += liters
    
    command = input()

print(f"{water_quantity} liters left")
