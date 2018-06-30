def solution(s):
    cnt=0
    for i in list(s):
        if i=='(':
            cnt+=1
        elif i==')':
            cnt-=1
        if cnt<0:
            return False
    if cnt!=0:
        return False
    return True