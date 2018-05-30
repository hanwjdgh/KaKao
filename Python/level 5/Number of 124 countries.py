def change124(n):
    answer = ""
    while n>0:
        n,a = divmod(n,3)
        if a==0:
            n-=1
        answer = "412"[a]+answer
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))