def number_generator(x, n):
    # �Լ��� �ϼ��ϼ���
    answer=[]
    tem=x
    for a in range(0,n):
        answer.append(x)
        x+=tem
    return answer

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(number_generator(3,5))