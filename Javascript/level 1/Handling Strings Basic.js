function alpha_string46(s){
  // �Լ��� �ϼ��ϼ���
	if((s.length === 4 || s.length === 6) && !isNaN(s))
  	return true;
  return false;
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( alpha_string46("a234") );