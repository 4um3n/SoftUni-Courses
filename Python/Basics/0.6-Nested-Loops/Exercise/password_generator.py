n = int(input())
l = int(input())

for a in range(1, n):
    char1 = a
    for b in range(1, n):
        char2 = b
        for c in range(97, 97 + l):
            char3 = chr(c)
            for d in range(97, 97 + l):
                char4 = chr(d)
                for e in range(1, n + 1):
                    if e <= char2 or e <= char1:
                        continue

                    char5 = e
                    print(f"{char1}{char2}{char3}{char4}{char5}", end=" ")
