import os
from time import sleep


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def create_reset_field(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def print_board(board):
    [print(f"{'  '.join([str(n) for n in board[r]])}") for r in range(len(board))]
    print(f"\n{'  '.join(['|' for _ in range(len(board[0]))])}")
    print(f"{'  '.join([str(i) for i in range(len(board[0]))])}")


def check_free_spots_on_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if not board[r][c]:
                return board

    return create_reset_field(len(board), len(board[0]))


def check_free_spots_on_column(board, column):
    for row in range(len(board) - 1, -1, -1):
        try:
            if not board[row][column]:
                return row, column
        except IndexError:
            return


def create_line_of_four(board, direction, row, column):
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
        if row not in range(len(board)) or column not in range(len(board[row])):
            line.clear()
            return line

        line.append(board[row][column])
        row, column = moves[direction](row, column)

    return line


def check_for_winner(board, player, row, column):
    directions = ['up', 'down', 'left', 'right', 'up_left', 'up_right', 'down_left', 'down_right']
    for direction in directions:
        line = create_line_of_four(board, direction, row, column)
        if line and all([player == spot for spot in line]):
            return player


def setup():
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

    return create_reset_field(*field_dimensions)


def get_column_input(player):
    column = None
    while column is None:
        try:
            column = int(input(f"\nPlayer {player}, please choose a column: "))
            if column < 0:
                raise ValueError
        except ValueError:
            print(f"You have entered an invalid column!")
            sleep(2)
            continue

    return column


def play(player, board):
    board = check_free_spots_on_board(board)
    row, column = None, None
    while row is None:
        column = get_column_input(player)
        try:
            row, column = check_free_spots_on_column(board, column)
        except TypeError:
            print(f"You have entered an invalid column!")
            sleep(2)
            continue

    board[row][column] = player
    return check_for_winner(board, player, row, column)


answer = input(f"Do you want to play? (Y/y for yes): ").lower()
while answer == 'y':
    field = setup()
    winner = None
    players = [1, 2]
    while winner is None:
        clear_console()
        print_board(field)
        field = check_free_spots_on_board(field)
        current_player = players[0]
        winner = play(current_player, field)
        players.append(players.pop(0))

    clear_console()
    print_board(field)
    print(f"The winner is player {winner}")
    answer = input(f"Do you want to play again? (Y/y for yes): ").lower()
