battlefield = [[int(n) for n in input().split()] for _ in range(int(input()))]
destroyed_ships = 0
for attack in input().split():
    r, c = attack.split("-")
    r, c = int(r), int(c)
    if battlefield[r][c] > 0:
        battlefield[r][c] -= 1
        if battlefield[r][c] == 0:
            destroyed_ships += 1

print(destroyed_ships)
