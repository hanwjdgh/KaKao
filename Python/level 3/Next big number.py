def nextBigNumber(n):
    num = str(bin(n)).count('1')
    for i in range(n+1,1000001):
        if str(bin(i)).count('1') == num:
            return i

#�Ʒ� �ڵ�� �׽�Ʈ�� ���� ��� �ڵ��Դϴ�.
print(nextBigNumber(78))