def solution(n, works):
    answer = 0
    works = sorted(works)
    leng = len(works)
    
    while n > 0:
        max_v = max(works)
        for i in range(leng-1 , -1, -1):
            if works[i] == max_v:
                if works[i] > 0:
                    works[i] -= 1
                n-=1
            if n==0:
                break
    for i in range(leng):
        answer += works[i] * works[i]
    return answer