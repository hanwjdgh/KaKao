function sumDivisor(num) {
	var answer = 0;
	for(var a =1; a<=num; a++){
  		if(num%a==0)
      	answer+=a;
  }
	return answer;
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log(sumDivisor(12));