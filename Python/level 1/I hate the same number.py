def no_continuous(s):
    # 함수를 완성하세요
    answer = []
    tem =""
    for a in range(len(s)):
        if a==0:
            answer.append(s[a])
            tem = s[a]
        elif tem != s[a]:
            answer.append(s[a])
            tem = s[a]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))