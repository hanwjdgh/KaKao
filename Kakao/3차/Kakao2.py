dic={}

def init():
    for i in range(1,27):
        dic[chr(i+64)] = i
    
def solution(msg):
    answer = []
    init()
    
    m_len = len(msg)
    si = 26
    temp = list(msg)
    leng = 1
    cnt = 0

    while cnt < m_len:
        t_ans = 0
        chk = 0
        for i in range(leng, 0, -1):
            t = "".join(temp[cnt:cnt+i])
            if t in dic:
                t_ans = dic[t]
                tem = "".join(temp[cnt:cnt+i+1])
                si += 1
                dic[str(tem)] = si           
                leng = max(leng, len(tem))
                cnt += i
                break
        answer.append(t_ans)

    return answer