
def check_win(board, player):
    pass

board = [0,1,2,3,4,5,6,7,8]



def print_board():
    
    for i in range(0, 8, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if (i == 0 or i==3):
            print("----------")

print_board()