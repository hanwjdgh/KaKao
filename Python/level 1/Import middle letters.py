def string_middle(str):
    # �Լ��� �ϼ��ϼ���
    tlen = len(str)
    if tlen % 2 == 1:
        return str[tlen//2]
    else:
        return str[tlen//2-1]+str[tlen//2]

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(string_middle("power"))