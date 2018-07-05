def solution(s):
    result = []
    for i in range(0,len(s)):
        for j in range(1,len(s)+1):
            if str(s[i:j])==str(s[i:j])[::-1]:
                result.append(len(s[i:j]))
            if str(s[j:i])==str(s[j:i])[::-1]:
                result.append(len(s[j:i]))
    return max(result)

#69.3