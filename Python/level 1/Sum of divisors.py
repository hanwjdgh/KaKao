def sumDivisor(num):
    answer = 0
    for a in range(1,num+1):
        if num % a ==0:
            answer+=a
    return answer

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(sumDivisor(12))