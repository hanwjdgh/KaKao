def water_melon(n):
    # �Լ��� �ϼ��ϼ���.
    arr = "��"
    arr2 = "��"
    answer = ""
    for a in range(0,n):
        if a%2 ==0:
            answer += arr
        else:
            answer += arr2
    return answer


# ������ ���� �׽�Ʈ�ڵ��Դϴ�.
print("n�� 3�� ���: " + water_melon(3));
print("n�� 4�� ���: " + water_melon(4));
