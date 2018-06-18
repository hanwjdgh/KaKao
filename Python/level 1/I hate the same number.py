def solution(arr):
    answer = []
    tem =""
    for a in range(len(arr)):
        if a==0:
            answer.append(arr[a])
            tem = arr[a]
        elif tem != arr[a]:
            answer.append(arr[a])
            tem = arr[a]
    return answer
'''
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''