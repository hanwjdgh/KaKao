def toWeirdCase(s):
    # �Լ��� �ϼ��ϼ���
    list = s.split(" ")
    list2 = []
    for str in list:
        answer=""
        for tst in range(len(str)):
            if tst %2==0:
                answer+=str[tst].upper()
            else:
                answer+=str[tst].lower()
        list2.append(answer)
    
    return " ".join(list2)

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print("��� : {}".format(toWeirdCase("try hello world")));