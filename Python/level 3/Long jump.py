def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b

#�Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(jumpCase(4))
