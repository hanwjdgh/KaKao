def solution(A, B):
    matR = [ len(B[0])*[0] for i in range (len(A)) ]
    for i in range (len(matR) ):
        for j in range ( len(matR[i]) ):
            for k in range ( len(A[i] ) ):
                matR[i][j] += A[i][k]*B[k][j]
    return matR