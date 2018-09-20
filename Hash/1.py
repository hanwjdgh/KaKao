def solution(participant, completion):
    dic={}
    answer = ''
    for var in participant:
        if not var in dic:
            dic[var] = 1
        else:
            dic[var] += 1
    
    for var in completion:
        if var in dic:
            dic[var] -= 1
    
    for var in dic.keys():
        if dic[var]==1:
            answer = var
    return answer