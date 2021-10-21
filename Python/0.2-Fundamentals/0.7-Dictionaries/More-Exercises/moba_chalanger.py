def add_player(pl, pos, sk, pool):
    sk = int(sk)
    if pl not in pool:
        pool[pl] = {}
    
    if pos not in pool[pl] or pool[pl][pos] < sk:
        pool[pl][pos] = sk
    
    return pool


def fight(pl1, pl2, pool):
    equal_positions = [f for f in pool[pl1].keys() for s in pool[pl2].keys() if f == s]
    for pos in equal_positions:
        if pool[pl1][pos] < pool[pl2][pos]:
            del pool[pl1]
            break
        elif pool[pl2][pos] < pool[pl1][pos]:
            del pool[pl2]
            break

    return pool


command, players_pool = input(), {}
while command != "Season end":
    if " vs " in command:
        player1, player2 = command.split(" vs ")
        if player1 in players_pool and player2 in players_pool:
            players_pool = fight(player1, player2, players_pool)
    else:
        player, position, skill = command.split(" -> ")
        players_pool = add_player(player, position, skill, players_pool)

    command = input()

for ple, items in sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{ple}: {sum(items.values())} skill")
    for ple2, s in sorted(items.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {ple2} <::> {s}")
