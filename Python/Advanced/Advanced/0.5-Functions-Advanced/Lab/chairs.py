def combinations(names, count, combs=[]):
    if len(combs) == count:
        print(', '.join(combs))
        return

    for i in range(len(names)):
        combs.append(names[i])
        combinations(names[i+1:], count, combs)
        combs.pop()

    return


names_data = input().split(", ")
n = int(input())
combinations(names_data, n)
