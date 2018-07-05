def solution(board):
    answer = 0
    if(len(board)==1):
        if(board[0][0]==0):
            return 0
        else:
            return 1
    for i, lists in enumerate(board):
        for a in range(0,len(lists)):
            lists[a] = 0 if lists[a]==0 else 1
            
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) +1
                answer = answer if answer > board[i][j] else board[i][j]
    return pow(answer,2)