def solution(n, works):
    if n >= sum(works):
        return 0
    works = sorted(works)
    print(works)
    for i in range(0,n):
        for j in range(len(works)-1,-1,-1):
            print(works[j],works[j-1])
            if works[j] > works[j-1]:
                break
        print(j)
        works[j] -= 1

        print(works)
    return sum([i*i for i in works])

solution(4,[4,3,3])