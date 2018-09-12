"""
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
"""

def friendblock(m,n,board):
    cnt = 0
    out = 0
    while True:
        table = [[0 for cols in range(n)]for rows in range(m)]
        for i in range(0,m-2+1):
            for j in range(0,n-2+1):
                tem = ""
                chk = 0
                for a in range(0,2):
                    for b in range(0,2):
                        if chk==0 and board[i+a][j+b] !="0":
                            tem = board[i+a][j+b]
                            chk += 1
                        elif tem == board[i+a][j+b]:
                            chk += 1
                if chk==4:
                    for a in range(0,2):
                        for b in range(0,2):
                            table[i+a][j+b] = 1
                else:
                    out += 1
        if out == (m-1) * (n-1):
            break
        
        else:
            out = 0
            for i in range(0,m):
                for j in range(0,n):
                    if table[i][j] == 1:
                        cnt+=1
                        board[i] = board[i].replace(board[i][j],"0",1)

            for i in range(m-1,0,-1):
                for j in range(n-1,-1,-1):
                    if board[i][j] == "0":
                        for a in range(i,-1,-1):
                            if board[a][j] != "0":
                                list1, list2 = list(board[i]),list(board[a])
                                list1[j] = list2[j]
                                board[i] = ''.join(list1)
                                list2[j] = "0"
                                board[a] = ''.join(list2)
                                break
    print(cnt)

friendblock(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])
friendblock(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])