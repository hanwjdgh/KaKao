def solution(heights):
    answer = []
    temp = []
    for i, var in enumerate(heights):
        tm = []
        tm.append(var)
        tm.append(i+1)
        s = 0
        while len(temp) > 0:
            if temp[s][0] > var:
                answer.append(temp[s][1])
                break
            temp.pop(0)
        if len(temp) ==0:
            answer.append(0)
        temp.insert(0,tm)
    return answer