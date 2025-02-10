# imps
import print_board
import checkwin
import check_full

# vars
running = False
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
boardCapFields = [False, False, False, False, False, False, False, False, False]
player_1 = "P_1"
player_2 = "P_2"
turningPlayer = player_1
a1_captured = False
a2_captured = False
a3_captured = False
b1_captured = False
b2_captured = False
b3_captured = False
c1_captured = False
c2_captured = False
c3_captured = False


# funcs
def play_game():
    running = True
    while running:
        print_board.print_board(board)
        choice = str(input(turningPlayer + ": enter a field to place your marker: "))
        if capture(turningPlayer, choice):
            if check_full.check_full(boardCapFields):
                running = False
                print_board.print_board(board)
                print("Draw")
            checkwin.check_win(board)
            switchPlayer()


def switchPlayer():
    global turningPlayer
    if turningPlayer == player_1:
        turningPlayer = player_2
    elif turningPlayer == player_2:
        turningPlayer = player_1


def capture(turningPlayer, field):
    if boardCapFields[int(field) - 1] == False:
        if turningPlayer == player_1:
            board[int(field) - 1] = "X"
            boardCapFields[int(field) - 1] = True
            return True
        elif turningPlayer == player_2:
            board[int(field) - 1] = "O"
            boardCapFields[int(field) - 1] = True
            return True
    return False


# main function
try:
    if __name__ == '__main__':
        play_game()
except KeyboardInterrupt:
    print("\nexit")
