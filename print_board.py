import os


# Prints the board
def print_board(board):
    clearConsole()
    for i in range(0, 8, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if (i == 0 or i == 3):
            print("---------")
    print()


def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
