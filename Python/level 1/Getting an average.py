def average(array):
    # �Լ��� �ϼ��ؼ� �Ű����� array�� ��հ��� return�ϵ��� ����� ������.
    sum = 0
    for a in array:
        sum += a
    return sum/len(array)

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
list = [5,3,4] 
print("��հ� : {}".format(average(list)));