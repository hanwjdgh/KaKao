def Jaden_Case(s):
    # �Լ��� �ϼ��ϼ���
    list = s.split(" ")
    list2 = []
    for str in list:
        tem = ""
        for a in range(len(str)):
            if a==0:
                tem +=str[a].upper()
            else:
                tem+=str[a].lower()
        list2.append(tem)
    return " ".join(list2)        
    
# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(Jaden_Case("3people unFollowed me for the last week"))