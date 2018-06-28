def solution(x, n):
    answer=[]
    tem=x
    for a in range(0,n):
        answer.append(x)
        x+=tem
    return answer