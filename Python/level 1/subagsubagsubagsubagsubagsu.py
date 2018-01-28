def water_melon(n):
    # 함수를 완성하세요.
    arr = "수"
    arr2 = "박"
    answer = ""
    for a in range(0,n):
        if a%2 ==0:
            answer += arr
        else:
            answer += arr2
    return answer


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
