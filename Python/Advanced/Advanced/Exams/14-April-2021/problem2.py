def calculate_trow_score(dart, r, c):
    if r not in range(len(dart)) or c not in range(len(dart[r])):
        return 0

    if dart[r][c] == "D":
        return sum([int(dart[r1][c1]) for r1, c1 in ((r, 0), (r, -1), (0, c), (-1, c))]) * 2

    elif dart[r][c] == "T":
        return sum([int(dart[r1][c1]) for r1, c1 in ((r, 0), (r, -1), (0, c), (-1, c))]) * 3

    elif dart[r][c] == "B":
        return "B"

    else:
        return int(dart[r][c])


def play(players, scores, dart, winner=None, i=0):
    if winner is not None:
        return f"{winner} won the game with {scores[winner]['trows']} throws!"

    row, col = (int(n) for n in input()[1:-1].split(", "))
    player = players[0] if i % 2 == 0 else players[1]
    current_score = calculate_trow_score(dart, row, col)
    if isinstance(current_score, str):
        winner = player
        scores[player]['trows'] += 1

    elif isinstance(current_score, int):
        scores[player]['score'] -= current_score
        scores[player]['trows'] += 1
        if scores[player]['score'] <= 0:
            winner = player

    return play(players, scores, dart, winner, i+1)


players_data = input().split(", ")
matrix = [input().split() for _ in range(7)]
scores_data = {players_data[0]: {'score': 501, 'trows': 0}, players_data[1]: {'score': 501, 'trows': 0}}
print(play(players_data, scores_data, matrix))
