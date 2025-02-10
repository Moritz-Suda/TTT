def check_full(board):
    capCount = 0
    for i in range(len(board)):
        if board[i]:
            capCount = capCount + 1
    if capCount == 9:
        return True
    return False
#    if a1_captured is True:
#        if a2_captured is True:
#            if a3_captured is True:
#                if b1_captured is True:
#                    if b2_captured is True:
#                        if b3_captured is True:
#                            if c1_captured is True:
#                                if c2_captured is True:
#                                    if c3_captured is True:
#                                        print("You've fucked up!")
