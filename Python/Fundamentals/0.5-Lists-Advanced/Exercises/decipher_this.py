message = input().split()
for i in range(len(message)):
    first_letter, message[i] = [], list(message[i])
    while message[i][0].isdigit():
        first_letter.append(message[i].pop(0))

    message[i][0], message[i][-1] = message[i][-1], message[i][0]
    message[i] = chr(int(''.join(first_letter))) + "".join(message[i])

print(' '.join(message))
