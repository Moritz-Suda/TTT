#Prints the board
def print_board(board):
    
    for i in range(0, 8, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if (i == 0 or i==3):
            print("-------------")