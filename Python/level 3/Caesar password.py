import string

def caesar(s, n):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    s = list(s)
    for i, char in enumerate(s):
        if char in lower:
            tem = (lower.index(char) + n) % 26
            s[i] = lower[tem]
        elif char in upper:
            tem = (upper.index(char) + n) % 26
            s[i] = upper[tem]
        else:
            continue
    return ''.join(s)

# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))