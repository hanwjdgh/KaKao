function printTriangle(num) {
  var result = ''
  // �Լ��� �ϼ��ϼ���
  for(var a=0; a<num; a++)
    result+='*'.repeat(a+1)+'\n';
  return result
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( printTriangle(3) );