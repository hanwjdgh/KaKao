import math
def nextSqure(n):
    # �Լ��� �ϼ��ϼ���
    tem = math.sqrt(n)
    if int(tem) == tem:
        return int(pow(tem+1,2))
    return 'no'

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print("��� : {}".format(nextSqure(121)));