def solution(genres, plays):
    answer = []
    leng = len(genres)
    dic = {}
    temp=[]
    for i in range(leng):
        tm = []
        if not genres[i] in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]
        tm.append(genres[i])
        tm.append(plays[i])
        tm.append(i)
        temp.append(tm)
    res = sorted(dic.items(), key =lambda x:x[1],reverse=True)
    temp.sort(key = lambda element : element[1],reverse=True)
    
    for key in res:
        cnt = 0
        for i,val in enumerate(temp):
            if key[0] in val:
                cnt += 1
                answer.append(val[2])
            if cnt == 2:
                break
    return answer