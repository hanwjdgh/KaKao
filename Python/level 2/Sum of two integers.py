def adder(a, b):
    # �Լ��� �ϼ��ϼ���
    if a > b: 
        a, b = b, a
    return sum(list(range(a, b+1)))

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print( adder(3, 5))