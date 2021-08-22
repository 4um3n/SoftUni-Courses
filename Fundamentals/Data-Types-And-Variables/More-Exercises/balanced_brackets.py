lines_count = int(input())
is_bracket_open = False
is_balanced = True

for line in range(lines_count):
    command_input = input()

    if command_input == "(":

        if is_bracket_open:
            is_balanced = False
            break

        is_bracket_open = True

    elif command_input == ")":

        if not is_bracket_open:
            is_balanced = False
            break

        is_bracket_open = False

if is_balanced:
    print(f"BALANCED")
else:
    print(f"UNBALANCED")