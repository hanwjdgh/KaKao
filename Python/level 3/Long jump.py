def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))
