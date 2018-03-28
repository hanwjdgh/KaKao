def longest_palindrom(s):
    result = []
    for i in range(0,len(s)):
        for j in range(1,len(s)+1):
            if str(s[i:j])==str(s[i:j])[::-1]:
                result.append(len(s[i:j]))
            if str(s[j:i])==str(s[j:i])[::-1]:
                result.append(len(s[j:i]))
    return max(result)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))