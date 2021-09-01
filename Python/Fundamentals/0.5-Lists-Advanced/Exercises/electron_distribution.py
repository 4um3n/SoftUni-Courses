electrons_count = int(input())
electron_shells, i = [], 0
while electrons_count > 0:
    i += 1
    shell_capacity = 2 * (i)**2
    electron_shells.append(electrons_count) if electrons_count < shell_capacity else electron_shells.append(shell_capacity) 
    electrons_count -= shell_capacity

print(electron_shells)
