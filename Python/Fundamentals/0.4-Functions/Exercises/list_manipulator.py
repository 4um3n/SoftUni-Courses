def exchange(data: list, index: int):
    if index not in range(len(data)):
        print(f"Invalid index")
        return data

    data1 = data[index + 1:]
    data1.extend(data[:index + 1])
    return data1


def max_n(data: list, int_type: str):
    if int_type == "even":
        nums = [i for i in data if i % 2 == 0]
    elif int_type == "odd":
        nums = [i for i in data if i % 2 == 1]
        
    if len(nums) == 0:
        return None

    n = max(nums)
    ind = 0
    for i in range(len(data)):
        if data[i] == n:
            ind = i
    return ind


def min_n(data: list, int_type: str):
    if int_type == "even":
        nums = [i for i in data if i % 2 == 0]
    elif int_type == "odd":
        nums = [i for i in data if i % 2 == 1]
        
    if len(nums) == 0:
        return None
    
    n = min(nums)
    ind = 0
    for i in range(len(data)):
        if data[i] == n:
            ind = i
    return ind


def first_n(data: list, int_type: str, count: int):
    if count > len(data):
        return None
    
    if int_type == "even":
        evens = [n for n in data if n % 2 == 0]
        return [evens[i] for i in range(count) if i < len(evens)]
    
    odds = [n for n in data if n % 2 == 1]
    return [odds[i] for i in range(count) if i < len(odds)]


def last_n(data: list, int_type: str, count: int):
    if count > len(data):
        return None
    
    if int_type == "even":
        evens = [n for n in data if n % 2 == 0]
        if count > len(evens):
            count = len(evens)
        return evens[len(evens) - count:]
    
    odds = [n for n in data if n % 2 == 1]
    if count > len(odds):
        count = len(odds)
    return odds[len(odds) - count:]


numbers = [int(n) for n in input().split()]
command = input()
while command != "end":
    command = command.split()
    if "exchange" in command:
        ind = int(command[1])
        numbers = exchange(numbers, ind)
    
    elif "max" in command:
        n_type = command[1]
        ind = max_n(numbers, n_type)
        if ind is None:
            print(f"No matches")
        else:
            print(ind)
    
    elif "min" in command:
        n_type = command[1]
        ind = min_n(numbers, n_type)
        if ind is None:
            print(f"No matches")
        else:
            print(ind)

    elif "first" in command:
        c, n_type = int(command[1]), command[2]
        numbers2 = first_n(numbers, n_type, c)
        if numbers2 is None:
            print(f"Invalid count")
        else:
            print(numbers2)

    elif "last" in command:
        c, n_type = int(command[1]), command[2]
        numbers2 = last_n(numbers, n_type, c)
        if numbers2 is None:
            print(f"Invalid count")
        else:
            print(numbers2)

    command = input()

print(numbers)