def solution(s):
    tlen = len(s)
    if tlen % 2 == 1:
        return s[tlen//2]
    else:
        return s[tlen//2-1]+s[tlen//2]