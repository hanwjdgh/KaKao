def Harshad(n):
    # n은 하샤드 수 인가요?
    list = [int(i) for i in str(n)]
    if n%sum(list) == 0:
    	return True
    else:
        return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))