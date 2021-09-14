evens = set()
odds = set()
for i in range(1, int(input()) + 1):
    value = sum(ord(char) for char in input()) // i
    if value % 2 == 0:
        evens.add(value)
    else:
        odds.add(value)

if sum(evens) > sum(odds):
    result = odds ^ evens
    print(', '.join(str(n) for n in result))
elif sum(evens) < sum(odds):
    result = odds - evens
    print(', '.join(str(n) for n in result))
else:
    result = odds & evens
    print(', '.join(str(n) for n in result))
