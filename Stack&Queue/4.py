def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        if prices[i] < prices[stack[-1]]:
            for j in stack[::-1]:
                if prices[i] < prices[j]:
                    answer[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)

    for i in range(0, len(stack)-1):
        answer[stack[i]] = len(prices) - stack[i] - 1
    return answer