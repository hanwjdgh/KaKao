import math
def solution(n):
    tem = math.sqrt(n)
    if int(tem) == tem:
        return int(pow(tem+1,2))
    return -1