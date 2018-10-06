def solution(array, commands):
    answer = []
    
    for var in commands:
        x, y = var[0], var[1]
        z = var[2]
        temp = array[x-1:y]
        temp = sorted(temp)
        answer.append(temp[z-1])
    return answer