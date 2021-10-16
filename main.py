def print_board(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['btm-L']}|{board['btm-M']}|{board['btm-R']}\n")


def win_condition(board):
    """Return True when there is a winner"""

    value = list(board.values())
    # Horizontal win condition
    if value[0] == value[1] and value[1] == value[2] and not value[0].isspace():
        return True
    elif value[3] == value[4] and value[4] == value[5] and not value[3].isspace():
        return True
    elif value[6] == value[7] and value[7] == value[8] and not value[6].isspace():
        return True

    # Vertical win condition
    elif value[0] == value[3] and value[3] == value[6] and not value[0].isspace():
        return True
    elif value[1] == value[4] and value[4] == value[7] and not value[1].isspace():
        return True
    elif value[2] == value[5] and value[5] == value[8] and not value[2].isspace():
        return True

    # Diagonal win condition
    elif value[0] == value[4] and value[4] == value[8] and not value[0].isspace():
        return True
    elif value[2] == value[4] and value[4] == value[6] and not value[2].isspace():
        return True
    else:
        return False


def move(turn, board, space_dic):
    """Accept int from users"""

    while True:
        try:
            print(f"{turn}'s turn. Select a space to move on.")
            for space in space_dic.values():
                print(space, end="  ")
            option = int(input('\nSelect a number from above: '))

            while option not in space_dic.keys():
                print("\nPlease select an existing number")
                option = int(input('Select a number from above: '))
            else:
                print()
                del space_dic[option]
                return option

        except ValueError:
            print("\nOnly Numbers are Allowed!")
            print_board(board)


def int_to_board(selection):
    """Convert int to specific space on the board"""

    if selection == 1:
        return 'top-L'
    elif selection == 2:
        return 'top-M'
    elif selection == 3:
        return 'top-R'
    elif selection == 4:
        return 'mid-L'
    elif selection == 5:
        return 'mid-M'
    elif selection == 6:
        return 'mid-R'
    elif selection == 7:
        return 'btm-L'
    elif selection == 8:
        return 'btm-M'
    elif selection == 9:
        return 'btm-R'


def change_turn(turn):
    """Change turn every time after user input"""
    if turn == 'X':
        return 'O'
    else:
        return 'X'


def game():
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'btm-L': ' ', 'btm-M': ' ', 'btm-R': ' '}

    space_to_select = {1: '1) Top Left', 2: '2) Top Middle', 3: '3) Top Right',
                       4: '4) Middle Left', 5: '5) Middle', 6: '6) Middle Right',
                       7: '7) Bottom Left', 8: '8) Bottom Left', 9: '9) Bottom Right'}
    turn = 'X'
    num_turn = 0
    print('Game Start!')
    while not win_condition(board) and num_turn < 9:
        num_turn += 1
        print_board(board)
        option = move(turn, board, space_to_select)
        board[int_to_board(option)] = turn
        turn = change_turn(turn)

    print_board(board)
    if win_condition(board):
        if turn == 'X':
            print('Congratulation!! O is the Winner!')
        else:
            print('Congratulation!! X is the Winner!')
    else:
        print('Draw! No Winners!')


if __name__ == '__main__':
    game()
