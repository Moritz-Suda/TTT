def check_win(board):
    if((board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[6] == "X" and board[7] == "X" and board[8] == "X")):
        return True, "P_1"
    if((board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] == "X")):
        return True, "P_1"
    if((board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[2] == "X" and board[4] == "X" and board[6] == "X")):
        return True, "P_1"

    if((board[0] == "O" and board[1] == "O" and board[2] == "O") or (board[3] == "O" and board[4] == "O" and board[5] == "O") or (board[6] == "O" and board[7] == "O" and board[8] == "O")):
        return True, "P_2"
    if((board[0] == "O" and board[3] == "O" and board[6] == "O") or (board[1] == "O" and board[4] == "O" and board[7] == "O") or (board[2] == "O" and board[5] == "O" and board[8] == "O")):
        return True, "P_2"
    if((board[0] == "O" and board[4] == "O" and board[8] == "O") or (board[2] == "O" and board[4] == "O" and board[6] == "O")):
        return True, "P_2"
    return False, None
