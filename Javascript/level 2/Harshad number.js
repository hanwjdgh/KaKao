function Harshad(n){
  //�Լ��� �ϼ��ϼ���
	var tem = n.toString();
  var arr = tem.split("");
  var nanu=0;
  for(var a=0; a<arr.length;a++){
    	nanu+=parseInt(arr[a]);
    }
	return (n%nanu==0)?true:false;
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log(Harshad(18))