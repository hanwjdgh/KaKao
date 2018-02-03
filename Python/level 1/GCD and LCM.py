def gcdlcm(a, b):
    answer = []
    answer.append(gcd(a,b))
    answer.append((a*b)/answer[0])
    return answer

def gcd(p,q):
    if q==0:
        return p
    return gcd(q,p%q)
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))