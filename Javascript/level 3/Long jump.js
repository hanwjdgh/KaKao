function jumpCase(num) {
	var answer = 0;
  if(num==1)
    return 1;
  else if(num==2)
    return 2;
 	answer = jumpCase(num - 1) + jumpCase(num - 2);
	return answer;
}

//�Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log(jumpCase(4));

