# imps
import print_board
import checkwin
import check_full
import random

# vars
running = False
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
boardCapFields = [False, False, False, False, False, False, False, False, False]
player_1 = "P_1"
player_2 = "P_2"
turningPlayer = player_1


# funcs
def start():
    print("Welcome!")
    choice = int(input("enter the mode you want to play (1: single- | 2: multi-player): "))
    if choice == 1:
        play_single()
    elif choice == 2:
        play_multi()


def play_single():
    running = True
    global player_2
    player_2 = "ai"
    
    while running:
        player = True
        while player:
            print_board.print_board(board)
            choice = str(input("Player 1: enter a field to place your marker: "))
            if capture(player_1, choice):
                win, player = checkwin.check_win(board)
                if win:
                    if player == player_1:
                        running = False
                        print_board.print_board(board)
                        print("Player 1 hat gewonnen!")
                        break
                if check_full.check_full(boardCapFields):
                    running = False
                    print_board.print_board(board)
                    print("Draw")
                    break
                player = False
        if running is False:
            break
        ai = True
        while ai:
            print_board.print_board(board)
            choice = str(random.randrange(1, 9))
            if capture(player_2, choice):
                win, player = checkwin.check_win(board)
                if win:
                    if player == player_2:
                        running = False
                        print_board.print_board(board)
                        print("AI hat gewonnen!")
                if check_full.check_full(boardCapFields):
                    running = False
                    print_board.print_board(board)
                    print("Draw")
                ai = False
                if running is not True:
                    break


def play_multi():
    running = True
    while running:
        print_board.print_board(board)
        choice = str(input(turningPlayer + ": enter a field to place your marker: "))
        if capture(turningPlayer, choice):
            win, player = checkwin.check_win(board)
            if win:
                if player == player_1:
                    running = False
                    print_board.print_board(board)
                    print("Player 1 hat gewonnen!")
                elif player == player_2:
                    running = False
                    print_board.print_board(board)
                    print("Player 2 hat gewonnen!")
            if check_full.check_full(boardCapFields):
                running = False
                print_board.print_board(board)
                print("Draw")
            switchPlayer()


def switchPlayer():
    global turningPlayer
    if turningPlayer == player_1:
        turningPlayer = player_2
    elif turningPlayer == player_2:
        turningPlayer = player_1


def capture(turningPlayer, field):
    if boardCapFields[int(field) - 1] is False:
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
        start()
except KeyboardInterrupt:
    print("\nexit")
