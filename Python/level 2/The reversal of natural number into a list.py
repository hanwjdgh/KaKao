def digit_reverse(n):
    # �Լ��� �ϼ��� �ּ���
    list = [int(a) for a in str(n)]
    list.reverse()
    return list

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print("��� : {}".format(digit_reverse(12345)));