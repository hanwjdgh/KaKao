def solution(progresses, speeds):
    answer = []

    var = []
    leng = len(progresses)

    for i in range(leng):
        cnt = (100 - progresses[i]) % speeds[i]
        if cnt == 0:
            var.append((100 - progresses[i]) // speeds[i])
        else:
            var.append((100 - progresses[i]) // speeds[i] + 1)

    s = 0
    b = 0
    while True:
        chk = 1
        for i in range(s+1, leng+1):
            if i == leng:
                b = 1
                break
            if progresses[i]+speeds[i]*var[s] >= 100:
                chk += 1
            else:
                s = i
                break
        answer.append(chk)
        if b == 1:
            break
    return answer