function average(array){
  //�Լ��� �ϼ��ϼ���
	var sum=0;
  for(var i=0;i<array.length;i++){
      sum+=array[i];
  }
  return sum/array.length;
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
var testArray = [5,3,4] 
console.log("��հ� : " + average(testArray));