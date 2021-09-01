neighborhood = [int(n) for n in input().split("@")]
i = 0
command = input()
while command != "Love!":
    i += int(command.split()[1])
    if i >= len(neighborhood):
        i = 0
    
    if neighborhood[i] <= 0:
        print(f"Place {i} already had Valentine's day.")
        command = input()
        continue

    neighborhood[i] -= 2
    if neighborhood[i] <= 0:
        print(f"Place {i} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {i}.")
if len(neighborhood) == neighborhood.count(0):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")
