def numPY(s):
    # �Լ��� �ϼ��ϼ���
    return s.lower().count('p') == s.lower().count('y')


# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print( numPY("pPoooyY") )
print( numPY("JYPPPVs") )