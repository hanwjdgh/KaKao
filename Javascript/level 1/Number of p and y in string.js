function numPY(s){
  return s.match(/p/ig).length == s.match(/y/ig).length;
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( numPY("pPoooyY") )
console.log( numPY("Pyy") )