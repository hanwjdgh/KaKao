def nextBigNumber(n):
    num = str(bin(n)).count('1')
    for i in range(n+1,1000001):
        if str(bin(i)).count('1') == num:
            return i

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))