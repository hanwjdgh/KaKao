def fibonacci(num):
    answer = 0
    a = 0
    b = 1
    for x in range(0,num):
        if x != 0:
            answer = a + b
            a = b
            b = answer
    return answer

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(fibonacci(3))