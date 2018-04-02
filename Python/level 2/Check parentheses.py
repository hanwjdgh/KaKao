def is_pair(s):
    # 함수를 완성하세요
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


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))