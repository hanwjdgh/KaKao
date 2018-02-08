def sumDivisor(num):
    answer = 0
    for a in range(1,num+1):
        if num % a ==0:
            answer+=a
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))