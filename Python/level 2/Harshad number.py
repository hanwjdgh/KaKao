def Harshad(n):
    # n�� �ϻ��� �� �ΰ���?
    list = [int(i) for i in str(n)]
    if n%sum(list) == 0:
    	return True
    else:
        return False

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(Harshad(18))