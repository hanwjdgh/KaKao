function printReversedTriangle(num) {
  var result = ''
  // �Լ��� �ϼ��ϼ���
  for ( var i = num; i > 0; i-- ) { 
    for ( var j = 0; j < i; j++ ) { 
      result += "*" 
    } 
    result += "\n" 
  }
  return result
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log("��� : " +'\n'+ printReversedTriangle(3));