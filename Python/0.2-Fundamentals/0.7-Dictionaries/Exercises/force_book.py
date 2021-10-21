def pipe(side, user, sides):
    users = [u for s in sides for u in sides[s]]
    if user not in users:
        if side not in sides:
            sides[side] = []
        
        sides[side].append(user)
    
    return sides


def arrow(side, user, sides):
    if side not in sides:
        sides[side] = []

    for s in sides:
        if user in sides[s]:
            sides[side].append(sides[s].pop(sides[s].index(user)))
            return sides
    
    sides_data[side].append(user)    
    return sides
        

command, sides_data = input(), {}
while command != "Lumpawaroo":
    if "|" in command:
        f_side, f_user = command.split(" | ")
        sides_data = pipe(f_side, f_user, sides_data)
    
    elif "->" in command:
        f_user, f_side = command.split(" -> ")
        sides_data = arrow(f_side, f_user, sides_data)
        print(f"{f_user} joins the {f_side} side!")

    command = input()

for s, users in sorted(sides_data.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(users) > 0:
        print(f"Side: {s}, Members: {len(users)}")
        for u in sorted(users):
            print(f"! {u}")
