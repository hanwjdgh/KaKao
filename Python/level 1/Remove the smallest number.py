def rm_small(mylist):
    # �Լ��� �ϼ��ϼ���
    mylist.remove(min(mylist))
    return mylist


# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
my_list = [4, 3, 2, 1]
print("��� {} ".format(rm_small(my_list)))
