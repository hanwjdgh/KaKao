def sum_digit(number):
    '''number�� �� �ڸ����� ���ؼ� return�ϼ���'''
    answer = 0
    for i in str(number):
        answer += int(i)
    return answer
# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print("��� : {}".format(sum_digit(123)));