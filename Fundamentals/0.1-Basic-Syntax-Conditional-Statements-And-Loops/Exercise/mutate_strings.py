first_word = input()
second_word = input()
control_word = first_word

for position in range(len(first_word)):
    current_word = control_word
    control_word = control_word[:position] + second_word[position] + control_word[position + 1:]

    if control_word == current_word:
        continue

    print(control_word)
