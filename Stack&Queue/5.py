def solution(arrangement):
    answer = 0
    leng = len(arrangement)
    
    stack = []
    temp = ''
    for i in range(leng):
        if arrangement[i] == '(':
            stack.append(arrangement[i])
            temp='('
        else:
            stack.pop()
            if temp == '(':
                answer += len(stack)
            else:
                answer += 1
            temp=')'
    return answer