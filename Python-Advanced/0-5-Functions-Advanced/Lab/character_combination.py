def print_combination(text, index):
    if index >= len(text):
        print(''.join(text))
        return

    print_combination(text, index + 1)
    for i in range(index+1, len(text)):
        text[index], text[i] = text[i], text[index]
        print_combination(text, index+1)
        text[index], text[i] = text[i], text[index]


data = list(input())
print_combination(data, 0)
