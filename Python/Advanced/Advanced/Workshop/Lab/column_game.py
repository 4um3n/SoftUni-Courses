import os
from time import sleep


def create_reset_field(rows, columns):
    field = [[0 for _ in range(columns)] for _ in range(rows)]
    return field


def print_field(field):
    [print(f"{'  '.join([str(n) for n in field[r]])}") for r in range(len(field))]
    print(f"\n{'  '.join(['|' for _ in range(len(field[0]))])}")
    print(f"{'  '.join([str(i) for i in range(len(field[0]))])}")


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def check_free_spots_on_field(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if not field[r][c]:
                return field

    return create_reset_field(len(field), len(field[0]))


def check_free_spots_on_column(field, column):
    for row in range(len(field) - 1, -1, -1):
        try:
            if not field[row][column]:
                return row, column
        except IndexError:
            return None


def create_line_of_four(field, direction, row, column):
    line = []
    moves = {
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
        'left': lambda r, c: (r, c - 1),
        'right': lambda r, c: (r, c + 1),
        'up_left': lambda r, c: (r - 1, c - 1),
        'down_right': lambda r, c: (r + 1, c + 1),
        'up_right': lambda r, c: (r - 1, c + 1),
        'down_left': lambda r, c: (r + 1, c - 1)
    }
    for _ in range(4):
        if row not in range(len(field)) or column not in range(len(field[row])):
            line.clear()
            return line

        line.append(field[row][column])
        row, column = moves[direction](row, column)

    return line


def check_for_winner(field, player, row, column):
    directions = ['up', 'down', 'left', 'right', 'up_left', 'up_right', 'down_left', 'down_right']
    for direction in directions:
        line = create_line_of_four(field, direction, row, column)
        if line and all([player == spot for spot in line]):
            return player


def play(players):
    winner = None

    # Get field dimensions, check if they are valid and if so, then create the field
    field_dimensions = []
    while not field_dimensions:
        text = "Please enter how many rows (minimum 4) and columns (minimum 4) field must have (Example: 5, 4): "
        try:
            field_dimensions = [int(n) for n in input(f"{text}").split(', ')]
            if len(field_dimensions) != 2 or field_dimensions[0] < 4 or field_dimensions[1] < 4:
                raise ValueError
        except ValueError:
            field_dimensions.clear()
            print(f"Field's rows and columns must be just like in the example: 5, 4")
            continue

    field = create_reset_field(*field_dimensions)

    # Play the game
    while winner is None:
        clear_console()
        print_field(field)
        player = players[0]

        # Check for free spots on the field and if there are no free spots, then reset the field
        field = check_free_spots_on_field(field)

        # Get input for the column and check if it is integer bigger than -1
        try:
            column = int(input(f"\nPlayer {player}, please choose a column: "))
            if column < 0:
                raise ValueError
        except ValueError:
            print(f"You have entered an invalid column!")
            sleep(2)
            continue

        # Check for free spots and wrong column
        try:
            row, column = check_free_spots_on_column(field, column)
        except TypeError:
            print(f"You have entered an invalid column!")
            sleep(2)
            continue

        # Assign current player value to the correct spot on the field and check if the player is a winner
        field[row][column] = player
        winner = check_for_winner(field, player, row, column)
        players.append(players.pop(0))

    clear_console()
    print_field(field)
    print(f"The winner is player {winner}")


answer = input(f"Do you want to play? (Y/y for yes): ").lower()
while answer == 'y':
    play([1, 2, 3])
    answer = input(f"Do you want to play again? (Y/y for yes): ").lower()
