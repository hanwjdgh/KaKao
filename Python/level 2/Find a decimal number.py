def numberOfPrime(n):
    # 1���� n������ �Ҽ��� �� ���ΰ���?
    answer = 0
    for a in range(2,n+1):
        cnt = 0
        for b in range(1,a+1):
            if a%b==0:
                cnt+=1
        if(cnt==2):
            answer+=1
    return answer


# �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
print(numberOfPrime(10))