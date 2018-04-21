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

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(nlcm([2,6,8,14]));