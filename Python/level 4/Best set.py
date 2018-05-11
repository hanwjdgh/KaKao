def bestSet(n, s):
    answer = [-1]
    result = [int(s/n) for i in range(0,n)]
    if n > s:
        return answer
    for i in range(0,s%n):
        result[i%n] += 1
    result.sort()
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(bestSet(3,13))