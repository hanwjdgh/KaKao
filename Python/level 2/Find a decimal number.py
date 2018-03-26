def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    answer = 0
    for a in range(2,n+1):
        cnt = 0
        for b in range(1,a+1):
            if a%b==0:
                cnt+=1
        if(cnt==2):
            answer+=1
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))