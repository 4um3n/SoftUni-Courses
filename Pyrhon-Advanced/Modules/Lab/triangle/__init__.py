def print_triangle(n):
    line = []
    for r in range(1, n+1):
        for c in range(1, r+1):
            line.append(str(c))
        print(' '.join(line))
        line.clear()

    for r in range(n-1, 0, -1):
        for c in range(1, r + 1):
            line.append(str(c))
        print(' '.join(line))
        line.clear()


