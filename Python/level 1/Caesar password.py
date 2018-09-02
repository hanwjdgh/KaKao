import string
def solution(s, n):
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