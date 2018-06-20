def solution(n):
    arr = "수"
    arr2 = "박"
    answer = ""
    for a in range(0,n):
        if a%2 ==0:
            answer += arr
        else:
            answer += arr2
    return answer