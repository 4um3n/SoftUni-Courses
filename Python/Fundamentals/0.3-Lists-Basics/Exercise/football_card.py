cards = input().split()
team_a_players = list(range(1, 12))
team_b_players = list(range(1, 12))

for card in cards:
    card = card.split("-")
    value_to_remove = int(card[1])

    if card[0] == "A":
        if value_to_remove in team_a_players:
            team_a_players.remove(value_to_remove)
    elif card[0] == "B":
        if value_to_remove in team_b_players:
            team_b_players.remove(value_to_remove)

    if len(team_a_players) < 7 or len(team_b_players) < 7:
        print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
        print(f"Game was terminated")
        exit()

print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
