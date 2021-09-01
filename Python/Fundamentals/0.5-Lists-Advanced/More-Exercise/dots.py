def check_chain(x, y):
    if field[x][y] and not visited[x][y]:
        visited[x][y] = True
        return check_chain(x - 1, y) + check_chain(x + 1, y) + check_chain(x, y - 1) + check_chain(x, y + 1) + 1
    else:
        return 0


rows_count, field = int(input()), []
for _ in range(rows_count):
    row = f"- {input()} -".split()
    field.append([1 if _ == "." else 0 for _ in row])

field.append([0 for _ in range(len(field[0]))])
field.insert(0, [0 for _ in range(len(field[0]))])
visited = [[0 for _ in range(len(field[0]))] for _ in range(len(field))]

dots = [[r, c] for r in range(len(field)) for c in range(len(field[0])) if field[r][c]]
max_chain_length = 0
for xy in dots:
    chain_length = check_chain(*xy)
    if max_chain_length < chain_length:
        max_chain_length = chain_length

print(max_chain_length)
