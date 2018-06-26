def gcd(p,q):
    if q==0:
        return p
    return gcd(q,p%q)

def solution(n, m):
    answer = []
    answer.append(gcd(n,m))
    answer.append((n*m)/answer[0])
    return answer