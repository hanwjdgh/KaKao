def getMinSum(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    for i,j in zip(A,B):
        answer+=i*j
    return answer

#�Ʒ� �ڵ�� ����� ���� �׽�Ʈ �ڵ��Դϴ�.

print(getMinSum([1,2],[3,4]))