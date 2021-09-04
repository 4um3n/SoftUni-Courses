plates = {}
for _ in range(int(input())):
    command = input().split()
    if "register" in command:
        user, plate = command[1], command[2]
        if user in plates:
            print(f"ERROR: already registered with plate number {plates[user]}")
        else:
            plates[user] = plate
            print(f"{user} registered {plates[user]} successfully")
    
    elif "unregister" in command:
        user = command[1]
        if user not in plates:
            print(f"ERROR: user {user} not found")
        else:
            del plates[user]
            print(f"{user} unregistered successfully")

for u, p in plates.items():
    print(f"{u} => {p}")
