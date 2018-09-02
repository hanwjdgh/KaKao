def solution(n):
    answer = 0
    var = 1
    sum = 0
    if n % 2 ==1:
        answer = 0
    else:
        n = n // 2
        for i in range(n):
            tmp = var
            var = var * 3 + sum * 2
            sum += tmp
        answer = var % 1000000007
    return answer