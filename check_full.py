def check_full(board):
    capCount = 0
    for i in range(len(board)):
        if board[i]:
            capCount = capCount + 1
    if capCount == 9:
        return True
    return False