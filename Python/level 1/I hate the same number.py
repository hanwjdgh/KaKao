def no_continuous(s):
    # �Լ��� �ϼ��ϼ���
    answer = []
    tem =""
    for a in range(len(s)):
        if a==0:
            answer.append(s[a])
            tem = s[a]
        elif tem != s[a]:
            answer.append(s[a])
            tem = s[a]
    return answer

# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print( no_continuous( "133303" ))