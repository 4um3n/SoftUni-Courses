train = [0 for _ in range(int(input()))]
command = input()
while command != "End":
    command = command.split()
    if "add" in command:
        people_count = int(command[1])
        train[-1] += int(people_count)
    elif "insert" in command:
        index = int(command[1])
        people_count = int(command[2])
        train[index] += people_count
    elif "leave" in command:
        index = int(command[1])
        people_count = int(command[2])
        train[index] -= people_count

    command = input()
    
print(train)