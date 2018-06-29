def solution(n):
    answer = ""
    while n>0:
        n,a = divmod(n,3)
        if a==0:
            n-=1
        answer = "412"[a]+answer
    return answer