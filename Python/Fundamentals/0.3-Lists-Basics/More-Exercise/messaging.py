numbers = input().split()
text = list(input())
message = []
for num in numbers:
    index = sum(int(n) for n in num)
    if index > len(text) - 1:
        index = index % len(text)

    message.append(text.pop(index))

print(''.join(message))
