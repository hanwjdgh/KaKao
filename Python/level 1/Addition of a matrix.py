def sumMatrix(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]+=B[i][j]
            
    return A
# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))