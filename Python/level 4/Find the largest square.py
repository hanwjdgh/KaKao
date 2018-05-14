def findLargestSquare(board):
    answer = 0
    for i, lists in enumerate(board):
        for a in range(0,len(lists)):
            lists[a] = 0 if lists[a]=='X' else 1
            
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) +1
                answer = answer if answer > board[i][j] else board[i][j]
    return pow(answer,2)

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))