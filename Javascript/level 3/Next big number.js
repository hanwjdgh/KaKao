function nextBigNumber(n){
  var cnt = n.toString(2).match(/1/g).length;
  for (var i = n+1; ; i++) { 
    if ( cnt == i.toString(2).match(/1/g).length) { 
      return i 
    } 
  }
}

//�Ʒ� �ڵ�� �׽�Ʈ�� ���� �ڵ��Դϴ�.
console.log(nextBigNumber(78));