function numberOfPrime(n) {
	var result = 0;
	// �Լ��� �ϼ��ϼ���.
	var cnt=0;
	for(var a=2;a<=n;a++){
    cnt=0;
  	for(var b=1;b<=a;b++){
    		if(a%b==0)
          cnt++;
    }
    if(cnt==2)
      result++;
  }
	return result;
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( numberOfPrime(10) )