def tiling(n):
    var = [1, 1]
    answer = 0
    if n==1:
        answer = var[1]
    else:
        for i in range(2,n+1):
            var.append(var[i-2]+var[i-1])
    answer = var[n]
    return answer%100000


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(tiling(3))