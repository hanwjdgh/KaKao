def solution(bridge_length, weight, truck_weights):
    answer = 1
    temp = []

    s = 0

    while True:
        if len(temp) != 0:
            if answer >= temp[0][0] + bridge_length:
                weight += temp[0][1]
                temp.pop(0)
                continue
        if weight >= truck_weights[s]:
            weight -= truck_weights[s]
            tm = []
            tm.append(answer)
            tm.append(truck_weights[s])
            temp.append(tm)
            if s == len(truck_weights)-1:
                answer += bridge_length
                break
            s += 1
            answer += 1
        else:
            weight += temp[0][1]
            answer = bridge_length + temp[0][0]
            temp.pop(0)

    return answer