def noOvertime(n, works):
    # �߱� ������ �ּ�ȭ �Ͽ��� ���� �߱� ������ ���ϱ��?
    for i in range(0,n):
        works[works.index(max(works))] -= 1
    return sum([i*i for i in works])
    