def solution(clothes):
    answer = 1
    dic = {}
    for var in clothes:
        if not var[1] in dic:
            dic[var[1]] = 1
        else:
            dic[var[1]] += 1
            
    for val in dic.values():
        answer *= (val+1)
    return answer-1