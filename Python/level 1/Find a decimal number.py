def solution(n):
    arr = [i for i in range(n+1)]
    arr[0],arr[1] = 0,0
    for i in range(2,n+1):
        if arr[i] != 0:
            if i*i > 1000001:
                break
            else:
                for j in range((i*i),n+1,i):
                    arr[j] = 0
    return len(arr)-arr.count(0)