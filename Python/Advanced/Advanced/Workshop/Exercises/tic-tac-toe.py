import os
from math import ceil
from time import sleep


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def setup():
    global player_one, player_two, board
    player_one_name = input(f"Enter player one name: ")
    player_two_name = input(f"Enter player two name: ")
    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    while player_one_sign != 'X' and player_one_sign != 'O':
        print(f"{player_one_name}, you can choose only between 'X' or 'O' ")
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = {'name': player_one_name, 'sign': player_one_sign}
    player_two = {'name': player_two_name, 'sign': player_two_sign}
    print(f"{player_one['name']} starts first.")
    sleep(2)
    clear_console()


def print_board():
    [print(f"| {' | '.join(board[r])} |") for r in range(len(board))]


def print_numerated_free_positions():
    positions_board, i = [], 0
    for r in range(len(board)):
        line = []
        for c in range(len(board[r])):
            i += 1
            if board[r][c] == ' ':
                line.append(str(i))
            else:
                line.append(board[r][c])

        positions_board.append(line)

    [print(f"| {' | '.join(positions_board[r])} |") for r in range(len(board))]


def check_for_free_positions():
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == " ":
                return True
    return False


def create_line_of_three(direction, row, col):
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
    for _ in range(3):
        if row not in range(len(board)) or col not in range(len(board[row])):
            line.clear()
            return line

        line.append(board[row][col])
        row, col = moves[direction](row, col)

    return line


def check_for_winner(player):
    directions = ['up', 'down', 'left', 'right', 'up_left', 'up_right', 'down_left', 'down_right']
    for row in range(len(board)):
        for col in range(len(board)):
            for direction in directions:
                line = create_line_of_three(direction, row, col)
                if line and all([spot == player['sign'] for spot in line]):
                    return player['name']


def play(player):
    row, col = None, None
    while row is None and col is None:
        try:
            position = int(input(f"{player_one['sign']} choose a free position [1-9]: "))
            row = ceil(position / 3) - 1
            col = (position % 3) - 1
            if position not in range(1, 10) or board[row][col] != ' ':
                raise ValueError
        except ValueError:
            print(f"Enter free and valid position [1-9]")
            row, col = None, None
            continue

    board[row][col] = player['sign']
    return check_for_winner(player)


answer = input(f"Do you want to play? (Y/y for yes): ").lower()
while answer == 'y':
    clear_console()
    player_one, player_two, winner = None, None, None
    board = [[" " for _ in range(3)] for _ in range(3)]
    setup()
    while winner is None:
        print_numerated_free_positions()
        winner = play(player_one)
        player_one, player_two = player_two, player_one
        clear_console()
        if not check_for_free_positions():
            print_board()
            print(f"It's a tie!")
            break
    else:
        print_board()
        print(f"{winner} won!")

    answer = input(f"\nDo you want to play again? (Y/y for yes): ").lower()
