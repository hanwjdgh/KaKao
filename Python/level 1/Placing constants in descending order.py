def solution(n):
    temp = list(str(n))
    temp = sorted(temp,reverse=True)
    return int(''.join(temp))