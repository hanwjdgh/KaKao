def strange_sort(strings, n):
    '''strings�� ���ڿ����� n��° ���ڸ� �������� �����ؼ� return�ϼ���'''
    return sorted(strings, key=lambda strings:strings[n])

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print( strange_sort(["sun", "bed", "car"], 1) )