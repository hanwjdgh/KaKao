def collatz(num):
    answer = 0
    while num > 1:
        if num %2 ==0:
            num /= 2
        else:
            num=(num*3)+1
        answer+=1
        if answer==500:
            answer=-1
            break
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))