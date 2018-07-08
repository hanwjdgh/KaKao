import math
def solution(n, k):
    list = [i for i in range(1,n+1)]
    answer = []
    for j in range(1,n+1):
        fac = math.factorial(n-1)
        print(k)
        answer.append(list.pop((k-1) // fac))
        n, k = n-1, k%fac
    return answer