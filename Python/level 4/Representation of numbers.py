def expressions(num):
    answer = 1
    tem = 1
    for a in range(1,num//2+1):
        tem = a
        for b in range(a+1,num//2+2):
            tem += b
            if tem == num:
                answer += 1
                break
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15))
