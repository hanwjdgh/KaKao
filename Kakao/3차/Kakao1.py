def find(last, leng):
    answer = []
    c = 0
    while len(answer) < leng:
        if c < last:
            if c >= 10:
                answer += str(chr(c+55))
            else:
                answer += str(c)
        else:
            temp = c
            t_str = []
            while temp > 0:    
                if temp % last != 0:
                    if temp % last >= 10:
                        t_str += str(chr((temp%last)+55))
                    else:
                        t_str += str(temp%last)
                else:
                    t_str += str(0)
                temp //= last
            answer += t_str[::-1]
        c += 1
    return answer

def solution(n, t, m, p):
    answer = ""
    temp = find(n, t*m)

    for i,var in enumerate(temp):
        if i%m == p-1:
            answer+=str(var)
        if len(answer)==t:
            break
    return answer