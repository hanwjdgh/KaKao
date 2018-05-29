answer=[]
def move(n,a,b,c):
    print(n,a,b,c)
    if n==1:
        answer.append([a,c])
    else:
        move(n-1,a,c,b)
        answer.append([a,c])
        move(n-1,b,a,c)
def hanoi(n):
    #answer.clear()
    move(n,1,2,3)
    return answer  # 2차원 배열을 반환해 주어야 합니다.


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(hanoi(2))