from functools import reduce

def gcd(a, b):
    if(b == 0): 
        return a
    return gcd(b, a%b)


def lcm(a,b):
    return a * b / gcd(a, b)

def nlcm(num):
    num.sort()
    return reduce(lcm,num)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));