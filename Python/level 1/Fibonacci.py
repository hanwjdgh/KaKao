def fibonacci(num):
    answer = 0
    a = 0
    b = 1
    for x in range(0,num):
        if x != 0:
            answer = a + b
            a = b
            b = answer
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))