import heapq

def solution(scoville, K):
    answer = 0

    lst = []
    for var in scoville:
        heapq.heappush(lst,var)
    
    while True:
        f = heapq.heappop(lst)
        if f >= K:
            break
        if len(lst) > 0:
            s = heapq.heappop(lst)
            var = f + s * 2
            heapq.heappush(lst,var)
            answer += 1
        else:
            answer = -1
            break
    return answer