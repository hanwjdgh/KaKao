function hide_numbers(s){
  let hide = null; 
  hide = s.substr(0,s.length-4).replace(/\d/g,"*") ;
  s = s.substr(s.length-4,4) ;
  return hide.concat(s);
  // s.replace(/\d(?=\d{4})/g, "*");
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log("��� : " + hide_numbers('01033334444'));