version = [int(n) for n in input().split(".")]
version[-1] += 1
i = -1
while version[i] > 9:
    version[i] = 0
    i -= 1
    version[i] += 1

print('.'.join(str(s) for s in version))
