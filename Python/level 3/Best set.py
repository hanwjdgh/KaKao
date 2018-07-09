def solution(n, s):
    answer = [-1]
    result = [int(s/n) for i in range(0,n)]
    if n > s:
        return answer
    for i in range(0,s%n):
        result[i%n] += 1
    result.sort()
    return result