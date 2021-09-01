targets = [int(n) for n in input().split()]
command = input()
while command != "End":
    command = command.split()
    if "Shoot" in command:
        index, power = int(command[1]), int(command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    
    elif "Add" in command:
        index, value = int(command[1]), int(command[2])
        if index not in range(len(targets)):
            print(f"Invalid placement!")
        else:
            targets.insert(index, value)
    
    elif "Strike" in command:
        index, radius = int(command[1]), int(command[2])
        if index - radius not in range(len(targets)) or index + radius not in range(len(targets)):
            print("Strike missed!")
        else:
            cutted = targets[:index - radius]
            cutted.extend(targets[index + radius + 1:])
            targets = cutted
    
    command = input()

print('|'.join(str(n) for n in targets))
