function noOvertime(no, works) {
	// �߱� ������ �ּ�ȭ �Ͽ��� ���� �߱� ������ ���ϱ��?
  var tem = 0;
	for(var i =0; i<no; i++){
    works[works.indexOf(Math.max.apply(null,works))] -= 1;
  }
	return works.reduce((result,x)=>result+Math.pow(x,2),0);
}