import math
def nextSqure(n):
    # 함수를 완성하세요
    tem = math.sqrt(n)
    if int(tem) == tem:
        return int(pow(tem+1,2))
    return 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));