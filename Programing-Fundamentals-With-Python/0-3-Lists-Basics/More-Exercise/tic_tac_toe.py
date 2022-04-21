deck = [[int(n) for n in input().split()] for _ in range(3)]
winner = None
for i in range(len(deck)):
    current_deck = [True if deck[i][n] == 1 else False for n in range(len(deck[i]))]
    if all(current_deck):
        winner = deck[i][0]
        break

    current_deck = [True if deck[i][n] == 2 else False for n in range(3)]
    if all(current_deck):
        winner = deck[i][0]
        break

    current_deck = [True if deck[n][i] == 1 else False for n in range(3)]
    if all(current_deck):
        winner = deck[i][0]
        break

    current_deck = [True if deck[n][i] == 2 else False for n in range(3)]
    if all(current_deck):
        winner = deck[i][0]
        break

i = 0
while winner is None and i < 3:
    i += 1
    current_deck = [True if n == i else False for n in [deck[0][0], deck[1][1], deck[2][2]]]
    if all(current_deck):
        winner = deck[0][0]

i = 0
while winner is None and i < 3:
    i += 1
    current_deck = [True if n == i else False for n in [deck[2][0], deck[1][1], deck[0][2]]]
    if all(current_deck):
        winner = deck[2][0]

if winner == 1:
    print(f"First player won")
elif winner == 2:
    print(f"Second player won")
elif winner is None:
    print(f"Draw!")
