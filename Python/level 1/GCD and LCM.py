def gcdlcm(a, b):
    answer = []
    answer.append(gcd(a,b))
    answer.append((a*b)/answer[0])
    return answer

def gcd(p,q):
    if q==0:
        return p
    return gcd(q,p%q)
# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(gcdlcm(3,12))