def productMatrix(A, B):
    matR = [ len(B[0])*[0] for i in range (len(A)) ]
    for i in range (len(matR) ):
        for j in range ( len(matR[i]) ):
            for k in range ( len(A[i] ) ):
                matR[i][j] += A[i][k]*B[k][j]
    return matR

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));