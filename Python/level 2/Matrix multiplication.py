def productMatrix(A, B):
    matR = [ len(B[0])*[0] for i in range (len(A)) ]
    for i in range (len(matR) ):
        for j in range ( len(matR[i]) ):
            for k in range ( len(A[i] ) ):
                matR[i][j] += A[i][k]*B[k][j]
    return matR

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("��� : {}".format(productMatrix(a,b)));