function fibonacci(num) {
	var answer = 0;
	var a =0;
  var b=1;
  for(var i=0; i<num; i++) {
        if(i != 0){
          answer = a + b;
          a = b;
          b = answer;
        }
  }
	return answer;
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log(fibonacci(3))