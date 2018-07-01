def solution(land):
    accum = [0] * len(land[0])

    for row in land:
        tmp = accum[:]
        for i in range(len(row)):
            accum[i] = row[i] + max(tmp[:i] + tmp[i+1:])

    return max(accum)