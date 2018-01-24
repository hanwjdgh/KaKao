def printTriangle(num):
    s=""
    for a in range(0,num):
        s+="*"*(a+1)+"\n"
    return s


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )