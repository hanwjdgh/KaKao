def solution(priorities, location):
    answer = 0
    temp = []
    for i,var in enumerate(priorities):
        tm = []
        tm.append(var)
        tm.append(i)
        temp.append(tm)

    s = 0
    cnt = 0
    while len(temp) > 0:
        x = temp[s]
        temp.pop(s)
        if len(list(filter(lambda v: v[0] > x[0], temp))) > 0:
            temp.append(x)
        else:
            cnt += 1
            if x[1] == location:
                answer = cnt
    return answer