def getMinSum(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    for i,j in zip(A,B):
        answer+=i*j
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))